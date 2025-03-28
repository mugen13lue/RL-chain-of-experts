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
    model = gp.Model("transportation")

    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="truck_trips")
    y = model.addVar(vtype=GRB.INTEGER, name="car_trips")

    # Constraints
    model.addConstr(50*x + 30*y >= 500, "packages")
    model.addConstr(20*x + 15*y == 20*truck + 15*car, "gas")
    model.addConstr(x <= 5, "truck_trips")
    model.addConstr(y >= 0.3*(x+y), "car_trips")

    # Objective function
    model.setObjective(20*x + 15*y, GRB.MINIMIZE)

    # Optimize the model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj