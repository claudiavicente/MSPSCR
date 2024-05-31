# libraries
import glob
import cobra
import os
import time
import pandas as pd

####
fba_fluxes_df = pd.DataFrame()
pfba_fluxes_df = pd.DataFrame()
fba_r_models = pd.DataFrame()
pfba_r_models = pd.DataFrame()
####

# recon 3D
recon3D = cobra.io.load_matlab_model('/home/matlab/Recon3DModel_301.mat')
recon3D.objective = 'biomass_maintenance'
fba_recon_3D = recon3D.optimize()
pfba_recon_3D = cobra.flux_analysis.parsimonious.pfba(recon3D)
fba_ov = fba_recon_3D.objective_value
pfba_ov = pfba_recon_3D.objective_value


# models simulation (pFBA)
f_path = "/home/matlab/TITC/TITC_post/"
file_paths = glob.glob(f_path + "*.mat")

t0 = time.time()
for i, file_path in enumerate(file_paths):
    model = cobra.io.load_matlab_model(file_path)
    model.id = os.path.splitext(os.path.basename(file_path))[0]
    model.objective = 'biomass_maintenance'
    
    t0_simulations = time.time()
    fba_solution = model.optimize()
    pfba_solution = cobra.flux_analysis.pfba(model)
    tf_simulations = time.time()  
    print(f"The simulations of {model.id} ({i+1}) fluxes takes: {tf_simulations - t0_simulations} seconds")

    # FBA 
    # fluxes df
    for reaction, flux in fba_solution.fluxes.items():
        if reaction not in fba_fluxes_df.columns:
            fba_fluxes_df[reaction] = 0.0
        fba_fluxes_df.at[model.id, reaction] = flux
    print(f"The fluxes of {model.id} ({i+1}) solution have been added to fba_fluxes_df")
    # r_models
    fba_r_models.loc[model.id, 'biomass_maintenance'] = fba_solution.fluxes["biomass_maintenance"]
    fba_r_models.loc[model.id, 'objective_value'] = fba_solution.objective_value
    fba_r_models.loc[model.id, 'percent_ov'] = (fba_solution.objective_value/fba_ov) * 100
    
    # pFBA 
    # fluxes df
    for reaction, flux in pfba_solution.fluxes.items():
        if reaction not in pfba_fluxes_df.columns:
            pfba_fluxes_df[reaction] = 0.0
        pfba_fluxes_df.at[model.id, reaction] = flux
    print(f"The fluxes of {model.id} ({i+1}) solution have been added to pfba_fluxes_df")
    # r_models
    pfba_r_models.loc[model.id, 'biomass_maintenance'] = pfba_solution.fluxes["biomass_maintenance"]
    pfba_r_models.loc[model.id, 'objective_value'] = pfba_solution.objective_value
    pfba_r_models.loc[model.id, 'percent_ov'] = (pfba_solution.objective_value/pfba_ov) * 100     

tf = time.time()
print(f"The simulations and dfs creation took: {(tf - t0)/60} minutes")

fba_fluxes_df.to_csv('/home/matlab/TITC/results_post/fba_fluxes_post.csv')
pfba_fluxes_df.to_csv('/home/matlab/TITC/results_post/pfba_fluxes_post.csv')
print("fluxes dfs have been stored")

fba_r_models.to_csv('/home/matlab/TITC/results_post/fba_rmodels_post.csv')
pfba_r_models.to_csv('/home/matlab/TITC/results_post/pfba_rmodels_post.csv')
print("r_models dfs have been stored")
