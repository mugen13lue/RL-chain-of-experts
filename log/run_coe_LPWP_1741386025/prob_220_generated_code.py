import gurobipy as gp
from gurobipy import GRB

def prob_220(full_weighted, semi_weighted, constraint1, constraint2, constraint3, constraint4):
    """
    Args:
        full_weighted: an integer, the quantity of full-weighted keyboards to manufacture
        semi_weighted: an integer, the quantity of semi-weighted keyboards to manufacture
        constraint1: an integer, the number of oscillator chips required for full-weighted keyboards
        constraint2: an integer, the number of oscillator chips required for semi-weighted keyboards
        constraint3: a float, the production time required for full-weighted keyboards
        constraint4: a float, the production time required for semi-weighted keyboards
        
    Returns:
        obj: a float, the total revenue generated
    """
    
    # Create a new model
    model = gp.Model("keyboard_production")
    
    # Decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="full_weighted_keyboards")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="semi_weighted_keyboards")
    
    # Set objective function
    model.setObjective(2800*x + 2400*y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(constraint1*x + constraint2*y <= 3500, "oscillator_chips_constraint")
    model.addConstr(constraint3*x + constraint4*y <= 6, "production_time_constraint")
    
    # Optimize the model
    model.optimize()
    
    # Get the total revenue generated
    obj = model.objVal
    
    return obj