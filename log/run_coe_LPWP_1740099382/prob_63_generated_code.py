import gurobipy as gp
from gurobipy import GRB

def prob_63(counter_top_sized, fridge_sized_one):
    """
    Args:
        counter_top_sized: an integer, representing the number of counter-top sized machines
        fridge_sized_one: an integer, representing the number of fridge sized machines

    Returns:
        obj: an integer, representing the objective value (number of machines)
    """
    # Create a new model
    model = gp.Model("ice_cream_machine")

    # Define decision variables
    counter_top = model.addVar(vtype=GRB.INTEGER, name="counter_top")
    fridge = model.addVar(vtype=GRB.INTEGER, name="fridge")

    # Set objective function: minimize the total number of machines
    model.setObjective(counter_top + fridge, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(50*counter_top + 70*fridge <= 500, "heat_output")
    model.addConstr(80*counter_top + 150*fridge >= 1000, "ice_cream_production")

    # Optimize model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj