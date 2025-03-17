import gurobipy as gp
from gurobipy import GRB

def prob_141(turkey_dinner, tuna_salad_sandwich):
    """
    Args:
        turkey_dinner: an integer, number of turkey dinners to be eaten
        tuna_salad_sandwich: an integer, number of tuna salad sandwiches to be eaten
    Returns:
        obj: an integer, optimal objective value (minimized fat intake)
    """
    # Create a new model
    model = gp.Model("diet_problem")

    # Define decision variables
    x1 = model.addVar(vtype=GRB.INTEGER, name="turkey_dinner")
    x2 = model.addVar(vtype=GRB.INTEGER, name="tuna_salad_sandwich")

    # Set objective function: minimize fat intake
    model.setObjective(12*x1 + 8*x2, GRB.MINIMIZE)

    # Add constraints
    model.addConstr(20*x1 + 18*x2 >= 150, "protein")
    model.addConstr(30*x1 + 25*x2 >= 200, "carbs")
    model.addConstr(x1 <= 0.4*(x1 + x2), "turkey_dinner_limit")

    # Optimize model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj