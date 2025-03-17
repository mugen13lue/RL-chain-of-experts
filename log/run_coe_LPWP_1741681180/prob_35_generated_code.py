from scipy.optimize import linprog

def prob_35(pill_A, pill_B, sleep_inducing_constraint, anti_inflammatory_constraint):
    c = [4, 5]  # Cost per pill A and pill B
    A = [[-3, -6], [-5, -1]]  # Coefficients of sleep-inducing and anti-inflammatory medicine for pill A and pill B
    b = [-sleep_inducing_constraint, -anti_inflammatory_constraint]  # Constraints for minimum medicine intake
    
    res = linprog(c, A_ub=A, b_ub=b)
    
    if res.success:
        return round(res.fun * (pill_A + pill_B), 2)  # Total cost
    else:
        return "No feasible solution found"