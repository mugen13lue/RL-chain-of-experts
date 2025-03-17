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
    
    # Set objective to minimize total number of workers
    model.setObjective(2*x + 4*y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(30*x + 70*y >= 500, "hot_dog_production")
    model.addConstr(2*x + 4*y <= 30, "worker_constraint")
    
    # Non-negativity constraints
    model.addConstr(x >= 0, "non_negativity_x")
    model.addConstr(y >= 0, "non_negativity_y")
    
    # Optimize model
    model.optimize()
    
    # Get the optimal solution
    number_of_butcher_shops = model.objVal
    
    return number_of_butcher_shops