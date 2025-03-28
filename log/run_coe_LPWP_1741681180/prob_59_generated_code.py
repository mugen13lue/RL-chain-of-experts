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
    model = gp.Model("bubble_tea_optimization")

    # Decision variables
    lychee_tea = model.addVar(vtype=GRB.INTEGER, name="lychee_tea")
    mango_tea = model.addVar(vtype=GRB.INTEGER, name="mango_tea")

    # Objective function: minimize total amount of tea
    model.setObjective(8 * mango_tea + 6 * lychee_tea, GRB.MINIMIZE)

    # Constraints
    model.addConstr(4 * mango_tea <= mango_juice_limit, "mango_juice_constraint")
    model.addConstr(6 * lychee_tea <= lychee_juice_limit, "lychee_juice_constraint")
    model.addConstr(lychee_tea >= lychee_flavored_limit, "lychee_flavored_constraint")
    model.addConstr(mango_tea >= lychee_tea, "mango_greater_than_lychee_constraint")

    # Optimize model
    model.optimize()

    # Return total amount of tea needed
    return model.objVal