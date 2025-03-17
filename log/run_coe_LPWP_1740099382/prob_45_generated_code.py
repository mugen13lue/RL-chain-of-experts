import gurobipy as gp
from gurobipy import GRB

def maximize_profit(blueberries, raspberries, total_acres, watering_cost_limit, labor_days_limit):
    """
    Args:
        blueberries: an integer, representing the number of acres for blueberries.
        raspberries: an integer, representing the number of acres for raspberries.
        total_acres: an integer, representing the total limit for acres.
        watering_cost_limit: an integer, representing the limit for watering cost.
        labor_days_limit: an integer, representing the limit for labor days.

    Returns:
        obj: an integer, representing the objective value (profit).
    """
    # Create a new model
    m = gp.Model("berry_farm")

    # Define decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="blueberries")
    y = m.addVar(vtype=GRB.INTEGER, name="raspberries")

    # Set objective function
    m.setObjective(56*x + 75*y, sense=GRB.MAXIMIZE)

    # Add constraints
    m.addConstr(6*x + 3*y <= labor_days_limit, "labor_constraint")
    m.addConstr(22*x + 25*y <= watering_cost_limit, "watering_cost_constraint")
    m.addConstr(x + y <= total_acres, "total_acres_constraint")

    # Optimize the model
    m.optimize()

    # Get the objective value
    obj = m.objVal

    return obj