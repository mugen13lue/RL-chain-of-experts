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
    # Create a new model
    model = gp.Model("diet_problem")

    # Define decision variables
    x1 = model.addVar(vtype=GRB.INTEGER, name="fish_meals")
    x2 = model.addVar(vtype=GRB.INTEGER, name="chicken_meals")

    # Set objective function: minimize fat intake
    model.setObjective(7*x1 + 10*x2, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(10*x1 + 15*x2 >= 130, "protein_constraint")
    model.addConstr(12*x1 + 8*x2 >= 120, "iron_constraint")
    model.addConstr(x2 >= 2*x1, "preference_constraint")

    # Optimize the model
    model.optimize()

    # Get the minimized fat intake
    obj = model.objVal

    return obj