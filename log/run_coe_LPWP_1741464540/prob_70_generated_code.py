import gurobipy as gp
from gurobipy import GRB

def prob_70(nurses, pharmacists, constraint1, constraint2, constraint3, constraint4, constraint5): 
    """
    Args:
        nurses: an integer, the number of nurses scheduled
        pharmacists: an integer, the number of pharmacists scheduled
        constraint1: an integer, the coefficient for the needs constraint (nurses)
        constraint2: an integer, the coefficient for the needs constraint (pharmacists)
        constraint3: an integer, the coefficient for the budget constraint (nurses)
        constraint4: an integer, the coefficient for the budget constraint (pharmacists)
        constraint5: an integer, the limit for the needs constraint
    Returns:
        obj: an integer, the value of the objective function
    """
    
    # Create a new model
    model = gp.Model("healthcare_scheduling")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="nurses")
    y = model.addVar(vtype=GRB.INTEGER, name="pharmacists")
    
    # Set objective function
    model.setObjective(x + y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(constraint1*x + constraint2*y == constraint5, "total_hours_constraint")
    model.addConstr(constraint3*x + constraint4*y <= 9000, "budget_constraint")
    
    # Optimize model
    model.optimize()
    
    # Get the optimal objective value
    obj = model.objVal
    
    return obj