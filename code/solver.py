import numpy as np
from scipy.optimize import linprog
import pandas as pd

def solve_MCP(df, N_G, N_D):
    supply_price = df[df['Supply/Demand']=='Supply']['Price'].to_numpy()
    supply_quantity = df[df['Supply/Demand']=='Supply']['Quantity'].to_numpy()
    demand_price = df[df['Supply/Demand']=='Demand']['Price'].to_numpy()
    demand_quantity = df[df['Supply/Demand']=='Demand']['Quantity'].to_numpy()
    c = np.append(supply_price,-demand_price)
    A_eq = np.array([np.append(np.ones(N_G), -np.ones(N_D))])
    b_eq = 0
    A = np.identity(N_G+N_D)
    b = np.append(supply_quantity,demand_quantity)
    return linprog(c, A_eq=A_eq, b_eq=b_eq, A_ub=A, b_ub=b)