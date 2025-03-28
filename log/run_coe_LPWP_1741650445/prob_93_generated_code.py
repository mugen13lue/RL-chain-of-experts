import gurobipy as gp
from gurobipy import GRB

def prob_93(generator_A, generator_B):
    """
    Args:
        generator_A: an integer, number of generator A
        generator_B: an integer, number of generator B
    Returns:
        obj: an integer, objective value
    """
    # Create a new model
    model = gp.Model("generator_problem")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")
    y = model.addVar(vtype=GRB.INTEGER, name="y")

    # Set objective function
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(40*x + 30*y >= 1000, "hydrogen_production")
    model.addConstr(300*x + 200*y <= 3000, "pollutant_limit")

    # Optimize the model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj