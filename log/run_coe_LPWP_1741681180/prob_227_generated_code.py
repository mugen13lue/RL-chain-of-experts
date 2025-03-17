from pulp import LpProblem, LpVariable, LpMinimize

def prob_227(subsoil, topsoil):
    # Create the linear programming problem
    prob = LpProblem("Minimize Water Usage", LpMinimize)

    # Define the variables
    x = LpVariable("x", lowBound=0, cat='Integer')  # Number of bags of subsoil
    y = LpVariable("y", lowBound=0, cat='Integer')  # Number of bags of topsoil

    # Add the objective function
    prob += 10*x + 6*y

    # Add constraints
    prob += 10*x + 6*y <= 150  # Water constraint
    prob += y >= 10  # Minimum topsoil constraint
    prob += y <= 0.3*x + 0.3*y  # Topsoil percentage constraint

    # Solve the problem
    prob.solve()

    # Return the minimized amount of water required
    return int(prob.objective.value())