import gurobipy as gp
from gurobipy import GRB

def prob_235(molars, canines):
    """
    Args:
        molars: an integer, the number of molars
        canines: an integer, the number of canines
    
    Returns:
        obj: an integer, the amount of pain killer needed
    """
    # Create a new model
    model = gp.Model("dentist_problem")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="x")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="y")
    P = model.addVar(lb=0, name="P")

    # Set objective function
    model.setObjective(P, GRB.MINIMIZE)

    # Add constraints
    model.addConstr(20*x + 15*y <= 3000)
    model.addConstr(3*x + 2.3*y <= P)
    model.addConstr(y >= 0.6*(x+y))
    model.addConstr(x >= 45)

    # Optimize model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj