---
title: Lab 4 Report
subtitle: 
author:
  - Adarsh Srivastava (A0254358X)
date: e0954759@u.nus.edu
tags:
---

## Part 1

**Function definitions:**

1. _sample_step : Here, we use the existing nodes sampled till now (which would include all the parents of current node) as evidence to get a Factor with just the probability of the one node. Then we use that to sample a value.
2. get_topologically_sorted_nodes: For all factors, build a graph with the nodes and the parents (nodes other than current node), remove the evidence nodes, then get a topologically sorted list.
3. get_probability_of_sample: For a given assignment, go through the given factors dict to get the probability of the assignment. Multiply all the probabilities for the assignment in all factors in the dict and return the value.
4. _get_conditional_probability: First, we account for evidence in both proposal and target factors. At the same time, we figure the cardinalities of all nodes under consideration. Then, we get the topologically sorted nodes, and also build the output factor using the nodes and the cardinalities. Then, for the given number of iterations, we sample the nodes, find the p(s) and q(s), and add the dividend (the weight unnormalized) to the sampled assignment in output. Finally, we normalize output before returning. 

## Part 2

**Function definitions:**

1. _sample_step: Use the values in samples of the nodes in markov blanket of node as evidence for the factor provided. This would leave just the current node, and we use the probabilities to sample it. 
2. get_markov_blanket: get the predecessors, successors and precessor of successors and return their concatenated list.
3. _get_conditional_probability: First, we form the networkx graph from all the nodes and edges except for the evidence nodes. Then, we get the topologically sorted list from this graph. This is the list we'll use to sample. For each node in this list, also get the list of nodes in the markov blanket and store them. For each of these nodes, account for the evidence, and then marginalize everything other than the markov blanket and the node itself. At the same time, get the cardinalities and use them to construct our output factor. Finally, run the sample step using initial sample for burn in iterations, then use the output of that as the new initial value for real iterations. In each sample step, add the count to the respective assignment in output factor. Finally, normalize the factor and return. 

