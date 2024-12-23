""" CS5340 Lab 1: Belief Propagation and Maximal Probability
See accompanying PDF for instructions.

Name: Adarsh Srivastava
Email: adarsh.srivastava@u.nus.edu
Student ID: A0254358X
"""

import copy
import math
from typing import List

import numpy as np

from factor import Factor, index_to_assignment, assignment_to_index, generate_graph_from_factors, \
    visualize_graph

"""For sum product message passing"""


def factor_product(A, B):
    """Compute product of two factors.

    Suppose A = phi(X_1, X_2), B = phi(X_2, X_3), the function should return
    phi(X_1, X_2, X_3)
    """
    if A.is_empty():
        return B
    if B.is_empty():
        return A

    # Create output factor. Variables should be the union between of the
    # variables contained in the two input factors
    out = Factor()
    out.var = np.union1d(A.var, B.var)

    # Compute mapping between the variable ordering between the two factors
    # and the output to set the cardinality
    out.card = np.zeros(len(out.var), np.int64)
    mapA = np.argmax(out.var[None, :] == A.var[:, None], axis=-1)
    mapB = np.argmax(out.var[None, :] == B.var[:, None], axis=-1)
    out.card[mapA] = A.card
    out.card[mapB] = B.card

    # For each assignment in the output, compute which row of the input factors
    # it comes from
    out.val = np.zeros(np.prod(out.card))
    assignments = out.get_all_assignments()
    idxA = assignment_to_index(assignments[:, mapA], A.card)
    idxB = assignment_to_index(assignments[:, mapB], B.card)

    """ YOUR CODE HERE
    You should populate the .val field with the factor product
    Hint: The code for this function should be very short (~1 line). Try to
      understand what the above lines are doing, in order to implement
      subsequent parts.
    """
    out.val = A.val[idxA] * B.val[idxB]
    return out


def factor_marginalize(factor, var):
    """Sums over a list of variables.

    Args:
        factor (Factor): Input factor
        var (List): Variables to marginalize out

    Returns:
        out: Factor with variables in 'var' marginalized out.
    """

    """ YOUR CODE HERE
    Marginalize out the variables given in var
    """
    for m_var in var:
        out = Factor()
        m_index = np.where(factor.var == m_var)[0][0]
        m_card = factor.card[m_index]
        out.var = np.delete(factor.var, m_index)
        out.card = np.delete(factor.card, m_index)
        out.val = np.zeros(np.prod(out.card))

        new_assignments = out.get_all_assignments()

        for row in new_assignments:
            summed_rows = [np.insert(row, m_index, x) for x in range(m_card)]
            indexes_to_sum_over = assignment_to_index(summed_rows, factor.card)
            summed_probability = np.sum(factor.val[indexes_to_sum_over])
            out_index = assignment_to_index(row, out.card)
            out.val[out_index] = summed_probability

        factor = out

    return out


def observe_evidence(factors, evidence=None):
    """Modify a set of factors given some evidence

    Args:
        factors (List[Factor]): List of input factors
        evidence (Dict): Dictionary, where the keys are the observed variables
          and the values are the observed values.

    Returns:
        List of factors after observing evidence
    """
    if evidence is None:
        return factors
    out = copy.deepcopy(factors)

    """ YOUR CODE HERE
    Set the probabilities of assignments which are inconsistent with the 
    evidence to zero.
    """
    observed_variables = list(evidence.keys())
    for i in range(len(factors)):
        common_vars = np.intersect1d(factors[i].var, observed_variables)
        assignments = factors[i].get_all_assignments()
        indices_of_evidence = np.isin(factors[i].var, common_vars).nonzero()[0]
        for j in range(len(common_vars)):
            assignments_to_be_zeroed = []
            for a in assignments:
                if a[indices_of_evidence[j]] != evidence[common_vars[j]]:
                    assignments_to_be_zeroed.append(a)
            indices_to_be_zeroed = assignment_to_index(assignments_to_be_zeroed, factors[i].card)
            for idx in indices_to_be_zeroed:
                out[i].val[idx] = 0
    return out


"""For max sum meessage passing (for MAP)"""


def factor_sum(A, B):
    """Same as factor_product, but sums instead of multiplies
    """
    if A.is_empty():
        return B
    if B.is_empty():
        return A

    # Create output factor. Variables should be the union between of the
    # variables contained in the two input factors
    out = Factor()
    out.var = np.union1d(A.var, B.var)

    # Compute mapping between the variable ordering between the two factors
    # and the output to set the cardinality
    out.card = np.zeros(len(out.var), np.int64)
    mapA = np.argmax(out.var[None, :] == A.var[:, None], axis=-1)
    mapB = np.argmax(out.var[None, :] == B.var[:, None], axis=-1)
    out.card[mapA] = A.card
    out.card[mapB] = B.card

    # For each assignment in the output, compute which row of the input factors
    # it comes from
    out.val = np.zeros(np.prod(out.card))
    assignments = out.get_all_assignments()
    idxA = assignment_to_index(assignments[:, mapA], A.card)
    idxB = assignment_to_index(assignments[:, mapB], B.card)

    """ YOUR CODE HERE
    You should populate the .val field with the factor sum. The code for this
    should be very similar to the factor_product().
    """

    out.val = A.val[idxA] + B.val[idxB]

    if (A.val_argmax is None) & (B.val_argmax is None):
        pass
    elif A.val_argmax is None:
        out.val_argmax = [B.val_argmax[i] for i in idxB]
    elif B.val_argmax is None:
        out.val_argmax = [A.val_argmax[i] for i in idxA]
    else:
        out.val_argmax = [{} for i in range(np.prod(out.card))]
        for i in range(len(out.val_argmax)):
            out.val_argmax[i] = {**A.val_argmax[idxA[i]], **B.val_argmax[idxB[i]]}
    return out


def factor_max_marginalize(factor, var):
    """Marginalize over a list of variables by taking the max.

    Args:
        factor (Factor): Input factor
        var (List): Variable to marginalize out.

    Returns:
        out: Factor with variables in 'var' marginalized out. The factor's
          .val_argmax field should be a list of dictionary that keep track
          of the maximizing values of the marginalized variables.
          e.g. when out.val_argmax[i][j] = k, this means that
            when assignments of out is index_to_assignment[i],
            variable j has a maximizing value of k.
          See test_lab1.py::test_factor_max_marginalize() for an example.
    """
    """ YOUR CODE HERE
    Marginalize out the variables given in var. 
    You should make use of val_argmax to keep track of the location with the
    maximum probability.
    """

    for m_var in var:
        out = Factor()
        m_index = np.where(factor.var == m_var)[0][0]
        m_card = factor.card[m_index]
        out.var = np.delete(factor.var, m_index)
        out.card = np.delete(factor.card, m_index)
        out.val = np.zeros(np.prod(out.card))
        out.val_argmax = [{} for i in range(np.prod(out.card))]

        new_assignments = out.get_all_assignments()

        for row in new_assignments:
            rows_to_max_over = [np.insert(row, m_index, x) for x in range(m_card)]
            indexes_to_max_over = assignment_to_index(rows_to_max_over, factor.card)
            max_probability = np.amax(factor.val[indexes_to_max_over])
            out_index = assignment_to_index(row, out.card)
            out.val[out_index] = max_probability

            #check this
            first_index_of_max_prob = np.where(factor.val == max_probability)[0][0]
            assignment_with_max_prob = index_to_assignment([first_index_of_max_prob], factor.card)[0]
            if factor.val_argmax is not None:
                out.val_argmax[out_index] = factor.val_argmax[first_index_of_max_prob]
            out.val_argmax[out_index][m_var] = assignment_with_max_prob[m_index]

        factor = out

    return out


def compute_joint_distribution(factors):
    """Computes the joint distribution defined by a list of given factors

    Args:
        factors (List[Factor]): List of factors

    Returns:
        Factor containing the joint distribution of the input factor list
    """
    joint = Factor()

    """ YOUR CODE HERE
    Compute the joint distribution from the list of factors. You may assume
    that the input factors are valid so no input checking is required.
    """
    for factor in factors:
        joint = factor_product(joint, factor)

    return joint


def compute_marginals_naive(V, factors, evidence):
    """Computes the marginal over a set of given variables

    Args:
        V (int): Single Variable to perform inference on
        factors (List[Factor]): List of factors representing the graphical model
        evidence (Dict): Observed evidence. evidence[k] = v indicates that
          variable k has the value v.

    Returns:
        Factor representing the marginals
    """

    output = Factor()

    """ YOUR CODE HERE
    Compute the marginal. Output should be a factor.
    Remember to normalize the probabilities!
    """
    joint = compute_joint_distribution(observe_evidence(factors, evidence))
    output = factor_marginalize(joint, [v for v in joint.var if v != V])
    # normalize
    output.val = output.val / np.sum(output.val)
    return output


def send_message(graph, messages, sender, taker):
    msgs_to_multiply = []
    for n in graph.neighbors(sender):
        if n != taker:
            msgs_to_multiply.append(messages[n][sender])
    if (graph.nodes[sender] is not None) and ('factor' in graph.nodes[sender]):
        msgs_to_multiply.append(graph.nodes[sender]['factor'])
    msgs_to_multiply.append(graph.edges[sender, taker]['factor'])

    msg_unmarginalized = compute_joint_distribution(msgs_to_multiply)
    messages[sender][taker] = factor_marginalize(msg_unmarginalized, [sender])


def collect(graph, messages, collector, giver):
    for n in graph.neighbors(giver):
        if n != collector:
            collect(graph, messages, giver, n)
    send_message(graph, messages, giver, collector)


def distribute(graph, messages, giver, collector):
    send_message(graph, messages, giver, collector)
    for n in graph.neighbors(collector):
        if n != giver:
            distribute(graph, messages, collector, n)


def compute_marginal(marginals, graph, messages, i):
    msgs = []
    for n in graph.neighbors(i):
        msgs.append(messages[n][i])
    if (graph.nodes[i] is not None) and ('factor' in graph.nodes[i]):
        msgs.append(graph.nodes[i]['factor'])

    marginal = compute_joint_distribution(msgs)
    marginal.val = marginal.val / np.sum(marginal.val)
    marginals.append(marginal)


def compute_marginals_bp(V, factors, evidence):
    """Compute single node marginals for multiple variables
    using sum-product belief propagation algorithm

    Args:
        V (List): Variables to infer single node marginals for
        factors (List[Factor]): List of factors representing the grpahical model
        evidence (Dict): Observed evidence. evidence[k]=v denotes that the
          variable k is assigned to value v.

    Returns:
        marginals: List of factors. The ordering of the factors should follow
          that of V, i.e. marginals[i] should be the factor for variable V[i].
    """
    # Dummy outputs, you should overwrite this with the correct factors
    marginals = []

    # Setting up messages which will be passed
    factors = observe_evidence(factors, evidence)
    graph = generate_graph_from_factors(factors)

    # Uncomment the following line to visualize the graph. Note that we create
    # an undirected graph regardless of the input graph since 1) this
    # facilitates graph traversal, and 2) the algorithm for undirected and
    # directed graphs is essentially the same for tree-like graphs.
    visualize_graph(graph)

    # You can use any node as the root since the graph is a tree. For simplicity
    # we always use node 0 for this assignment.
    root = 0

    # Create structure to hold messages
    num_nodes = graph.number_of_nodes()
    messages = [[None] * num_nodes for _ in range(num_nodes)]

    """ YOUR CODE HERE
    Use the algorithm from lecture 4 and perform message passing over the entire
    graph. Recall the message passing protocol, that a node can only send a
    message to a neighboring node only when it has received messages from all
    its other neighbors.
    Since the provided graphical model is a tree, we can use a two-phase 
    approach. First we send messages inward from leaves towards the root.
    After this is done, we can send messages from the root node outward.
    
    Hint: You might find it useful to add auxilliary functions. You may add 
      them as either inner (nested) or external functions.
    """
    for n in graph.neighbors(root):
        collect(graph, messages, root, n)

    for n in graph.neighbors(root):
        distribute(graph, messages, root, n)

    for i in V:
        compute_marginal(marginals, graph, messages, i)

    return marginals


def max_send_message(graph, messages, sender, taker):
    msgs_to_sum = []
    for n in graph.neighbors(sender):
        if n != taker:
            msgs_to_sum.append(messages[n][sender])
    if (graph.nodes[sender] is not None) and ('factor' in graph.nodes[sender]):
        msgs_to_sum.append(graph.nodes[sender]['factor'])
    msgs_to_sum.append(graph.edges[sender, taker]['factor'])

    msg_unmarginalized = Factor()
    for msg in msgs_to_sum:
        msg_unmarginalized = factor_sum(msg_unmarginalized, msg)

    messages[sender][taker] = factor_max_marginalize(msg_unmarginalized, [sender])


def max_collect(graph, messages, collector, giver):
    for n in graph.neighbors(giver):
        if n != collector:
            max_collect(graph, messages, giver, n)
    max_send_message(graph, messages, giver, collector)


def max_set_value(graph, messages, giver, collector):
    pass


def max_distribute(graph, messages, giver, collector):
    max_set_value(graph, messages, giver, collector)
    for n in graph.neighbors(collector):
        if n != giver:
            max_distribute(graph, messages, collector, n)


def map_eliminate(factors, evidence):
    """Obtains the maximum a posteriori configuration for a tree graph
    given optional evidence

    Args:
        factors (List[Factor]): List of factors representing the graphical model
        evidence (Dict): Observed evidence. evidence[k]=v denotes that the
          variable k is assigned to value v.

    Returns:
        max_decoding (Dict): MAP configuration
        log_prob_max: Log probability of MAP configuration. Note that this is
          log p(MAP, e) instead of p(MAP|e), i.e. it is the unnormalized
          representation of the conditional probability.
    """

    max_decoding = {}
    log_prob_max = 0.0

    """ YOUR CODE HERE
    Use the algorithm from lecture 5 and perform message passing over the entire
    graph to obtain the MAP configuration. Again, recall the message passing 
    protocol.
    Your code should be similar to compute_marginals_bp().
    To avoid underflow, first transform the factors in the probabilities
    to **log scale** and perform all operations on log scale instead.
    You may ignore the warning for taking log of zero, that is the desired
    behavior.
    """
    factors = observe_evidence(factors, evidence)

    np.seterr(divide='ignore')
    for factor in factors:
        factor.val = np.log(factor.val)

    graph = generate_graph_from_factors(factors)

    root = 0

    num_nodes = graph.number_of_nodes()
    messages = [[None] * num_nodes for _ in range(num_nodes)]

    for n in graph.neighbors(root):
        max_collect(graph, messages, root, n)

    # calculate max prob at root
    msgs = []
    message_at_root = Factor()
    for n in graph.neighbors(root):
        msgs.append(messages[n][root])
    if (graph.nodes[root] is not None) and ('factor' in graph.nodes[root]):
        message_at_root = graph.nodes[root]['factor']

    for msg in msgs:
        message_at_root = factor_sum(message_at_root, msg)

    root_max_val = np.argmax(message_at_root.val)
    message_at_root.val_argmax[root_max_val][root] = root_max_val

    max_decoding = message_at_root.val_argmax[root_max_val]
    max_decoding = {key: max_decoding[key] for key in sorted(max_decoding.keys()) if key not in evidence.keys()}
    log_prob_max = message_at_root.val[root_max_val]

    # for n in graph.neighbors(root):
    #     max_distribute(graph, messages, root, n)

    return max_decoding, log_prob_max
