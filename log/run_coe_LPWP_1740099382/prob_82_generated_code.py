import gurobipy as gp
from gurobipy import GRB

def prob_82(small_shop, large_shop):
    """
    Args:
        small_shop: an integer, the number of small butcher shops
        large_shop: an integer, the number of large butcher shops
        
    Returns:
        number_of_butcher_shops: an integer, the minimum total number of butcher shops
    """
    
    # Create a new model
    model = gp.Model("butcher_shop_optimization")
    
    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of small butcher shops
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of large butcher shops
    
    # Set objective function: minimize total number of butcher shops while meeting hot dog production constraint
    model.setObjective(x + y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(30*x + 70*y >= 500, "hot_dog_production")
    model.addConstr(2*x + 4*y <= 30, "worker_constraint")
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal solution
    number_of_butcher_shops = model.objVal
    
    return int(number_of_butcher_shops)