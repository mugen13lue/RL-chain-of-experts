def prob_103(small_bone, large_bone, medication_constraint, small_bone_percentage_constraint, minimum_large_bone_constraint):
    """
    Args:
        small_bone: an integer.
        large_bone: an integer.
        medication_constraint: an integer.
        small_bone_percentage_constraint: an integer.
        minimum_large_bone_constraint: an integer.
    Returns:
        amount_of_meat: an integer.
    """
    from scipy.optimize import linprog

    c = [12, 15]  # Coefficients of the objective function to minimize 12x + 15y

    A = [[10, 15],  # Coefficients of the constraints
         [12, 15],
         [-1, 0.5],
         [0, -1]]

    b = [medication_constraint,  # Right-hand side of the constraints
         medication_constraint,
         0,
         -minimum_large_bone_constraint]

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return res.fun  # Return the minimum amount of meat needed