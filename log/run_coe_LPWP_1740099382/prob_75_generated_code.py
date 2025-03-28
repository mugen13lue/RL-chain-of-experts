import gurobipy as gp
from gurobipy import GRB

def prob_75(traditional_machine, modern_machine):
    """
    Args:
        traditional_machine: an integer, represents the number of acres to be used for traditional machine
        modern_machine: an integer, represents the number of acres to be used for modern machine
    Returns:
        obj: an integer, represents the maximum amount of tea leaves that can be picked
    """
    
    # Create a new model
    model = gp.Model("Tea Leaves Picking")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="traditional_machine_acres")
    y = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="modern_machine_acres")

    # Set objective function
    model.setObjective(30*x + 40*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(30*x + 40*y <= 500, "tea_leaves_picked")
    model.addConstr(10*x + 15*y <= 6000, "waste_produced")
    model.addConstr(20*x + 15*y <= 9000, "fuel_usage")

    # Optimize model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj