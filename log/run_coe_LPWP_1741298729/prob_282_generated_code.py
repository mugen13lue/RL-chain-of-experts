import gurobipy as gp
from gurobipy import GRB

def prob_282(salinity_test, PH_test):
    """
    Args:
        salinity_test: an integer, representing the number of salinity tests
        PH_test: an integer, representing the number of pH tests
    Returns:
        obj: an integer, representing the objective value (number of probes)
    """
    model = gp.Model("probe_minimization")

    # Decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="salinity_tests")
    y = model.addVar(lb=250, vtype=GRB.INTEGER, name="PH_tests")

    # Constraints
    model.addConstr(x + y >= 400, "total_tests")
    model.addConstr(3*x <= salinity_test, "probes_salinity")
    model.addConstr(2*y <= PH_test, "probes_PH")
    model.addConstr(y <= 1.5*x, "ratio_constraint")

    # Objective function
    model.setObjective(3*x + 2*y, GRB.MINIMIZE)

    # Optimize the model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj