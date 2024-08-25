import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_auction(path):
    df = pd.read_csv(path)
    # renaming columns for easier access
    mapper={'Quantity (MWh)':'Quantity',  'Price (€/MWh)':'Price'}
    df=df.rename(columns=mapper)
    df_supply = df[df['Supply/Demand']=='Supply'].sort_values(by=['Price']).sort_values(by=['Price'])
    df_demand = df[df['Supply/Demand']=='Demand'].sort_values(by=['Price']).sort_values(by=['Price'], ascending=False)
    return df_supply, df_demand


def save_fig(fig, path='/Users/davidmiles-skov/Desktop/Academics/Projects/market-clearing-price/plots'):
    plt.savefig(fig, path=path, dpi=300)

def save_results():
    return