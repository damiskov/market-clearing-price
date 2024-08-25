import pandas as pd
import numpy as np
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

def save_results():
    return