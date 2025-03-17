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
    model = gp.Model("food_truck")

    # Decision variables
    x = model.addVar(lb=100, ub=150, vtype=GRB.INTEGER, name="mangos")
    y = model.addVar(lb=0, ub=50, vtype=GRB.INTEGER, name="guavas")

    # Objective function: Maximize profit
    model.setObjective(3*x + 4*y, sense=GRB.MAXIMIZE)

    # Constraints
    model.addConstr(5*x + 3*y <= 20000, "budget_constraint")
    model.addConstr(y <= (1/3)*x, "guava_constraint")

    # Optimize the model
    model.optimize()

    # Return the maximum profit
    return model.objVal