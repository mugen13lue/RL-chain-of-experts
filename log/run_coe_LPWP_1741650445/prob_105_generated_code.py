import gurobipy as gp
from gurobipy import GRB

def prob_105(cleansing_chemical, odor_removing_chemical):
    """
    Args:
        cleansing_chemical: an integer, the units of cleansing chemical used
        odor_removing_chemical: an integer, the units of odor-removing chemical used
    Returns:
        obj: an integer, the total time it takes for a house to be cleaned
    """
    model = gp.Model("house_cleaning")

    # Define decision variables as integer variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="cleansing_chemical")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="odor_removing_chemical")

    # Set objective function
    model.setObjective(4*x + 6*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(4*x + 6*y >= 60)
    model.addConstr(x >= 100)
    model.addConstr(x + y <= 300)
    model.addConstr(x <= 2*y)

    # Optimize the model
    model.optimize()

    # Get the total time
    obj = model.objVal

    return obj