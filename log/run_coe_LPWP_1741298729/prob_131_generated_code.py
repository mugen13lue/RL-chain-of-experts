import gurobipy as gp
from gurobipy import GRB

def prob_131(bananas, mangoes):
    """
    Args:
        bananas: an integer, number of bananas
        mangoes: an integer, number of mangoes
    Returns:
        obj: an integer, minimum sugar intake
    """
    obj = 1e9
    
    # Create a new model
    model = gp.Model("gorilla_diet")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="bananas")
    y = model.addVar(vtype=GRB.INTEGER, name="mangoes")
    
    # Set objective function: minimize sugar intake
    model.setObjective(10*x + 8*y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(80*x + 100*y >= 4000, "Calories")
    model.addConstr(20*x + 15*y >= 150, "Potassium")
    model.addConstr(10*x + 8*y <= 0.33*(x + y), "Sugar")
    model.addConstr(y <= 0.33*(x + y), "Mangoes Limit")
    
    # Optimize model
    model.optimize()
    
    # Get the optimal objective value
    obj = model.objVal
    
    return obj