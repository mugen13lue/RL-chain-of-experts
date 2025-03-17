import gurobipy as gp
from gurobipy import GRB

def prob_251(freight, air):
    """
    Args:
        freight: an integer, number of trips by freight
        air: an integer, number of trips by air
    Returns:
        obj: an integer, total number of trips
    """
    obj = 0
    
    # Create a new model
    m = gp.Model("transportation_problem")
    
    # Define decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="freight_trips")
    y = m.addVar(vtype=GRB.INTEGER, name="air_trips")
    
    # Set objective function: minimize total number of trips
    m.setObjective(x + y, GRB.MINIMIZE)
    
    # Add constraints
    m.addConstr(5*x + 3*y >= 200, "transportation_capacity")
    m.addConstr(300*x + 550*y <= 20000, "budget_constraint")
    m.addConstr(y >= 0.3*(x + y), "minimum_air_transport")
    m.addConstr(x >= 5, "minimum_freight_trips")
    
    # Optimize model
    m.optimize()
    
    # Get the total number of trips
    obj = m.objVal
    
    return obj