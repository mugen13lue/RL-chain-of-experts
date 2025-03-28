import gurobipy as gp
from gurobipy import GRB

def prob_52(dine_in_place, food_truck):
    """
    Args:
        dine_in_place: an integer, representing the number of dine-in places
        food_truck: an integer, representing the number of food trucks
    Returns:
        obj: an integer, representing the objective value (total number of stores)
    """
    
    # Create a new model
    model = gp.Model("sandwich_stores")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="dine_in_places")
    y = model.addVar(vtype=GRB.INTEGER, name="food_trucks")
    
    # Set objective: minimize Z = x + y
    model.setObjective(x + y, sense=GRB.MINIMIZE)
    
    # Add constraints
    sandwiches_constraint = model.addConstr(100*x + 50*y >= 500, "sandwiches_constraint")
    employees_constraint = model.addConstr(8*x + 3*y <= 35, "employees_constraint")
    
    # Optimize the model
    model.optimize()
    
    # Get the objective value
    obj = model.objVal
    
    return obj