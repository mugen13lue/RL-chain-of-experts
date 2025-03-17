from scipy.optimize import linprog

def prob_202(desks, drawers, assembly_constraint, sanding_constraint):
    """
    Args:
        desks: an integer, representing the number of desks
        drawers: an integer, representing the number of drawers
        assembly_constraint: an integer, representing the available minutes for assembly
        sanding_constraint: an integer, representing the available minutes for sanding
    Returns:
        profit: an integer, representing the maximum profit
    """
    c = [-100, -90]  # Coefficients of the objective function to minimize (-100x - 90y)
    A = [[40, 30], [20, 10]]  # Coefficients of the constraints for assembly and sanding
    b = [assembly_constraint, sanding_constraint]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    return -res.fun  # Return the maximum profit (negative because linprog minimizes by default)