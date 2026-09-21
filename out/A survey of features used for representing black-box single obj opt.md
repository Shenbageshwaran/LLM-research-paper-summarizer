# A survey of features used for representing black-box single-objective continuous optimization

**Authors:** Gjorgjina Cenikj, Ana Nikolikj, Gašper Petelin, Niki van Stein, Carola Doerr, Tome Eftimov  
**Type:** review

## Motivation

Different optimization problem instances and performance criteria require different algorithm instances for optimal resolution. Harnessing performance complementarity through per-instance algorithm selection and other machine learning tasks requires input features that characterize problem instances, algorithm instances, and their interactions. These features support algorithm selection, algorithm configuration, problem classification, and complementarity analysis of benchmark suites.

## Knowledge gap

Earlier surveys (such as [24,25]) provided valuable taxonomies but offered limited attention to algorithm features and completely omitted trajectory-based approaches. Tutorials ([18,26]) played an important pedagogical role but did not provide comprehensive synthesis of state-of-the-art and did not cover recent deep learning methods (CNN-based fitness maps, TransOpt, Deep-ELA, DoE2Vec) and trajectory-based representations (DynamoRep, Opt2Vec, probing trajectories).

## Goal

To provide a comprehensive overview of features used to represent optimization problem instances, algorithm instances, and their interactions in single-objective continuous black-box optimization, covering problem landscape features, algorithm features, high-level problem-algorithm interaction features, and trajectory-based features, with focus on recent works from the past five years and their applications in machine learning tasks.

## Methods

- The survey reviews and categorizes feature representation approaches into four families: (1) problem landscape features including high-level features, exploratory landscape analysis (ELA), topological landscape analysis (TLA), and deep learning-based approaches (CNNs, point cloud transformers, variational autoencoders, transformers); (2) algorithm features based on source code analysis; (3) high-level problem-algorithm interaction features including CNN-based, transformer-based, performance-based, graph embedding, and graph neural network approaches; (4) trajectory-based features including internal parameters, trajectory-based ELA, DynamoRep, Opt2Vec, iterative-based ELA, local optima networks, probing trajectories, and ClustOpt.

## Metrics

_none stated_

## Experiments

The survey reviews empirical studies using established benchmark suites (BBOB, CEC, Nevergrad) and problem generators (ISA, GP, TR, Affine, GKLS). Applications include algorithm selection, problem classification, performance prediction, and complementarity analysis of benchmark suites. Studies vary in sample sizes (ranging from 6d to 1000d samples), repetitions (1 to 100), and problem dimensions (primarily d ∈ {2,3,5,10,20}, with some extending to d ∈ {30,50}).</experiments>
<parameter name="metrics">Algorithm performance measured through fixed-budget evaluation (solution quality or target precision), fixed-target evaluation (budget needed to reach target quality), anytime performance (empirical cumulative distribution functions, empirical attainment functions). Feature evaluation uses classification accuracy, regression error metrics, ranking metrics, and complementarity measures (clustering, dimensionality reduction).

## Key findings

- ELA features remain the most commonly used problem landscape features but suffer from poor robustness to sampling strategy and sample size, and lack invariance to transformations (shifting, scaling, rotation)
- TLA and Deep-ELA features demonstrate invariance to problem transformations and comparable predictive performance to ELA
- Algorithm features are relatively underexplored compared to problem landscape features
- High-level problem-algorithm interaction features effectively capture algorithm performance but often require expensive prior computation of ELA features or algorithm runs
- Trajectory-based features provide rich information about problem-algorithm interactions without additional function evaluations, with varying computational costs suitable for different use cases
- Current algorithm selection models show poor generalization to unseen problem instances and across different benchmark suites beyond BBOB
- Lack of standardization in experimental setup (sample sizes, repetitions, dimensions, evaluation protocols) hinders reliable comparison of feature groups
- Most empirical work focuses on low-dimensional problems (d ≤ 20), with limited evaluation in higher dimensions

## Future work

- Develop standardized protocols for feature calculation including sample size per dimension, number of repetitions, and dimensions for benchmarking
- Explore adaptive sampling and aggregation schemes for ELA features to address sensitivity to sampling strategy and sample size
- Improve interpretability of deep learning-based landscape features to understand why particular decisions are made
- Conduct comprehensive comparative studies of feature groups under fixed experimental setups with consistent datasets and evaluation protocols
- Extend evaluation beyond BBOB benchmark to diverse problem benchmarks (CEC, Nevergrad) and problem generators to improve generalization
- Develop invariance-aware feature design that is robust to problem transformations
- Explore continual learning frameworks for algorithm selection models to handle dynamic problem distributions
- Investigate lightweight trajectory-based features for online early-run selection and warm-start switching
- Develop proper algorithm features representing modular frameworks and functional/structural characteristics of metaheuristics
- Perform systematic evaluations of feature robustness across different dimensionalities and assess sensitivity to function transformations and stochasticity
