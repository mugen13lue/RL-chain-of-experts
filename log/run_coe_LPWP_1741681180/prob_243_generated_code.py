import gurobipy as gp
from gurobipy import GRB

def prob_243(original_meal, experimental_meal):
    """
    Args:
        original_meal: an integer representing the number of original meals
        experimental_meal: an integer representing the number of experimental meals
    Returns:
        obj: an integer representing the objective value, i.e., the minimized cooking time
    """
    model = gp.Model("meal_optimization")

    # Decision variables
    x1 = model.addVar(vtype=GRB.INTEGER, name="original_meal")
    x2 = model.addVar(vtype=GRB.INTEGER, name="experimental_meal")

    # Objective function: minimize cooking time
    model.setObjective(10*x1 + 15*x2, GRB.MINIMIZE)

    # Constraints
    model.addConstr(20*x1 + 25*x2 <= 800, "food_waste_constraint")
    model.addConstr(45*x1 + 35*x2 <= 900, "wrapping_waste_constraint")

    # Optimize model
    model.optimize()

    # Get objective value
    obj = model.objVal

    return obj