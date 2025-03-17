import gurobipy as gp
from gurobipy import GRB

def prob_174(small_bins, large_bins):
    """
    Solve the recycling problem and maximize the total amount of recycling material that can be collected.

    Args:
        small_bins: an integer, number of small bins
        large_bins: an integer, number of large bins

    Returns:
        obj: an integer, total amount of recycling material
    """
    
    # Create a new model
    model = gp.Model("recycling_problem")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of small bins
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of large bins
    
    # Set objective function
    model.setObjective(25*x + 60*y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(2*x + 5*y <= 100)
    model.addConstr(x >= 3*y)
    model.addConstr(x >= 10)
    model.addConstr(y >= 4)
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal objective value
    obj = int(model.objVal)
    
    return obj