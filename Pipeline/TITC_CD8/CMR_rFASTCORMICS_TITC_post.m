%% rFASTCORMICS FOR TITC_pre scRNA-seq DATASET
%% 

addpath(genpath("/opt/ibm/ILOG/CPLEX_Studio1210/cplex/matlab/x86-64_linux/"))
addpath(genpath("/home/matlab/cobratoolbox/"))
addpath(genpath("/home/matlab/rFASTCORMICS/"))
feature astheightlimit 2000
initCobraToolbox(false)
%% 
% 

data = readtable('/home/matlab/CMR/post/data_titc.csv');
colnames = data.Properties.VariableNames(2:end);
rownames = table2cell(data(:, 1));
CPM = table2array(data(:, 2:end))
discretized = discretize_FPKM(CPM, colnames)
%% 
% 

load /home/matlab/rFASTCORMICS/rFASTCORMICS_RNA-seq/exampleData/dico_rFASTCORMICS.mat
load /home/matlab/Recon3DModel_301.mat;
A = fastcc_4_rfastcormics(Recon3DModel, 1e-4,0)
Cmodel = removeRxns(Recon3DModel, Recon3DModel.rxns(setdiff(1:numel(Recon3DModel.rxns),A)))
%% 
% 

biomass_rxn = {'biomass_maintenance'};
already_mapped_tag = 0;
epsilon = 1e-4;
consensus_proportion = 0.9;
unpenalizedSystems = {'Transport, endoplasmic reticular';
    'Transport, extracellular';
    'Transport, golgi apparatus';
    'Transport, mitochondrial';
    'Transport, peroxisomal';
    'Transport, lysosomal';
    'Transport, nuclear'};
Cmodel_subSystems = cellfun(@(x) x{1}, Cmodel.subSystems, 'UniformOutput', false);
unpenalized = Cmodel.rxns(ismember(Cmodel_subSystems,unpenalizedSystems));

optional_settings.unpenalized = unpenalized;
optional_settings.func = {'biomass_maintenance','DM_atp_c_'};
not_medium_constrained = 'EX_tag_hs[e]';
optional_settings.not_medium_constrained = not_medium_constrained;
%% 
% 

for i = 1:numel(colnames)
    [ContextModel, A_keep] = fastcormics_RNAseq(Cmodel, discretized(:,i), ...
        rownames, dico, biomass_rxn, already_mapped_tag, consensus_proportion, epsilon, optional_settings);

    filePath = fullfile('/home/matlab/TITC/TITC_post', colnames{i});
    save(filePath, 'ContextModel');
    models_keep(A_keep,i) = 1;
end
%% 
% 

delete clone*.log
%% 
