from scipy.optimize import linprog

def maximize_audience_reach(Pi_TV, Beta_Video, Gamma_Live):
    c = [-2000, -5000, -9000]  # Coefficients of the objective function to maximize audience
    A = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 1, 0], [-1/3, -1/3, -1/3], [-0.2, -0.2, -0.2]]
    b = [0, 0, 0, 8, 0, 0.2]
    bounds = [(0, None), (0, 8), (0, None)]

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    return -res.fun  # Return the negative of the maximum audience reach