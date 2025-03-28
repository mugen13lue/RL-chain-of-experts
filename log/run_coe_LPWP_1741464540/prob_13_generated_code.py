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
    model = gp.Model("advertising_exposure")

    # Variables
    num_radio_ads = model.addVar(lb=15, ub=40, vtype=GRB.INTEGER, name="radio_ads")
    num_social_media_ads = model.addVar(lb=35, vtype=GRB.INTEGER, name="social_media_ads")

    # Objective Function
    model.setObjective(60500*num_radio_ads + 50000*num_social_media_ads, sense=GRB.MAXIMIZE)

    # Constraints
    model.addConstr(5000*num_radio_ads + 9150*num_social_media_ads <= 250000, "budget")
    
    # Optimize model
    model.optimize()

    return int(model.objVal)