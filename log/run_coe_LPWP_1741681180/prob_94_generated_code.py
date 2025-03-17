import gurobipy as gp
from gurobipy import GRB

def prob_94():
    """
    Solves the optimization problem to maximize the amount of rare compound produced by chemical reactions A and B.
    Returns:
        objective: an integer, representing the amount of rare compound produced
    """
    # Create a new model
    model = gp.Model("chemical_reactions")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")
    y = model.addVar(vtype=GRB.INTEGER, name="y")

    # Set objective function
    model.setObjective(10*x + 8*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(5*x + 7*y <= 1000, "Rare_Inert_Gas")
    model.addConstr(6*x + 3*y <= 800, "Treated_Water")
    model.addConstr(x >= 0, "Non-negativity_x")
    model.addConstr(y >= 0, "Non-negativity_y")

    # Optimize the model
    model.optimize()

    # Get the optimal objective value
    objective = model.objVal

    return objective