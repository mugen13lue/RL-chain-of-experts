import gurobipy as gp
from gurobipy import GRB

def prob_32(regular_model, premium_model, upperbound_regular_models, upperbound_premium_models, maximum_cars):
    """
    Args:
        regular_model: an integer, representing the number of regular models to make per day (not used)
        premium_model: an integer, representing the number of premium models to make per day (not used)
        upperbound_regular_models: an integer, representing the upper bound limit for regular models
        upperbound_premium_models: an integer, representing the upper bound limit for premium models
        maximum_cars: an integer, representing the maximum number of cars to make per day
    Returns:
        profit: an integer, representing the maximum profit achievable
    """
    # Create a new model
    model = gp.Model("car_production")

    # Define decision variables
    x1 = model.addVar(lb=0, ub=upperbound_regular_models, vtype=GRB.INTEGER, name="regular_models")
    x2 = model.addVar(lb=0, ub=upperbound_premium_models, vtype=GRB.INTEGER, name="premium_models")

    # Set objective function
    model.setObjective(5000*x1 + 8500*x2, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(x1 + x2 <= maximum_cars, "production_constraint")
    model.addConstr(x1 <= 8, "regular_demand_constraint")
    model.addConstr(x2 <= 6, "premium_demand_constraint")

    # Optimize model
    model.optimize()

    # Get the optimal profit
    profit = model.objVal

    return profit