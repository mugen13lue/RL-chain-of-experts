from gurobipy import *

def prob_13(radio_ads, social_media_ads):
    """
    Args:
        radio_ads: an integer representing the number of radio ads
        social_media_ads: an integer representing the number of social media ads
    Returns:
        obj: an integer representing the maximum exposure
    """
    
    radio_cost = 5000
    social_media_cost = 9150
    radio_exposure = 60500
    social_media_exposure = 50000
    budget = 250000
    
    # Create a new model
    model = Model("advertising_exposure")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="radio_ads")
    y = model.addVar(vtype=GRB.INTEGER, name="social_media_ads")
    
    # Set objective function
    model.setObjective(radio_exposure * x + social_media_exposure * y, GRB.MAXIMIZE)
    
    # Add budget constraint
    model.addConstr(radio_cost * x + social_media_cost * y <= budget)
    
    # Add constraints for minimum and maximum number of ads
    model.addConstr(x >= 15)
    model.addConstr(x <= 40)
    model.addConstr(y >= 35)
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal solution
    max_exposure = int(model.objVal)
    optimal_radio_ads = int(x.x)
    optimal_social_media_ads = int(y.x)
    
    return max_exposure, optimal_radio_ads, optimal_social_media_ads