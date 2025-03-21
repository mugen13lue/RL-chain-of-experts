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
    model = gp.Model("Pizza_Baking")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="medium_pizzas")
    y = model.addVar(vtype=GRB.INTEGER, name="large_pizzas")

    # Constraints
    model.addConstr(8*x + 12*y >= 10000, "Dough")
    model.addConstr(4*x + 5*y >= 4400, "Toppings")
    model.addConstr(x >= 200, "Medium_Pizzas")
    model.addConstr(y >= 2*x, "Large_Pizzas")

    # Objective
    model.setObjective(8*x + 12*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    obj = model.objVal

    return obj