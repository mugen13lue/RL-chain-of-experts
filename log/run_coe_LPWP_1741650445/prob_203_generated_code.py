from gurobipy import *

def prob_203(black_milk_tea, matcha_milk_tea):
    """
    Args:
        black_milk_tea: an integer, quantity of black milk tea to be made
        matcha_milk_tea: an integer, quantity of matcha milk tea to be made
    Returns:
        obj: a float, the maximum profit
    """
    # Create a new model
    model = Model("MilkTeaProduction")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="black_milk_tea")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="matcha_milk_tea")

    # Set objective function
    model.setObjective(7.5*x + 5*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(600*x + 525*y <= 30000, "milk_constraint")
    model.addConstr(10*x + 5*y <= 500, "honey_constraint")

    # Optimize model
    model.optimize()

    # Get the maximum profit
    obj = model.objVal

    return obj