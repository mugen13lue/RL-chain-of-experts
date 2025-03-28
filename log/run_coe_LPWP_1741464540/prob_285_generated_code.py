import gurobipy as gp
from gurobipy import GRB

def prob_285(wide_trail, narrow_trail):
    """
    Args:
        wide_trail: an integer, the number of wide trails
        narrow_trail: an integer, the number of narrow trails
    Returns:
        obj: an integer, the total amount of garbage produced
    """
    obj = 6 * wide_trail + 3 * narrow_trail
    return obj

def solve_park_trails():
    model = gp.Model("park_trails")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of wide trails
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of narrow trails

    # Constraints
    model.addConstr(x <= 3, "wide_trail_limit")
    model.addConstr(x + y <= 225, "total_visitors_limit")

    # Objective
    model.setObjective(6 * x + 3 * y, GRB.MINIMIZE)

    # Solve
    model.optimize()

    # Get the optimal solution
    wide_trail = round(x.x)
    narrow_trail = round(y.x)

    return wide_trail, narrow_trail

# Get the optimal solution
wide_trail, narrow_trail = solve_park_trails()
total_garbage = prob_285(wide_trail, narrow_trail)

print("Number of wide trails:", wide_trail)
print("Number of narrow trails:", narrow_trail)
print("Total amount of garbage produced:", total_garbage)