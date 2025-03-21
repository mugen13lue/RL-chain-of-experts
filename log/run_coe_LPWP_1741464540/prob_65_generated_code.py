from pulp import LpMaximize, LpProblem, LpVariable

def prob_65(small_oil_well, large_oil_well):
    """
    Args:
        small_oil_well: an integer, number of acres to be used for small oil wells
        large_oil_well: an integer, number of acres to be used for large oil wells

    Returns:
        Total_Production_of_Oil: an integer, total production of oil
    """
    # Create the LP maximization problem
    prob = LpProblem("Oil Production Maximization", LpMaximize)

    # Define decision variables
    x = LpVariable("x", lowBound=0, cat='Continuous')
    y = LpVariable("y", lowBound=0, cat='Continuous')

    # Add the objective function
    prob += 2*x + 5*y, "Total Production of Oil"

    # Add constraints
    prob += 2*x + 5*y <= 300, "Production Constraint"
    prob += 5*x + 10*y <= 2500, "Drill Bits Constraint"
    prob += 10*x + 20*y <= 4500, "Pollution Constraint"

    # Solve the problem
    prob.solve()

    # Get the total production of oil
    Total_Production_of_Oil = 2*x.value() + 5*y.value()

    return Total_Production_of_Oil