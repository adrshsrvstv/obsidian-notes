""" CS5340 Lab 4 Part 1: Importance Sampling
See accompanying PDF for instructions.

Name: Adarsh Srivastava
Email: adarsh.srivastava@u.nus.edu
Student ID: A0254358X
"""

import os
import json
import numpy as np
import networkx as nx
from factor_utils import factor_evidence, factor_product, assignment_to_index
from factor import Factor
from argparse import ArgumentParser
from tqdm import tqdm

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(PROJECT_DIR, 'data')
INPUT_DIR = os.path.join(DATA_DIR, 'inputs')
PREDICTION_DIR = os.path.join(DATA_DIR, 'predictions')

""" ADD HELPER FUNCTIONS HERE """

""" END HELPER FUNCTIONS HERE """


def _sample_step(nodes, proposal_factors):
    """
    Performs one iteration of importance sampling where it should sample a sample for each node. The sampling should
    be done in topological order.

    Args:
        nodes: numpy array of nodes. nodes are sampled in the order specified in nodes
        proposal_factors: dictionary of proposal factors where proposal_factors[1] returns the
                sample distribution for node 1

    Returns:
        dictionary of node samples where samples[1] return the scalar sample for node 1.
    """
    samples = {}

    """ YOUR CODE HERE: Use np.random.choice """
    for node in nodes:
        proposal = factor_evidence(proposal_factors[node], samples)
        samples[node] = np.random.choice([*range(proposal.card[0])], p=proposal.val)
    """ END YOUR CODE HERE """

    assert len(samples.keys()) == len(nodes)
    return samples


def get_topologically_sorted_nodes(factors, evidence):
    g = nx.DiGraph()
    for node, factor in factors.items():
        g.add_node(node)
        for var in factor.var:
            if var != node:
                if var not in g:
                    g.add_node(var)
                g.add_edge(var, node)
    g.remove_nodes_from([*evidence.keys()])
    return list(nx.lexicographical_topological_sort(g))


def get_probability_of_sample(factor_dict, assignments_dict):
    p = np.float64(1)
    for _, factor in factor_dict.items():
        idx = assignment_to_index(np.array([assignments_dict[n] for n in factor.var]), factor.card)
        p = np.multiply(p, factor.val[idx])
    return p


def _get_conditional_probability(target_factors, proposal_factors, evidence, num_iterations):
    """
    Performs multiple iterations of importance sampling and returns the conditional distribution p(Xf | Xe) where
    Xe are the evidence nodes and Xf are the query nodes (unobserved).

    Args:
        target_factors: dictionary of node:Factor pair where Factor is the target distribution of the node.
                        Other nodes in the Factor are parent nodes of the node. The product of the target
                        distribution gives our joint target distribution.
        proposal_factors: dictionary of node:Factor pair where Factor is the proposal distribution to sample node
                        observations. Other nodes in the Factor are parent nodes of the node
        evidence: dictionary of node:val pair where node is an evidence node while val is the evidence for the node.
        num_iterations: number of importance sampling iterations

    Returns:
        Approximate conditional distribution of p(Xf | Xe) where Xf is the set of query nodes (not observed) and
        Xe is the set of evidence nodes. Return result as a Factor
    """
    out = Factor()

    """ YOUR CODE HERE """
    # for evidence_node, value in evidence.items():
    #     proposal_factors[evidence_node] = get_factor_for_evidence_node(evidence_node, value, value + 1)

    cardinality = {}
    for node, factor in proposal_factors.items():
        proposal_factors[node] = factor_evidence(factor, evidence)

    for node, factor in target_factors.items():
        cardinality[node] = target_factors[node].card[np.where(target_factors[node].var == node)[0][0]]
        target_factors[node] = factor_evidence(factor, evidence)

    nodes = get_topologically_sorted_nodes(proposal_factors, evidence)
    out.var = np.array(nodes, np.int64)
    out.card = np.array([cardinality[x] for x in out.var], np.int64)
    out.val = np.zeros(np.prod(out.card), np.float64)

    for i in tqdm(range(num_iterations)):
        s = _sample_step(nodes, proposal_factors)
        ps = get_probability_of_sample(target_factors, s)
        qs = get_probability_of_sample(proposal_factors, s)
        assignment = np.array([s[node] for node in nodes])
        idx = assignment_to_index(assignment, out.card)
        out.val[idx] = np.add(out.val[idx], np.divide(np.float64(ps), np.float64(qs)))

    out.val = np.divide(out.val, np.sum(out.val))
    """ END YOUR CODE HERE """

    return out


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
    target_factors_dict = input_config['target-factors']
    proposal_factors_dict = input_config['proposal-factors']
    assert isinstance(target_factors_dict, dict) and isinstance(proposal_factors_dict, dict)

    def parse_factor_dict(factor_dict):
        var = np.array(factor_dict['var'])
        card = np.array(factor_dict['card'])
        val = np.array(factor_dict['val'])
        return Factor(var=var, card=card, val=val)

    target_factors = {int(node): parse_factor_dict(factor_dict=target_factor) for
                      node, target_factor in target_factors_dict.items()}
    proposal_factors = {int(node): parse_factor_dict(factor_dict=proposal_factor_dict) for
                        node, proposal_factor_dict in proposal_factors_dict.items()}
    evidence = input_config['evidence']
    evidence = {int(node): ev for node, ev in evidence.items()}
    num_iterations = input_config['num-iterations']
    return target_factors, proposal_factors, evidence, num_iterations


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
    target_factors, proposal_factors, evidence, num_iterations = load_input_file(input_file=input_file)

    # solution part
    conditional_probability = _get_conditional_probability(target_factors=target_factors,
                                                           proposal_factors=proposal_factors,
                                                           evidence=evidence, num_iterations=num_iterations)
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
