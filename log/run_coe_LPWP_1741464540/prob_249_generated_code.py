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
    # Create a new model
    model = gp.Model("store_allocation")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of retail stores
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of factory outlets

    # Set objective function: Minimize the number of stores open subject to constraints
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(200*x + 80*y >= 1200, "Customers_Constraint")
    model.addConstr(6*x + 4*y <= 50, "Employees_Constraint")

    # Optimize the model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj