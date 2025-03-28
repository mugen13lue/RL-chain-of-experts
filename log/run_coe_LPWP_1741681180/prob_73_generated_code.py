import gurobipy as gp
from gurobipy import GRB

def prob_73(regular, hybrid):
    """
    Args:
        regular: an integer, number of regular vans
        hybrid: an integer, number of hybrid vans
    Returns:
        regular_vans: an integer, number of regular vans needed
        hybrid_vans: an integer, number of hybrid vans needed
    """
    model = gp.Model("van_optimization")

    # Decision variables
    x1 = model.addVar(vtype=GRB.INTEGER, name="regular_vans", obj=1)
    x2 = model.addVar(vtype=GRB.INTEGER, name="hybrid_vans", obj=1)

    # Objective function: minimize total number of vans
    model.modelSense = GRB.MINIMIZE

    # Constraints
    model.addConstr(500*x1 + 300*x2 >= 20000, "packages_constraint")
    model.addConstr(200*x1 + 100*x2 <= 7000, "pollutants_constraint")

    # Optimize model
    model.optimize()

    # Get the total number of vans
    regular_vans = x1.x
    hybrid_vans = x2.x

    return regular_vans, hybrid_vans