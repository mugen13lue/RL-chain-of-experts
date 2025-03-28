import gurobipy as gp
from gurobipy import GRB

def prob_72(small_branch, large_branch, constraint1, constraint2):
    """
    Args:
        small_branch: an integer, the number of small branches
        large_branch: an integer, the number of large branches
        constraint1: an integer, the value of the first constraint
        constraint2: an integer, the value of the second constraint
    Returns:
        obj_value: an integer, the objective value of the problem
    """
    
    # Create a new model
    model = gp.Model("branch_optimization")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of small branches
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of large branches
    
    # Set objective function
    model.setObjective(x + y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(50*x + 100*y >= constraint1, "Customers_Constraint")
    model.addConstr(10*x + 15*y <= constraint2, "Tellers_Constraint")
    
    # Optimize the model
    model.optimize()
    
    # Get the objective value
    obj_value = model.objVal
    
    return obj_value