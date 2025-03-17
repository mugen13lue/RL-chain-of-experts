import gurobipy as gp
from gurobipy import GRB

def prob_64(small_container, large_container):
    """
    Args:
        small_container: an integer, number of small containers used
        large_container: an integer, number of large containers used
    Returns:
        obj: an integer, amount of paste produced
    """
    # Create a new model
    model = gp.Model("paste_production")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="small_containers")
    y = model.addVar(vtype=GRB.INTEGER, name="large_containers")

    # Set objective function
    model.setObjective(20*x + 30*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(10*x + 20*y <= 500, "water_constraint")
    model.addConstr(15*x + 20*y <= 700, "powdered_pill_constraint")

    # Optimize model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj