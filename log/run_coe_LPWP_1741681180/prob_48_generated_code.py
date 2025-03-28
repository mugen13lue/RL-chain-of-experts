import gurobipy as gp
from gurobipy import GRB

def prob_48(factory_1, factory_2, constraint_1, constraint_2, constraint_3):
    """
    Args:
        factory_1: an integer (number of hours for factory 1),
        factory_2: an integer (number of hours for factory 2),
        constraint_1: an integer (limit for constraint 1),
        constraint_2: an integer (limit for constraint 2),
        constraint_3: an integer (limit for constraint 3),
    Returns:
        cost: an integer (the minimized cost of production),
    """
    # Create a new model
    model = gp.Model("teddy_bear_production")

    # Define decision variables
    x1 = model.addVar(vtype=GRB.INTEGER, name="factory_1_hours")
    x2 = model.addVar(vtype=GRB.INTEGER, name="factory_2_hours")

    # Set objective function: minimize total cost
    model.setObjective(300*x1 + 600*x2, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(5*x1 + 10*x2 >= constraint_1, "black_bears_constraint")
    model.addConstr(6*x1 + 10*x2 >= constraint_2, "white_bears_constraint")
    model.addConstr(3*x1 >= constraint_3, "brown_bears_constraint")

    # Non-negativity constraints
    model.addConstr(x1 >= 0, "non_negativity_factory_1")
    model.addConstr(x2 >= 0, "non_negativity_factory_2")

    # Optimize the model
    model.optimize()

    # Get the minimized cost of production
    cost = model.objVal

    return cost