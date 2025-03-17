import gurobipy as gp
from gurobipy import GRB

def prob_238(large_pizzas, medium_pizzas):
    """
    Args:
        large_pizzas: an integer, number of large pizzas
        medium_pizzas: an integer, number of medium pizzas
    Returns:
        obj: an integer, time spent baking
    """
    # Create a new model
    model = gp.Model("pizza_baking")

    # Decision variables
    x1 = model.addVar(vtype=GRB.INTEGER, name="large_pizzas")
    x2 = model.addVar(vtype=GRB.INTEGER, name="medium_pizzas")

    # Objective function: minimize time spent baking
    model.setObjective(12*x1 + 8*x2, GRB.MINIMIZE)

    # Constraints
    model.addConstr(12*x1 + 8*x2 >= 10000, "dough_constraint")
    model.addConstr(5*x1 + 4*x2 >= 4400, "toppings_constraint")
    model.addConstr(x2 >= 200, "medium_pizzas_constraint")
    model.addConstr(x1 >= 2*x2, "large_pizzas_constraint")

    # Optimize the model
    model.optimize()

    # Get the optimal solution
    obj = model.objVal

    return obj