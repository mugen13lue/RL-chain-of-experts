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
    model = gp.Model("Pizza_Optimization")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of large pizzas
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of medium pizzas

    # Constraints
    model.addConstr(12*x + 8*y >= 10000, "Dough")
    model.addConstr(5*x + 4*y >= 4400, "Toppings")
    model.addConstr(y >= 200, "Medium_Pizzas")
    model.addConstr(x >= 2*y, "Large_Pizzas")

    # Objective
    model.setObjective(12*x + 8*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj