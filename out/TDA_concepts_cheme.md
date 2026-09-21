# Topological data analysis: Concepts, computation, and applications in chemical engineering

**Authors:** Alexander D. Smith, Paweł Dłotko, Victor M. Zavala  
**Type:** review

## Motivation

Statistical and signal processing techniques provide limited capabilities to analyze certain types of datasets. Topological Data Analysis (TDA) addresses this limitation by analyzing data from a fundamentally different perspective—representing datasets as geometric objects and extracting topological features that are multiscale and stable under perturbations (noise, translation, rotation).

## Knowledge gap

Prior work in data analysis relies primarily on statistical and signal processing paradigms, which fail to capture geometric and topological structure of data. TDA fills this gap by providing coordinate-independent, metric-robust methods for analyzing data geometry.

## Goal

To review the key mathematical concepts and computational methods of TDA and present applications in chemical engineering, demonstrating how persistent homology techniques can extract informative features from complex datasets that correlate with emerging features of practical interest.

## Methods

- Simplicial homology
- Persistent homology
- Čech complexes
- Morse filtration
- Cubical complexes
- Persistence diagrams
- Persistence images
- Persistence landscapes
- Vectorization of persistence diagrams
- Inverse analysis via integer optimization

## Metrics

- Classification accuracy (perfect classification on synthetic point clouds; 85±2% on liquid crystal images)
- Mean squared error (0.07±0.003 for 3D field reactivity prediction)
- Wasserstein distance (for comparing persistence diagrams)
- Bottleneck distance (for comparing persistence diagrams)
- 5-fold cross validation

## Experiments

Multiple case studies including: (1) binary classification of 2D point clouds; (2) phase-plane analysis of dynamical systems with perturbations and noise; (3) topology of 2D scalar fields from diffusion equations with varying diffusion coefficients; (4) optical response of liquid crystal sensors to chemical warfare agent simulants (DMMP) vs. water; (5) flow cytometry scatter field evolution during cell stimulation; (6) 3D water density fields from molecular dynamics simulations correlated with experimental reactivity parameters.

## Key findings

- TDA extracts topological features that distinguish datasets with identical statistical descriptors
- Persistence diagrams are stable under perturbations and vary continuously with data changes
- Topological features from point clouds enable perfect classification via linear SVM
- Phase-plane topology captures dynamical system behavior and detects anomalies with minimal information
- Topological features of 2D scalar fields correlate continuously with diffusion coefficients
- Liquid crystal sensor optical patterns show 85±2% classification accuracy based on topological features; inverse analysis reveals DMMP exposure creates few large clusters while water exposure creates many small clusters
- 3D water density topology from MD simulations predicts experimental reactivity (MSE 0.07±0.003) with simpler models than CNNs
- Topological features of probability density functions characterize temporal evolution in flow cytometry data

## Future work

- Expansion of TDA applications to additional chemical engineering problems
- Development of more scalable computational methods for large datasets
- Integration of TDA with other machine learning techniques
- Application to higher-dimensional flow cytometry data beyond 2D
- Further investigation of inverse analysis for physical interpretation of topological features
