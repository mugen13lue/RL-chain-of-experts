from pulp import LpProblem, LpMinimize, LpVariable

def prob_156(vans, trucks):
    """
    Args:
        vans: an integer, number of vans
        trucks: an integer, number of trucks
        
    Returns:
        obj: an integer, the minimum number of vans that can be used
    """
    # Create the LP minimization problem
    prob = LpProblem("Minimize Vans", LpMinimize)
    
    # Define the variables
    num_vans = LpVariable("Number of Vans", lowBound=0, cat='Integer')
    num_trucks = LpVariable("Number of Trucks", lowBound=0, cat='Integer')
    
    # Add the constraints
    prob += 50*num_vans + 100*num_trucks >= 2000
    prob += num_trucks <= num_vans
    
    # Set the objective
    prob += num_vans
    
    # Solve the problem
    prob.solve()
    
    # Return the minimum number of vans used
    return int(num_vans.varValue)