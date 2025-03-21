import gurobipy as gp
from gurobipy import GRB

def prob_210(light_oil, non_sticky_oil, heavy_oil):
    """
    Calculates the maximum net revenue for Maple Oil processing problem.

    Args:
        light_oil: an integer representing the number of tanks of light oil to process
        non_sticky_oil: an integer representing the number of tanks of non-sticky oil to process
        heavy_oil: an integer representing the number of tanks of heavy oil to process

    Returns:
        obj: an integer representing the maximum net revenue
    """
    # Create a new model
    model = gp.Model("oil_processing")

    # Define decision variables
    light_oil_tanks = model.addVar(vtype=GRB.INTEGER, name="light_oil")
    non_sticky_oil_tanks = model.addVar(vtype=GRB.INTEGER, name="non_sticky_oil")
    heavy_oil_tanks = model.addVar(vtype=GRB.INTEGER, name="heavy_oil")

    # Set objective function
    model.setObjective(550*light_oil_tanks + 750*non_sticky_oil_tanks + 950*heavy_oil_tanks, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(3*light_oil_tanks + 6*non_sticky_oil_tanks + 9*heavy_oil_tanks <= 250, "compound_A_constraint")
    model.addConstr(3*light_oil_tanks + 2*non_sticky_oil_tanks + 3*heavy_oil_tanks <= 150, "compound_B_constraint")

    # Optimize the model
    model.optimize()

    # Get the maximum net revenue
    obj = model.objVal

    return obj