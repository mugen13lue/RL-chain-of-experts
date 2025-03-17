import gurobipy as gp
from gurobipy import GRB

def prob_134(cheesecake, caramel_cake, cheesecake_calories, cheesecake_sugar, caramel_cake_calories, caramel_cake_sugar, min_caramel_cake_slices, max_calories):
    """
    Args:
        cheesecake: an integer, the number of slices of cheesecake
        caramel_cake: an integer, the number of slices of caramel cake
        cheesecake_calories: an integer, the calories in each slice of cheesecake
        cheesecake_sugar: an integer, the sugar content in each slice of cheesecake
        caramel_cake_calories: an integer, the calories in each slice of caramel cake
        caramel_cake_sugar: an integer, the sugar content in each slice of caramel cake
        min_caramel_cake_slices: an integer, the minimum number of slices of caramel cake to eat
        max_calories: an integer, the maximum number of calories to consume in one day

    Returns:
        total_amount_of_sugar: an integer, the total amount of sugar consumed
    """
    model = gp.Model("cake_eating")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="cheesecake_slices")
    y = model.addVar(vtype=GRB.INTEGER, name="caramel_cake_slices")

    # Constraints
    model.addConstr(cheesecake_calories * x + caramel_cake_calories * y <= max_calories, "calories_constraint")
    model.addConstr(x >= 3*y, "cheesecake_preference_constraint")
    model.addConstr(y >= min_caramel_cake_slices, "min_caramel_cake_constraint")

    # Objective
    model.setObjective(cheesecake_sugar * x + caramel_cake_sugar * y, sense=GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    total_amount_of_sugar = model.objVal

    return total_amount_of_sugar