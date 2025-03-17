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
    # Create a new model
    model = gp.Model("syrup_optimization")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x")  # servings of syrup 1
    y = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="y")  # servings of syrup 2

    # Set objective function: minimize sugar intake
    model.setObjective(0.5*x + 0.3*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(0.5*x + 0.2*y <= 5, "Throat_Medicine")
    model.addConstr(0.4*x + 0.5*y >= 4, "Lung_Medicine")

    # Optimize model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj