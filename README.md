# Market Clearing Price Solver

## Project Overview

This is an implementation of a solver and visualiser for the market clearing price of a day-ahead energy market. The programme will take a csv of the following format

| Company | Supply/Demand | ID  | Quantity [MWh] | Price [€/MWh] |
| ------- | ------------- | --- | -------------- | ------------- |
| ...     | ...           | ... | ...            | ...           |

it must be uploaded in the following format: `data/name.csv`. The market clearing price will be solved, as well as ... .

The results will be stored as csv files in a directory `/solutions/name` and visualised (see examples in `/plots/name`). As is, the programme will run based on an example auction created Pierre Pinson for the [course](http://pierrepinson.com/index.php/teaching/) *31761 - Renewables in Energy Markets* at the Technical University of Denmark.

## Problem Background

A **market-clearing price** is the price of a good or service at which the quantity supplied equals the quantity demanded, also called the equilibrium price. In the context of the day-ahead energy market, this is the price at which market supply, dictated by generators, is equal to market demand (dictated by retailers, large consumers, aggregators etc).

### Inputs

All offers in the market are formulated in terms of a quantity $P$ and a price $\lambda$.

Supply side ($N_{G}$ supply offers):
- Set of offers: 
```math
\mathcal{L}_{G} = \left\{G_{j}, \ j = 1, \dots, N_{G}\right\}
```

- Maximum quantity for offer $G_{j}:$ $P_{j}^{G}$
- Price for offer $G_{j}$: $\lambda_{j}^{G}$

Demand side ($N_{D}$ demand offers):
- Set of offers:
```math
\mathcal{L}_{D} = \left\{ D_{i}, \ i = 1, \dots, N_{D} \right\}
```
- Maximum quantity for offer $D_{i}:$ $P_{i}^{D}$
- Price for offer $D_{i}$: $\lambda_{i}^{D}$

### Decision Variables

- Generation schedule: $\mathbf{y}^{G} = \left[y_{j}^{G}, \dots, y_{N_{G}}^{G}\right]^{\top}$
	- Subject to: $0 \leq y_{j}^{G} \leq P_{j}^{G}$
- Consumption schedule: $\mathbf{y}^{D} = \left[y_{i}^{D}, \dots, y_{N_{D}}^{D}\right]^{\top}$
	- Subject to: $0 \leq y_{i}^{D} \leq P_{i}^{D}$
### Centralised Welfare Optimisation

The above conditions can be combined to formulate the *social welfare maximisation* problem:

```math
\begin{align}
\underset{\mathbf{y}^{G}, \mathbf{y}^{D}}{\max} \quad &\sum\limits_{i=1}^{N_{D}}\lambda_{i}^{D}y_{i}^{D} - \sum\limits_{j=1}^{N_{G}}\lambda_{j}^{G}y_{j}^{G} \\
\text{subject to} \quad &\sum\limits_{j=1}^{N_{G}}y_{j}^{G} - \sum\limits_{i=1}^{N_{D}} y_{i}^{D} = 0 \\
&0 \leq y_{i}^{D} \leq P_{i}^{D},\ i= 1, \dots, N_{D} \\
&0 \leq y_{i}^{G} \leq P_{i}^{G},\ i= 1, \dots, N_{G}
\end{align}
```

Reformulating as a *minimisation problem*
```math
\begin{align}
\underset{\mathbf{y}^{G}, \mathbf{y}^{D}}{\min} \quad &\sum\limits_{j=1}^{N_{G}}\lambda_{j}^{G}y_{j}^{G} - \sum\limits_{i=1}^{N_{D}}\lambda_{i}^{D}y_{i}^{D} 
\end{align}
```
Subject to the same constraints as above. We have now formulated a standard constrained **Linear Program:**

```math
\begin{align}
\underset{\mathbf{y}}{\min} \quad &\mathbf{c}^{\top}\mathbf{y} \\
\text{subject to} \quad &\mathbf{A}\mathbf{y} \leq \mathbf{b} \\
&\mathbf{A}_{\text{eq}}\mathbf{y} = \mathbf{b}_{\text{eq}}\\
& \mathbf{y} \geq 0
\end{align}
```

#### Vectors and Matrices in the Objective Function
Where the vectors $\mathbf{y}$ of optimisation variables and $\mathbf{c}$ of weights in the objective function are constructed as
```math
\begin{align}
\mathbf{y} &= \begin{bmatrix} \mathbf{y}_{G} \\ \mathbf{y}_{D} \end{bmatrix} = \begin{bmatrix} y_{1}^{G} \\ y_{2}^{G} \\ \vdots \\ y_{N_{G}}^{G} \\ y_{1}^{D} \\ y_{2}^{D}\\ \vdots \\ y_{N_{D}}^{D} \end{bmatrix}, \quad \mathbf{y} \in \mathbb{R}^{N_{G}+N_{D}}
\end{align}
```
and 
```math
\begin{align}
\mathbf{c} &= \begin{bmatrix} \mathbf{\lambda}_{G} \\ -\mathbf{\lambda}_{D} \end{bmatrix} = \left\[\begin{matrix} \lambda_{1}^{G} \\ \lambda_{2}^{G} \\ \vdots \\ \lambda_{N_{G}}^{G} \\ -\lambda_{1}^{D} \\ -\lambda_{2}^{D}\\ \vdots \\ -\lambda_{N_{D}}^{D} \end{matrix}\right], \quad \mathbf{c} \in \mathbb{R}^{N_{G}+N_{D}}
\end{align}
```

#### Vectors and Matrices Defining Constraints

For the equality constraint (balance of generation and consumption)

```math
\mathbf{A}_{\text{eq}} = \left[1, \dots, 1, -1, \dots, -1\right] \in \mathbb{R}^{N_{G}+N_{D}}, \quad \mathbf{b}_{\text{eq}} = 0
```

For the inequality constraint (ensuring generation and consumption levels are within limits)
```math
\mathbf{A} = I \in \mathbb{R}^{\left( N_{G}+N_{D} \right) \times \left( N_{G}+N_{D} \right)}
```
and 
```math
b = \begin{bmatrix} P_{1}^{G} \\ \vdots \\ P_{N_{G}}^{G} \\ P_{1}^{D} \\ \vdots \\ P_{N_{D}}^{D} \end{bmatrix} \in \mathbb{R}^{N_{G}+N_{D}}
```
