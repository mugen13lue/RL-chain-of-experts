from gurobipy import *

def prob_23(elephants, tigers):
    """
    Args:
        elephants: an integer, the number of elephants to make
        tigers: an integer, the number of tigers to make
    Returns:
        profit: an integer, the maximum profit
    """
    # Create a new model
    m = Model("souvenir_shop")

    # Define decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="elephants")
    y = m.addVar(vtype=GRB.INTEGER, name="tigers")

    # Set objective function
    m.setObjective(5*x + 4*y, sense=GRB.MAXIMIZE)

    # Add constraints
    m.addConstr(50*x + 40*y <= 5000, "wood_constraint")
    m.addConstr(20*x + 30*y <= 4000, "plastic_constraint")

    # Optimize model
    m.optimize()

    # Get the maximum profit
    profit = m.objVal

    return profit