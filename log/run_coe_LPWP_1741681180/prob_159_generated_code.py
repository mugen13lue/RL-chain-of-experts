from scipy.optimize import linprog

def prob_159(trucks, vans):
    c = [300, 100]  # Cost coefficients for trucks and vans
    A = [[1000, 500], [-1, 0], [0, -1]]  # Coefficients for constraints
    b = [50000, 0, 0]  # RHS of constraints
    bounds = [(0, None), (0, None)]  # Bounds for variables x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    obj = res.fun  # Optimal objective value

    return int(obj)