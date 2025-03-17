import gurobipy as gp
from gurobipy import GRB

def prob_41(hardwood, vinyl_planks):
    """
    Args:
        hardwood: an integer, the quantity of hardwood flooring produced weekly
        vinyl_planks: an integer, the quantity of vinyl planks produced weekly
    Returns:
        profit: a float, the maximum profit that can be achieved
    """
    model = gp.Model("flooring_production")

    # Variables
    x = model.addVar(lb=20000, ub=50000, vtype=GRB.INTEGER, name="hardwood")
    y = model.addVar(lb=10000, ub=30000, vtype=GRB.INTEGER, name="vinyl_planks")

    # Objective function
    model.setObjective(2.5*x + 3*y, sense=GRB.MAXIMIZE)

    # Constraints
    model.addConstr(x + y >= 60000, "total_demand")
    
    # Optimize model
    model.optimize()

    return model.objVal