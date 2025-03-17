from scipy.optimize import linprog

def prob_13():
    c = [-60500, -50000]  # Coefficients of the objective function to maximize exposure
    A = [[5000, 9150], [-1, 0], [1, 0], [0, -1], [0, 1]]  # Coefficients of the constraints
    b = [250000, -15, 40, -35, 1000]  # Right-hand side of the constraints

    res = linprog(c, A_ub=A, b_ub=b, method='highs')
    max_exposure = -res.fun  # Maximum exposure achieved
    radio_ads = res.x[0]  # Number of radio ads
    social_media_ads = res.x[1]  # Number of social media ads

    return max_exposure, radio_ads, social_media_ads