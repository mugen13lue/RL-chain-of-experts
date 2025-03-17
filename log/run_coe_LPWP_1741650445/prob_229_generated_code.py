import gurobipy as gp
from gurobipy import GRB

def prob_229(low_power, high_power):
    """
    Solves the air conditioner problem.

    Args:
        low_power: an integer, number of low-powered air conditioners
        high_power: an integer, number of high-powered air conditioners

    Returns:
        obj: an integer, total number of air conditioners
    """
    model = gp.Model("air_conditioner_problem")

    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="low_power")
    y = model.addVar(vtype=GRB.INTEGER, name="high_power")
    total_air_conditioners = model.addVar(vtype=GRB.INTEGER, name="total_air_conditioners")

    # Constraints
    model.addConstr(12*x + 17*y >= 250, "Cooling_Capacity")
    model.addConstr(150*x + 250*y <= 3400, "Electricity_Usage")
    model.addConstr(x <= 0.3*(x+y), "Limit_Low_powered")
    model.addConstr(y >= 7, "Minimum_High_powered")
    model.addConstr(total_air_conditioners == x + y, "Total_Air_Conditioners")

    # Objective
    model.setObjective(total_air_conditioners, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    # Return total number of air conditioners
    return int(total_air_conditioners.x)