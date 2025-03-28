import gurobipy as gp
from gurobipy import GRB

def prob_160(small_bouquets, large_bouquets):
    """
    Args:
        small_bouquets: an integer, number of small bouquets
        large_bouquets: an integer, number of large bouquets
    Returns:
        obj: an integer, number of flowers
    """
    # Create a new model
    model = gp.Model("flower_transport")

    # Define decision variables
    x = model.addVar(lb=0, ub=80, vtype=GRB.INTEGER, name="small_bouquets")
    y = model.addVar(lb=0, ub=50, vtype=GRB.INTEGER, name="large_bouquets")

    # Set objective function
    model.setObjective(5*x + 10*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(x + y <= 70, "total_bouquets")
    model.addConstr(x >= 2*y, "twice_as_many_small")
    model.addConstr(y >= 20, "min_large_bouquets")

    # Optimize the model
    model.optimize()

    # Get the optimal objective value
    obj = int(model.objVal)

    return obj