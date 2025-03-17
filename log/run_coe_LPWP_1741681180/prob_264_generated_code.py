import gurobipy as gp
from gurobipy import GRB

def prob_264(specialized_third_party, common_third_party_annotation_company):
    """
    Args:
        specialized_third_party: an integer, the number of images annotated by the specialized third-party company
        common_third_party_annotation_company: an integer, the number of images annotated by the common third-party annotation company

    Returns:
        obj: an integer, the cost of annotating the whole dataset
    """
    # Create a new model
    model = gp.Model("annotation_optimization")

    # Define variables
    x = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x")  # hours allocated to specialized company
    y = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="y")  # hours allocated to common company

    # Set objective function
    model.setObjective(100 * x + 72 * y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(60 * x + 40 * y == 10000, "total_images_constraint")
    model.addConstr(x >= 3333.33, "specialized_images_constraint")

    # Optimize the model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj