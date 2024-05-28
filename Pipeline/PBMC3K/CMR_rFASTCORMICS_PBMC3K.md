::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: rtcContent
# rFASTCORMICS FOR THE PBMC 3K scRNA-seq DATASET {#rfastcormics-for-the-pbmc-3k-scrna-seq-dataset .S0}

::: S1
(Pacheco et al., 2019, EBioMedicine)
:::

##  {#section .S2}

## SET UP {#set-up .S3}

:::::::::::::::::: CodeBlock
:::: inlineWrapper
::: S4
[addpath(genpath(pwd)) ]{style="white-space: pre;"}
:::
::::

:::: inlineWrapper
::: S5
[addpath(genpath([\'/Users/claudiavicentecomorera/cobratoolbox\']{style="color: rgb(160, 32, 240);"}))
]{style="white-space: pre;"}
:::
::::

:::::::: {.inlineWrapper .outputs}
::: S6
[feature [astheightlimit
2000]{style="color: rgb(160, 32, 240);"}]{style="white-space: pre;"}
:::

:::::: S7
::::: {.inlineElement .eoOutputWrapper .embeddedOutputsVariableStringElement uid="9C947231" scroll-top="null" scroll-left="null" data-width="732" data-height="21" hashorizontaloverflow="false" testid="output_0" style="max-height: 261px; width: 762.026px;"}
:::: textElement
<div>

[ans = ]{.variableNameElement}\'feature astHeightLimit 500\'

</div>
::::
:::::
::::::
::::::::

::::::: {.inlineWrapper .outputs}
::: S8
[initCobraToolbox(false)]{style="white-space: pre;"}
:::

::::: S7
:::: {.inlineElement .eoOutputWrapper .embeddedOutputsTextElement .scrollableOutput uid="47EB5A20" scroll-top="null" scroll-left="null" data-width="732" data-height="2432" hashorizontaloverflow="true" testid="output_1" style="max-height: 261px; width: 762.026px;"}
::: textElement
\_\_\_\_\_ \_\_\_\_\_ \_\_\_\_\_ \_\_\_\_\_ \_\_\_\_\_ \| / \_\_\_\| /
\_ \\ \| \_ \\ \| \_ \\ / \_\_\_ \\ \| COnstraint-Based Reconstruction
and Analysis \| \| \| \| \| \| \| \|\_\| \| \| \|\_\| \| \| \|\_\_\_\|
\| \| The COBRA Toolbox - 2024 \| \| \| \| \| \| \| \_ { \| \_ / \|
\_\_\_ \| \| \| \|\_\_\_ \| \|\_\| \| \| \|\_\| \| \| \| \\ \\ \| \| \|
\| \| Documentation: \\\_\_\_\_\_\| \\\_\_\_\_\_/ \|\_\_\_\_\_/ \|\_\|
\\\_\\ \|\_\| \|\_\| \| <http://opencobra.github.io/cobratoolbox> \| \>
Checking if git is installed \... Done (version: 2.39.3). \> Checking if
the repository is tracked using git \... Done. \> Checking if curl is
installed \... Done. \> Checking if remote can be reached \... Done. \>
Initializing and updating submodules (this may take a while)\... Done.
\> Adding all the files of The COBRA Toolbox \... Done. \> Define CB map
output\... set to svg. \> TranslateSBML is installed and working
properly. \> Configuring solver environment variables \... - \[\*\-\--\]
ILOG_CPLEX_PATH:
/Applications/CPLEX_Studio1210/cplex/matlab/x86-64_osx - \[\-\-\--\]
GUROBI_PATH: \--\> set this path manually after installing the solver (
see
[instructions](https://opencobra.github.io/cobratoolbox/docs/solvers.html)
) - \[\-\-\--\] TOMLAB_PATH: \--\> set this path manually after
installing the solver ( see
[instructions](https://opencobra.github.io/cobratoolbox/docs/solvers.html)
) - \[\-\-\--\] MOSEK_PATH: \--\> set this path manually after
installing the solver ( see
[instructions](https://opencobra.github.io/cobratoolbox/docs/solvers.html)
) Done. \> Checking available solvers and solver interfaces \...Gurobi
installed at this location? Licence file current? Version identifier:
12.10.0.0 \| 2019-11-26 \| 843d4de CPXPARAM_Output_WriteLevel 3
CPXPARAM_Output_CloneLog -1 Found incumbent of value 0.000000 after 0.00
sec. (0.00 ticks) Root node processing (before b&c): Real time = 0.01
sec. (0.00 ticks) Parallel b&c, 8 threads: Real time = 0.00 sec. (0.00
ticks) Sync time (average) = 0.00 sec. Wait time (average) = 0.00 sec.
\-\-\-\-\-\-\-\-\-\-\-- Total (root+branch&cut) = 0.01 sec. (0.00 ticks)
Could not find installation of tomlab_cplex, so it cannot be tested
Original LP has 1 row, 2 columns, 1 non-zero Objective value = 0 OPTIMAL
SOLUTION FOUND BY LP PRESOLVER \> \[glpk\] Primal optimality condition
in solveCobraLP satisfied.Could not find installation of mosek, so it
cannot be tested
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--
pdco.m Version pdco5 of 15 Jun 2018 Primal-dual barrier method to
minimize a convex function subject to linear constraints Ax + r = b, bl
\<= x \<= bu Michael Saunders SOL and ICME, Stanford University
Contributors: Byunggyoo Kim (SOL), Chris Maes (ICME) Santiago Akle
(ICME), Matt Zahr (ICME) Aekaansh Verma (ME)
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--
The objective is linear The matrix A is an explicit sparse matrix m = 1
n = 2 nnz(A) = 1 max \|b \| = 0 max \|x0\| = 1.0e+00 xsize = 1.0e+00 max
\|y0\| = 1 max \|z0\| = 1.0e+00 zsize = 1.0e+00 x0min = 1 featol =
1.0e-06 d1max = 1.0e-04 z0min = 1 opttol = 1.0e-06 d2max = 5.0e-04 mu0 =
1.0e-01 steptol = 0.99 bigcenter= 1000 LSMR/MINRES: atol1 = 1.0e-10
atol2 = 1.0e-15 btol = 0.0e+00 conlim = 1.0e+12 itnlim = 10 show = 0
Method = 2 (1 or 11=chol 2 or 12=QR 3 or 13=LSMR 4 or 14=MINRES
21=SQD(LU) 22=SQD(MA57)) Eliminating dy before dx Bounds: \[0,inf\]
\[-inf,0\] Finite bl Finite bu Two bnds Fixed Free 0 0 0 0 0 2 0 \[0,
bu\] \[bl, 0\] excluding fixed variables 0 0 Itn mu stepx stepz Pinf
Dinf Cinf Objective nf center QR 0 -6.6 -99.0 -Inf 1.2500000e-07 1.0 1
-1.0 1.000 1.000 -99.0 -99.0 -Inf 0.0000000e+00 1 1.0 1 2 -3.0 1.000
1.000 -99.0 -99.0 -Inf 0.0000000e+00 1 1.0 3 -5.0 1.000 1.000 -99.0
-99.0 -Inf 0.0000000e+00 1 1.0 4 -7.0 1.000 1.000 -99.0 -99.0 -Inf
0.0000000e+00 1 1.0 Converged max \|x\| = 0.000 max \|y\| = 0.000 max
\|z\| = 0.000 scaled max \|x\| = 0.000 max \|y\| = 0.000 max \|z\| =
0.000 unscaled max \|x\| and max \|z\| exclude fixed variables PDitns =
4 QRitns = 0 cputime = 0.2 Distribution of vector x z \[ 1, 10 ) 0 2 \[
0.1, 1 ) 0 0 \[ 0.01, 0.1 ) 0 0 \[ 0.001, 0.01 ) 0 0 \[ 0.0001, 0.001 )
0 0 \[ 1e-05, 0.0001 ) 0 0 \[ 1e-06, 1e-05 ) 0 0 \[ 1e-07, 1e-06 ) 0 0
\[ 1e-08, 1e-07 ) 0 0 \[ 0, 1e-08 ) 2 0 Elapsed time is 0.222692
seconds. \> \[pdco\] Primal optimality condition in solveCobraLP
satisfied. \> \[pdco\] Dual optimality condition in solveCobraLP
satisfied. Elapsed time is 0.003358 seconds. In 0.0068551 sec, file
written to
/Users/claudiavicentecomorera/cobratoolbox/binary/maci64/bin/minos/data/FBA/qFBA.txt
Could not find installation of cplex_direct, so it cannot be tested \>
\[cplexlp\] Primal optimality condition in solveCobraLP satisfied. \>
\[cplexlp\] Dual optimality condition in solveCobraLP satisfied. Could
not find installation of tomlab_snopt, so it cannot be tested Done. \>
Setting default solvers \...Could not find installation of mosek, so it
cannot be tested Done. \> Saving the MATLAB path \... Done. - The MATLAB
path was saved in the default location. \> Summary of available solvers
and solver interfaces Support LP MILP QP MIQP NLP EP
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--
gurobi active 0 0 0 0 - - ibm_cplex active 1 1 1 1 - - tomlab_cplex
active 0 0 0 0 - - glpk active 1 1 - - - - mosek active 0 - 0 - - 0
matlab active 1 - - - 1 - pdco active 1 - 1 - - 1 quadMinos active
1 - - - - - dqqMinos active 1 - 1 - - - cplex_direct active 0 0 0 - - -
cplexlp active 1 - - - - - qpng passive - - 1 - - - tomlab_snopt
passive - - - - 0 - lp_solve legacy 1 - - - - -
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--
Total - 8 2 4 1 1 1 + Legend: - = not applicable, 0 = solver not
compatible or not installed, 1 = solver installed. \> You can solve LP
problems using: \'ibm_cplex\' - \'glpk\' - \'pdco\' - \'cplexlp\' \> You
can solve MILP problems using: \'ibm_cplex\' - \'glpk\' \> You can solve
QP problems using: \'ibm_cplex\' - \'pdco\' \> You can solve MIQP
problems using: \'ibm_cplex\' \> You can solve NLP problems using: \>
You can solve EP problems using: \'pdco\' Gurobi installed at this
location? Licence file current? Gurobi installed at this location?
Licence file current? Gurobi installed at this location? Licence file
current? Gurobi installed at this location? Licence file current? \>
Checking for available updates \... skipped removing:
/Users/claudiavicentecomorera/cobratoolbox/src/analysis/thermo/componentContribution/new
removing:
/Users/claudiavicentecomorera/cobratoolbox/src/analysis/thermo/groupContribution/new
removing:
/Users/claudiavicentecomorera/cobratoolbox/src/analysis/thermo/inchi/new
removing:
/Users/claudiavicentecomorera/cobratoolbox/src/analysis/thermo/molFiles/new
removing:
/Users/claudiavicentecomorera/cobratoolbox/src/analysis/thermo/protons/new
removing:
/Users/claudiavicentecomorera/cobratoolbox/src/analysis/thermo/trainingModel/new
:::
::::
:::::
:::::::
::::::::::::::::::

::: S9
Import the data and split into 3 variables:
:::

:::::::::::::::::::::::::: CodeBlock
::::::::: {.inlineWrapper .outputs}
::: S10
[data =
readtable([\'data_pbmc.csv\']{style="color: rgb(160, 32, 240);"});]{style="white-space: pre;"}
:::

::::::: S7
:::::: {.inlineElement .eoOutputWrapper .embeddedOutputsWarningElement uid="EFC30917" scroll-top="null" scroll-left="null" data-width="732" data-height="45" hashorizontaloverflow="false" testid="output_2" style="max-height: 261px; width: 762.026px;"}
::::: {.diagnosticMessage-wrapper .diagnosticMessage-warningType}
::: diagnosticMessage-messagePart
Warning: Column headers from the file were modified to make them valid
MATLAB identifiers before creating variable names for the table. The
original column headers are saved in the VariableDescriptions property.\
Set \'PreserveVariableNames\' to true to use the original column headers
as table variable names.
:::

::: diagnosticMessage-stackPart
:::
:::::
::::::
:::::::
:::::::::

:::: inlineWrapper
::: S11
[colnames =
data.Properties.VariableNames(2:end);]{style="white-space: pre;"}
:::
::::

:::: inlineWrapper
::: S5
[rownames = table2cell(data(:, 1));]{style="white-space: pre;"}
:::
::::

:::::::::::::: {.inlineWrapper .outputs}
::: S6
[CPM = table2array(data(:, 2:end))]{style="white-space: pre;"}
:::

:::::::::::: S7
::::::::::: {.inlineElement .eoOutputWrapper .embeddedOutputsVariableMatrixElement uid="60028C66" scroll-top="null" scroll-left="null" data-width="732" testid="output_3" style="width: 762.026px; white-space: normal; font-style: normal; color: rgb(64, 64, 64); font-size: 12px;"}
:::::::::: {.matrixElement .veSpecifier .saveLoad style="white-space: normal; font-style: normal; color: rgb(64, 64, 64); font-size: 12px;"}
:::: {.veVariableName .variableNameElement .double style="width: 732px; white-space: normal; font-style: normal; color: rgb(64, 64, 64); font-size: 12px;"}
::: {.headerElementClickToInteract style="white-space: normal; font-style: normal; color: rgb(64, 64, 64); font-size: 12px;"}
[CPM =
]{style="white-space: normal; font-style: normal; color: rgb(64, 64, 64); font-size: 12px;"}[32738×2638]{.veVariableValueSummary
.veMetaSummary
style="white-space: normal; font-style: normal; color: rgb(179, 179, 179); font-size: 12px;"}
:::
::::

::: {.veScalingFactor style="white-space: normal; font-style: normal; color: rgb(64, 64, 64); font-size: 12px;"}
10^5^[ ×]{.multiply
style="white-space: normal; font-style: normal; color: rgb(64, 64, 64); font-size: 12px;"}
:::

:::::: {.valueContainer layout="{\"columnWidth\":73,\"totalColumns\":\"2638\",\"totalRows\":\"32738\",\"charsPerColumn\":10}" style="white-space: nowrap; font-style: normal; color: rgb(64, 64, 64); font-size: 12px;"}
::: {.variableValue style="width: 659px; white-space: pre; font-style: normal; color: rgb(64, 64, 64); font-size: 12px;"}
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
:::

::: {.horizontalEllipsis style="white-space: nowrap; font-style: normal; color: rgb(64, 64, 64); font-size: 12px;"}
:::

::: {.verticalEllipsis style="white-space: nowrap; font-style: normal; color: rgb(64, 64, 64); font-size: 12px;"}
:::
::::::
::::::::::
:::::::::::
::::::::::::
::::::::::::::
::::::::::::::::::::::::::

::: S9
:::

::: S1
:::

## DISCRETIZATION STEP {#discretization-step .S3}

::: S1
Discretize the gene expression values into expressed, not expressed and
unknown expression status:
:::

:::::::::::::: CodeBlock
::::::::::::: {.inlineWrapper .outputs}
::: S10
[discretized = discretize_FPKM(CPM, colnames)
]{style="white-space: pre;"}
:::

::::::::::: S7
:::::::::: {.inlineElement .eoOutputWrapper .embeddedOutputsVariableMatrixElement uid="51504B04" scroll-top="null" scroll-left="null" data-width="732" testid="output_4" style="width: 762.026px; white-space: normal; font-style: normal; color: rgb(64, 64, 64); font-size: 12px;"}
::::::::: {.matrixElement .veSpecifier .saveLoad style="white-space: normal; font-style: normal; color: rgb(64, 64, 64); font-size: 12px;"}
:::: {.veVariableName .variableNameElement .double style="width: 732px; white-space: normal; font-style: normal; color: rgb(64, 64, 64); font-size: 12px;"}
::: {.headerElementClickToInteract style="white-space: normal; font-style: normal; color: rgb(64, 64, 64); font-size: 12px;"}
[discretized =
]{style="white-space: normal; font-style: normal; color: rgb(64, 64, 64); font-size: 12px;"}[32738×2638]{.veVariableValueSummary
.veMetaSummary
style="white-space: normal; font-style: normal; color: rgb(179, 179, 179); font-size: 12px;"}
:::
::::

:::::: {.valueContainer layout="{\"columnWidth\":44,\"totalColumns\":\"2638\",\"totalRows\":\"32738\",\"charsPerColumn\":6}" style="white-space: nowrap; font-style: normal; color: rgb(64, 64, 64); font-size: 12px;"}
::: {.variableValue style="width: 662px; white-space: pre; font-style: normal; color: rgb(64, 64, 64); font-size: 12px;"}
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
:::

::: {.horizontalEllipsis style="white-space: nowrap; font-style: normal; color: rgb(64, 64, 64); font-size: 12px;"}
:::

::: {.verticalEllipsis style="white-space: nowrap; font-style: normal; color: rgb(64, 64, 64); font-size: 12px;"}
:::
::::::
:::::::::
::::::::::
:::::::::::
:::::::::::::
::::::::::::::

##  {#section-1 .S2}

## rFASTCORMICS {#rfastcormics .S3}

### NEEDED INPUTS {#needed-inputs .S12}

::: S1
Apart from the data, rFASTCORMICS needs some more inputs before run:
:::

-   A file which links the geneIDs from the RNA-seq data to the gene
    identifiers in the model (Entrez).
-   A consistent reconstruction (as Recon3D)

::::::::::::::::::::::::::: CodeBlock
:::: inlineWrapper
::: S4
[load [dico_rFASTCORMICS.mat
]{style="color: rgb(160, 32, 240);"}]{style="white-space: pre;"}
:::
::::

:::: inlineWrapper
::: S5
[load
[Recon3DModel_301.mat]{style="color: rgb(160, 32, 240);"};]{style="white-space: pre;"}
:::
::::

::::::::::::::: {.inlineWrapper .outputs}
::: S6
[A = fastcc_4_rfastcormics(model, 1e-4,0) ]{style="white-space: pre;"}
:::

::::::::::::: S7
:::: {.inlineElement .eoOutputWrapper .embeddedOutputsTextElement uid="FC385C12" scroll-top="null" scroll-left="null" data-width="732" data-height="32" hashorizontaloverflow="false" testid="output_5" style="max-height: 261px; width: 762.026px;"}
::: textElement
The input model is consistent. Elapsed time is 14.364739 seconds.
:::
::::

:::::::::: {.inlineElement .eoOutputWrapper .embeddedOutputsVariableMatrixElement uid="4971E9F0" scroll-top="null" scroll-left="null" data-width="732" testid="output_6" style="width: 762.026px; white-space: normal; font-style: normal; color: rgb(64, 64, 64); font-size: 12px;"}
::::::::: {.matrixElement .veSpecifier .saveLoad style="white-space: normal; font-style: normal; color: rgb(64, 64, 64); font-size: 12px;"}
:::: {.veVariableName .variableNameElement .double style="width: 732px; white-space: normal; font-style: normal; color: rgb(64, 64, 64); font-size: 12px;"}
::: {.headerElementClickToInteract style="white-space: normal; font-style: normal; color: rgb(64, 64, 64); font-size: 12px;"}
[A =
]{style="white-space: normal; font-style: normal; color: rgb(64, 64, 64); font-size: 12px;"}[10600×1]{.veVariableValueSummary
.veMetaSummary
style="white-space: normal; font-style: normal; color: rgb(179, 179, 179); font-size: 12px;"}
:::
::::

:::::: {.valueContainer layout="{\"columnWidth\":44,\"totalColumns\":\"1\",\"totalRows\":\"10600\",\"charsPerColumn\":6}" style="white-space: nowrap; font-style: normal; color: rgb(64, 64, 64); font-size: 12px;"}
::: {.variableValue style="width: 46px; white-space: pre; font-style: normal; color: rgb(64, 64, 64); font-size: 12px;"}
1 2 3 4 5 6 7 8 9 10
:::

::: {.horizontalEllipsis .hide style="white-space: nowrap; font-style: normal; color: rgb(64, 64, 64); font-size: 12px;"}
:::

::: {.verticalEllipsis style="white-space: nowrap; font-style: normal; color: rgb(64, 64, 64); font-size: 12px;"}
:::
::::::
:::::::::
::::::::::
:::::::::::::
:::::::::::::::

::::::::: {.inlineWrapper .outputs}
::: S8
[Cmodel = removeRxns(model,
model.rxns(setdiff(1:numel(model.rxns),A)))]{style="white-space: pre;"}
:::

::::::: S7
:::::: {.inlineElement .eoOutputWrapper .embeddedOutputsVariableStringElement .scrollableOutput uid="025921CB" scroll-top="null" scroll-left="null" data-width="732" data-height="574" hashorizontaloverflow="false" testid="output_7" style="max-height: 261px; width: 762.026px;"}
::::: textElement
<div>

[Cmodel = [struct with fields:]{.headerElement}]{.variableNameElement}

</div>

<div>

S: \[5835×10600 double\] mets: {5835×1 cell} b: \[5835×1 double\]
csense: \[5835×1 char\] rxns: {10600×1 cell} lb: \[10600×1 double\] ub:
\[10600×1 double\] c: \[10600×1 double\] osense: -1 genes: {2248×1 cell}
rules: {10600×1 cell} metCharges: \[5835×1 int64\] metFormulas: {5835×1
cell} metSmiles: {5835×1 cell} metNames: {5835×1 cell} metHMDBID:
{5835×1 cell} metInChIString: {5835×1 cell} metKEGGID: {5835×1 cell}
metPubChemID: {5835×1 cell} description: \'Recon3DModel.mat\' grRules:
{10600×1 cell} rxnGeneMat: \[10600×2248 double\] rxnConfidenceScores:
\[10600×1 double\] rxnNames: {10600×1 cell} rxnNotes: {10600×1 cell}
rxnECNumbers: {10600×1 cell} rxnReferences: {10600×1 cell} rxnKEGGID:
{10600×1 cell} subSystems: {10600×1 cell} metCHEBIID: {5835×1 cell}
metPdMap: {5835×1 cell} metReconMap: {5835×1 cell} modelID:
\'Recon3DModel\' rxnCOG: {10600×1 cell} rxnKeggOrthology: {10600×1 cell}
rxnReconMap: {10600×1 cell} version: \'Recon3D_01\' PleaseCite: \'Brunk
et al, Nat Biotech, 2018; doi:10.1038/nbt.4072\'

</div>
:::::
::::::
:::::::
:::::::::
:::::::::::::::::::::::::::

::: S9
:::

::: S1
:::

### PARAMETERS AND OPTIONAL INPUTS {#parameters-and-optional-inputs .S12}

::: S1
We will use the parameters and inputs defined in rFASTCORMICS example
scripts, excluding the medium constraint.
:::

::::::::::::::::::::::::::::::::::::::: CodeBlock
:::: inlineWrapper
::: S4
[biomass_rxn =
{[\'biomass_maintenance\']{style="color: rgb(160, 32, 240);"}};
]{style="white-space: pre;"}
:::
::::

:::: inlineWrapper
::: S5
[already_mapped_tag = 0;]{style="white-space: pre;"}
:::
::::

:::: inlineWrapper
::: S5
[epsilon = 1e-4; ]{style="white-space: pre;"}
:::
::::

:::: inlineWrapper
::: S5
[consensus_proportion = 0.9; ]{style="white-space: pre;"}
:::
::::

:::: inlineWrapper
::: S5
[unpenalizedSystems = {[\'Transport, endoplasmic
reticular\']{style="color: rgb(160, 32, 240);"};]{style="white-space: pre;"}
:::
::::

:::: inlineWrapper
::: S5
[ [\'Transport,
extracellular\']{style="color: rgb(160, 32, 240);"};]{style="white-space: pre;"}
:::
::::

:::: inlineWrapper
::: S5
[ [\'Transport, golgi
apparatus\']{style="color: rgb(160, 32, 240);"};]{style="white-space: pre;"}
:::
::::

:::: inlineWrapper
::: S5
[ [\'Transport,
mitochondrial\']{style="color: rgb(160, 32, 240);"};]{style="white-space: pre;"}
:::
::::

:::: inlineWrapper
::: S5
[ [\'Transport,
peroxisomal\']{style="color: rgb(160, 32, 240);"};]{style="white-space: pre;"}
:::
::::

:::: inlineWrapper
::: S5
[ [\'Transport,
lysosomal\']{style="color: rgb(160, 32, 240);"};]{style="white-space: pre;"}
:::
::::

:::: inlineWrapper
::: S5
[ [\'Transport,
nuclear\']{style="color: rgb(160, 32, 240);"}};]{style="white-space: pre;"}
:::
::::

:::: inlineWrapper
::: S5
[Cmodel_subSystems = cellfun(@(x) x{1}, Cmodel.subSystems,
[\'UniformOutput\']{style="color: rgb(160, 32, 240);"}, false);
]{style="white-space: pre;"}
:::
::::

:::: inlineWrapper
::: S5
[unpenalized =
Cmodel.rxns(ismember(Cmodel_subSystems,unpenalizedSystems));]{style="white-space: pre;"}
:::
::::

:::: inlineWrapper
::: S5
:::
::::

:::: inlineWrapper
::: S5
[optional_settings.unpenalized = unpenalized;
]{style="white-space: pre;"}
:::
::::

:::: inlineWrapper
::: S5
[optional_settings.func =
{[\'biomass_maintenance\']{style="color: rgb(160, 32, 240);"},[\'DM_atp_c\_\']{style="color: rgb(160, 32, 240);"}};
]{style="white-space: pre;"}
:::
::::

:::: inlineWrapper
::: S5
[not_medium_constrained =
[\'EX_tag_hs\[e\]\']{style="color: rgb(160, 32, 240);"};]{style="white-space: pre;"}
:::
::::

:::: inlineWrapper
::: S15
[optional_settings.not_medium_constrained =
not_medium_constrained;]{style="white-space: pre;"}
:::
::::
:::::::::::::::::::::::::::::::::::::::

###  {#section-2 .S16}

### CONTEXT-SPECIFIC SINGLE MODELS CREATION {#context-specific-single-models-creation .S12}

::: S1
By setting all the inputs into the
[fastcormics_RNAseq]{style=" font-weight: bold; font-style: italic;"}
function, a model for each cell (column) of the data will be build:
:::

:::::::::::::::::::::::::::::::: CodeBlock
:::: inlineWrapper
::: S4
[[for ]{style="color: rgb(0, 0, 255);"}i = 1:numel(colnames)
]{style="white-space: pre;"}
:::
::::

:::: inlineWrapper
::: S5
[ \[ContextModel, A_keep\] = fastcormics_RNAseq(Cmodel,
discretized(:,i),
[\...]{style="color: rgb(0, 0, 255);"}]{style="white-space: pre;"}
:::
::::

:::: inlineWrapper
::: S5
[ rownames, dico, biomass_rxn, already_mapped_tag, consensus_proportion,
epsilon, optional_settings);]{style="white-space: pre;"}
:::
::::

:::: inlineWrapper
::: S5
[ ]{style="white-space: pre;"}
:::
::::

:::: inlineWrapper
::: S5
[ filePath =
fullfile([\'PBMC_Models\']{style="color: rgb(160, 32, 240);"},
colnames{i});]{style="white-space: pre;"}
:::
::::

:::: inlineWrapper
::: S5
[ save(filePath, [\'ContextModel\']{style="color: rgb(160, 32, 240);"});
]{style="white-space: pre;"}
:::
::::

:::: inlineWrapper
::: S5
[ [models_keep]{.warning_squiggle_rte}(A_keep,i) =
1;]{style="white-space: pre;"}
:::
::::

::::::::::::::::: {.inlineWrapper .outputs}
::: S6
[[end]{style="color: rgb(0, 0, 255);"}]{style="white-space: pre;"}
:::

::::::::::::::: S7
:::: {.inlineElement .eoOutputWrapper .embeddedOutputsTextElement uid="1E695435" scroll-top="null" scroll-left="null" data-width="732" data-height="46" hashorizontaloverflow="false" testid="output_8" style="max-height: 261px; width: 762.026px;"}
::: textElement
creating model.rev unnesting subsystems 2143 of 2248 genes matched
:::
::::

:::::: {.inlineElement .eoOutputWrapper .embeddedOutputsWarningElement uid="157C7F1B" scroll-top="null" scroll-left="null" data-width="732" data-height="18" hashorizontaloverflow="false" testid="output_9" style="max-height: 261px; width: 762.026px;"}
::::: {.diagnosticMessage-wrapper .diagnosticMessage-warningType}
::: diagnosticMessage-messagePart
Warning: No optional settings detected
:::

::: diagnosticMessage-stackPart
:::
:::::
::::::

:::: {.inlineElement .eoOutputWrapper .embeddedOutputsTextElement uid="5D7CB56D" scroll-top="null" scroll-left="null" data-width="732" data-height="18" hashorizontaloverflow="false" testid="output_10" style="max-height: 261px; width: 762.026px;"}
::: textElement
Elapsed time is 46.868621 seconds.
:::
::::

:::::: {.inlineElement .eoOutputWrapper .embeddedOutputsErrorElement uid="B743E524" scroll-top="null" scroll-left="null" data-width="732" data-height="31" hashorizontaloverflow="false" testid="output_11" style="max-height: 261px; width: 762.026px;"}
::::: {.diagnosticMessage-wrapper .diagnosticMessage-errorType}
::: diagnosticMessage-messagePart
Error using save\
Cannot create \'AAACATACAACCAC_1.mat\' because \'PBMC_Models\' does not
exist.
:::

::: diagnosticMessage-stackPart
:::
:::::
::::::
:::::::::::::::
:::::::::::::::::
::::::::::::::::::::::::::::::::

::: S9
:::

::::: CodeBlock
:::: inlineWrapper
::: S17
[delete
[clone\*.log]{style="color: rgb(160, 32, 240);"}]{style="white-space: pre;"}
:::
::::
:::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

\
