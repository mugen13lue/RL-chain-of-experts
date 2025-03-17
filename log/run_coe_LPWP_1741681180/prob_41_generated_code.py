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
    # Create a new model
    model = gp.Model("flooring_production")

    # Define decision variables
    x1 = model.addVar(lb=0, ub=50000, vtype=GRB.CONTINUOUS, name="hardwood")
    x2 = model.addVar(lb=0, ub=30000, vtype=GRB.CONTINUOUS, name="vinyl_planks")

    # Set objective function
    model.setObjective(2.5*x1 + 3*x2, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(x1 >= 20000)
    model.addConstr(x2 >= 10000)
    model.addConstr(x1 + x2 >= 60000)

    # Optimize the model
    model.optimize()

    # Get the optimal profit
    profit = model.objVal

    return profit