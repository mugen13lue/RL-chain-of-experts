import gurobipy as gp
from gurobipy import GRB

def prob_193(car, bus, constraint1, constraint2):
    """
    Args:
        car: number of cars (integer)
        bus: number of buses (integer)
        constraint1: value of the first constraint (integer)
        constraint2: value of the second constraint (integer)
    Returns:
        obj: the objective value (integer)
    """
    
    # Create a new model
    model = gp.Model("transportation_optimization")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="cars")
    y = model.addVar(vtype=GRB.INTEGER, name="buses")
    
    # Set objective function
    model.setObjective(10*x + 30*y, GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(4*x + 20*y >= constraint1, "min_employees_constraint")
    model.addConstr(y <= constraint2, "max_buses_constraint")
    
    # Optimize the model
    model.optimize()
    
    # Get the objective value
    obj = model.objVal
    
    return obj