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
    model = gp.Model("Pizza Optimization")

    # Variables
    num_medium_pizzas = model.addVar(vtype=GRB.INTEGER, name="num_medium_pizzas")
    num_large_pizzas = model.addVar(vtype=GRB.INTEGER, name="num_large_pizzas")

    # Constraints
    model.addConstr(8*num_medium_pizzas + 12*num_large_pizzas >= 10000, "Dough")
    model.addConstr(4*num_medium_pizzas + 5*num_large_pizzas >= 4400, "Toppings")
    model.addConstr(num_medium_pizzas >= 200, "Medium Pizzas")
    model.addConstr(num_large_pizzas >= 2*num_medium_pizzas, "Large Pizzas")

    # Objective
    model.setObjective(8*num_medium_pizzas + 12*num_large_pizzas, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj