import gurobipy as gp
from gurobipy import GRB

def prob_112(demonstration_1, demonstration_2, _10, _20, _25, _12, _15, _18, _5, _3, _120, _100, _50):
    """
    Args:
        demonstration_1: an integer, represents the number of demonstration 1
        demonstration_2: an integer, represents the number of demonstration 2
        _10: an integer, represents the number of mint used in demonstration 1
        _20: an integer, represents the number of active ingredient used in demonstration 1
        _25: an integer, represents the amount of minty foam produced in demonstration 1
        _12: an integer, represents the number of mint used in demonstration 2
        _15: an integer, represents the number of active ingredient used in demonstration 2
        _18: an integer, represents the amount of minty foam produced in demonstration 2
        _5: an integer, represents the amount of black tar produced in demonstration 1
        _3: an integer, represents the amount of black tar produced in demonstration 2
        _120: an integer, represents the available amount of mint
        _100: an integer, represents the available amount of active ingredients
        _50: an integer, represents the maximum amount of black tar allowed

    Returns:
        obj: an integer, the objective value which is the amount of minty foam produced
    """
    # Create a new model
    model = gp.Model("minty_foam_production")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")
    y = model.addVar(vtype=GRB.INTEGER, name="y")

    # Set objective function
    model.setObjective(25*x + 18*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(10*x + 12*y <= 120, "mint_constraint")
    model.addConstr(20*x + 15*y <= 100, "active_ingredient_constraint")
    model.addConstr(5*x + 3*y <= 50, "black_tar_constraint")

    # Optimize the model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj