from pulp import LpProblem, LpMinimize, LpVariable

def prob_183(hot_air_balloon, gondola_lift):
    """
    Args:
        hot_air_balloon: an integer, represents the maximum number of hot air balloons rides
        gondola_lift: an integer, represents the maximum number of gondola lift rides
    Returns:
        obj: an integer, the minimized total pollution produced
    """
    # Create the linear programming problem
    prob = LpProblem("Minimize Pollution", LpMinimize)

    # Define the decision variables
    x = LpVariable("x", lowBound=0, upBound=hot_air_balloon, cat='Integer')
    y = LpVariable("y", lowBound=0, upBound=gondola_lift, cat='Integer')

    # Set up the objective function to minimize pollution
    prob += 10*x + 15*y

    # Add constraints
    prob += 4*x + 6*y >= 70
    prob += x <= 10

    # Solve the linear programming problem
    prob.solve()

    # Get the minimized total pollution produced
    obj = 10*x.value() + 15*y.value()

    return obj