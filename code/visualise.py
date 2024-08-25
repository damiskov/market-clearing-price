import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from data_handle import save_fig

def gen_supply_demand(df_supply, df_demand,name, save):
    quantity_supply, quantity_demand = df_supply['Quantity'].to_numpy(), df_demand['Quantity'].to_numpy()
    price_supply, price_demand = df_supply['Price'].to_numpy(), df_demand['Price'].to_numpy()
    
    # Setting up demand data

    x_demand = np.cumsum(quantity_demand)[::-1] 
    x_demand = np.append(x_demand[0], x_demand)
    x_demand = np.append(x_demand, np.array([0]))
    
    y_demand = price_demand[::-1]
    y_demand = np.append(np.array([0]), y_demand)
    y_demand = np.append(y_demand, np.array(y_demand[-1]))

    # Setting supply data

    x_supply = np.cumsum(quantity_supply)
    x_supply = np.append(np.array([0]), x_supply)
    y_supply = np.append(np.array([0]), price_supply)

    fig, ax = plt.subplots()
    fig.figsize=(10, 6)

    ax.step(x_supply, y_supply, where='post', label='Supply', color='cornflowerblue', linewidth=2, marker='.')
    ax.step(x_demand, y_demand, where='post', label='Demand', color='lightcoral', linewidth=2, marker='.')

    # labels and title
    ax.set_xlabel('Energy [MWh]')
    ax.set_ylabel('Price [€/MWh]')
    ax.set_title('Supply/Demand Curves')
    ax.grid(True)
    ax.legend(loc='upper right')
    if save:
        save_fig(name, 'supply_demand')

    return fig, ax

def plot_social_welfare():
    return

def gen_accepted_vs_offered(df,type,result,N_G,name,save):
    
    # Set up
    
    labels = df['ID'] 
    
    if type=='Supply':
        colors = ['lightblue', 'midnightblue']
        actual =  result.x[:N_G]
        offer = df[df['Supply/Demand']=='Supply']['Quantity'].to_numpy()
    else:
        colors = ['lightcoral', 'darkred']
        actual = result.x[N_G::]
        offer = df[df['Supply/Demand']=='Demand']['Quantity'].to_numpy()


    y_pos = np.arange(len(labels))

    # Plotting 

    fig, ax = plt.subplots()
    # make figure wider
    fig.set_figwidth(14)
    ax.barh(y_pos, offer, alpha=0.6, color=colors[0],label='Offered')

    # Going over, IDs again, indicating actual amount of electricity supplied

    ax.barh(y_pos, actual, alpha=0.8, color=colors[1], label='Accepted')

    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=10)
    ax.set_xlabel('MWh')
    ax.set_ylabel('ID')
    ax.set_title("Supply (Accepted + Offered)")
    plt.xticks(rotation=45)
    plt.legend(loc='upper right')

    if save:
        figname = f'{type}_allocation'
        save_fig(name, figname)

    return fig, ax
        
    



def plot_accepted_vs_offered(df_supply, df_demand, result, N_G,name,save=False):

    # For supply

    fig_supply, ax_supply = gen_accepted_vs_offered(df_supply, 'Supply',result, N_G, name,save)
    plt.show()

    # For demand
    fig_demand, ax_demand = gen_accepted_vs_offered(df_demand, 'Demand',result, N_G,name, save)
    plt.show()





def plot_supply_demand(df_supply, df_demand,name, save):
    fig, ax = gen_supply_demand(df_supply, df_demand,name, save)
    plt.show()

def scatter_df(df, type):
    x,y = df["Quantity"].to_numpy(),df["Price"].to_numpy()
    fig, ax = plt.subplots()
    ax.scatter(x,y)
    ax.set_xlabel("Quantity (MWh)")
    ax.set_ylabel("Price (€/MWh)")
    plt.show()
