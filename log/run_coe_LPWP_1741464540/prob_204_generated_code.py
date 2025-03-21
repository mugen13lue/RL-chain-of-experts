from pulp import LpProblem, LpVariable, LpMinimize

def prob_204(milk, vegetables):
    """
    Args:
        milk: an integer, amount of milk
        vegetables: an integer, amount of vegetables
    Returns:
        obj: an integer, objective value (cost)
    """
    # Create the LP minimization problem
    prob = LpProblem("Minimize Cost", LpMinimize)

    # Define the variables
    x = LpVariable("Milk", lowBound=0, cat='Integer')
    y = LpVariable("Vegetables", lowBound=0, cat='Integer')

    # Add the objective function
    prob += x + 2*y, "Total Cost"

    # Add the constraints
    prob += 40*x + 15*y >= 100, "Calcium"
    prob += 25*x + 30*y >= 50, "Iron"

    # Solve the problem
    prob.solve()

    # Return the objective value (cost)
    return int(prob.objective.value())