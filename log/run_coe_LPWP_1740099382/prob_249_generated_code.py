import gurobipy as gp
from gurobipy import GRB

def prob_249(retail_store, factory_outlet):
    """
    Args:
        retail_store: an integer indicating the number of retail stores
        factory_outlet: an integer indicating the number of factory outlets
    
    Returns:
        obj: an integer representing the objective value (number of stores)
    """
    obj = 1e9
    
    # Create a new model
    model = gp.Model("store_allocation")
    
    # Define decision variables
    num_retail_stores = model.addVar(vtype=GRB.INTEGER, name="num_retail_stores")  # number of retail stores
    num_factory_outlets = model.addVar(vtype=GRB.INTEGER, name="num_factory_outlets")  # number of factory outlets
    
    # Set objective function: minimize the number of stores open
    model.setObjective(num_retail_stores + num_factory_outlets, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(200*num_retail_stores + 80*num_factory_outlets >= 1200, "Customers_Constraint")
    model.addConstr(6*num_retail_stores + 4*num_factory_outlets <= 50, "Employees_Constraint")
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal objective value
    if model.status == GRB.OPTIMAL:
        obj = model.objVal
    
    return obj