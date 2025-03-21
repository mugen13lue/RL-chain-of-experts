from pulp import LpMaximize, LpProblem, LpVariable

def prob_138(medicine_A, medicine_B):
    # Create a LP maximization problem
    prob = LpProblem("Maximize_People_Treated", LpMaximize)

    # Define decision variables
    x = LpVariable("x", lowBound=0, upBound=5, cat='Integer')  # Number of doses of medicine A
    y = LpVariable("y", lowBound=0, cat='Integer')  # Number of doses of medicine B

    # Set up the objective function to maximize
    prob += 12*x + 8*y

    # Add constraints
    prob += 30*x + 40*y <= 300  # Imported material constraint
    prob += 50*x + 30*y <= 400  # mRNA constraint
    prob += y >= x  # Number of doses of medicine B must be larger than medicine A

    # Solve the problem
    prob.solve()

    # Get the maximum number of people that can be treated
    max_people_treated = 12*x.varValue + 8*y.varValue

    return int(max_people_treated)