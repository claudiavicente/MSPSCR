# INTRODUCTION

**Metabolic trajectory inference at single-cell resolution** is a project developed as a Bachelor's Thesis (TFG), to infer metabolic trajectories from single-cell expression data. This entails the development of a computational tool, to integrate expression data and metabolic models at the single-cell level.

## FEATURES

This repository contains: 
1. **rFASTCORMICS_examples**: rFASTCORMICS example and part of the additional example scripts can be found. There are also Jupyter Notebooks to simulate the generated single models with FBA.
  - scripts that end with *"example"* uses Recon2 as consistent model
  - scripts that end with *"example_3D"* uses Recon3D as consistent model
  - scripts starting with *"FS"* carry out the models simulation
2. **Tests**: the pipeline steps are tested on subsets of RNA-seq and PBMC 3K datasets.
3. **PBMC3K**: the final computational pipeline is applied to the PBMC 3K dataset.

## PBMC3K SCRIPTS ORGANIZATION

| Abbreviation | Description                            |
|--------------|----------------------------------------|
| PP           | Preprocessing                          |
| CMR          | Context-specific models reconstruction|
| FS           | Fluxes simulation                      |
| VIS          | Visualization (and analysis)           |

## DATA ACCESS

The used RNA-seq data can be obtained from the [GTEx Portal](https://www.gtexportal.org/).

The PBMC3K data is available at 10x Genomics, it can be directly downloaded [here](http://cf.10xgenomics.com/samples/cell-exp/1.1.0/pbmc3k/pbmc3k_filtered_gene_bc_matrices.tar.gz).

Middle-steps data (as fluxome dataframe and cell-types identification) are stored [here](https://universitatdevic-my.sharepoint.com/:f:/g/personal/claudia_vicente_uvic_cat/Egr1py82Nt5Lg1j-etbi5fQBe69Qd8aiAIgho4Ne_R-_TQ?e=1idV9J) and can also be downloaded.
