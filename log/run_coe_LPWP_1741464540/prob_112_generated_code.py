from scipy.optimize import linprog

def prob_112(demonstration_1, demonstration_2, mint_d1, active_d1, foam_d1, mint_d2, active_d2, foam_d2, tar_d1, tar_d2, mint_avail, active_avail, tar_max):
    """
    Args:
        demonstration_1: an integer, represents the number of demonstration 1
        demonstration_2: an integer, represents the number of demonstration 2
        mint_d1: an integer, represents the number of mint used in demonstration 1
        active_d1: an integer, represents the number of active ingredient used in demonstration 1
        foam_d1: an integer, represents the amount of minty foam produced in demonstration 1
        mint_d2: an integer, represents the number of mint used in demonstration 2
        active_d2: an integer, represents the number of active ingredient used in demonstration 2
        foam_d2: an integer, represents the amount of minty foam produced in demonstration 2
        tar_d1: an integer, represents the amount of black tar produced in demonstration 1
        tar_d2: an integer, represents the amount of black tar produced in demonstration 2
        mint_avail: an integer, represents the available amount of mint
        active_avail: an integer, represents the available amount of active ingredients
        tar_max: an integer, represents the maximum amount of black tar allowed

    Returns:
        obj: an integer, the objective value which is the amount of minty foam produced
    """
    c = [-foam_d1, -foam_d2]  # Coefficients of the objective function to be minimized

    A = [[mint_d1, mint_d2], [active_d1, active_d2], [tar_d1, tar_d2]]  # Coefficients of the left-hand side of constraints
    b = [mint_avail, active_avail, tar_max]  # Right-hand side of constraints

    bounds = [(0, None), (0, None)]  # Bounds for variables x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return -res.fun  # Return the negative of the optimized objective value since linprog minimizes by default