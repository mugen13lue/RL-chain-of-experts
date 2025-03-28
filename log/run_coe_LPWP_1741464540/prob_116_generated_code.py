import gurobipy as gp
from gurobipy import GRB

def prob_116(factory_1, factory_2, base_gel):
    """
    Args:
        factory_1: an integer, units of acne cream produced by factory 1 per hour
        factory_2: an integer, units of acne cream produced by factory 2 per hour
        base_gel: an integer, units of base gel required by both factories per hour
    Returns:
        total_time: an integer, total time needed to minimize the total time
    """
    # Create a new model
    model = gp.Model("factory_optimization")

    # Create decision variables
    x = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x")  # hours factory 1 is run
    y = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="y")  # hours factory 2 is run

    # Set objective function to minimize the total time
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(12*x + 20*y >= 800, "acne_cream_production")  # Ensure minimum acne cream production
    model.addConstr(15*x + 10*y >= 1000, "anti_bacterial_cream_production")  # Ensure minimum anti-bacterial cream production
    model.addConstr(30*x + 45*y <= 5000, "base_gel_availability")  # Ensure base gel availability

    # Optimize model
    model.optimize()

    # Get total time needed
    total_time = model.objVal

    return total_time