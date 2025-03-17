import gurobipy as gp
from gurobipy import GRB

def prob_76(light_grilled_cheese_sandwiches, heavy_grilled_cheese_sandwiches):
    """
    Args:
        light_grilled_cheese_sandwiches: an integer, the number of light grilled cheese sandwiches
        heavy_grilled_cheese_sandwiches: an integer, the number of heavy grilled cheese sandwiches
    Returns:
        total_production_time: an integer, the total production time
    """
    model = gp.Model("grilled_cheese_production")

    # Variables
    x = model.addVar(name="light_sandwiches")
    y = model.addVar(name="heavy_sandwiches")

    # Constraints
    model.addConstr(2*x + 3*y <= 300, "bread_constraint")
    model.addConstr(3*x + 5*y <= 500, "cheese_constraint")
    model.addConstr(y >= 3*x, "heavy_minimum_constraint")

    # Objective
    model.setObjective(10*x + 15*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    total_production_time = int(model.objVal)
    
    return total_production_time