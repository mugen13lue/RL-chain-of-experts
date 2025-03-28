import gurobipy as gp
from gurobipy import GRB

def prob_187():
    """
    Solves the optimization problem related to corn transportation.
    Returns the minimum total number of trips needed to transport at least 500 boxes of corn.
    """
    
    # Create a new model
    model = gp.Model("corn_transportation")
    
    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="x")  # Number of ferry trips
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="y")  # Number of light rail trips
    
    # Set objective function
    model.setObjective(x + y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(20*x + 15*y >= 500, "corn_requirement")
    model.addConstr(y >= 4*x, "light_rail_constraint")
    
    # Optimize the model
    model.optimize()
    
    # Get the objective value
    obj = model.objVal
    
    return obj

# Call the function to solve the optimization problem
min_total_trips = prob_187()
print("Minimum total number of trips needed:", min_total_trips)