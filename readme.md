# Problem:

Cluster a multi-sequence alignment (MSA) of 400 Covid-19 sequences.  

The goal is to identify the different strains of Covid-19.

To see a full write-up of the analysis and results, visit the project page on [www.meehl.org](www.meehl.org)

# Data:

The data is a FASTA file containing 400 Covid-19 sequences.  The sequences are in the following format:

```fasta
>sequence00000
TGTGTGGCTGTCA...
>sequence00000
TGTGTGGCTGTCA...
...
>sequence00399
TGTGTGGCTGTCA...
```

## Additional Information:
* The data for each sample in the fasta consists of two lines; a header line with the sequence name followed by a line that contains a modified MSA sequence
* A “.” in the MSA indicates that no change is detected in that location between all the sequences
* Each location in the sequence can be either a A,T,G,C,N, and -
* A,T,G,C are unique detectable result at each location in the sample 
* A “N” indicates it could not be determined if it was a A,T,G,C at that location in that sample
* A “-“ indicates that nothing was detected at that location in that sample 



# Approach:
For this exercise, I will not research current best methods.  Instead I will challenge myself to 
develope a procedure using only my current knowledge of clustering and dimensionality reduction.

To challenge myself, I'll avoid libraries like `Biopython` that are specifically designed for bioinformatics.  Instead I will use raw python and `numpy` to manipulate sequences.  For the linear algebra of the clustering techniques, I will use solely `numpy` and only use `sklearn` for some convenience functions.

## Similarity Measure
The first step in clustering will be to generate a similarity data structure from the sequence data.  I will use the Hamming distance as the distance metric.  The Hamming distance is the number of positions at which the corresponding symbols are different.  This is a good distance metric for sequences since it works with discrete categorical data.

The Hamming distance between the sequences can be used to create a neighborhood graph of the sequences.  This neighborhood graph will heavily weight more similar sequences.  This gives us a good sense of the local structure of the data.  We will represent the graph as an adjacency matrix.

## Clustering Algorithms
The next step is to cluster the graph.  I have two ideas for this, using different perspectives.

The first perspective is to use linear algebra to find a low dimensional representation.  I will first convert the similarity matrix into a Laplacian matrix, which allows use to have at least one eigenvalue equal to zero.  We can then use a clustering algorithm like $k$-means on this low-dimensional representation.  This approach is called spectral clustering.

The second perspective is to treat the neighborhood graph as a low dimensional manifold in high-dimensional space.  I will calculate the geodesic distance from the similarity matrix.   I will then use a manifold learning algorithm like ISOMAP to calculate a low-dimensional representation that preserves the geodesic distances.  Then a clustering algorithm like $k$-means can then be used to find the clusters.

For the clustering algorithm, I will use $k$-means.  I will also implement my own version of $k$-means to challenge myself.

# Contents

My analysis is broken into the following notebooks:

1. [Data Cleaning](01_data_cleaning.ipynb)
2. [Spectral Clustering](02_spectral_clustering.ipynb)
3. [My Implementation of $k$-means](03_spectrial_with_my_kmeans.ipynb)
4. [Alternate Method: ISOMAP](04_isomap_clustering.ipynb)

