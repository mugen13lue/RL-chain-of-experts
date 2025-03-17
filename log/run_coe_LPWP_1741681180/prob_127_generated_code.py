from scipy.optimize import minimize

def minimize_fat_intake(cashews, almonds, calories_per_almond, protein_per_almond, calories_per_cashew, protein_per_cashew, twice, fat_per_almond, fat_per_cashew, calorie_target, protein_target):
    """
    Args:
        cashews: an integer
        almonds: an integer
        calories_per_almond: an integer
        protein_per_almond: an integer
        calories_per_cashew: an integer
        protein_per_cashew: an integer
        twice: an integer
        fat_per_almond: an integer
        fat_per_cashew: an integer
        calorie_target: an integer
        protein_target: an integer
    Returns:
        obj: an integer
    """
    def objective(x):
        return x[0]*fat_per_almond + x[1]*fat_per_cashew
    
    def calorie_constraint(x):
        return x[0]*calories_per_almond + x[1]*calories_per_cashew - calorie_target
    
    def protein_constraint(x):
        return x[0]*protein_per_almond + x[1]*protein_per_cashew - protein_target
    
    def servings_constraint(x):
        return x[0] - twice*x[1]
    
    x0 = [cashews, almonds]
    constraints = ({'type': 'eq', 'fun': calorie_constraint},
                   {'type': 'eq', 'fun': protein_constraint},
                   {'type': 'eq', 'fun': servings_constraint})
    
    result = minimize(objective, x0, constraints=constraints)
    
    return result.fun

# Example usage
print(minimize_fat_intake(1, 1, 200, 20, 300, 25, 2, 15, 12, 10000, 800))