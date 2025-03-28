import gurobipy as gp
from gurobipy import GRB

def prob_205(protein_bars, noodles):
    """
    Minimize the cost of the diet.

    Args:
        protein_bars: an integer representing the number of protein bars.
        noodles: an integer representing the number of servings of noodles.

    Returns:
        obj: the objective value, i.e., the minimum cost of the diet.
    """
    # Create a new model
    model = gp.Model("diet_problem")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="noodles")
    y = model.addVar(vtype=GRB.INTEGER, name="protein_bars")

    # Set objective function: Minimize Cost
    model.setObjective(5*x + 2.5*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(600*x + 250*y >= 2000, "Calories")
    model.addConstr(1.5*x + 5*y >= 16, "Protein")

    # Optimize model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj