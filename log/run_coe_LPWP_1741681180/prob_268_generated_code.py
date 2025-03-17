import pulp

def prob_268(in_vivo, ex_vivo, constraint1, constraint2):
    # Define the Linear Programming problem
    prob = pulp.LpProblem("Minimize Radiation Exposure", pulp.LpMinimize)

    # Define decision variables
    x = pulp.LpVariable("in_vivo_experiments", lowBound=0, cat='Integer')
    y = pulp.LpVariable("ex_vivo_experiments", lowBound=0, cat='Integer')

    # Objective function
    prob += 2*x + 3*y

    # Constraints
    prob += 30*x + 45*y <= constraint1
    prob += 60*x + 30*y <= constraint2

    # Solve the problem
    prob.solve()

    # Get the optimal solution
    in_vivo_optimal = int(pulp.value(x))
    ex_vivo_optimal = int(pulp.value(y))
    obj = int(pulp.value(prob.objective))

    return in_vivo_optimal, ex_vivo_optimal, obj