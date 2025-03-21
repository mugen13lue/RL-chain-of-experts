import gurobipy as gp
from gurobipy import GRB

def prob_205():
    """
    Minimize the cost of the diet.

    Returns:
        obj: the objective value, i.e., the minimum cost of the diet.
    """
    # Create a new model
    model = gp.Model("diet_problem")

    # Decision variables
    x = model.addVar(vtype=GRB.CONTINUOUS, name="noodles")
    y = model.addVar(vtype=GRB.CONTINUOUS, name="protein_bars")

    # Set objective
    model.setObjective(5*x + 2.5*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(600*x + 250*y >= 2000, "Calories")
    model.addConstr(1.5*x + 5*y >= 16, "Protein")

    # Optimize model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj