import gurobipy as gp
from gurobipy import GRB

def prob_114(apple_flavored_baby, carrot_flavored_baby):
    """
    Args:
        apple_flavored_baby: an integer, number of servings of apple flavored baby food
        carrot_flavored_baby: an integer, number of servings of carrot flavored baby food

    Returns:
        objective_value: an integer, the maximum fat intake
    """
    # Create a new model
    model = gp.Model("baby_food_optimization")

    # Define decision variables
    x = model.addVar(name="apple_flavored_servings")
    y = model.addVar(name="carrot_flavored_servings")

    # Set objective function: maximize fat intake
    model.setObjective(2*x, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(2*x + 4*y >= 0, "fat_requirement")
    model.addConstr(5*x + 3*y <= 100, "folate_requirement")
    model.addConstr(y >= 2, "min_carrot_servings")
    model.addConstr(x == 3*y, "apple_to_carrot_ratio")

    # Optimize the model
    model.optimize()

    # Get the optimal objective value
    objective_value = model.objVal

    return objective_value