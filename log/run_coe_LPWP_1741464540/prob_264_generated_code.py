import gurobipy as gp
from gurobipy import GRB

def prob_264(specialized_third_party, common_third_party_annotation_company):
    """
    Args:
        specialized_third_party: an integer, the number of images annotated by the specialized third-party company
        common_third_party_annotation_company: an integer, the number of images annotated by the common third-party annotation company
    Returns:
        obj: an integer, the cost of annotating the whole dataset
    """
    
    # Create a new model
    model = gp.Model("annotation_optimization")
    
    # Define decision variables
    x = model.addVar(name="x")  # hours allocated to the specialized company
    y = model.addVar(name="y")  # hours allocated to the common company
    
    # Set objective function: minimize total cost
    model.setObjective(100*x + 72*y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(x + y >= 250, "total_hours_constraint")
    model.addConstr(x >= (1/3)*(x + y), "specialized_company_constraint")
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal objective value
    obj = model.objVal
    
    return obj