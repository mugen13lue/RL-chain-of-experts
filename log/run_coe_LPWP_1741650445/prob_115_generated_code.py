import gurobipy as gp
from gurobipy import GRB

def prob_115():
    """
    Returns:
        obj: an integer, the total time it takes for the lawn to be ready
    """
    obj = 1e9
    
    # Create a new model
    model = gp.Model("lawn_optimization")
    
    # Define decision variables
    x = model.addVar(lb=0, ub=300, vtype=GRB.INTEGER, name="fertilizer")
    y = model.addVar(lb=0, ub=300, vtype=GRB.INTEGER, name="seeds")
    
    # Set objective function
    model.setObjective(0.5*x + 1.5*y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(x + y <= 300, "total_units_constraint")
    model.addConstr(x >= 50, "minimum_fertilizer_constraint")
    model.addConstr(x <= 2*y, "fertilizer_to_seeds_ratio_constraint")
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal objective value
    obj = model.objVal
    
    return obj