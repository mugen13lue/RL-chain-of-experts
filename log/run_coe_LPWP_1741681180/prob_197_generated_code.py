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

    # Decision variables
    canoes = model.addVar(vtype=GRB.INTEGER, name="canoes")
    diesel_boats = model.addVar(vtype=GRB.INTEGER, name="diesel_boats")

    # Objective function: minimize the total number of canoes and diesel boats
    model.setObjective(canoes + diesel_boats, sense=GRB.MINIMIZE)

    # Constraints
    model.addConstr(canoes >= 3 * diesel_boats)  # Number of canoes at least 3 times the number of diesel boats
    model.addConstr(10 * canoes + 15 * diesel_boats >= 1000)  # At least 1000 fish need to be transported

    # Optimize the model
    model.optimize()

    # Retrieve the total number of canoes and diesel boats needed
    total_number_of_canoes_and_diesel_boats = canoes.x + diesel_boats.x

    return total_number_of_canoes_and_diesel_boats