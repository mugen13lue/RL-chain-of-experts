import gurobipy as gp
from gurobipy import GRB

def prob_144(chlorine, water_softener):
    """
    Args:
        chlorine: an integer representing the number of units of chlorine to be added to the pool.
        water_softener: an integer representing the number of units of water softener to be added to the pool.
    Returns:
        total_time: an integer representing the minimum total time it takes for the pool to be ready.
    """
    # Create a new model
    model = gp.Model("pool_optimization")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="chlorine")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="water_softener")

    # Set objective function
    model.setObjective(x + 2*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(x <= 0.5*y, "chlorine_limit")
    model.addConstr(x >= 200, "min_chlorine")
    model.addConstr(x + y <= 500, "total_chemicals")

    # Optimize the model
    model.optimize()

    # Get the total time
    total_time = model.objVal

    return total_time