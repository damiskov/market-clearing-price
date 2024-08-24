# Market Clearing Price Solver

## Project Overview

This is an implementation of a solver and visualiser for the market clearing price of a day-ahead energy market. The programme can take two csv files of the following format:

| Name | ID  | Quantity [MWh] | Price [€/MWh]  |
| ---- | --- | -------------- | ------------- |
| ...  | ... | ...            | .              |

for both supply and demand. They must be uploaded in  the following format: `data/name/name_supply.csv` and `data/name/name_demand.csv`. The market clearing price will be solved, as well as ... .

The results will be stored as csv files in a directory `/solutions/name` and visualised (see examples in `/plots/name`). As is, the programme will run based on an example auction created Pierre Pinson for the [course](http://pierrepinson.com/index.php/teaching/) *31761 - Renewables in Energy Markets* at the Technical University of Denmark.

## Problem Background

A **market-clearing price** is the price of a good or service at which the quantity supplied equals the quantity demanded, also called the equilibrium price. In the context of the day-ahead energy market, this is the price at which market supply, dictated by generators, is equal to market demand (dictated by retailers, large consumers, aggregators etc).

## Requirements
- Python 3.12
- NumPy
- Scipy...
