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
    x = model.addVar(vtype=GRB.INTEGER, name="truck_trips")
    y = model.addVar(vtype=GRB.INTEGER, name="car_trips")
    
    # Set objective function: minimize total gas consumed
    model.setObjective(20*x + 15*y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(50*x + 30*y >= 500, "packages_constraint")
    model.addConstr(20*x + 15*y == truck*20 + car*15, "gas_constraint")
    model.addConstr(x <= 5, "truck_trips_constraint")
    model.addConstr(y >= 0.3*(x + y), "car_trips_constraint")
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal objective value
    obj = model.objVal
    
    return obj