import gurobipy as gp
from gurobipy import GRB

def prob_35(pill_A, pill_B, sleep_inducing_constraint, anti_inflammatory_constraint):
    """
    Args:
        pill_A: an integer, number of pill A
        pill_B: an integer, number of pill B
        sleep_inducing_constraint: an integer, constraint value for sleep inducing medicine
        anti_inflammatory_constraint: an integer, constraint value for anti-inflammatory medicine
    Returns:
        cost: an integer, minimum cost
    """
    # Create a new model
    model = gp.Model("pill_optimization")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")
    y = model.addVar(vtype=GRB.INTEGER, name="y")

    # Set objective function
    model.setObjective(4*x + 5*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(3*x + 6*y >= sleep_inducing_constraint, "sleep_inducing_constraint")
    model.addConstr(5*x + y >= anti_inflammatory_constraint, "anti_inflammatory_constraint")

    # Optimize model
    model.optimize()

    # Get the minimum cost
    cost = model.objVal

    return cost