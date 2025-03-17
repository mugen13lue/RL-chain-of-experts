import gurobipy as gp
from gurobipy import GRB

def prob_253(small_boxes, large_boxes):
    """
    Solves the Box Packing problem.

    Args:
        small_boxes: an integer, representing the number of small boxes to be used.
        large_boxes: an integer, representing the number of large boxes to be used.

    Returns:
        obj: an integer, representing the objective value (minimize the total number of boxes needed).
    """
    
    # Create a new model
    model = gp.Model("box_packing")
    
    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="small_boxes")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="large_boxes")
    
    # Set objective function
    model.setObjective(x + y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(x >= 3*y, "constraint1")
    model.addConstr(25*x + 45*y >= 750, "constraint2")
    model.addConstr(y >= 5, "constraint3")
    
    # Optimize the model
    model.optimize()
    
    # Get the objective value
    obj = model.objVal
    
    return obj