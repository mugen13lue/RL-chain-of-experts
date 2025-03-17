from pulp import LpProblem, LpMinimize, LpVariable

def prob_230(calcium_pills, vitamin_d_pills):
    """
    Args:
        calcium_pills: an integer (number of calcium pills)
        vitamin_d_pills: an integer (number of vitamin D pills)
    Returns:
        total_time: an integer (total time for the medication to be effective)
    """
    total_time = 1e9

    # Define the LP problem
    prob = LpProblem("Medication Optimization Problem", LpMinimize)

    # Define decision variables
    C = LpVariable("Calcium_pills", lowBound=0, cat='Integer')
    V = LpVariable("Vitamin_D_pills", lowBound=0, cat='Integer')

    # Set up the objective function
    prob += 5 * C + 6 * V

    # Add constraints
    prob += C + V >= 130
    prob += V >= 40
    prob += C > V

    # Solve the LP problem
    prob.solve()

    # Get the optimal values
    optimal_C = int(C.varValue)
    optimal_V = int(V.varValue)

    total_time = 5 * optimal_C + 6 * optimal_V

    return total_time