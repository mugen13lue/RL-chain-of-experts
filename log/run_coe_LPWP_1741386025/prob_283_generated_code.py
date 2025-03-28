import gurobipy as gp
from gurobipy import GRB

def prob_283():
    """
    Returns:
        obj: an integer, representing the objective value
    """
    
    # Create a new model
    model = gp.Model("staff_optimization")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="full_time_staff")
    y = model.addVar(vtype=GRB.INTEGER, name="part_time_staff")
    
    # Set objective function: minimize total number of staff hired
    model.setObjective(x + y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(40*x + 15*y >= 1000, "Labor_Hours")
    model.addConstr(1280*x + 450*y <= 31500, "Budget_Constraint")
    model.addConstr(x >= 0, "Non-negativity_x")
    model.addConstr(y >= 0, "Non-negativity_y")
    
    # Optimize the model
    model.optimize()
    
    # Get the objective value
    obj = model.objVal
    
    return obj