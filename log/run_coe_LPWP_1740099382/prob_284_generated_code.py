import gurobipy as gp
from gurobipy import GRB

def prob_284(heavy_duty_yard_machine, gas_lawn_mower):
    """
    Args:
        heavy_duty_yard_machine: an integer, the square feet to be cut using heavy duty yard machine
        gas_lawn_mower: an integer, the square feet to be cut using gas lawn mower

    Returns:
        obj: an integer, the objective value (time required)
    """
    m = gp.Model("grass_cutting")

    # Variables
    x = m.addVar(lb=0, vtype=GRB.INTEGER, name="x")  # square feet cut by heavy-duty yard machine
    y = m.addVar(lb=0, vtype=GRB.INTEGER, name="y")  # square feet cut by gas lawn mower

    # Constraints
    m.addConstr(2*x + 5*y <= 2500)
    m.addConstr(12*x + 10*y <= 2000)
    m.addConstr(3*x + 2*y <= 450)

    # Objective
    m.setObjective(2*x + 5*y, sense=GRB.MINIMIZE)

    # Optimize model
    m.optimize()

    # Return objective value
    return m.objVal