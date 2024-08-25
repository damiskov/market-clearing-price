import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from scipy.optimize import linprog
from solver import solve_MCP
from  data_handle import load_auction, save_results
from visualise import plot_accepted_vs_offered, plot_supply_demand, plot_social_welfare

def main():
    path = os.getcwd()
    name = 'test'
    data_path = f'{path}/data/{name}.csv'
    df = load_auction(data_path)
    df_supply, df_demand = df[df['Supply/Demand']=='Supply'], df[df['Supply/Demand']=='Demand']
    N_G = len(df_supply)
    N_D = len(df_demand)

    # Make necessary directories, if they do not already exist
    if not os.path.isdir(f'{path}/solutions/{name}'):
        os.mkdir(f'{path}/solutions/{name}')
    if not os.path.isdir(f'{path}/plots/{name}'):
        os.mkdir(f'{path}/plots/{name}')
   
    
    # Solving

    result = solve_MCP(df, N_G,N_D)
    save = True
    print(f"""
       y:
          {result.x}

    """)

    # Making plots
    # plot_supply_demand(df_supply, df_demand, save)
    # plot_accepted_vs_offered(df_supply, df_demand,result, N_G, N_D,save)
    # plot_social_welfare()


    # save results
    supply_allocations = {'ID': df_supply["ID"].to_numpy(), 'Allocated':result.x[:N_G]}
    demand_allocations = {'ID': df_demand["ID"].to_numpy(), 'Allocated':result.x[N_G:]}
    df_supply_allocation = pd.DataFrame.from_dict(supply_allocations)
    df_demand_allocation = pd.DataFrame.from_dict(demand_allocations)

    





    return

if __name__=="__main__":
    main()