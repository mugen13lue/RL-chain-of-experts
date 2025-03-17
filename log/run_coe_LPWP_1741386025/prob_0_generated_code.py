from scipy.optimize import linprog

def prob_0(DogCapability,TruckCapability,DogCost,TruckCost,MaxBudget):
    """
    Args:
        DogCapability: an integer, indicates the amount of fish which sled dogs can take per trip
        TruckCapability: an integer, indicates the amount of fish which trucks can take per trip
        DogCost: an integer, indicates the cost per trip for a sled dog
        TruckCost: an integer, indicates the cost per trip for a truck
        MaxBudget: an integer, denotes the upper limit of the budget

    Returns:
        FishTransported: an integer, denotes the amount of fish transported after calculation
    """
    c = [-1, -1]  # Coefficients of the objective function to maximize x + y
    A = [[-DogCapability, TruckCapability], [-TruckCapability, DogCapability], [DogCost, TruckCost]]  # Coefficients of the inequality constraints
    b = [0, 0, MaxBudget]  # Right-hand side of the inequality constraints

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))

    x = res.x[0]  # Number of trips taken by sled dogs
    y = res.x[1]  # Number of trips taken by trucks

    FishTransported = DogCapability * x + TruckCapability * y
    return FishTransported