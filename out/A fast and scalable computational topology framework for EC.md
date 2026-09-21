# A fast and scalable computational topology framework for the Euler characteristic

**Authors:** Daniel J. Laky, Victor M. Zavala  
**Type:** empirical

## Motivation

Fast methods for computing the Euler characteristic (EC) are required to enable processing of high-throughput data and real-time implementations. This represents a challenge when processing high-resolution 2D field data (e.g., images) and 3D field data (e.g., video, hyperspectral images, and space-time data obtained from fluid dynamics and molecular simulations).

## Knowledge gap

Prior work by Snidaro and Foresti presented vertex contribution methods for computing EC in 2D fields, but a major contribution of this work is the generalization of this method to 3D fields (including handling of non-binary fields and parallel implementation).

## Goal

To present parallel algorithms and software implementations to enable fast computations of the Euler characteristic for 2D and 3D fields using vertex contributions, and to demonstrate their performance on synthetic and real-world data.

## Methods

- Vertex contributions approach using cubical simplexes
- Parallel algorithms for 2D and 3D field processing
- Level set filtration/percolation procedures
- Low-memory streaming algorithms for processing data beyond dynamic memory size
- Adjacency function (fadj) for determining vertex contribution types in 3D

## Metrics

- Processing speed in megapixels per second (MP s−1) for 2D fields
- Processing speed in million voxels per second (MV s−1) for 3D fields
- Speedup efficiency with respect to number of CPU cores
- Comparison with GUDHI and CHUNKYEuler tools

## Experiments

Synthetic random fields at standard sizes (1280×720, 1920×1080, 2048×2048, 4096×4096 for 2D; 128×128×128, 256×256×256 for 3D); microscopy data from liquid crystal sensors with varying SO2 concentrations; 3D molecular dynamics simulations of biomass reactants in cosolvent/water mixtures; hyperspectral imaging data of kiwifruit ripeness (360 images); computational fluid dynamics simulations.

## Key findings

- The proposed implementation computes the EC 2-3 orders of magnitude faster than GUDHI
- Processing speeds are comparable to CHUNKYEuler (state-of-the-art tool)
- The vertex contributions approach is more flexible than CHUNKYEuler, enabling computation of other topological descriptors (perimeter, area, volume) in addition to EC
- Parallel implementation achieves 62% efficiency for 2D fields and 75-80% efficiency for 3D fields with 24 cores
- Low-memory versions enable processing of data objects beyond the size of dynamic memory, though with ~10x slowdown
- For real applications: liquid crystal microscopy can process 11 grid-squares in real-time at 30 FPS using serial version; hyperspectral images process at 0.2 seconds per image with 24 cores vs 100 seconds with GUDHI

## Future work

- Extending vertex contribution methods to compute more complex topological descriptors such as fractal dimension
- Generalizing methods to larger dimensions (4D data such as hyperspectral imaging with temporal dimension)
- Exploring optimal decomposition schemes for cubical fields to balance memory efficiency with computational speed
- Generalizing vertex contributions to regular non-cubical lattices or Voronoi cells
- Investigating sensitivity of the system to connectivity, image resolution, filtration values, and preprocessing techniques
