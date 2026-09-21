# Euler Characteristic Tools for Topological Data Analysis

**Authors:** Olympio Hacquard, Vadim Lebovici  
**Type:** empirical

## Motivation

Extracting topological information from data typically relies on persistence diagrams, which are expensive to compute and difficult to vectorize for machine learning. While Euler characteristic-based descriptors are simpler and computationally cheaper, they have been underexplored. The paper argues that Euler characteristic tools deserve more attention because they: (1) demonstrate good predictive power in various settings, (2) can be computed in linear time instead of matrix multiplication time, (3) have known theoretical results for random complexes, and (4) naturally generalize to multi-parameter settings where persistence diagrams lack complete combinatorial descriptors.

## Knowledge gap

Prior work on Euler characteristic techniques in topological data analysis has been limited and scattered. While persistence diagrams are well-studied, there is no complete combinatorial descriptor for multi-parameter families of topological spaces, making Euler characteristic tools (which naturally generalize to multi-parameter settings) underexplored. Additionally, theoretical guarantees (stability and asymptotic properties) for Euler characteristic descriptors and their hybrid transforms have not been systematically established.

## Goal

To demonstrate that Euler characteristic profiles and their hybrid transforms are informative and highly efficient topological descriptors that achieve state-of-the-art performance in supervised tasks at minimal computational cost, and to provide theoretical guarantees including stability results and asymptotic properties for these descriptors.

## Methods

- Euler characteristic profiles (pointwise Euler characteristic of families of simplicial complexes)
- Hybrid transforms (integral transforms mixing Lebesgue integration with Euler characteristic techniques)
- Sublevel-sets filtrations and function-Cech filtrations
- Alpha complexes and Cech complexes for point clouds
- Kernel density estimators for multi-parameter filtrations
- Heat kernel signature and Ricci/Forman curvatures for graph data
- XGBoost, random forest, and support vector machine classifiers

## Metrics

- R² score (curvature regression)
- Classification accuracy with standard deviation
- Computation time in seconds
- Feature dimension reduction analysis
- PCA and LDA visualizations for unsupervised/supervised clustering

## Experiments

Curvature regression on surfaces (1000 points on unit disk); ORBIT5K dataset (700 training and 300 testing orbits for each of 5 classes); Sydney urban objects recognition dataset (3D LIDAR point clouds, multi-class classification); Graph classification on 8 benchmark datasets (mutag, cox2, dhfr, proteins, collab, imdb-b, imdb-m, nci1); Synthetic experiments on Poisson and Ginibre point processes, manifold samplings (torus and sphere), and signal-in-clutter noise detection.

## Key findings

- Euler characteristic curves achieve state-of-the-art accuracy comparable to persistence diagram methods (e.g., 83.8% on ORBIT5K with ECC+XGB vs 91.2% for Persformer, but at much lower computational cost)
- Hybrid transforms act as efficient information compressors, requiring much smaller resolution than Euler profiles to reach similar performance
- Hybrid transforms outperform Euler profiles in unsupervised tasks and with linear classifiers due to their ability to capture fine-grained information
- Euler profiles are 10+ times faster to compute than persistence images; hybrid transforms are 4 times faster in the two-parameter case
- Multi-parameter descriptors (up to 5 parameters) can be computed efficiently, outperforming persistence diagrams on graph classification
- Stability results show L¹ norms of Euler profiles are controlled by signed 1-Wasserstein distance between signed barcodes
- Asymptotic normality and law of large numbers established for hybrid transforms in both one-parameter and multi-parameter settings

## Future work

- Application to cubical complexes built from images and 3D volumes, with thorough benchmarking against other persistence methods and state-of-the-art image processing methods
- Study of time-varying simplicial complexes using non-monotone filtrations
- Investigation of multi-parameter persistence with more than 3 filtration parameters
- Derivation of multi-dimensional central limit theorems for hybrid transforms beyond the current translation-invariant assumptions
