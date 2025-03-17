import gurobipy as gp
from gurobipy import GRB

def prob_243():
    """
    Returns:
        obj: an integer representing the objective value, i.e., the minimized cooking time
    """
    # Create a new model
    model = gp.Model("meal_optimization")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="original_meals")
    y = model.addVar(vtype=GRB.INTEGER, name="experimental_meals")

    # Set objective function
    model.setObjective(10*x + 15*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(20*x + 25*y <= 800, "food_waste_constraint")
    model.addConstr(45*x + 35*y <= 900, "wrapping_waste_constraint")

    # Optimize model
    model.optimize()

    # Get the optimized objective value
    obj = model.objVal

    return obj