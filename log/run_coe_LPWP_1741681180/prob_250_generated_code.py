import gurobipy as gp
from gurobipy import GRB

def prob_250(cans, glass_bottles, required_capacity, constraint2, constraint3):
    """
    Args:
        cans: an integer, representing the number of cans produced
        glass_bottles: an integer, representing the number of glass bottles produced
        required_capacity: an integer, representing the minimum required capacity in ml
        constraint2: an integer, representing the multiplier for cans compared to glass bottles
        constraint3: an integer, representing the minimum number of glass bottles required
    Returns:
        obj: an integer, representing the objective value (maximized number of units)
    """
    # Create a new model
    model = gp.Model("soda_production")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="cans")
    y = model.addVar(vtype=GRB.INTEGER, name="glass_bottles")

    # Set objective function: maximize the total number of units produced
    model.setObjective(x + y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(250*x + 1000*y >= required_capacity, "capacity_constraint")
    model.addConstr(x >= constraint2*y, "cans_constraint")
    model.addConstr(y >= constraint3, "glass_bottles_constraint")

    # Optimize the model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj