import gurobipy as gp
from gurobipy import GRB

def prob_41():
    """
    Returns:
        profit: a float, the maximum profit that can be achieved
    """
    # Create a new model
    model = gp.Model("flooring_production")

    # Define decision variables
    x = model.addVar(lb=20000, ub=50000, vtype=GRB.CONTINUOUS, name="hardwood")
    y = model.addVar(lb=10000, ub=30000, vtype=GRB.CONTINUOUS, name="vinyl_planks")

    # Set objective function
    model.setObjective(2.5*x + 3*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(x + y >= 60000, "shipping_contract")
    model.addConstr(x >= 20000, "hardwood_demand")
    model.addConstr(y >= 10000, "vinyl_demand")

    # Optimize the model
    model.optimize()

    # Get the optimal profit
    profit = model.objVal

    return profit