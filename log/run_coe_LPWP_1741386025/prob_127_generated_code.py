import gurobipy as gp
from gurobipy import GRB

def prob_127(cashews, almonds, calories_almonds, protein_almonds, calories_cashews, protein_cashews, twice, fat_almonds, fat_cashews, min_calories, min_protein):
    """
    Args:
        cashews: an integer (unused)
        almonds: an integer (unused)
        calories_almonds: an integer
        protein_almonds: an integer
        calories_cashews: an integer
        protein_cashews: an integer
        twice: an integer
        fat_almonds: an integer
        fat_cashews: an integer
        min_calories: an integer
        min_protein: an integer
    Returns:
        obj: an integer
    """
    # Create a new model
    model = gp.Model("diet_problem")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="x")  # servings of almonds
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="y")  # servings of cashews
    F = model.addVar(lb=0, vtype=GRB.INTEGER, name="F")  # fat intake

    # Set objective function: minimize fat intake
    model.setObjective(F, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(calories_almonds*x + calories_cashews*y >= min_calories, "Calories")
    model.addConstr(protein_almonds*x + protein_cashews*y >= min_protein, "Protein")
    model.addConstr(x >= twice*y, "Almonds Constraint")
    model.addConstr(fat_almonds*x + fat_cashews*y == F, "Fat")

    # Optimize the model
    model.optimize()

    # Return the optimal objective value
    return model.objVal