import gurobipy as gp
from gurobipy import GRB

def prob_59(lychee_bubble_tea, mango_bubble_tea, mango_juice_limit, lychee_juice_limit, lychee_flavored_limit):
    """
    Args:
        lychee_bubble_tea: an integer representing the number of lychee bubble teas made
        mango_bubble_tea: an integer representing the number of mango bubble teas made
        mango_juice_limit: an integer representing the limit of mango juice available
        lychee_juice_limit: an integer representing the limit of lychee juice available
        lychee_flavored_limit: an integer representing the minimum number of lychee flavored bubble teas required
    Returns:
        amount_of_tea: an integer representing the total amount of tea needed
    """
    # Create a new model
    model = gp.Model("bubble_tea_optimization")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="mango_bubble_tea")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="lychee_bubble_tea")

    # Set objective function
    model.setObjective(8*x + 6*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(4*x + 6*y <= mango_juice_limit, "mango_juice_constraint")
    model.addConstr(8*x + 6*y <= lychee_juice_limit, "lychee_juice_constraint")
    model.addConstr(y >= 0.4*(x + y), "lychee_flavored_constraint")
    model.addConstr(x >= y, "mango_greater_than_lychee_constraint")

    # Optimize the model
    model.optimize()

    # Get the total amount of tea needed
    amount_of_tea = model.objVal

    return amount_of_tea