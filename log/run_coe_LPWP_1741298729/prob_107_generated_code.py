import gurobipy as gp
from gurobipy import GRB

def prob_107(fish, chicken):
    """
    Args:
        fish: an integer, number of fish meals
        chicken: an integer, number of chicken meals
    Returns:
        obj: an integer, minimized fat intake
    """
    model = gp.Model("diet_problem")

    # Define decision variables with upper bounds
    x = model.addVar(lb=0, ub=fish, vtype=GRB.INTEGER, name="fish_meals")
    y = model.addVar(lb=0, ub=chicken, vtype=GRB.INTEGER, name="chicken_meals")
    F = model.addVar(lb=0, vtype=GRB.INTEGER, name="fat_intake")

    # Set objective function: minimize fat intake
    model.setObjective(F, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(10*x + 15*y >= 130)
    model.addConstr(12*x + 8*y >= 120)
    model.addConstr(7*x + 10*y == F)
    model.addConstr(y >= 2*x)

    # Optimize model
    model.optimize()

    # Get the minimized fat intake
    obj = model.objVal

    return obj