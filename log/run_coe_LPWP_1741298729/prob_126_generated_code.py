import gurobipy as gp
from gurobipy import GRB

def prob_126(machine_1, machine_2, constraint1, constraint2, constraint3):
    """
    Args:
        machine_1: an integer (number of hours for machine 1)
        machine_2: an integer (number of hours for machine 2)
        constraint1: an integer (value of constraint 1)
        constraint2: an integer (value of constraint 2)
        constraint3: an integer (value of constraint 3)
    Returns:
        obj: an integer (objective value - total time)
    """
    
    # Create a new model
    model = gp.Model("cream_production")
    
    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x")  # hours machine 1 is used
    y = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="y")  # hours machine 2 is used
    
    # Set objective function
    model.setObjective(x + y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(30*x + 45*y >= constraint1, "Eye_Cream_Production")
    model.addConstr(60*x + 30*y >= constraint2, "Foot_Cream_Production")
    model.addConstr(20*x + 15*y <= constraint3, "Distilled_Water_Usage")
    
    # Optimize the model
    model.optimize()
    
    # Get the objective value
    obj = model.objVal
    
    return obj