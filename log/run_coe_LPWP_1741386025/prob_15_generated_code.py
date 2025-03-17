from gurobipy import *

def prob_15(senior_citizens, young_adults):
    """
    Args:
        senior_citizens: an integer representing the number of senior citizens employed by the store
        young_adults: an integer representing the number of young adults employed by the store
    Returns:
        obj: an integer representing the minimized wage bill
    """
    
    # Create a new model
    model = Model("Wage Optimization")
    
    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="senior_citizens")
    y = model.addVar(vtype=GRB.INTEGER, name="young_adults")
    
    # Objective function: Minimize Z = 500x + 750y
    model.setObjective(500*x + 750*y, GRB.MINIMIZE)
    
    # Constraints
    model.addConstr(500*x + 750*y <= 30000, "total_wage_constraint")
    model.addConstr(x + y >= 50, "min_workers_constraint")
    model.addConstr(y >= 10, "min_young_adults_constraint")
    model.addConstr(y >= (1/3) * x, "ratio_constraint")
    
    # Optimize the model
    model.optimize()
    
    if model.status == GRB.OPTIMAL:
        obj = model.objVal
    else:
        obj = 1e9  # Return a large value if no optimal solution found
    
    return obj