import gurobipy as gp
from gurobipy import GRB

def prob_68(kids_size_bottle_capacity, adult_size_bottle_capacity, ratio, available_cough_syrup):
    """
    Args:
        kids_size_bottle_capacity: an integer, the capacity of kids size bottle
        adult_size_bottle_capacity: an integer, the capacity of adult size bottle
        ratio: an integer, the ratio of adult size bottle to kids size bottle
        available_cough_syrup: an integer, the total amount of cough syrup available
    Returns:
        number_of_bottles: an integer, the maximum total number of bottles that can be produced
    """
    # Create a new model
    model = gp.Model("cough_syrup_production")

    # Define decision variables
    x = model.addVar(lb=50, vtype=GRB.INTEGER, name="kids_size_bottles")
    y = model.addVar(vtype=GRB.INTEGER, name="adult_size_bottles")

    # Set objective function
    model.setObjective(x + y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(x * kids_size_bottle_capacity + y * adult_size_bottle_capacity <= available_cough_syrup)
    model.addConstr(y >= ratio * x)

    # Optimize model
    model.optimize()

    # Get the optimal solution
    number_of_bottles = int(model.objVal)

    return number_of_bottles