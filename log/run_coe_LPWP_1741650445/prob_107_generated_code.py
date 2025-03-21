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

    # Variables
    fish_meals = model.addVar(name="fish_meals")
    chicken_meals = model.addVar(name="chicken_meals")
    fat_intake = model.addVar(name="fat_intake")

    # Constraints
    model.addConstr(10*fish_meals + 15*chicken_meals >= 130)
    model.addConstr(12*fish_meals + 8*chicken_meals >= 120)
    model.addConstr(7*fish_meals + 10*chicken_meals == fat_intake)
    model.addConstr(chicken_meals >= 2*fish_meals)

    # Objective
    model.setObjective(fat_intake, GRB.MINIMIZE)

    # Solve the model
    model.optimize()

    return int(fat_intake.x) if model.status == GRB.OPTIMAL else None