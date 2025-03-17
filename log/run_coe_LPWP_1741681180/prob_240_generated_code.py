import pulp

def prob_240(prevention, treatment):
    """
    Args:
        prevention: an integer, number of prevention pills to purchase
        treatment: an integer, number of treatment pills to purchase
    Returns:
        obj: an integer, maximum number of patients that can be treated
    """
    
    # Create a LP minimization problem
    prob = pulp.LpProblem("Maximize_Patients_Treated", pulp.LpMaximize)
    
    # Define decision variables
    num_prevention_pills = pulp.LpVariable("prevention_pills", lowBound=0, cat='Integer')
    num_treatment_pills = pulp.LpVariable("treatment_pills", lowBound=0, cat='Integer')
    
    # Objective function
    prob += pulp.lpSum([num_prevention_pills, num_treatment_pills])
    
    # Constraints
    prob += 15*num_prevention_pills + 25*num_treatment_pills <= 10000
    prob += num_prevention_pills >= 2*num_treatment_pills
    prob += num_treatment_pills >= 50
    
    # Solve the problem
    prob.solve()
    
    # Return the maximum number of patients that can be treated
    return int(pulp.value(prob.objective))