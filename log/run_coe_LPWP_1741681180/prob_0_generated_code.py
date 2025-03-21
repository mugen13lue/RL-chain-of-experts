from scipy.optimize import linprog

def maximize_fish_transport(DogCapability, TruckCapability, DogCost, TruckCost, MaxBudget, FishAvailable):
    """
    Args:
        DogCapability: an integer, indicates the amount of fish which sled dogs can take per trip
        TruckCapability: an integer, indicates the amount of fish which trucks can take per trip
        DogCost: an integer, indicates the cost per trip for a sled dog
        TruckCost: an integer, indicates the cost per trip for a truck
        MaxBudget: an integer, denotes the upper limit of the budget
        FishAvailable: an integer, denotes the total amount of fish available to transport

    Returns:
        FishTransported: an integer, denotes the amount of fish transported after calculation
    """
    
    c = [-DogCapability, -TruckCapability]  # coefficients for the objective function to maximize
    A = [[1, -1], [DogCapability, TruckCapability], [DogCost, TruckCost]]  # constraints for the amount of fish, budget, and number of trips
    b = [0, FishAvailable, MaxBudget]  # RHS of the constraints
    
    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))  # solving the linear programming problem
    
    FishTransported = -res.fun  # extracting the maximum value of the objective function
    
    return int(FishTransported)