import gurobipy as gp
from gurobipy import GRB

def prob_110(syrup_1, syrup_2):
    """
    Args:
        syrup_1: a float, the number of servings of syrup 1
        syrup_2: a float, the number of servings of syrup 2
    Returns:
        obj: a float, the objective value (sugar intake)
    """
    model = gp.Model("syrup_optimization")

    # Define variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="x")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="y")

    # Set objective
    model.setObjective(0.5*x + 0.3*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(0.5*x + 0.2*y <= 5, name="Throat_Medicine")
    model.addConstr(0.4*x + 0.5*y >= 4, name="Lungs_Medicine")

    # Optimize model
    model.optimize()

    # Get objective value
    obj = model.objVal

    return obj