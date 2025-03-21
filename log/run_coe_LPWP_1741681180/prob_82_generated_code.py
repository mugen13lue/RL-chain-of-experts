import pulp

def prob_82(small_shop, large_shop):
    # Define the Linear Programming problem
    prob = pulp.LpProblem("Minimize Butcher Shops", pulp.LpMinimize)

    # Define the decision variables
    x = pulp.LpVariable("Small_Shop", lowBound=0, cat='Integer')
    y = pulp.LpVariable("Large_Shop", lowBound=0, cat='Integer')

    # Define the objective function
    prob += x + y

    # Define the constraints
    prob += 30*x + 70*y >= 500
    prob += 2*x + 4*y <= 30

    # Solve the Linear Programming problem
    prob.solve()

    # Get the optimal values of x and y
    small_shop = int(x.varValue)
    large_shop = int(y.varValue)

    return small_shop, large_shop