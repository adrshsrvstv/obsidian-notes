Adarsh Srivastava  
adarsh.srivastava@u.nus.edu  
A0254358X

- **_get_clique_factors**: Here we are assigning factors to cliques in ascending  order of cardinality (to assign smaller cliques with relevant factors first) and checking if factor is a subset of clique before assigning.
- **_get_jt_clique_and_edges**: We are performing dummy variable elimination steps for an arbitrary ordering and finding find maximal cliques from each elimination. For all such cliques, we are connecting them with each other if they have a common factor, with cardinality of sepset being the weight of the edge. Then performing Kruskal's to find the mst, which is our JT.
- **_update_mrf_w_evidence**: We remove evidence nodes since their value is fixed - adding an edge between parents to avoid disjoint graphs. We take 'slices' from all factors that have any evidence node using factor_evidence. 
- **_get_clique_potentials**: Standard sum-product algorithm of collect then distribute potentials.
- **_get_node_marginal_probabilities**: Marginalizing smallest cliques first to find marginal probabilities. We arrange cliques potentials in ascending order of cardinality of variables, then using the smallest potential containing a variable to marginalize.