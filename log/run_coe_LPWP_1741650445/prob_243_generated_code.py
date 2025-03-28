import gurobipy as gp
from gurobipy import GRB

def prob_243():
    """
    Returns:
        obj: an integer representing the objective value, i.e., the minimized cooking time
    """
    model = gp.Model("meal_optimization")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="original_combos")
    y = model.addVar(vtype=GRB.INTEGER, name="experimental_combos")

    # Constraints
    model.addConstr(20*x + 25*y <= 800, "food_waste_constraint")
    model.addConstr(45*x + 35*y <= 900, "wrapping_waste_constraint")

    # Objective
    model.setObjective(10*x + 15*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    # Return objective value
    return int(model.objVal)