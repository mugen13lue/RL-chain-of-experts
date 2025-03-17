import gurobipy as gp
from gurobipy import GRB

def prob_141(turkey_dinner, tuna_salad_sandwich):
    """
    Args:
        turkey_dinner: an integer,
        tuna_salad_sandwich: an integer,
    Returns:
        obj: an integer,
    """
    obj = 1e9
    
    # Create a new model
    model = gp.Model("diet_problem")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="turkey_dinner")
    y = model.addVar(vtype=GRB.INTEGER, name="tuna_salad_sandwich")
    
    # Set objective function to minimize fat intake
    model.setObjective(12*x + 8*y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(20*x + 18*y >= 150, "protein_constraint")
    model.addConstr(30*x + 25*y >= 200, "carbs_constraint")
    model.addConstr(x <= 0.4*(x+y), "turkey_dinner_limit")
    
    # Optimize model
    model.optimize()
    
    # Get the optimal objective value
    obj = model.objVal
    
    return obj