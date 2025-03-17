import gurobipy as gp
from gurobipy import GRB

def prob_281(coconut_oil, lavender):
    """
    Args:
        coconut_oil: an integer, the number of units of coconut oil to be added
        lavender: an integer, the number of units of lavender to be added
    Returns:
        obj: an integer, the total amount of time
    """
    obj = 1e9
    
    # Create a new model
    model = gp.Model("body_wash_optimization")
    
    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="coconut_oil")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="lavender")
    
    # Set objective function
    model.setObjective(0.7*x + 0.9*y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(x >= 300, name="coconut_oil_requirement")
    model.addConstr(x + y <= 550, name="total_ingredient_limit")
    model.addConstr(x <= 3*y, name="coconut_oil_to_lavender_ratio")
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal objective value
    obj = model.objVal
    
    return obj