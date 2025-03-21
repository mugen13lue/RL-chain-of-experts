import gurobipy as gp
from gurobipy import GRB

def prob_27(model_trains, planes, wood_train, paint_train, wood_plane, paint_plane, wood_available, paint_available):
    """
    Args:
        model_trains: an integer, number of model trains
        planes: an integer, number of planes
        wood_train: an integer, units of wood required for a model train
        paint_train: an integer, units of paint required for a model train
        wood_plane: an integer, units of wood required for a plane
        paint_plane: an integer, units of paint required for a plane
        wood_available: an integer, available units of wood
        paint_available: an integer, available units of paint
    Returns:
        obj: an integer, maximum profit
    """
    # Create a new model
    model = gp.Model("profit_maximization")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="model_trains")
    y = model.addVar(vtype=GRB.INTEGER, name="planes")

    # Set objective function
    model.setObjective(8*x + 10*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(wood_train*x + wood_plane*y <= wood_available)
    model.addConstr(paint_train*x + paint_plane*y <= paint_available)

    # Optimize model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj