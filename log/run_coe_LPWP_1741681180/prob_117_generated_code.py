from scipy.optimize import linprog

def prob_117(burgers, pizza):
    """
    Args:
        burgers: an integer, the number of burgers
        pizza: an integer, the number of pizza slices
    Returns:
        obj: an integer, the objective value (cholesterol intake)
    """
    fat_burger = 10
    fat_pizza = 8
    cal_burger = 300
    cal_pizza = 250
    chol_burger = 12
    chol_pizza = 10
    
    c = [chol_burger, chol_pizza]
    
    A = [[-fat_burger, -fat_pizza],
         [-cal_burger, -cal_pizza],
         [-1, 2]]
    
    b = [-130, -3000, 0]
    
    res = linprog(c, A_ub=A, b_ub=b)
    
    return res.fun