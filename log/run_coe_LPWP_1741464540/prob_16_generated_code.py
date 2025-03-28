from scipy.optimize import linprog

def prob_16():
    c = [-400000, -5000, -3000]  # Coefficients of the objective function to maximize total audience

    A = [[1000, 200, 100],  # Cost constraints
         [-400000, 0, 0],  # Viewer constraint for z-tube
         [0, -5000, 0],  # Viewer constraint for soorchle
         [0, 0, -3000]]  # Viewer constraint for wassa

    b = [10000, 0.05, 15, 0.33]  # Right-hand side of constraints

    res = linprog(c, A_ub=A, b_ub=b, method='highs')

    return int(-res.fun)  # Return the maximized total audience