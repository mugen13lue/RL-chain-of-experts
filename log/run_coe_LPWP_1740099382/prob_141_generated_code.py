import gurobipy as gp
from gurobipy import GRB

def prob_141(turkey_dinner, tuna_salad_sandwich):
    """
    Args:
        turkey_dinner: an integer, number of turkey dinners
        tuna_salad_sandwich: an integer, number of tuna salad sandwiches
    Returns:
        obj: an integer, minimized fat intake
    """
    # Create a new model
    model = gp.Model("meal_optimization")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="turkey_dinner")
    y = model.addVar(vtype=GRB.INTEGER, name="tuna_salad_sandwich")

    # Set objective function: minimize fat intake
    model.setObjective(12*x + 8*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(20*x + 18*y >= 150, "Protein")
    model.addConstr(30*x + 25*y >= 200, "Carbs")
    model.addConstr(x <= 0.4*(x + y), "Turkey_Dinner_Limit")

    # Optimize model
    model.optimize()

    # Get the minimized fat intake
    obj = model.objVal

    return obj