import gurobipy as gp
from gurobipy import GRB

def prob_167(small_wagons, large_wagons, twice):
    """
    Args:
        small_wagons: an integer, number of small wagons
        large_wagons: an integer, number of large wagons
        twice: an integer, twice the number of large wagons
    Returns:
        obj: an integer, number of wagons
    """
    # Create a new model
    model = gp.Model("wagon_optimization")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of small wagons
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of large wagons

    # Set objective function: minimize total number of wagons
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(x >= 2*y, "small_wagons_constraint")
    model.addConstr(y >= 10, "large_wagons_constraint")
    model.addConstr(20*x + 50*y == 2000, "ore_constraint")

    # Optimize model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj