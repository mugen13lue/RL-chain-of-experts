import gurobipy as gp
from gurobipy import GRB

def minimize_fat_intake(cashews, almonds, calorie_cashews, protein_cashews, calorie_almonds, protein_almonds, fat_cashews, fat_almonds, calorie_target, protein_target):
    """
    Args:
        cashews: an integer
        almonds: an integer
        calorie_cashews: an integer
        protein_cashews: an integer
        calorie_almonds: an integer
        protein_almonds: an integer
        fat_cashews: an integer
        fat_almonds: an integer
        calorie_target: an integer
        protein_target: an integer
    Returns:
        obj: an integer
        servings: a tuple of integers (servings of almonds, servings of cashews)
    """
    # Create a new model
    model = gp.Model("diet_problem")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="x")  # Number of servings of almonds
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="y")  # Number of servings of cashews

    # Set objective function: minimize fat intake
    model.setObjective(fat_almonds*x + fat_cashews*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(calorie_almonds*x + calorie_cashews*y >= calorie_target, "calorie_constraint")
    model.addConstr(protein_almonds*x + protein_cashews*y >= protein_target, "protein_constraint")
    model.addConstr(x >= 2*y, "twice_constraint")

    # Optimize the model
    model.optimize()

    # Return the optimal objective value and servings
    obj = model.objVal
    servings = (int(x.x), int(y.x))
    return obj, servings