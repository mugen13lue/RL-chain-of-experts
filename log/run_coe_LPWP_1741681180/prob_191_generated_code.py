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
    m = gp.Model("transportation")

    # Decision variables
    x_truck = m.addVar(vtype=GRB.INTEGER, name="truck")
    x_car = m.addVar(vtype=GRB.INTEGER, name="car")

    # Objective function: minimize total gas consumed
    m.setObjective(20*x_truck + 15*x_car, GRB.MINIMIZE)

    # Constraints
    m.addConstr(50*x_truck + 30*x_car >= 500, "packages")
    m.addConstr(x_truck <= 5, "max_truck_trips")
    m.addConstr(x_car >= 0.3*(x_truck + x_car), "min_car_trips")

    # Optimize model
    m.optimize()

    # Return the objective value
    return int(m.objVal)