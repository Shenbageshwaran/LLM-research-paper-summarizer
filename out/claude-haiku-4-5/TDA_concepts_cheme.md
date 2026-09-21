# Topological data analysis: Concepts, computation, and applications in chemical engineering

**Authors:** Alexander D. Smith, Paweł Dłotko, Victor M. Zavala  
**Type:** review

## Motivation

Statistical and signal processing techniques provide limited capabilities to analyze certain types of datasets. Topological Data Analysis (TDA) addresses this limitation by analyzing data from a fundamentally different perspective—representing datasets as geometric objects and extracting topological features that are multiscale and stable under perturbations (noise, translation, rotation).

## Knowledge gap

Prior work in data analysis relies primarily on statistical and signal processing paradigms that cannot capture geometric and topological structure of data. The paper addresses the gap by introducing TDA as a complementary approach that quantifies shape and topology of data in a coordinate-independent and noise-robust manner.

## Goal

To review the key mathematical concepts and computational methods of TDA and present applications in chemical engineering, demonstrating how persistent homology techniques can extract informative topological features from complex datasets that correlate with emerging features of practical interest.

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
- Mean squared error (0.07±0.003 for reactivity prediction from 3D MD simulations)
- Wasserstein distance (for comparing persistence diagrams)
- Bottleneck distance (for comparing persistence diagrams)
- 5-fold cross validation

## Experiments

Point cloud classification; time-series and phase-plane analysis; 2D scalar field topology (diffusion equation); liquid crystal sensor image analysis; flow cytometry probability density function analysis; 3D molecular dynamics simulations of water density fields

## Key findings

- TDA extracts topological features that distinguish datasets with identical statistical descriptors
- Persistence diagrams are stable under perturbations and continuous deformations
- Topological features from point clouds enable perfect binary classification via SVM
- Topological features of 2D diffusion fields correlate continuously with diffusion coefficients
- Liquid crystal sensor optical patterns show 85±2% classification accuracy based on topological features
- 3D water density topology from MD simulations predicts experimental reactivity with MSE of 0.07±0.003
- Inverse analysis reveals physically meaningful geometric features driving classification decisions

## Future work

- Extension of TDA to higher-dimensional flow cytometry data beyond 2D
- Development of more sophisticated approaches for multi-channel image analysis (e.g., RGB channels)
- Scalability improvements for large-scale datasets
- Integration of TDA with other machine learning techniques
- Application to additional chemical engineering problems beyond those demonstrated
