from gurobipy import *

def prob_0(DogCapability, TruckCapability, DogCost, TruckCost, MaxBudget):
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
    
    # Create a new model
    model = Model("FishTransportation")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of trips taken by sled dogs
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of trips taken by trucks

    # Set objective function: maximize the number of fish transported
    model.setObjective(50*x + 100*y, GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(DogCapability*x + TruckCapability*y <= MaxBudget, "BudgetConstraint")
    model.addConstr(x <= y, "DogTripsLessThanTruckTrips")

    # Optimize the model
    model.optimize()

    # Get the optimal solution
    FishTransported = int(model.objVal)

    return FishTransported