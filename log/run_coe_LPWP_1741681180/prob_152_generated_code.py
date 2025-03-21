import gurobipy as gp
from gurobipy import GRB

def prob_152():
    """
    Returns:
        obj: an integer, total amount of time needed to transport the ducks
    """
    # Create a new model
    model = gp.Model("duck_transportation")

    # Define decision variables
    boat_trips = model.addVar(vtype=GRB.INTEGER, name="boat_trips")
    canoe_trips = model.addVar(vtype=GRB.INTEGER, name="canoe_trips")

    # Set objective function: minimize total time
    model.setObjective(20*boat_trips + 40*canoe_trips, GRB.MINIMIZE)

    # Add constraints
    model.addConstr(boat_trips + canoe_trips <= 12, "max_trips_constraint")
    model.addConstr(canoe_trips >= 0.6*(boat_trips+canoe_trips), "canoe_percentage_constraint")
    model.addConstr(10*boat_trips + 8*canoe_trips >= 300, "min_ducks_constraint")

    # Optimize the model
    model.optimize()

    # Get the total amount of time needed to transport the ducks
    obj = model.objVal

    return obj