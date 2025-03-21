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
    model = gp.Model("advertising")

    # Variables
    x = model.addVar(lb=15, ub=40, vtype=GRB.INTEGER, name="radio_ads")
    y = model.addVar(lb=35, vtype=GRB.INTEGER, name="social_media_ads")

    # Objective Function
    model.setObjective(60500*x + 50000*y, sense=GRB.MAXIMIZE)

    # Constraints
    model.addConstr(5000*x + 9150*y <= 250000, "budget")
    
    # Optimize model
    model.optimize()

    return int(model.objVal)