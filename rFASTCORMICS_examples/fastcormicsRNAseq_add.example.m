%% 
% Setup
%(Pacheco et al., 2019, EBioMedicine)
addpath(genpath(pwd))

%optional
set(0,'defaultTextInterpreter','none')
set(groot,'defaulttextinterpreter','none');
set(groot, 'DefaultAxesTickLabelInterpreter', 'none')
set(groot, 'defaultLegendInterpreter','none');

feature astheightlimit 2000

altcolor= [255 255 255;255 204 204; 255 153 153; 255 102 102; 255 51 51;...
    255 0 0; 204 0 0; 152 0 0; 102 0 0;  51 0 0]/255; %shorter 10% = 1 bar

delete clone*.log %delete some files generated by cplex
%% 3.1 Expression data input
% Import the gene expression data into Matlab. 

data_cancer = readtable('fpkm_BRCA_cancer.txt', "ReadRowNames",true);
data_control = readtable('fpkm_BRCA_control.txt', "ReadRowNames",true);
conditions= {'cancer', 'control'};

data = [data_cancer, data_control];

fpkm = table2array(data);
rownames = data.Properties.RowNames;
colnames = data.Properties.VariableNames;
%% 
% discretization step 

discretized = discretize_FPKM(fpkm, colnames,1); %with figures
%discretized = discretize_FPKM(fpkm, colnames); % no figures
%% 3.2.	Context-specific model reconstruction
% human reconstruction Recon 2.04 
% 
% can also be downloaded from https://www.vmh.life/files/reconstructions/Recon/2.04/Recon2.v04.mat_.zip. 

load Recon2.v04.mat
%% 
% consitent model creation

A = fastcc_4_rfastcormics(modelR204, 1e-4,0);
consistent_model = removeRxns(modelR204, modelR204.rxns(setdiff(1:numel(modelR204.rxns),A)));
%% 
% setting parameters

load medium_example.mat
load dico_ML.mat

epsilon = 1e-4;
consensus_proportion = 0.9;
already_mapped_tag = 0;
unpenalizedSystems = {'Transport, endoplasmic reticular';
    'Transport, extracellular';
    'Transport, golgi apparatus';
    'Transport, mitochondrial';
    'Transport, peroxisomal';
    'Transport, lysosomal';
    'Transport, nuclear'};
unpenalized = consistent_model.rxns(ismember(consistent_model.subSystems,unpenalizedSystems));
optional_settings.unpenalized = unpenalized;

optional_settings.func = {'DM_atp_c_', 'biomass_reaction'}; % forced reactions

not_medium_constrained = 'EX_tag_hs(e)';% if no constrain is used please remove the field.
optional_settings.not_medium_constrained = not_medium_constrained;

optional_settings.medium = medium_example;% if no medium is used please remove the field.

biomass_rxn = {'biomass_reaction'};
%% 
% reconstruct the context-specific models
% 
% consensus models

[model_cancer, A_final_cancer] = fastcormics_RNAseq(consistent_model, discretized(:,1:10), rownames, dico, biomass_rxn, already_mapped_tag, consensus_proportion, epsilon, optional_settings);
[model_control, A_final_control] = fastcormics_RNAseq(consistent_model, discretized(:,11:20), rownames, dico, biomass_rxn, already_mapped_tag, consensus_proportion, epsilon, optional_settings);

%% 
% sample-specific models

for i = 1:numel(colnames) %for each sample
    [ContextModel, A_keep] = fastcormics_RNAseq(consistent_model, discretized(:,i), ...
        rownames, dico, biomass_rxn, already_mapped_tag, consensus_proportion, epsilon, optional_settings);
     name=strcat('SampleModel_',colnames{i});
        save (name, 'ContextModel');   
        models_keep_consensus(A_keep,i) = 1;
end
%%
delete clone*.log %delete some files generated by cplex
