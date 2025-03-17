from scipy.optimize import linprog

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
    c = [-8, -10]  # Coefficients of the objective function to minimize (-8x - 10y)
    A = [[wood_train, wood_plane], [paint_train, paint_plane]]  # Coefficients of the constraints for wood and paint
    b = [wood_available, paint_available]  # Available units of wood and paint

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return round(-res.fun)  # Return the maximum profit