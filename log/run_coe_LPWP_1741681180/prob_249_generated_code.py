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
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of retail stores
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of factory outlets

    # Set objective function: minimize the number of stores that must be open
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(200*x + 80*y >= 1200, "min_customers_per_day")
    model.addConstr(6*x + 4*y <= 50, "max_employees_available")

    # Optimize the model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    # Print the optimal solution
    print("Optimal number of retail stores to open:", x.x)
    print("Optimal number of factory outlets to open:", y.x)

    return obj