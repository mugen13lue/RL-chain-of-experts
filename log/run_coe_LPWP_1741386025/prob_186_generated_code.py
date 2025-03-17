from pulp import LpProblem, LpMinimize, LpVariable, value

def prob_186(cows, elephants):
    """
    Args:
        cows: an integer, number of cows
        elephants: an integer, number of elephants
    Returns:
        obj: an integer, objective value
    """
    # Create the LP problem
    prob = LpProblem("Minimize Animals", LpMinimize)

    # Define decision variables
    x = LpVariable("Cows", lowBound=0, cat='Integer')
    y = LpVariable("Elephants", lowBound=0, cat='Integer')

    # Add constraints
    prob += 20*x + 50*y >= 1000
    prob += y <= x
    prob += x <= 2*y

    # Set the objective
    prob += x + y

    # Solve the LP problem
    prob.solve()

    # Get the objective value
    obj = value(prob.objective)

    return int(obj)