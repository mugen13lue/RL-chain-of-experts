import gurobipy as gp
from gurobipy import GRB

def prob_111(crab_cakes, lobster_roll, constraint1, constraint2, constraint3, constraint4, constraint5, constraint6):
    """
    Args:
        crab_cakes: an integer, representing the number of crab cakes to eat
        lobster_roll: an integer, representing the number of lobster rolls to eat
        constraint1: an integer, representing the first constraint threshold
        constraint2: an integer, representing the second constraint threshold
        constraint3: an integer, representing the third constraint threshold
        constraint4: an integer, representing the fourth constraint threshold
        constraint5: an integer, representing the fifth constraint threshold
        constraint6: an integer, representing the sixth constraint threshold
    Returns:
        obj: an integer, representing the minimized unsaturated fat intake
    """
    
    # Create a new model
    model = gp.Model("diet_problem")
    
    # Decision variables
    x = model.addVar(lb=0, name="crab_cakes")
    y = model.addVar(lb=0, name="lobster_roll")
    
    # Set objective function
    model.setObjective(4*x + 6*y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(5*x + 8*y >= 80, "vitamin_A_constraint")
    model.addConstr(7*x + 4*y >= 100, "vitamin_C_constraint")
    model.addConstr(y <= 0.4*(x + y), "lobster_roll_constraint")
    
    # Optimize model
    model.optimize()
    
    # Get the minimized unsaturated fat intake
    obj = model.objVal
    
    return obj