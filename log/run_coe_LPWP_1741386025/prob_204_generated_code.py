from gurobipy import *

def prob_204(milk, vegetables):
    """
    Args:
        milk: an integer, amount of milk
        vegetables: an integer, amount of vegetables
    Returns:
        obj: an integer, objective value (cost)
    """
    # Create a new model
    model = Model("Milk and Vegetables Consumption")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of glasses of milk
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of plates of vegetables

    # Set objective function: Minimize Cost
    model.setObjective(x + 2*y, GRB.MINIMIZE)

    # Add constraints
    model.addConstr(40*x + 15*y >= 100, "Calcium")
    model.addConstr(25*x + 30*y >= 50, "Iron")

    # Optimize the model
    model.optimize()

    # Get the objective value (cost)
    obj = model.objVal

    return obj