from pulp import LpProblem, LpMinimize, LpVariable

def prob_93(generator_A, generator_B):
    """
    Args:
        generator_A: an integer, number of generator A
        generator_B: an integer, number of generator B
    Returns:
        obj: an integer, objective value
    """
    # Create a LP minimization problem
    prob = LpProblem("Generator Problem", LpMinimize)

    # Define decision variables
    x = LpVariable("x", lowBound=0, cat='Integer')
    y = LpVariable("y", lowBound=0, cat='Integer')

    # Add constraints
    prob += 40*x + 30*y >= 1000
    prob += 300*x + 200*y <= 3000

    # Set the objective function
    prob += x + y

    # Solve the LP problem
    prob.solve()

    # Get the objective value
    obj = int(x.varValue) * generator_A + int(y.varValue) * generator_B

    return obj