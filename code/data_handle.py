import pandas as pd
import matplotlib.pyplot as plt
import os 

def load_auction(path):
    df = pd.read_csv(path)
    # renaming columns for easier access
    mapper={'Quantity (MWh)':'Quantity',  'Price (€/MWh)':'Price'}
    df=df.rename(columns=mapper)
    # df_supply = df[df['Supply/Demand']=='Supply'].sort_values(by=['Price']).sort_values(by=['Price'])
    # df_demand = df[df['Supply/Demand']=='Demand'].sort_values(by=['Price']).sort_values(by=['Price'], ascending=False)
    return df


def save_fig(name, figname):
    path = f'{os.getcwd()}/plots/{name}/{figname}.png'
    plt.savefig(path, dpi=300)

def save_results(df_supply, df_demand, result,name, N_G):
    save_path = f"{os.getcwd()}/solutions/{name}/"
    supply_allocations = {'ID': df_supply["ID"].to_numpy(), 'Allocated':result.x[:N_G]}
    demand_allocations = {'ID': df_demand["ID"].to_numpy(), 'Allocated':result.x[N_G:]}
    df_supply_allocation = pd.DataFrame.from_dict(supply_allocations)
    df_demand_allocation = pd.DataFrame.from_dict(demand_allocations)
    df_supply_allocation.to_csv(save_path+"supply_allocation.csv", index=False)
    df_demand_allocation.to_csv(save_path+"demand_allocation.csv", index=False)
    with open(save_path+"MCP.txt", "w") as f:
        f.write(str(result.eqlin["marginals"][0]))
    return