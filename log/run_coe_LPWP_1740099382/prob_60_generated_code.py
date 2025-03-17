import gurobipy as gp
from gurobipy import GRB

def prob_60(seasonal_snow_remover, permanent_snow_remover):
    """
    Args:
        seasonal_snow_remover: an integer, the number of seasonal snow removers
        permanent_snow_remover: an integer, the number of permanent snow removers
    Returns:
        number_of_snow_removers: an integer, the objective value (i.e., minimized number of snow removers)
    """
    model = gp.Model("snow_remover")

    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="seasonal_snow_remover")
    y = model.addVar(vtype=GRB.INTEGER, name="permanent_snow_remover")

    # Set objective
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(6*x + 10*y >= 300, "Labor_Hours_Constraint")
    model.addConstr(120*x + 250*y <= 6500, "Budget_Constraint")

    # Optimize model
    model.optimize()

    number_of_snow_removers = model.objVal

    return number_of_snow_removers