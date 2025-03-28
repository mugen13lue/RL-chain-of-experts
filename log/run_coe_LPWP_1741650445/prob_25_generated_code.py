import gurobipy as gp
from gurobipy import GRB

def prob_25(apartments, townhouses):
    """
    
    Args:
        apartments: an integer, amount of money invested in apartments
        townhouses: an integer, amount of money invested in townhouses
    
    Returns:
        profit: an integer, maximum profit
    """
    
    # Create a new model
    model = gp.Model("investment_optimization")
    
    # Decision variables
    x = model.addVar(lb=0, ub=200000, name="apartments")
    y = model.addVar(lb=0, name="townhouses")
    
    # Objective function: maximize profit
    model.setObjective(0.10*x + 0.15*y, sense=GRB.MAXIMIZE)
    
    # Constraints
    model.addConstr(x + y == 600000, "total_investment")
    model.addConstr(x >= 0.5*y, "minimum_investment_ratio")
    
    # Optimize model
    model.optimize()
    
    # Get the optimal profit
    profit = model.objVal
    
    return profit