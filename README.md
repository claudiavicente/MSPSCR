# INTRODUCTION

**Metabolic state prediction at single-cell resolution** is a project developed as a Bachelor's Thesis (TFG), to recover metabolic states from single-cell expression data. This entails the development of a computational tool, to integrate expression data and metabolic models at the single-cell level.

## FEATURES

This repository contains: 
1. **rFASTCORMICS_examples**: rFASTCORMICS (Pacheco et al., 2019, EBioMedicine) example and part of the additional example scripts can be found. There are also Jupyter Notebooks to simulate the generated single models with FBA.
    * scripts that end with `"example"` use Recon2 as consistent model
    * scripts that end with `"example_3D"` use Recon3D as consistent model
    * scripts starting with `"FS"` carry out the models simulation
2. **Tests**: the pipeline steps are tested on subsets of RNA-seq and PBMC 3K datasets.
3. **Pipeline/PBMC3K**: the final computational pipeline is applied to the PBMC 3K dataset.
   > The *Pipeline/PBMC3K/CMR_rFASTCORMICS_PBMC3K.html* can be visualized here: [![HTML Preview](https://img.shields.io/badge/HTML_Preview-View-pink.svg)](https://htmlpreview.github.io/?https://github.com/claudiavicente/MSPSCR/blob/main/Pipeline/PBMC3K/CMR_rFASTCORMICS_PBMC3K.html).
   > The ".mlx" file of the same script can be found in the same directory.

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

Middle-steps data (as fluxome data frame and cell-types identification) are stored [here](https://universitatdevic-my.sharepoint.com/:f:/g/personal/claudia_vicente_uvic_cat/Egr1py82Nt5Lg1j-etbi5fQBe69Qd8aiAIgho4Ne_R-_TQ) and can also be downloaded.
