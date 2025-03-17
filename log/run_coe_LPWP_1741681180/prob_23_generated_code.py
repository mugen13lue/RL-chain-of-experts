import gurobipy as gp
from gurobipy import GRB

def prob_23(elephants, tigers):
    """
    Args:
        elephants: an integer, the number of elephants to make
        tigers: an integer, the number of tigers to make
    Returns:
        profit: an integer, the maximum profit
    """
    # Create a new model
    model = gp.Model("profit_maximization")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="elephants")
    y = model.addVar(vtype=GRB.INTEGER, name="tigers")

    # Set objective function
    model.setObjective(5*x + 4*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(50*x + 40*y <= 5000, "wood_constraint")
    model.addConstr(20*x + 30*y <= 4000, "plastic_constraint")

    # Optimize model
    model.optimize()

    # Get the optimal solution
    profit = model.objVal

    return profit