import gurobipy as gp
from gurobipy import GRB

def prob_7(wired_headphones, wireless_headphones):
    """
    Args:
        wired_headphones: an integer representing the number of wired headphones.
        wireless_headphones: an integer representing the number of wireless headphones.

    Returns:
        obj: an integer representing the maximum profit.
    """
    
    # Create a new model
    model = gp.Model("headphones_production")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="wired_headphones")
    y = model.addVar(vtype=GRB.INTEGER, name="wireless_headphones")

    # Set objective function: maximize profit
    model.setObjective(50*x + 20*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(x <= 100, "wired_team_constraint")
    model.addConstr(y <= 170, "wireless_team_constraint")
    model.addConstr(x + y <= 150, "audio_testing_machine_constraint")
    model.addConstr(x >= 0, "non_negative_wired_constraint")
    model.addConstr(y >= 0, "non_negative_wireless_constraint")

    # Optimize the model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj