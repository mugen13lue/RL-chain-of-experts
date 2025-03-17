import gurobipy as gp
from gurobipy import GRB

def prob_206(plush_toys, dolls):
    """
    Args:
        plush_toys: an integer representing the number of plush toys
        dolls: an integer representing the number of dolls

    Returns:
        obj: an integer representing the maximum profit
    """
    # Create a new model
    model = gp.Model("toy_store")

    # Define decision variables with initial values
    x = model.addVar(lb=plush_toys, ub=plush_toys, vtype=GRB.INTEGER, name="plush_toys")
    y = model.addVar(lb=dolls, ub=dolls, vtype=GRB.INTEGER, name="dolls")

    # Set objective function
    model.setObjective(4*x + 2*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(3*x + 2*y <= 700, "budget_constraint")
    model.addConstr(y <= 2*x, "doll_sales_constraint")

    # Optimize model
    model.optimize()

    # Get the maximum profit
    obj = model.objVal

    return obj