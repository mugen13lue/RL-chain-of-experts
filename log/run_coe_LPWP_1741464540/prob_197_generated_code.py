import gurobipy as gp
from gurobipy import GRB

def prob_197(small_canoes, smaller_diesel_boats):
    """
    Args:
        small_canoes: an integer, the number of small canoes used
        smaller_diesel_boats: an integer, the number of smaller diesel boats used
        
    Returns:
        total_number_of_canoes_and_diesel_boats: an integer, the total number of canoes and diesel boats needed
    """
    model = gp.Model("fish_transportation")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="canoes")
    y = model.addVar(vtype=GRB.INTEGER, name="diesel_boats")

    # Constraints
    model.addConstr(10*x + 15*y >= 1000, "transportation_constraint")
    model.addConstr(x >= 3*y, "environmental_constraint")

    # Objective
    model.setObjective(x + y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    total_number_of_canoes_and_diesel_boats = int(x.x + y.x)

    return total_number_of_canoes_and_diesel_boats