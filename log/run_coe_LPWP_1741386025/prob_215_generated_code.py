import gurobipy as gp
from gurobipy import GRB

def prob_215(freezers, washing_machine, constraint1, constraint2):
    """
    Args:
        freezers: an integer representing the number of freezers
        washing_machine: an integer representing the number of washing machines
        constraint1: an integer representing the first constraint
        constraint2: an integer representing the second constraint

    Returns:
        obj: an integer representing the objective value
    """
    # Create a new model
    model = gp.Model("repairman_optimization")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="washing_machines")
    y = model.addVar(vtype=GRB.INTEGER, name="freezers")

    # Set objective function
    model.setObjective(250*x + 375*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(30*x + 20*y <= 5000, name="inspection_time_constraint")
    model.addConstr(90*x + 125*y <= 20000, name="fixing_time_constraint")
    model.addConstr(x >= 0, name="non_negativity_constraint_x")
    model.addConstr(y >= 0, name="non_negativity_constraint_y")

    # Optimize the model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj