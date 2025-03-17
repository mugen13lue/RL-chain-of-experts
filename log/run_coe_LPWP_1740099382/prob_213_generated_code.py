import gurobipy as gp
from gurobipy import GRB

def prob_213(regular_handbags, premium_handbags):
    """
    Args:
        regular_handbags (int): Number of regular handbags to sell
        premium_handbags (int): Number of premium handbags to sell

    Returns:
        profit (int): Maximum monthly profit
    """
    # Create a new model
    model = gp.Model("handbags_profit_maximization")

    # Define decision variables
    x = model.addVar(lb=0, ub=475, vtype=GRB.INTEGER, name="regular_handbags")
    y = model.addVar(lb=0, ub=475, vtype=GRB.INTEGER, name="premium_handbags")

    # Set objective function
    model.setObjective(30*x + 180*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(200*x + 447*y <= 250000, "budget_constraint")

    # Optimize model
    model.optimize()

    # Get the optimal solution
    profit = model.objVal

    return profit