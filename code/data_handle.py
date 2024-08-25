import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_auction(path):
    df = pd.read_csv(path)
    # renaming columns for easier access
    mapper={'Quantity (MWh)':'Quantity',  'Price (€/MWh)':'Price'}
    df=df.rename(columns=mapper)
    # df_supply = df[df['Supply/Demand']=='Supply'].sort_values(by=['Price']).sort_values(by=['Price'])
    # df_demand = df[df['Supply/Demand']=='Demand'].sort_values(by=['Price']).sort_values(by=['Price'], ascending=False)
    return df


def save_fig(name, path='/Users/davidmiles-skov/Desktop/Academics/Projects/market-clearing-price/plots'):
    fname = '/Users/davidmiles-skov/Desktop/Academics/Projects/market-clearing-price/plots/'+name+'.png'
    plt.savefig(fname, dpi=300)

def save_results():
    return