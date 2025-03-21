import gurobipy as gp
from gurobipy import GRB

def prob_80(regular, emergency_fire):
    """
    Args:
        regular: an integer, representing the number of regular fire fighters.
        emergency_fire: an integer, representing the number of emergency fire fighters.
    
    Returns:
        obj: an integer, representing the minimum total number of fire fighters.
    """
    # Create a new model
    model = gp.Model("fire_fighters")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="regular_fire_fighters")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="emergency_fire_fighters")

    # Set objective function: minimize total number of fire fighters
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(10*x + 6*y >= 300, "total_hours_constraint")
    model.addConstr(300*x + 100*y <= 7000, "budget_constraint")

    # Optimize the model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj