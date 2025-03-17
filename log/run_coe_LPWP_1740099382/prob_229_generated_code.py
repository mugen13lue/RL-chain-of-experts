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
    # Create a new model
    model = gp.Model("air_conditioner_problem")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="low_powered", obj=1)
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="high_powered", obj=1)

    # Set objective function
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(12*x + 17*y >= 250, "cooling_capacity")
    model.addConstr(150*x + 250*y <= 3400, "electricity")
    model.addConstr(x <= 0.3*(x+y), "low_powered_limit")
    model.addConstr(y >= 7, "high_powered_minimum")

    # Optimize model
    model.optimize()

    # Get the total number of air conditioners
    obj = model.objVal

    return obj