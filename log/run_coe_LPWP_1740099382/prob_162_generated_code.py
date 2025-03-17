import gurobipy as gp
from gurobipy import GRB

def prob_162(bus, car):
    """
    Args:
        bus: an integer (number of bus trips)
        car: an integer (number of car trips)
    
    Returns:
        obj: an integer (total time required to transport the monkeys)
    """
    obj = 1e9
    
    # Create a new model
    m = gp.Model("monkey_transportation")
    
    # Define decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="bus_trips")
    y = m.addVar(vtype=GRB.INTEGER, name="car_trips")
    
    # Set objective function: minimize total time
    m.setObjective(30*x + 15*y, GRB.MINIMIZE)
    
    # Add constraints
    m.addConstr(20*x + 6*y >= 300, "monkey_constraint")
    m.addConstr(0.6*x <= y, "car_trips_constraint")
    m.addConstr(x <= 10, "bus_trips_constraint")
    
    # Optimize model
    m.optimize()
    
    # Get the total time required
    obj = m.objVal
    
    return obj