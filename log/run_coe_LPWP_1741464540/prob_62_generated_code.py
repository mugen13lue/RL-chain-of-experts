import gurobipy as gp
from gurobipy import GRB

def prob_62(rural, urban, _100, _8, _200, _20, _260, _3000):
    """
    Args:
        rural: an integer, number of rural factories
        urban: an integer, number of urban factories
        _100: an integer, number of phones that a rural factory can make per day
        _8: an integer, number of managers required for a rural factory
        _200: an integer, number of phones that an urban factory can make per day
        _20: an integer, number of managers required for an urban factory
        _260: an integer, available number of managers
        _3000: an integer, minimum number of phones required per day
    Returns:
        number_of_factories: an integer, total number of factories
    """
    # Create a new model
    model = gp.Model("factories")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of rural factories
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of urban factories

    # Set objective function
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(8*x + 20*y <= 260, "managers_constraint")
    model.addConstr(100*x + 200*y >= 3000, "phones_constraint")

    # Optimize model
    model.optimize()

    # Get the optimal solution
    number_of_factories = model.objVal

    return number_of_factories