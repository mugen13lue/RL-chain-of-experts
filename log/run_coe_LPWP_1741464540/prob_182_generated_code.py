import gurobipy as gp
from gurobipy import GRB

def prob_182(helicopter, car):
    """
    Solves the Fish Transportation Problem and calculates the total time needed.

    Args:
        helicopter: an integer representing the number of helicopter trips
        car: an integer representing the number of car trips

    Returns:
        obj: an integer representing the total time needed
    """
    # Create a new model
    model = gp.Model("Fish_Transportation")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of helicopter trips
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of car trips

    # Set objective function: Minimize total time
    model.setObjective(40*x + 30*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(30*x + 20*y >= 300, "Fish_Constraint")
    model.addConstr(x <= 5, "Helicopter_Trips_Constraint")
    model.addConstr(y >= 0.6*(x+y), "Car_Trips_Constraint")

    # Optimize the model
    model.optimize()

    # Get the total time needed
    obj = model.objVal

    return obj