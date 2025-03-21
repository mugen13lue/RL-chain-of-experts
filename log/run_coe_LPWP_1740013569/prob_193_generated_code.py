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
    m = gp.Model("transportation")

    # Define decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="x")  # Number of cars
    y = m.addVar(vtype=GRB.INTEGER, name="y")  # Number of buses

    # Set objective function
    m.setObjective(10*x + 30*y, GRB.MINIMIZE)

    # Add constraints
    m.addConstr(4*x + 20*y >= constraint1, "constraint1")
    m.addConstr(y <= constraint2, "constraint2")

    # Optimize model
    m.optimize()

    # Get the objective value
    obj = m.objVal

    return obj