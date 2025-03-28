from scipy.optimize import linprog

def prob_29(regular_mix, sour_surprise_mix, constraint1, constraint2):
    c = [-3, -5]  # Coefficients of the objective function to minimize (-3x - 5y)
    A = [[0.8, 0.1], [0.2, 0.9]]  # Coefficients of the constraints for regular and sour candy
    b = [constraint1, constraint2]  # Limits of available regular and sour candy
    bounds = [(0, None), (0, None)]  # Non-negativity constraint for x and y

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    return -res.fun  # Return the maximum profit achieved

# Example usage
regular_mix = 0
sour_surprise_mix = 0
constraint1 = 80
constraint2 = 60
print(prob_29(regular_mix, sour_surprise_mix, constraint1, constraint2))