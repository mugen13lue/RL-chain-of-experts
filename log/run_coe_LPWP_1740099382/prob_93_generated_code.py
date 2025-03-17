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

    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")
    y = model.addVar(vtype=GRB.INTEGER, name="y")

    # Set objective
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Constraints
    model.addConstr(40*x + 30*y >= 1000)
    model.addConstr(300*x + 200*y <= 3000)
    model.addConstr(x >= 0)
    model.addConstr(y >= 0)

    # Optimize model
    model.optimize()

    # Get objective value
    obj = model.objVal

    return obj