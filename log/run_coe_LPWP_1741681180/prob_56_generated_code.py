from pulp import LpProblem, LpMinimize, LpVariable

def prob_56(wraps, platters, meat_wrap, rice_wrap, meat_platter, rice_platter, time_wrap, time_platter, wrap_to_platter_ratio): 
    """
    Args:
        wraps: an integer (number of wraps to produce)
        platters: an integer (number of platters to produce)
        meat_wrap: an integer (units of meat required for a wrap)
        rice_wrap: an integer (units of rice required for a wrap)
        meat_platter: an integer (units of meat required for a platter)
        rice_platter: an integer (units of rice required for a platter)
        time_wrap: an integer (time in minutes to produce a wrap)
        time_platter: an integer (time in minutes to produce a platter)
        wrap_to_platter_ratio: an integer (minimum ratio of wraps to platters)
        
    Returns:
        obj: a float (minimum total production time)
    """
    # Create a LP minimization problem
    prob = LpProblem("FastFoodProduction", LpMinimize)
    
    # Define decision variables
    wraps_var = LpVariable("Wraps", lowBound=0, cat='Integer')
    platters_var = LpVariable("Platters", lowBound=0, cat='Integer')
    
    # Add objective function
    prob += time_wrap * wraps_var + time_platter * platters_var
    
    # Add constraints
    prob += meat_wrap * wraps_var + meat_platter * platters_var >= 3000
    prob += rice_wrap * wraps_var + rice_platter * platters_var >= 2500
    prob += wraps_var >= wrap_to_platter_ratio * platters_var
    
    # Solve the problem
    prob.solve()
    
    # Return the minimum total production time
    return prob.objective.value()