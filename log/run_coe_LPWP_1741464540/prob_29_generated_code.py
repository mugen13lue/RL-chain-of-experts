from pulp import LpMaximize, LpProblem, LpVariable

def prob_29(regular_mix, sour_surprise_mix, constraint1, constraint2):
    """
    Args:
        regular_mix: a float, the amount of regular mix candy created
        sour_surprise_mix: a float, the amount of sour surprise mix candy created
        constraint1: an integer, the limit of available regular candy
        constraint2: an integer, the limit of available sour candy
    Returns:
        obj: a float, the maximum profit achieved
    """
    # Create a LP maximization problem
    prob = LpProblem("Maximize_Profit", LpMaximize)

    # Define decision variables
    x = LpVariable("regular_mix", lowBound=0)
    y = LpVariable("sour_surprise_mix", lowBound=0)

    # Set the objective function
    prob += 3*x + 5*y

    # Add constraints
    prob += 0.8*x + 0.1*y <= constraint1
    prob += 0.2*x + 0.9*y <= constraint2

    # Solve the problem
    prob.solve()

    # Get the maximum profit achieved
    obj = prob.objective.value()

    return obj