import gurobipy as gp
from gurobipy import GRB

def prob_46(vegetable, fruits):
    """
    Solve the problem to minimize cost.

    Args:
        vegetable: an integer, representing the number of servings of vegetables
        fruits: an integer, representing the number of servings of fruits

    Returns:
        obj: an integer, representing the objective value (cost)
    """
    # Create a new model
    model = gp.Model("diet_problem")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="vegetables")
    y = model.addVar(vtype=GRB.INTEGER, name="fruits")

    # Set objective function: minimize cost
    model.setObjective(3*x + 5*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(2*x + 4*y >= 20, "vitamins")
    model.addConstr(3*x + y >= 30, "minerals")

    # Optimize the model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj