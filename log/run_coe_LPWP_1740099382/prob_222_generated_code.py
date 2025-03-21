import gurobipy as gp
from gurobipy import GRB

def prob_222(strawberry_cookie, sugar_cookie):
    """
    Args:
        strawberry_cookie: an integer, the number of strawberry cookies to make
        sugar_cookie: an integer, the number of sugar cookies to make

    Returns:
        profit: a float, the maximum profit
    """
    model = gp.Model("cookie_optimization")

    # Decision variables
    x1 = model.addVar(lb=0, ub=100, vtype=GRB.CONTINUOUS, name="strawberry_cookies")
    x2 = model.addVar(lb=0, ub=80, vtype=GRB.CONTINUOUS, name="sugar_cookies")

    # Objective function
    model.setObjective(5.5*x1 + 12*x2, sense=GRB.MAXIMIZE)

    # Constraints
    model.addConstr(x1 + x2 <= 100, "production_constraint")
    model.addConstr(x1 <= 100, "strawberry_demand_constraint")
    model.addConstr(x2 <= 80, "sugar_demand_constraint")

    # Optimize model
    model.optimize()

    # Get the maximum profit
    profit = model.objVal

    return profit