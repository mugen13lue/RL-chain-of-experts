from pulp import LpMaximize, LpProblem, LpVariable

def prob_194(small_trucks, large_trucks):
    """
    Args:
        small_trucks: an integer, representing the number of small trucks
        large_trucks: an integer, representing the number of large trucks
    Returns:
        obj: an integer, representing the maximum amount of snow that can be transported
    """
    
    # Create the LP problem
    prob = LpProblem("Snow_Removal_Problem", LpMaximize)
    
    # Define the decision variables
    x = LpVariable("x", lowBound=0, cat='Integer')  # Number of small trucks
    y = LpVariable("y", lowBound=0, cat='Integer')  # Number of large trucks
    
    # Add the objective function
    prob += 30*x + 50*y
    
    # Add constraints
    prob += 2*x + 4*y <= 30
    prob += x >= 10
    prob += y >= 3
    prob += x == 2*y
    
    # Solve the LP problem
    prob.solve()
    
    # Return the maximum amount of snow that can be transported
    return int(prob.objective.value())