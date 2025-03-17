import gurobipy as gp
from gurobipy import GRB

def prob_11():
    """
    Returns:
        obj: a float, representing the maximum profit earned from the investment
    """
    # Create a new model
    m = gp.Model("investment")

    # Define decision variables
    x = m.addVar(lb=0, vtype=GRB.CONTINUOUS, name="condos")
    y = m.addVar(lb=0, vtype=GRB.CONTINUOUS, name="detached_houses")

    # Set objective function
    m.setObjective(0.5*x + y, sense=GRB.MAXIMIZE)

    # Add constraints
    m.addConstr(x + y <= 760000, "budget")
    m.addConstr(0.2*(x + y) <= x, "min_investment_condos")
    m.addConstr(y >= 20000, "min_investment_detached_houses")

    # Optimize model
    m.optimize()

    # Get the optimal objective value
    obj = m.objVal

    return obj