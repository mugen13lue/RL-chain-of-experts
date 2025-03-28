import gurobipy as gp
from gurobipy import GRB

def prob_33(long_desks, short_desks):
    """
    Args:
        long_desks: an integer (number of long desks),
        short_desks: an integer (number of short desks)
        
    Returns:
        objective_value: a float (objective value, seating availability)
    """
    # Create a new model
    model = gp.Model("desk_optimization")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of long desks
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of short desks
    
    # Set objective function: maximize seating availability
    model.setObjective(6*x + 2*y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(300*x + 100*y <= 2000, "Budget")
    model.addConstr(10*x + 4*y <= 200, "Space")
    model.addConstr(x >= 0, "Non-negativity_x")
    model.addConstr(y >= 0, "Non-negativity_y")
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal objective value
    objective_value = model.objVal
    
    return objective_value