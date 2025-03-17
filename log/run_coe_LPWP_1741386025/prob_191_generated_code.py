import gurobipy as gp
from gurobipy import GRB

def prob_191(truck, car):
    """
    
    Args:
        truck: an integer, representing the number of truck trips
        car: an integer, representing the number of car trips
        
    Returns:
        obj: an integer, representing the amount of gas consumed
    """
    
    # Create a new model
    model = gp.Model("transportation_problem")
    
    # Define decision variables
    x = model.addVar(lb=0, ub=5, vtype=GRB.INTEGER, name="truck_trips")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="car_trips")
    
    # Set objective function: minimize 20x + 15y
    model.setObjective(20*x + 15*y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(x + y >= 0.3*(x + y), "car_trip_constraint")
    model.addConstr(50*x + 30*y >= 500, "package_constraint")
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal objective value
    obj = model.objVal
    
    return obj