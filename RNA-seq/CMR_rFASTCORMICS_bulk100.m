addpath(genpath(pwd)) 
addpath(genpath('/Users/claudiavicentecomorera/cobratoolbox')) 
feature astheightlimit 2000
initCobraToolbox(false)
%% 
% 

data = readtable('bulk_data100.csv');
colnames = data.Properties.VariableNames(2:end);
rownames = table2cell(data(:, 1));
TPM = table2array(data(:, 2:end))
discretized = discretize_FPKM(TPM, colnames) 
%% 
% 

load dico_rFASTCORMICS.mat 
load Recon3DModel_301.mat;
A = fastcc_4_rfastcormics(model, 1e-4,0) 
Cmodel = removeRxns(model, model.rxns(setdiff(1:numel(model.rxns),A)))
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
     
    filePath = fullfile('RNAseq_Models', colnames{i});
    save(filePath, 'ContextModel');   
    models_keep(A_keep,i) = 1;
end
%% 
% 

delete clone*.log