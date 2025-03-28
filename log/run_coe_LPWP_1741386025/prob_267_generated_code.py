import gurobipy as gp
from gurobipy import GRB

def prob_267():
    """
    Returns:
        obj: an integer, representing the total number of sports equipment produced
    """
    
    # Create a new model
    model = gp.Model("sports_equipment")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of basketballs
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of footballs
    
    # Set objective function
    model.setObjective(x + y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(5*x + 3*y <= 1500, "Materials")
    model.addConstr(x + 2*y <= 750, "Hours")
    model.addConstr(x >= 3*y, "MinimumBasketballs")
    model.addConstr(y >= 50, "MinimumFootballs")
    
    # Optimize the model
    model.optimize()
    
    # Get the total number of sports equipment produced
    obj = model.objVal
    
    return obj