from pulp import LpMaximize, LpProblem, LpVariable

def prob_210(light_oil, non_sticky_oil, heavy_oil):
    # Create the LP problem
    prob = LpProblem("Maximize Net Revenue", LpMaximize)

    # Define decision variables
    x1 = LpVariable("x1", lowBound=0, cat='Integer')
    x2 = LpVariable("x2", lowBound=0, cat='Integer')
    x3 = LpVariable("x3", lowBound=0, cat='Integer')

    # Define objective function
    prob += 550*x1 + 750*x2 + 950*x3, "Net Revenue"

    # Define constraints
    prob += 3*x1 + 6*x2 + 9*x3 <= 250, "Compound A Constraint"
    prob += 3*x1 + 2*x2 + 3*x3 <= 150, "Compound B Constraint"

    # Solve the problem
    prob.solve()

    # Get the optimal solution
    optimal_net_revenue = prob.objective.value()

    return optimal_net_revenue

# Example usage
print(prob_210(0, 0, 0))  # Output: 0