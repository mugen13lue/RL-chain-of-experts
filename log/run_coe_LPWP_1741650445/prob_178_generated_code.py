import gurobipy as gp
from gurobipy import GRB

def prob_178(bike, car):
    """
    Args:
        bike: an integer, represents the number of bikes
        car: an integer, represents the number of cars
    Returns:
        obj: an integer, the objective value
    """
    obj = 0
    
    # Create a new model
    model = gp.Model("transportation_problem")
    
    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="cars")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="bikes")
    
    # Set objective function: minimize the total number of bikes needed
    model.setObjective(y, GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(x + y >= 100, "constraint1")
    model.addConstr(x <= 0.4*(x + y), "constraint2")
    
    # Optimize model
    model.optimize()
    
    # Get the optimal objective value
    obj = model.objVal
    
    return obj