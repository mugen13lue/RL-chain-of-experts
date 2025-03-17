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
    hardwood_production = model.addVar(lb=0, ub=50000, vtype=GRB.CONTINUOUS, name="hardwood")
    vinyl_production = model.addVar(lb=0, ub=30000, vtype=GRB.CONTINUOUS, name="vinyl_planks")

    # Set objective function
    model.setObjective(2.5*hardwood_production + 3*vinyl_production, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(hardwood_production >= 20000, name="demand_hardwood")
    model.addConstr(vinyl_production >= 10000, name="demand_vinyl_planks")
    model.addConstr(hardwood_production + vinyl_production >= 60000, name="shipping_constraint")

    # Optimize the model
    model.optimize()

    # Get the optimal profit
    profit = model.objVal

    return profit