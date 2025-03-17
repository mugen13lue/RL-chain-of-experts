import gurobipy as gp
from gurobipy import GRB

def prob_204(milk, vegetables):
    """
    Args:
        milk: an integer, amount of milk
        vegetables: an integer, amount of vegetables
    Returns:
        obj: an integer, objective value (cost)
    """
    # Create a new model
    model = gp.Model("min_cost_diet")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of glasses of milk
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of plates of vegetables

    # Set objective function: Minimize Cost
    model.setObjective(x + 2*y, GRB.MINIMIZE)

    # Add constraints
    model.addConstr(40*x + 15*y >= 100, "calcium_constraint")
    model.addConstr(25*x + 30*y >= 50, "iron_constraint")

    # Optimize model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj