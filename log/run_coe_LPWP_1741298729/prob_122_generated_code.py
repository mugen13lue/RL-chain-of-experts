import gurobipy as gp
from gurobipy import GRB

def prob_122(cheap_box, expensive_box, constraint1, constraint2, constraint3):
    """
    Solve a linear programming problem to maximize the amount of foam produced.

    Args:
        cheap_box: an integer, the number of cheap boxes to make
        expensive_box: an integer, the number of expensive boxes to make
        constraint1: a list of three integers [3, 5, 200], representing the metal constraint
        constraint2: a list of three integers [5, 8, 300], representing the acid constraint
        constraint3: a list of three integers [2, 3, 50], representing the heat constraint

    Returns:
        obj: an integer, the maximum amount of foam produced
    """
    # Create a new model
    model = gp.Model("foam_production")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="cheap_boxes")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="expensive_boxes")

    # Set objective function
    model.setObjective(8*x + 10*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(3*x + 5*y <= constraint1[2], name="metal_constraint")
    model.addConstr(5*x + 8*y <= constraint2[2], name="acid_constraint")
    model.addConstr(2*x + 3*y <= constraint3[2], name="heat_constraint")

    # Optimize model
    model.optimize()

    # Get the maximum amount of foam produced
    obj = model.objVal

    return obj