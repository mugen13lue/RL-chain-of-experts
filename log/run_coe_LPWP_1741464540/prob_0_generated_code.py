from scipy.optimize import linprog

def prob_0(DogCapability, TruckCapability, DogCost, TruckCost, MaxBudget):
    # Define the coefficients of the objective function
    c = [-DogCapability, -TruckCapability]  # Coefficients for maximizing fish transported

    # Define the coefficients of the inequality constraints
    A = [[DogCost, TruckCost]]  # Coefficients for budget constraint
    b = [MaxBudget]  # Upper limit of the budget

    # Define the bounds for the variables
    x_bounds = (0, None)  # Number of sled dog trips
    y_bounds = (0, None)  # Number of truck trips

    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    # Extract the optimal solution
    x_opt = res.x[0]  # Number of sled dog trips
    y_opt = res.x[1]  # Number of truck trips

    # Calculate the amount of fish transported
    FishTransported = DogCapability * x_opt + TruckCapability * y_opt

    return FishTransported