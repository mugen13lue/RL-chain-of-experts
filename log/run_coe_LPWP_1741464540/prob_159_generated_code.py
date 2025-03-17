import gurobipy as gp
from gurobipy import GRB

def prob_159(trucks, vans):
    """
    Args:
        trucks: an integer, number of trucks
        vans: an integer, number of vans
    Returns:
        obj: an integer, number of trips
    """
    # Create a new model
    model = gp.Model("shipment_planning")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="trucks")
    y = model.addVar(vtype=GRB.INTEGER, name="vans")

    # Set objective function: minimize total number of trips
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(1000*x + 500*y >= 50000, "num_patties")
    model.addConstr(300*x + 100*y <= 12500, "budget_constraint")
    model.addConstr(x <= y, "truck_limit")

    # Set the values of decision variables based on input parameters
    x.lb = trucks
    y.lb = vans

    # Optimize model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj