import gurobipy as gp
from gurobipy import GRB

def prob_276():
    """
    Returns:
        obj: an integer, the maximum caloric intake
    """
    
    # Create a new model
    model = gp.Model("senior_home_snacks")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="spinach")
    y = model.addVar(vtype=GRB.INTEGER, name="soybeans")
    
    # Set objective function
    model.setObjective(30*x + 100*y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(100*x + 80*y >= 12000, "fibre_constraint")
    model.addConstr(5*x + 12*y >= 300, "iron_constraint")
    model.addConstr(x >= y, "spinach_soybeans_constraint")
    
    # Optimize the model
    model.optimize()
    
    # Get the maximum caloric intake
    obj = model.objVal
    
    return obj