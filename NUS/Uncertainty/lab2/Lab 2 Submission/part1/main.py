""" CS5340 Lab 2 Part 1: Junction Tree Algorithm
See accompanying PDF for instructions.

Name: Adarsh Srivastava
Email: e0954759@u.nus.edu
Student ID: A0254358X
"""
import itertools
import os
import numpy as np
import json
import networkx as nx
from argparse import ArgumentParser

from factor import Factor
from jt_construction import construct_junction_tree
from factor_utils import factor_product, factor_evidence, factor_marginalize

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
INPUT_DIR = os.path.join(DATA_DIR, 'inputs')  # we will store the input data files here!
PREDICTION_DIR = os.path.join(DATA_DIR, 'predictions')  # we will store the prediction files here!

""" ADD HELPER FUNCTIONS HERE """

""" END HELPER FUNCTIONS HERE """


def _update_mrf_w_evidence(all_nodes, evidence, edges, factors):
    """
    Update the MRF graph structure from observing the evidence

    Args:
        all_nodes: numpy array of nodes in the MRF
        evidence: dictionary of node:observation pairs where evidence[x1] returns the observed value of x1
        edges: numpy array of edges in the MRF
        factors: list of Factors in teh MRF

    Returns:
        numpy array of query nodes
        numpy array of updated edges (after observing evidence)
        list of Factors (after observing evidence; empty factors should be removed)
    """

    query_nodes = all_nodes
    updated_edges = edges
    updated_factors = []

    """ YOUR CODE HERE """

    g = nx.Graph(list(map(tuple, edges)))

    for node_to_eliminate in evidence.keys():
        neighbors = list(itertools.combinations([n for n in g.neighbors(node_to_eliminate)], 2))
        g.add_edges_from(neighbors)
        g.remove_node(node_to_eliminate)

    updated_edges = np.array(list(g.edges))
    query_nodes = np.array(list(g.nodes))

    for factor in factors:
        updated_factor = factor_evidence(factor, evidence)
        # updated_factor.normalize()
        if len(updated_factor.var) != 0:
            updated_factors.append(updated_factor)
    """ END YOUR CODE HERE """

    return query_nodes, updated_edges, updated_factors


def collect(giver, collector, graph, jt_clique_factors, jt_cliques, messages):
    for n in graph.neighbors(giver):
        if n != collector:
            collect(n, giver, graph, jt_clique_factors, jt_cliques, messages)

    msg = jt_clique_factors[giver]

    for n in graph.neighbors(giver):
        msg = factor_product(msg, messages[n][giver])

    variables_to_marginalize = list(set(jt_cliques[giver]) - set(jt_cliques[collector]))

    if len(variables_to_marginalize) == 0:
        messages[giver][collector] = msg
    else:
        messages[giver][collector] = factor_marginalize(msg, variables_to_marginalize)


def distribute(receiver, sender, graph, jt_clique_factors, jt_cliques, messages):
    msg = jt_clique_factors[sender]
    for n in graph.neighbors(sender):
        if n != receiver:
            msg = factor_product(msg, messages[n][sender])

    variables_to_marginalize = list(set(jt_cliques[sender]) - set(jt_cliques[receiver]))

    messages[sender][receiver] = factor_marginalize(msg, variables_to_marginalize)

    for n in graph.neighbors(receiver):
        if n != sender:
            distribute(n, receiver, graph, jt_clique_factors, jt_cliques, messages)


def _get_clique_potentials(jt_cliques, jt_edges, jt_clique_factors):
    """
    Returns the list of clique potentials after performing the sum-product algorithm on the junction tree

    Args:
        jt_cliques: list of junction tree nodes e.g. [[x1, x2], ...]
        jt_edges: numpy array of junction tree edges e.g. [i,j] implies that jt_cliques[i] and jt_cliques[j] are
                neighbors
        jt_clique_factors: list of clique factors where jt_clique_factors[i] is the factor for cliques[i]

    Returns:
        list of clique potentials computed from the sum-product algorithm
    """
    clique_potentials = jt_clique_factors

    """ YOUR CODE HERE """
    root_clique = 0
    graph = nx.Graph(list(map(tuple, jt_edges)))

    messages = [[Factor()] * len(jt_cliques) for _ in range(len(jt_cliques))]

    for n in graph.neighbors(root_clique):
        collect(n, root_clique, graph, jt_clique_factors, jt_cliques, messages)

    for n in graph.neighbors(root_clique):
        distribute(n, root_clique, graph, jt_clique_factors, jt_cliques, messages)

    for i, clique in enumerate(jt_cliques):
        for n in graph.neighbors(i):
            clique_potentials[i] = factor_product(clique_potentials[i], messages[n][i])

    """ END YOUR CODE HERE """

    assert len(clique_potentials) == len(jt_cliques)
    return clique_potentials


def _get_node_marginal_probabilities(query_nodes, cliques, clique_potentials):
    """
    Returns the marginal probability for each query node from the clique potentials.

    Args:
        query_nodes: numpy array of query nodes e.g. [x1, x2, ..., xN]
        cliques: list of cliques e.g. [[x1, x2], ... [x2, x3, .., xN]]
        clique_potentials: list of clique potentials (Factor class)

    Returns:
        list of node marginal probabilities (Factor class)

    """
    query_marginal_probabilities = []

    """ YOUR CODE HERE """
    cliques_with_index = list(enumerate(cliques))
    query_nodes_with_index = list(enumerate(query_nodes))
    cliques_with_index.sort(key=lambda x: len(x[1]))

    for node in query_nodes:
        clique_index_with_node = None
        extra_variables = np.array([])
        for i, clique in cliques_with_index:
            if node in clique:
                clique_index_with_node = i
                extra_variables = np.setdiff1d(clique, [node])
                break
        clique_potentials[clique_index_with_node].normalize()
        if len(extra_variables) == 0:
            query_marginal_probabilities.append(clique_potentials[clique_index_with_node])
        else:
            query_marginal_probabilities.append(factor_marginalize(clique_potentials[clique_index_with_node], extra_variables))
    """ END YOUR CODE HERE """

    return query_marginal_probabilities


def get_conditional_probabilities(all_nodes, evidence, edges, factors):
    """
    Returns query nodes and query Factors representing the conditional probability of each query node
    given the evidence e.g. p(xf|Xe) where xf is a single query node and Xe is the set of evidence nodes.

    Args:
        all_nodes: numpy array of all nodes (random variables) in the graph
        evidence: dictionary of node:evidence pairs e.g. evidence[x1] returns the observed value for x1
        edges: numpy array of all edges in the graph e.g. [[x1, x2],...] implies that x1 is a neighbor of x2
        factors: list of factors in the MRF.

    Returns:
        numpy array of query nodes
        list of Factor
    """
    query_nodes, updated_edges, updated_node_factors = _update_mrf_w_evidence(all_nodes=all_nodes, evidence=evidence,
                                                                              edges=edges, factors=factors)

    jt_cliques, jt_edges, jt_factors = construct_junction_tree(nodes=query_nodes, edges=updated_edges,
                                                               factors=updated_node_factors)

    clique_potentials = _get_clique_potentials(jt_cliques=jt_cliques, jt_edges=jt_edges, jt_clique_factors=jt_factors)

    query_node_marginals = _get_node_marginal_probabilities(query_nodes=query_nodes, cliques=jt_cliques,
                                                            clique_potentials=clique_potentials)

    return query_nodes, query_node_marginals


def parse_input_file(input_file: str):
    """ Reads the input file and parses it. DO NOT EDIT THIS FUNCTION. """
    with open(input_file, 'r') as f:
        input_config = json.load(f)

    nodes = np.array(input_config['nodes'])
    edges = np.array(input_config['edges'])

    # parse evidence
    raw_evidence = input_config['evidence']
    evidence = {}
    for k, v in raw_evidence.items():
        evidence[int(k)] = v

    # parse factors
    raw_factors = input_config['factors']
    factors = []
    for raw_factor in raw_factors:
        factor = Factor(var=np.array(raw_factor['var']), card=np.array(raw_factor['card']),
                        val=np.array(raw_factor['val']))
        factors.append(factor)
    return nodes, edges, evidence, factors


def main():
    """ Entry function to handle loading inputs and saving outputs. DO NOT EDIT THIS FUNCTION. """
    argparser = ArgumentParser()
    argparser.add_argument('--case', type=int, required=True,
                           help='case number to create observations e.g. 1 if 1.json')
    args = argparser.parse_args()

    case = args.case
    input_file = os.path.join(INPUT_DIR, '{}.json'.format(case))
    nodes, edges, evidence, factors = parse_input_file(input_file=input_file)

    # solution part:
    query_nodes, query_conditional_probabilities = get_conditional_probabilities(all_nodes=nodes, edges=edges,
                                                                                 factors=factors, evidence=evidence)

    predictions = {}
    for i, node in enumerate(query_nodes):
        probability = query_conditional_probabilities[i].val
        predictions[int(node)] = list(np.array(probability, dtype=float))

    if not os.path.exists(PREDICTION_DIR):
        os.makedirs(PREDICTION_DIR)
    prediction_file = os.path.join(PREDICTION_DIR, '{}.json'.format(case))
    with open(prediction_file, 'w') as f:
        json.dump(predictions, f, indent=1)
    print('INFO: Results for test case {} are stored in {}'.format(case, prediction_file))


if __name__ == '__main__':
    main()
