import gurobipy as gp
from gurobipy import GRB

def prob_57(cash_based, card_only):
    """
    Args:
        cash_based: an integer, number of cash-based machines
        card_only: an integer, number of card-only machines
    Returns:
        obj: an integer, the objective value
    """
    obj = 0
    
    # Create a new model
    model = gp.Model("machine_allocation")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="cash_based")
    y = model.addVar(vtype=GRB.INTEGER, name="card_only")
    
    # Set objective function: minimize total number of machines
    model.setObjective(x + y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(x + y >= 500)
    model.addConstr(4*x + 5*y <= 90)
    model.addConstr(y <= x)
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal objective value
    obj = model.objVal
    
    return obj