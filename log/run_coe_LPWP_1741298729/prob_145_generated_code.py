import gurobipy as gp
from gurobipy import GRB

def prob_145(process_1, process_2):
    """
    Args:
        process_1: an integer, number of times process 1 should be run
        process_2: an integer, number of times process 2 should be run

    Returns:
        obj: an integer, total time needed to minimize
    """
    # Create a new model
    model = gp.Model("drug_company_optimization")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x")  # Number of hours process 1 is run
    y = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="y")  # Number of hours process 2 is run

    # Set objective function: minimize total time needed
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(50*x + 60*y <= 2000, "preliminary_material_constraint")
    model.addConstr(35*x + 50*y >= 1200, "pain_killers_production_constraint")
    model.addConstr(12*x + 30*y >= 1200, "sleeping_pills_production_constraint")

    # Optimize the model
    model.optimize()

    # Get the total time needed
    obj = model.objVal

    return obj