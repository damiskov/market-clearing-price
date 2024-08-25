import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import linprog
from solver import solve_MCP
from  data_handle import load_auction, save_results
from visualise import plot_accepted_vs_offered, plot_supply_demand, plot_social_welfare








def main():

    path = '/Users/davidmiles-skov/Desktop/Academics/Projects/market-clearing-price/data/test.csv'
    df = load_auction(path)
    df_supply, df_demand = df[df['Supply/Demand']=='Supply'], df[df['Supply/Demand']=='Demand']
    N_G = len(df_supply)
    N_D = len(df_demand)
    result = solve_MCP(df, N_G,N_D)
    save = True
    print(f"""
y:
          {result.x}

    """)

    plot_supply_demand(df_supply, df_demand, save)


    plot_accepted_vs_offered(df_supply, df_demand,result, N_G, N_D,save)




    return

if __name__=="__main__":
    main()