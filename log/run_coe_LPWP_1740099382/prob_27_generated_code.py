from gurobipy import *

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
    m = Model("Model_Trains_and_Planes")

    # Decision variables
    x = m.addVar(vtype=GRB.CONTINUOUS, name="model_trains")
    y = m.addVar(vtype=GRB.CONTINUOUS, name="planes")

    # Objective function
    m.setObjective(8*x + 10*y, sense=GRB.MAXIMIZE)

    # Constraints
    m.addConstr(wood_train*x + wood_plane*y <= wood_available, "wood_constraint")
    m.addConstr(paint_train*x + paint_plane*y <= paint_available, "paint_constraint")
    m.addConstr(x >= 0, "non_negativity_model_trains")
    m.addConstr(y >= 0, "non_negativity_planes")

    # Optimize model
    m.optimize()

    return int(m.objVal)