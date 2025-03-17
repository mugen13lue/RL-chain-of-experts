import gurobipy as gp
from gurobipy import GRB

def prob_223(Pi_TV, Beta_Video, Gamma_Live):
    """
    Args:
        Pi_TV: an integer, representing the number of commercials to run on Pi TV
        Beta_Video: an integer, representing the number of commercials to run on Beta Video
        Gamma_Live: an integer, representing the number of commercials to run on Gamma Live
    Returns:
        obj: an integer, representing the maximum audience
    """
    
    # Create a new model
    model = gp.Model("commercial_optimization")
    
    # Define decision variables
    x1 = model.addVar(vtype=GRB.INTEGER, name="Pi_TV_Commercials")  # Number of commercials on Pi TV
    x2 = model.addVar(vtype=GRB.INTEGER, name="Beta_Video_Commercials")  # Number of commercials on Beta Video
    x3 = model.addVar(vtype=GRB.INTEGER, name="Gamma_Live_Commercials")  # Number of commercials on Gamma Live
    
    # Set objective function: maximize audience reach
    model.setObjective(2000*x1 + 5000*x2 + 9000*x3, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(1200*x1 + 2000*x2 + 4000*x3 <= 20000, "Budget")
    model.addConstr(x2 <= 8, "Beta_Video_Limit")
    model.addConstr(x3 <= 2*x1, "Gamma_Live_Limit")
    model.addConstr(x1 >= 0.2*(x1 + x2 + x3), "Pi_TV_Minimum")
    model.addConstr(x3 <= 0.33*(x1 + x2 + x3), "Gamma_Live_Maximum")
    
    # Optimize the model
    model.optimize()
    
    # Get the maximum audience reach
    obj = model.objVal
    
    return obj