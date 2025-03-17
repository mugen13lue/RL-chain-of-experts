import gurobipy as gp
from gurobipy import GRB

def prob_82():
    """
    Returns:
        number_of_butcher_shops: an integer, the minimum total number of butcher shops
    """
    
    # Create a new model
    model = gp.Model("butcher_shop_optimization")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of small butcher shops
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of large butcher shops
    
    # Set objective function: minimize the total number of butcher shops
    model.setObjective(x + y, GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(30*x + 70*y >= 500, "production_constraint")
    model.addConstr(2*x + 4*y <= 30, "worker_constraint")
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal solution
    number_of_butcher_shops = model.objVal
    
    return int(number_of_butcher_shops)