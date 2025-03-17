import gurobipy as gp
from gurobipy import GRB

def prob_13(radio_ads, social_media_ads):
    """
    Args:
        radio_ads: an integer representing the number of radio ads
        social_media_ads: an integer representing the number of social media ads
    Returns:
        obj: an integer representing the maximum exposure
    """
    # Create a new model
    model = gp.Model("advertising_exposure")

    # Define decision variables
    x = model.addVar(lb=15, ub=40, vtype=GRB.INTEGER, name="radio_ads")
    y = model.addVar(lb=35, vtype=GRB.INTEGER, name="social_media_ads")

    # Set objective function
    model.setObjective(60500*x + 50000*y, sense=GRB.MAXIMIZE)

    # Add budget constraint
    model.addConstr(5000*x + 9150*y <= 250000, "budget_constraint")

    # Add constraints
    model.addConstr(x >= 15, "minimum_radio_ads")
    model.addConstr(x <= 40, "maximum_radio_ads")
    model.addConstr(y >= 35, "minimum_social_media_ads")

    # Optimize the model
    model.optimize()

    # Get the maximum exposure
    obj = model.objVal

    return obj