""" CS5340 Lab 4 Part 2: Gibbs Sampling
See accompanying PDF for instructions.

Name: Adarsh Srivastava
Email: adarsh.srivastava@u.nus.edu
Student ID: A0254358X
"""

import copy
import os
import json
import numpy as np
from tqdm import tqdm
from collections import Counter
from argparse import ArgumentParser
from factor_utils import factor_evidence, factor_marginalize, assignment_to_index
from factor import Factor
import networkx as nx

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(PROJECT_DIR, 'data')
INPUT_DIR = os.path.join(DATA_DIR, 'inputs')
PREDICTION_DIR = os.path.join(DATA_DIR, 'predictions')
GROUND_TRUTH_DIR = os.path.join(DATA_DIR, 'ground-truth')

""" HELPER FUNCTIONS HERE """

""" END HELPER FUNCTIONS HERE"""


def _sample_step(nodes, factors, in_samples):
    """
    Performs gibbs sampling for a single iteration. Returns a sample for each node

    Args:
        nodes: numpy array of nodes
        factors: dictionary of factors e.g. factors[x1] returns the local factor for x1
        in_samples: dictionary of input samples (from previous iteration)

    Returns:
        dictionary of output samples where samples[x1] returns the sample for x1.
    """
    samples = copy.deepcopy(in_samples)

    """ YOUR CODE HERE """
    for node in nodes:
        # calculate probability based on markov blankets
        proposal = factor_evidence(factors[node], {n: samples[n] for n in factors[node].var if n != node})
        proposal.normalize()
        samples[node] = np.random.choice([*range(proposal.card[0])], p=proposal.val)

    """ END YOUR CODE HERE """

    return samples


def get_markov_blanket(g, node):
    pred = list(g.predecessors(node))
    succ = list(g.successors(node))
    pred_of_succ = [pred for node in succ for pred in g.predecessors(node)]
    return pred + succ + pred_of_succ


def _get_conditional_probability(nodes, edges, factors, evidence, initial_samples, num_iterations, num_burn_in):
    """
    Returns the conditional probability p(Xf | Xe) where Xe is the set of observed nodes and Xf are the query nodes
    i.e. the unobserved nodes. The conditional probability is approximated using Gibbs sampling.

    Args:
        nodes: numpy array of nodes e.g. [x1, x2, ...].
        edges: numpy array of edges e.g. [i, j] implies that nodes[i] is the parent of nodes[j].
        factors: dictionary of Factors e.g. factors[x1] returns the conditional probability of x1 given all other nodes.
        evidence: dictionary of evidence e.g. evidence[x4] returns the provided evidence for x4.
        initial_samples: dictionary of initial samples to initialize Gibbs sampling.
        num_iterations: number of sampling iterations
        num_burn_in: number of burn-in iterations

    Returns:
        returns Factor of conditional probability.
    """
    assert num_iterations > num_burn_in
    conditional_prob = Factor()

    """ YOUR CODE HERE """
    g = nx.DiGraph()
    g.add_nodes_from(list(nodes))
    g.add_edges_from(list(edges))
    g.remove_nodes_from([*evidence.keys()])  # evidence

    nodes = list(nx.lexicographical_topological_sort(g))  # evidence nodes already removed

    cardinality = {}
    mb = {}

    for node in nodes:
        mb[node] = get_markov_blanket(g, node)

    for node, factor in factors.items():
        if node not in evidence.keys():
            cardinality[node] = factor.card[np.where(factor.var == node)[0][0]]
            factor = factor_evidence(factor, evidence)
            factors[node] = factor_marginalize(factor, np.setdiff1d(factor.var, mb[node]+[node]))

    conditional_prob.var = np.array(nodes, np.int64)
    conditional_prob.card = np.array([cardinality[x] for x in conditional_prob.var], np.int64)
    conditional_prob.val = np.zeros(np.prod(conditional_prob.card), np.float64)

    in_samples = initial_samples

    for i in tqdm(range(num_burn_in)):
        in_samples = _sample_step(nodes, factors, in_samples)


    for i in tqdm(range(num_iterations - num_burn_in)):
        s = _sample_step(nodes, factors, in_samples)
        assignment = np.array([s[node] for node in nodes])
        idx = assignment_to_index(assignment, conditional_prob.card)
        conditional_prob.val[idx] += 1
        in_samples = s

    conditional_prob.normalize()

    """ END YOUR CODE HERE """

    return conditional_prob


def load_input_file(input_file: str) -> (Factor, dict, dict, int):
    """
    Returns the target factor, proposal factors for each node and evidence. DO NOT EDIT THIS FUNCTION

    Args:
        input_file: input file to open

    Returns:
        Factor of the target factor which is the target joint distribution of all nodes in the Bayesian network
        dictionary of node:Factor pair where Factor is the proposal distribution to sample node observations. Other
                    nodes in the Factor are parent nodes of the node
        dictionary of node:val pair where node is an evidence node while val is the evidence for the node.
    """
    with open(input_file, 'r') as f:
        input_config = json.load(f)
    proposal_factors_dict = input_config['proposal-factors']

    def parse_factor_dict(factor_dict):
        var = np.array(factor_dict['var'])
        card = np.array(factor_dict['card'])
        val = np.array(factor_dict['val'])
        return Factor(var=var, card=card, val=val)

    nodes = np.array(input_config['nodes'], dtype=int)
    edges = np.array(input_config['edges'], dtype=int)
    node_factors = {int(node): parse_factor_dict(factor_dict=proposal_factor_dict) for
                    node, proposal_factor_dict in proposal_factors_dict.items()}

    evidence = {int(node): ev for node, ev in input_config['evidence'].items()}
    initial_samples = {int(node): initial for node, initial in input_config['initial-samples'].items()}

    num_iterations = input_config['num-iterations']
    num_burn_in = input_config['num-burn-in']
    return nodes, edges, node_factors, evidence, initial_samples, num_iterations, num_burn_in


def main():
    """
    Helper function to load the observations, call your parameter learning function and save your results.
    DO NOT EDIT THIS FUNCTION.
    """
    argparser = ArgumentParser()
    argparser.add_argument('--case', type=int, required=True,
                           help='case number to create observations e.g. 1 if 1.json')
    args = argparser.parse_args()
    # np.random.seed(0)

    case = args.case
    input_file = os.path.join(INPUT_DIR, '{}.json'.format(case))
    nodes, edges, node_factors, evidence, initial_samples, num_iterations, num_burn_in = \
        load_input_file(input_file=input_file)

    # solution part
    conditional_probability = _get_conditional_probability(nodes=nodes, edges=edges, factors=node_factors,
                                                           evidence=evidence, initial_samples=initial_samples,
                                                           num_iterations=num_iterations, num_burn_in=num_burn_in)
    print(conditional_probability)
    # end solution part

    # json only recognises floats, not np.float, so we need to cast the values into floats.
    save__dict = {
        'var': np.array(conditional_probability.var).astype(int).tolist(),
        'card': np.array(conditional_probability.card).astype(int).tolist(),
        'val': np.array(conditional_probability.val).astype(float).tolist()
    }

    if not os.path.exists(PREDICTION_DIR):
        os.makedirs(PREDICTION_DIR)
    prediction_file = os.path.join(PREDICTION_DIR, '{}.json'.format(case))

    with open(prediction_file, 'w') as f:
        json.dump(save__dict, f, indent=1)
    print('INFO: Results for test case {} are stored in {}'.format(case, prediction_file))


if __name__ == '__main__':
    main()
