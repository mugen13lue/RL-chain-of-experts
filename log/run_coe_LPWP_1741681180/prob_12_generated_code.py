from pulp import LpMaximize, LpProblem, LpVariable

def prob_12():
    # Create the LP object, set up as a maximization problem
    prob = LpProblem("Maximize Profit", LpMaximize)

    # Define decision variables
    x = LpVariable("regular_sandwiches", lowBound=0, cat='Integer')
    y = LpVariable("special_sandwiches", lowBound=0, cat='Integer')

    # Set up the objective function
    prob += 3*x + 4*y, "Total Profit"

    # Add constraints
    prob += 2*x + 3*y <= 40, "Eggs Constraint"
    prob += 3*x + 5*y <= 70, "Bacon Constraint"

    # Solve the LP problem
    prob.solve()

    # Get the optimal solution
    optimal_profit = round(prob.objective.value(), 2)
    optimal_regular_sandwiches = x.varValue
    optimal_special_sandwiches = y.varValue

    return optimal_profit, optimal_regular_sandwiches, optimal_special_sandwiches