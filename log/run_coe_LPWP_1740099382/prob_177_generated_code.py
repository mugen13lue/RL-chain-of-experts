import gurobipy as gp
from gurobipy import GRB

def prob_177(tractor, car, twice):
    """
    Args:
        tractor: an integer, representing the number of tractors used
        car: an integer, representing the number of cars used
        twice: an integer, representing the minimum number of cars compared to tractors
    Returns:
        obj: an integer, representing the minimized total number of tractors and cars needed
    """
    # Create a new model
    model = gp.Model("corn_transportation")

    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of tractors used
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of cars used

    # Set objective
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Constraints
    model.addConstr(40*x + 20*y >= 500, "corn_sent_constraint")
    model.addConstr(y >= 2*x, "number_of_cars_constraint")

    # Optimize model
    model.optimize()

    # Get the minimized total number of tractors and cars needed
    obj = model.objVal

    return obj