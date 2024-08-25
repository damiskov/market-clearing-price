import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from data_handle import save_fig

def plot_supply_demand(df_supply, df_demand, save=False):
    quantity_supply, quantity_demand = df_supply['Quantity'].to_numpy(), df_demand['Quantity'].to_numpy()
    price_supply, price_demand = df_supply['Price'].to_numpy(), df_demand['Price'].to_numpy()
    
    # Setting up demand data

    x_demand = np.cumsum(quantity_demand)[::-1]
    x_demand = np.append(x_demand[0], x_demand)
    y_demand = price_demand[::-1]
    y_demand = np.append(np.array([0]), y_demand)

    # Setting supply data

    x_supply = np.cumsum(quantity_supply)
    x_supply = np.append(np.array([0]), x_supply)
    y_supply = np.append(np.array([0]), price_supply)

    fig, ax = plt.subplots()
    fig.figsize=(10, 6)

    ax.step(x_supply, y_supply, where='post', label='Supply', color='cornflowerblue', linewidth=2)
    ax.step(x_demand, y_demand, where='post', label='Demand', color='lightcoral', linewidth=2)

    # labels and title
    ax.set_xlabel('Energy [MWh]')
    ax.set_ylabel('Price [€/MWh]')
    ax.set_title('Supply/Demand Curves')
    ax.grid(True)
    ax.legend(loc='upper right')
    if save:
        save_fig(fig)

    # Show the plot
    plt.show()

def plot_social_welfare():
    return

def plot_AvsO_help(df,type ,save):
    if type=='Supply':
        colours = ['lightblue', 'midnightblue']
    else:
        colours = ['lightcoral', 'darkred']
    



def plot_accepted_vs_offered(df_supply, df_demand, save=False):



