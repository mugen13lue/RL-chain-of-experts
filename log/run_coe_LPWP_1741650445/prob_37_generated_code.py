import gurobipy as gp
from gurobipy import GRB

def prob_37(mango_cost, guava_cost):
    """
    Args:
        mango_cost: an integer, the cost of one mango
        guava_cost: an integer, the cost of one guava
    Returns:
        profit: an integer, the maximum profit
    """
    # Create a new model
    model = gp.Model("profit_maximization")

    # Decision variables
    x = model.addVar(lb=100, ub=150, vtype=GRB.INTEGER, name="mangos")
    y = model.addVar(ub=50, vtype=GRB.INTEGER, name="guavas")

    # Objective function: Maximize profit
    model.setObjective(3*x + 4*y, sense=GRB.MAXIMIZE)

    # Constraints
    model.addConstr(mango_cost*x + guava_cost*y <= 20000, "budget_constraint")
    model.addConstr(y <= (1/3)*x, "guava_sales_limit")

    # Optimize the model
    model.optimize()

    # Return the maximum profit
    return model.objVal