%% rFASTCORMICS FOR 30 PBMC scRNA-seq SAMPLES
% 
%% Setup

addpath(genpath(pwd)) 
feature astheightlimit 2000
%% 
% 

data = readtable('data_pbmc400.csv');
colnames = data.Properties.VariableNames(277:end);
rownames = table2cell(data(:, 1));
CPM = table2array(data(:, 277:end))
%%
%discretized = discretize_FPKM(CPM, colnames,1)
discretized = discretize_FPKM(CPM, colnames)
%%
load Recon3DModel_301.mat, 
Recon3DModel.description='Recon'; 
%% 
% 

A = fastcc_4_rfastcormics(Recon3DModel, 1e-4, 0); 
Cmodel = removeRxns(Recon3DModel, Recon3DModel.rxns(setdiff(1:numel(Recon3DModel.rxns),A)))
%%
%dico = readtable('dico.csv')
load dico_rFASTCORMICS.mat
%% 
% 
%% 
% * *already mapped tag:* 1, if the data was already to the model.rxns in this 
% case data p = n  and  0, if the data has to be mapped  using the GPR rules of 
% the model

already_mapped_tag = 0;
%% 
% 
%% 
% * *epsilon*        avoids small number errors

epsilon = 1e-4; %avoid small number errors
%% 
% 

consensus_proportion = 0.9;
%% 
% 

unpenalizedSystems = {'Transport, endoplasmic reticular';
    'Transport, extracellular';
    'Transport, golgi apparatus';
    'Transport, mitochondrial';
    'Transport, peroxisomal';
    'Transport, lysosomal';
    'Transport, nuclear'};

Cmodel_subSystems = cellfun(@(x) x{1}, Cmodel.subSystems, 'UniformOutput', false); % unpenalizedSystems cells were char and model.subSystems cells were cells
unpenalized = Cmodel.rxns(ismember(Cmodel_subSystems,unpenalizedSystems));
optional_settings.unpenalized = unpenalized;
optional_settings.func = {'DM_atp_c_', 'biomass_maintenance'}; % forced reactions
not_medium_constrained = 'EX_tag_hs[e]';
optional_settings.not_medium_constrained = not_medium_constrained;

biomass_rxn = {'biomass_maintenance'};
%% 
% Single context - models for each sample (cell):

for i = 1:numel(colnames) 
    [ContextModel, A_keep] = fastcormics_RNAseq(Cmodel, discretized(:,i), ...
        rownames, dico, biomass_rxn, already_mapped_tag, consensus_proportion, epsilon, optional_settings);
     
    filePath = fullfile('PBMC_Models', colnames{i});
    save(filePath, 'ContextModel');   
    models_keep(A_keep,i) = 1;
end
%% 
% Consensus models: 

[model_out_consensus, A_keep_consensus] = fastcormics_RNAseq(Cmodel, discretized, rownames, dico, ...
    biomass_rxn, already_mapped_tag, consensus_proportion, epsilon, optional_settings);
%%
delete clone*.log