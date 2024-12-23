import numpy as np
import networkx as nx
from networkx.algorithms import tree
from factor import Factor
from factor_utils import factor_product
import itertools

""" ADD HELPER FUNCTIONS HERE (IF NEEDED) """

""" END ADD HELPER FUNCTIONS HERE """


def _get_clique_factors(jt_cliques, factors):
    """
    Assign node factors to cliques in the junction tree and derive the clique factors.

    Args:
        jt_cliques: list of junction tree maximal cliques e.g. [[x1, x2, x3], [x2, x3], ... ]
        factors: list of factors from the original graph

    Returns:
        list of clique factors where the factor(jt_cliques[i]) = clique_factors[i]
    """
    clique_factors = [Factor() for _ in jt_cliques]

    """ YOUR CODE HERE """
    jt_cliques_with_index = list(enumerate(jt_cliques))
    jt_cliques_with_index.sort(key=lambda x: len(x[1]))
    factors.sort(key=lambda x: len(x.var))

    for factor in factors:
        for i, clique in jt_cliques_with_index:
            if set(factor.var).issubset(set(clique)):
                clique_factors[i] = factor_product(clique_factors[i], factor)
                break

    """ END YOUR CODE HERE """

    assert len(clique_factors) == len(jt_cliques), 'there should be equal number of cliques and clique factors'
    return clique_factors


def _get_jt_clique_and_edges(nodes, edges):
    """
    Construct the structure of the junction tree and return the list of cliques (nodes) in the junction tree and
    the list of edges between cliques in the junction tree. [i, j] in jt_edges means that cliques[j] is a neighbor
    of cliques[i] and vice versa. [j, i] should also be included in the numpy array of edges if [i, j] is present.
    
    Useful functions: nx.Graph(), nx.find_cliques(), tree.maximum_spanning_edges(algorithm="kruskal").

    Args:
        nodes: numpy array of nodes [x1, ..., xN]
        edges: numpy array of edges e.g. [x1, x2] implies that x1 and x2 are neighbors.

    Returns:
        list of junction tree cliques. each clique should be a maximal clique. e.g. [[X1, X2], ...]
        numpy array of junction tree edges e.g. [[0,1], ...], [i,j] means that cliques[i]
            and cliques[j] are neighbors.
    """
    jt_cliques = []
    jt_edges = np.array(edges)  # dummy value

    """ YOUR CODE HERE """
    ordering = nodes[::-1]

    g = nx.Graph(list(map(tuple, edges)))

    for node_to_eliminate in ordering:
        g.add_edges_from(list(itertools.combinations([n for n in g.neighbors(node_to_eliminate)], 2)))
        cliques_iterator = nx.find_cliques(g, nodes=[node_to_eliminate])
        for clique in cliques_iterator:
            jt_cliques.append(clique)
        g.remove_node(node_to_eliminate)

    clique_graph = nx.Graph()
    for i, j in itertools.combinations(range(len(jt_cliques)), 2):
        separator_set = tuple(set(jt_cliques[i]).intersection(set(jt_cliques[j])))
        if separator_set:
            clique_graph.add_weighted_edges_from([(i, j, len(separator_set))])

    mst = tree.maximum_spanning_edges(clique_graph, algorithm="kruskal", data=False)

    jt_edges = np.array(list(mst))
    """ END YOUR CODE HERE """

    return jt_cliques, jt_edges


def construct_junction_tree(nodes, edges, factors):
    """
    Constructs the junction tree and returns its the cliques, edges and clique factors in the junction tree.
    DO NOT EDIT THIS FUNCTION.

    Args:
        nodes: numpy array of random variables e.g. [X1, X2, ..., Xv]
        edges: numpy array of edges e.g. [[X1,X2], [X2,X1], ...]
        factors: list of factors in the graph

    Returns:
        list of cliques e.g. [[X1, X2], ...]
        numpy array of edges e.g. [[0,1], ...], [i,j] means that cliques[i] and cliques[j] are neighbors.
        list of clique factors where jt_cliques[i] has factor jt_factors[i] where i is an index
    """
    jt_cliques, jt_edges = _get_jt_clique_and_edges(nodes=nodes, edges=edges)
    jt_factors = _get_clique_factors(jt_cliques=jt_cliques, factors=factors)
    return jt_cliques, jt_edges, jt_factors
