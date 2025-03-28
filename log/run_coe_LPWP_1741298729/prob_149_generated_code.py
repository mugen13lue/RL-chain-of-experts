import gurobipy as gp
from gurobipy import GRB

def prob_149(vans, trucks):
    """
    Args:
        vans: an integer, the number of trips by vans
        trucks: an integer, the number of trips by trucks
    Returns:
        obj: an integer, the objective value
    """
    obj = 0
    
    # Create a new model
    m = gp.Model("transportation_problem")
    
    # Define decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="x")  # number of trips by vans
    y = m.addVar(vtype=GRB.INTEGER, name="y")  # number of trips by trucks
    
    # Set objective function: minimize total number of trips
    m.setObjective(x + y, GRB.MINIMIZE)
    
    # Add constraints
    m.addConstr(50*x + 80*y >= 1500, "min_boxes_constraint")
    m.addConstr(30*x + 50*y <= 1000, "budget_constraint")
    m.addConstr(x >= y, "van_truck_constraint")
    
    # Optimize model
    m.optimize()
    
    # Get the optimal objective value
    obj = m.objVal
    
    return obj