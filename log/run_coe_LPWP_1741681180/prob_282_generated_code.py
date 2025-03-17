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
    obj = 0
    
    # Create a new model
    model = gp.Model("probe_optimization")
    
    # Define variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of salinity tests
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of pH tests
    
    # Set objective function: minimize total number of probes
    model.setObjective(3*x + 2*y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(y >= 250, "min_PH_tests")
    model.addConstr(x + y >= 400, "total_tests")
    model.addConstr(y <= 1.5*x, "max_PH_salinity_ratio")
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal objective value
    obj = model.objVal
    
    return obj