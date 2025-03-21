from scipy.optimize import linprog

def prob_126(machine_1, machine_2, constraint1, constraint2, constraint3):
    c = [1, 1]  # Coefficients of the objective function to minimize x + y

    A = [
        [-30, -45],  # Coefficients of Eye Cream Production constraint: 30x + 45y >= 1300
        [-60, -30],  # Coefficients of Foot Cream Production constraint: 60x + 30y >= 1500
        [20, 15]     # Coefficients of Distilled Water Usage constraint: 20x + 15y <= 1200
    ]

    b = [-1300, -1500, 1200]  # Right-hand side values of the constraints

    bounds = [(0, None), (0, None)]  # Non-negativity constraints for x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return res.fun