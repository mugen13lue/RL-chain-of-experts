from gurobipy import *

def prob_174(small_bins, large_bins):
    """
    Solve the recycling problem and maximize the total amount of recycling material that can be collected.

    Args:
        small_bins: an integer, number of small bins
        large_bins: an integer, number of large bins

    Returns:
        obj: an integer, total amount of recycling material
    """
    
    # Constants
    small_workers = 2
    large_workers = 5
    small_capacity = 25
    large_capacity = 60
    total_workers = 100
    
    # Create a new model
    model = Model("Recycling Problem")
    
    # Decision variables
    small_bin_var = model.addVar(vtype=GRB.INTEGER, name="Small_Bins")
    large_bin_var = model.addVar(vtype=GRB.INTEGER, name="Large_Bins")
    
    # Constraints
    model.addConstr(small_bin_var == 3 * large_bin_var, "Small_Bins_Constraint")
    model.addConstr(large_bin_var >= 4, "Large_Bins_Constraint")
    model.addConstr(small_bin_var >= 10, "Small_Bins_Min_Constraint")
    model.addConstr(small_workers * small_bin_var + large_workers * large_bin_var <= total_workers, "Workers_Constraint")
    
    # Objective function
    model.setObjective(small_capacity * small_bin_var + large_capacity * large_bin_var, GRB.MAXIMIZE)
    
    # Optimize the model
    model.optimize()
    
    # Get the total amount of recycling material
    obj = model.objVal
    
    return obj