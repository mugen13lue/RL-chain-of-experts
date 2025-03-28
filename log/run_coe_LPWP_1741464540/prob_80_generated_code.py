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

    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="regular_fire_fighters")
    y = model.addVar(vtype=GRB.INTEGER, name="emergency_fire_fighters")

    # Set objective
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(10*x + 6*y >= 300, "total_hours_constraint")
    model.addConstr(300*x + 100*y <= 7000, "budget_constraint")

    # Optimize model
    model.optimize()

    # Return the minimum total number of fire fighters
    return int(model.objVal)