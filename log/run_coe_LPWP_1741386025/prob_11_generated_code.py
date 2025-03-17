import gurobipy as gp
from gurobipy import GRB

def prob_11(condos, detached_houses):
    """
    Args:
        condos: a float, representing the amount invested in condos
        detached_houses: a float, representing the amount invested in detached houses
    
    Returns:
        obj: a float, representing the maximum profit earned from the investment
    """
    # Create a new model
    model = gp.Model("investment_optimization")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="condos")
    y = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="detached_houses")

    # Set objective function
    model.setObjective(0.5*x + y, sense=GRB.MAXIMIZE)

    # Add constraints
    budget_constraint = model.addConstr(x + y <= 760000, "budget_constraint")
    min_condos_constraint = model.addConstr(0.2*(x + y) <= x, "min_condos_constraint")
    min_detached_constraint = model.addConstr(y >= 20000, "min_detached_constraint")

    # Optimize the model
    model.optimize()

    # Get the maximum profit earned
    obj = model.objVal

    return obj