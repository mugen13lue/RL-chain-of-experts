import gurobipy as gp
from gurobipy import GRB

def prob_22(regular_glass_pane, tempered_glass_pane, regular_glass_cooling_time, tempered_glass_cooling_time, regular_glass_profit, tempered_glass_profit):
    """
    Args:
        regular_glass_pane: an integer, the time required in the heating machine for one regular glass pane
        tempered_glass_pane: an integer, the time required in the heating machine for one tempered glass pane
        regular_glass_cooling_time: an integer, the time required in the cooling machine for one regular glass pane
        tempered_glass_cooling_time: an integer, the time required in the cooling machine for one tempered glass pane
        regular_glass_profit: an integer, the profit per pane of regular glass
        tempered_glass_profit: an integer, the profit per pane of tempered glass
    Returns:
        obj: an integer, the maximum profit
    """
    model = gp.Model("glass_factory")

    # Decision variables
    regular_panes = model.addVar(vtype=GRB.INTEGER, name="regular_panes")
    tempered_panes = model.addVar(vtype=GRB.INTEGER, name="tempered_panes")

    # Objective function
    model.setObjective(regular_glass_profit * regular_panes + tempered_glass_profit * tempered_panes, sense=GRB.MAXIMIZE)

    # Constraints
    model.addConstr(regular_glass_pane * regular_panes + tempered_glass_pane * tempered_panes <= 300, "heating_time_constraint")
    model.addConstr(regular_glass_cooling_time * regular_panes + tempered_glass_cooling_time * tempered_panes <= 300, "cooling_time_constraint")

    # Optimize model
    model.optimize()

    # Get the maximum profit
    obj = model.objVal

    return obj