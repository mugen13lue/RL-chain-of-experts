import gurobipy as gp
from gurobipy import GRB

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
    model = gp.Model("FishTransportation")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of trips taken by sled dogs
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of trips taken by trucks
    
    # Set objective function
    model.setObjective(x * DogCapability + y * TruckCapability, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(DogCost * x + TruckCost * y <= MaxBudget, "BudgetConstraint")
    model.addConstr(x <= y, "SledDogTripsConstraint")
    
    # Optimize model
    model.optimize()
    
    # Get the optimal solution
    FishTransported = int(model.objVal)
    
    return FishTransported