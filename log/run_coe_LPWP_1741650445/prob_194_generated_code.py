import gurobipy as gp
from gurobipy import GRB

def prob_194():
    """
    Returns:
        obj: an integer, representing the maximum amount of snow that can be transported
    """
    
    # Create a new model
    model = gp.Model("snow_removal")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of small trucks
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of large trucks

    # Set objective function
    model.setObjective(30*x + 50*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(2*x + 4*y <= 30, "people_constraint")
    model.addConstr(x >= 10, "small_truck_constraint")
    model.addConstr(y >= 3, "large_truck_constraint")
    model.addConstr(x == 2*y, "ratio_constraint")

    # Optimize the model
    model.optimize()

    # Get the optimal objective value
    obj = int(model.objVal)

    return obj