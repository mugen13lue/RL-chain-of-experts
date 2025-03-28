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
    model = gp.Model("cough_syrup_production")

    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="kids_bottles")
    y = model.addVar(vtype=GRB.INTEGER, name="adult_bottles")

    # Constraints
    model.addConstr(x >= 50)
    model.addConstr(x + 3*y <= available_cough_syrup / kids_size_bottle_capacity)
    model.addConstr(y >= 3*x)

    # Objective function
    model.setObjective(x + y, sense=GRB.MAXIMIZE)

    # Optimize the model
    model.optimize()

    number_of_bottles = int(model.objVal)

    return number_of_bottles