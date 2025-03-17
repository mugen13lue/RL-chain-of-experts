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

    # Set objective function
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(x >= 3, "Motion_Activated_Constraint")
    model.addConstr(y <= manual_limit * (x + y), "Manual_Constraint")
    model.addConstr(motion_activated_drops * x + manual_drops * y >= capacity, "Drop_Rate_Constraint")
    model.addConstr(motion_activated_power * x + manual_power * y <= power_limit, "Energy_Constraint")

    # Optimize the model
    model.optimize()

    if model.status == GRB.OPTIMAL:
        obj = model.objVal

    return obj