import gurobipy as gp
from gurobipy import GRB

def prob_89(goat, chicken, goat_meat, goat_base, chicken_meat, chicken_base):
    """
    Args:
        goat: an integer, number of goat curry bowls
        chicken: an integer, number of chicken curry bowls
        goat_meat: an integer, units of goat meat required per bowl of goat curry
        goat_base: an integer, units of curry base required per bowl of goat curry
        chicken_meat: an integer, units of chicken meat required per bowl of chicken curry
        chicken_base: an integer, units of curry base required per bowl of chicken curry
    Returns:
        obj: an integer, total amount of curry base used
    """
    # Create a new model
    model = gp.Model("curry_optimization")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="goat_curry_bowls")
    y = model.addVar(vtype=GRB.INTEGER, name="chicken_curry_bowls")

    # Set objective function: minimize total amount of curry base used
    model.setObjective(6*x + 5*y, GRB.MINIMIZE)

    # Add constraints
    model.addConstr(3*x <= 1500, "goat_meat_constraint")
    model.addConstr(5*y <= 2000, "chicken_meat_constraint")
    model.addConstr(y >= 0.25*(x + y), "chicken_percentage_constraint")
    model.addConstr(x > y, "popularity_constraint")

    # Optimize the model
    model.optimize()

    # Get the total amount of curry base used
    obj = model.objVal

    return obj