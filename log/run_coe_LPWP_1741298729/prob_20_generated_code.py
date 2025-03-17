from pulp import LpMaximize, LpProblem, LpVariable

def prob_20(banana_haters_package, combo_package):
    # Create the LP maximization problem
    prob = LpProblem("Maximize Net Profit", LpMaximize)

    # Define decision variables
    x = LpVariable("x", lowBound=0, cat='Integer')  # Number of banana-haters packages
    y = LpVariable("y", lowBound=0, cat='Integer')  # Number of combo packages

    # Set up the objective function to maximize net profit
    prob += 6*x + 7*y

    # Add constraints
    prob += 6*x + 5*y <= 10  # Apples constraint
    prob += 30*x + 6*y <= 20  # Bananas constraint
    prob += 30*x + 20*y <= 80  # Grapes constraint

    # Solve the problem
    prob.solve()

    # Return the maximum net profit
    return int(prob.objective.value())