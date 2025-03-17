import gurobipy as gp
from gurobipy import GRB

def prob_81(motion_activated, manual, motion_activated_drops, motion_activated_power, manual_drops, manual_power, manual_limit, capacity, power_limit):
    """
    Args:
        motion_activated: an integer, representing the number of motion activated machines
        manual: an integer, representing the number of manual machines
        motion_activated_drops: an integer, representing the number of drops per minute for motion activated machines
        motion_activated_power: an integer, representing the power consumption (in kWh) for motion activated machines
        manual_drops: an integer, representing the number of drops per minute for manual machines
        manual_power: an integer, representing the power consumption (in kWh) for manual machines
        manual_limit: a float, representing the maximum ratio of manual machines
        capacity: an integer, representing the minimum drops per minute requirement
        power_limit: an integer, representing the maximum power consumption (in kWh) requirement

    Returns:
        obj: an integer, representing the minimized total number of machines
    """
    obj = 1e9
    
    # Create a new model
    model = gp.Model("hand_sanitizer")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="motion_activated")
    y = model.addVar(vtype=GRB.INTEGER, name="manual")

    # Set objective function: minimize total number of machines
    model.setObjective(x + y, GRB.MINIMIZE)

    # Add constraints
    model.addConstr(motion_activated_drops * x + manual_drops * y >= capacity)
    model.addConstr(motion_activated_power * x + manual_power * y <= power_limit)
    model.addConstr(y <= manual_limit * (x + y))
    model.addConstr(x >= 3)

    # Optimize model
    model.optimize()

    if model.status == GRB.OPTIMAL:
        obj = model.objVal

    return obj