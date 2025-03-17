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
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of tractors
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of cars

    # Set objective
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Constraints
    model.addConstr(40*x + 20*y >= 500, "corn_weight")
    model.addConstr(y >= twice*x, "car_tractor_ratio")
    model.addConstr(x >= 0, "non_negativity_x")
    model.addConstr(y >= 0, "non_negativity_y")

    # Optimize model
    model.optimize()

    # Return the minimized total number of tractors and cars needed
    return int(x.x + y.x) if model.status == GRB.OPTIMAL else None