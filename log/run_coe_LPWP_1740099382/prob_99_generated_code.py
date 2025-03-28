import gurobipy as gp
from gurobipy import GRB

def prob_99(peach_flavored_candy, cherry_flavored_candy):
    """
    Args:
        peach_flavored_candy: an integer, the number of peach flavored candy packs
        cherry_flavored_candy: an integer, the number of cherry flavored candy packs

    Returns:
        obj: an integer, the minimal amount of special syrup used
    """
    # Create a new model
    model = gp.Model("candy_production")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="peach_candy")
    y = model.addVar(vtype=GRB.INTEGER, name="cherry_candy")

    # Set objective function
    model.setObjective(5*x + 4*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(3*x <= 3000, "peach_flavoring")
    model.addConstr(5*y <= 4000, "cherry_flavoring")
    model.addConstr(5*x + 4*y <= peach_flavored_candy*5 + cherry_flavored_candy*4, "special_syrup")
    model.addConstr(x >= y, "peach_candy_packs")
    model.addConstr(y >= 0.3*(x+y), "cherry_candy_percentage")

    # Optimize the model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj