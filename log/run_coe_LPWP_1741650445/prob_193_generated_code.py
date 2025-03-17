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
    model = gp.Model("transportation")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")
    y = model.addVar(vtype=GRB.INTEGER, name="y")

    # Constraints
    model.addConstr(4*x + 20*y >= constraint1, "employees_constraint")
    model.addConstr(y <= constraint2, "bus_constraint")

    # Objective
    model.setObjective(10*x + 30*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    obj = model.objVal

    return obj