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

    # Define decision variables based on function arguments
    x = model.addVar(vtype=GRB.INTEGER, name="counter_top")
    y = model.addVar(vtype=GRB.INTEGER, name="fridge")

    # Set objective function: minimize the total number of machines
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(50*x + 70*y <= 500, "heat_output")
    model.addConstr(80*x + 150*y >= 1000, "ice_cream_production")
    model.addConstr(x >= 0, "non_negativity_counter_top")
    model.addConstr(y >= 0, "non_negativity_fridge")

    # Optimize the model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj