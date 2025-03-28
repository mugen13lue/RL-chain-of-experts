import gurobipy as gp
from gurobipy import GRB

def prob_78(small, large, twice):
    """
    Args:
        small: an integer, representing the number of small crates
        large: an integer, representing the number of large crates
        twice: an integer, representing the requirement of large crates being twice the number of small crates

    Returns:
        obj: an integer, representing the objective value (number of crates produced)
    """
    
    # Create a new model
    model = gp.Model("banana_crates")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of small crates
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of large crates
    
    # Set objective function: maximize the total number of crates produced
    model.setObjective(x + y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(20*x + 50*y <= 500, "total_bananas")
    model.addConstr(y >= 2*x, "large_twice_small")
    model.addConstr(x >= 5, "at_least_5_small_crates")
    
    # Optimize the model
    model.optimize()
    
    # Get the objective value
    obj = int(model.objVal)
    
    return obj