import gurobipy as gp
from gurobipy import GRB

def prob_55(windrower, hay_harvester):
    """
    Args:
        windrower: an integer,
        hay_harvester: an integer,
    Returns:
        obj: an integer,
    """
    m = gp.Model("hay_processing")

    # Define variables
    x = m.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x")  # acres processed by windrower
    y = m.addVar(lb=0, vtype=GRB.CONTINUOUS, name="y")  # acres processed by hay harvester

    # Set objective
    m.setObjective(10*x + 8*y, sense=GRB.MAXIMIZE)

    # Add constraints
    m.addConstr(10*x + 8*y <= 200, "hay_processing_constraint")
    m.addConstr(5*x + 3*y <= 800, "methane_gas_production_constraint")
    m.addConstr(2*x + y <= 300, "fuel_constraint")

    # Optimize model
    m.optimize()

    # Get the objective value
    obj = m.objVal

    return obj