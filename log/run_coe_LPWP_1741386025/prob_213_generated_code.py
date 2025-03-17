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
    model = gp.Model("handbag_optimization")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="regular_handbags")
    y = model.addVar(vtype=GRB.INTEGER, name="premium_handbags")

    # Set objective function
    model.setObjective(30*x + 180*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(200*x + 447*y <= 250000, "budget_constraint")
    model.addConstr(x <= 475, "regular_handbags_constraint")
    model.addConstr(y <= 475, "premium_handbags_constraint")

    # Optimize model
    model.optimize()

    # Get the optimal solution
    profit = model.objVal

    return profit