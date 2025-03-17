from pulp import LpProblem, LpMaximize, LpVariable

def prob_257(palladium_heavy_catalyst, platinum_heavy_catalyst):
    """
    Args:
        palladium_heavy_catalyst (int): The number of palladium-heavy catalyst to be used.
        platinum_heavy_catalyst (int): The number of platinum-heavy catalyst to be used.

    Returns:
        obj (int): The maximum amount converted into carbon dioxide.
    """
    # Define the Linear Programming problem
    prob = LpProblem("Catalyst Optimization Problem", LpMaximize)

    # Define decision variables
    x = LpVariable("x", lowBound=0, cat='Integer')  # Number of palladium-heavy catalysts used
    y = LpVariable("y", lowBound=0, cat='Integer')  # Number of platinum-heavy catalysts used

    # Define the objective function to maximize
    prob += 5*x + 4*y

    # Add constraints
    prob += 15*x + 20*y <= 450  # Platinum constraint
    prob += 25*x + 14*y <= 390  # Palladium constraint

    # Solve the problem
    prob.solve()

    # Get the maximum amount converted into carbon dioxide
    obj = 5*x.value() + 4*y.value()

    return obj