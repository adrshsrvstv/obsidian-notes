---
title: Big Data - Lecture 5, 6
author:
  - Adarsh Srivastava
date: 17 November, 2024
tags:
---

- broadcast join - map side: small table should fit into main memory because otherwise lots of disk IO due to random access
	- each mapper gets
		- the full small table in memory
		- a split of the large table
	- and emits the joined keys from its own split
	- reducer is identity function or not needed at all
- reduce side join (common join): 
	- mapper gets
		- a split of the one of the tables
	- and simply emit (key, entire row/tuple) for all rows of the table split they are operating on, with key being the key to join on
	- reducer gets all values for a key and actually does the join
	- this is much more expensive because mapper emits a large output, then reducer needs to join key wise. Plus key wise shuffling and sorting needs to happen.
		- we can use **secondary sort** by table name to ensure all tuples from one table arrive before the other table so we can cross and join them better

- Similarity measures:
	- manhattan distance = sum(|a-b|)
	- euclidean distance
	- cosine similarity = $cos(\theta)$ = a.b/|a|.|b|
	- Jaccard similarity = $\frac{|A \cap B|}{|A \cup B|}$
	- Jaccard distance = 1- jaccard similarity
- Finding similar documents in a database:
	- All pairs similarity: find all 'near duplicate' pairs in a corpus
	- Similarity search: given a document D, find all "near duplicates" of D

- Idea: Actual pairwise similarity calculation for a huge corpus is intractable - do approximate similarity calculation

### Locality Sensitive Hashing
It's an algorithm for solving the approximate or exact Near Neighbor Search in high dimensional spaces. It hashes similar input items into the same "buckets" with high probability.

Our goal is to replace large sets by much smaller representations called “signatures.” The important property we need for signatures is that we can compare the signatures of two sets and estimate the Jaccard similarity of the underlying sets from the signatures alone.

- Techniques:
	- Shingling: Instead of searching by words, break each doc into a set of k-shingles, where a k-shingle is a contiguous block of k words in the document. *k should be picked large enough that the probability of any given shingle appearing in any given document is low.*
	- Locality preserving hash function: a hash function $h$ is called locality preserving if probability of $h(c_1)=h(c_2)$ is high when documents $c_1$ and $c_2$ are similar, i.e., $P(h(c_1)=h(c_2)) \approx sim(c_1, c_2)$  
	- Minhashing:
		- In principle - it is selecting a random hash. ("To minhash a set represented by a column of the characteristic matrix, pick a permutation of the rows. The minhash value of any column is the number of the first row, in the permuted order, in which the column has a 1." = select any random hash)
		- In practice = just use the smallest hash. This is random enough.
		- Selecting a random hash is in effect equivalent to selecting a random shingle to compare - since the hash functions are chosen such that there's only a small chance of collision.
- How to compare?
	- have a certain number of hash functions - say 200.
	- 200 has function? WTF? Well, you can have one good hash function and have 200 distinct random numbers to XOR that hash function with, and you get 200 hash functions.
	- Now we have a vector for each document - where we select the minhashes for all 200 hash functions applied on all the shingles of each document. 
	- Two documents are candidate pairs if a "sufficient number" of minhashes are the same for them. Let's say 50. We compare the minhash vectors for at least that many matches.
- Map reduce implementation (for just one minhash)
	- Map phase: (id, document) -> (id, set of shingles) -> emit (minhash of shingles, id)
	- Reduce phase: (minhash, list of ids) -> (minhash, pair of docs from this list) -> emit(pair if actually similar)


Reading on why minhashing works:
- [infolab.stanford.edu/\~ullman/mmds/ch3.pdf](http://infolab.stanford.edu/~ullman/mmds/ch3.pdf)
- [MinHash for dummies](http://matthewcasperson.blogspot.com/2013/11/minhash-for-dummies.html)
- Summary - selecting 200 minhashes from 200 hashing algorithms is equivalent to selecting 200 shingles randomly from a document set of shingles. Comparing randomly selected shingles for similarity is a good approximation of actual similarity between all shingles, if the shingles are of a decent size, say 5 or 6 (so that probability of finding a shingle in a document is low). ( also look at [avoidtrouble.wordpress.com/wp-content/uploads/2019/02/14-k-means-algorithm-30-jan-2018\_reference-material-iii\_findingsimilarsets.pdf](https://avoidtrouble.wordpress.com/wp-content/uploads/2019/02/14-k-means-algorithm-30-jan-2018_reference-material-iii_findingsimilarsets.pdf))


## Clustering - K means

- K means: 
	- choose initial centers randomly or acc to kmeans++
	- assign classes to all points same as their "nearest" centroid
	- recompute centroid to be mean of all class points
	- repeat 2-3 until convergence
- 