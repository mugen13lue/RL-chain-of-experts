import gurobipy as gp
from gurobipy import GRB

def prob_84(experiment_alpha, experiment_beta):
    """
    Args:
        experiment_alpha: an integer, represents the number of times to conduct experiment alpha
        experiment_beta: an integer, represents the number of times to conduct experiment beta
    Returns:
        obj: an integer, the maximum amount of electricity produced
    """
    metal_alpha = 3
    acid_alpha = 5
    electricity_alpha = 8
    
    metal_beta = 5
    acid_beta = 4
    electricity_beta = 10
    
    metal_available = 800
    acid_available = 750
    
    # Create a new model
    model = gp.Model("electricity_production")
    
    # Define decision variables
    x_alpha = model.addVar(vtype=GRB.INTEGER, name="x_alpha")
    x_beta = model.addVar(vtype=GRB.INTEGER, name="x_beta")
    
    # Set objective function
    model.setObjective(electricity_alpha * x_alpha + electricity_beta * x_beta, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(metal_alpha * x_alpha + metal_beta * x_beta <= metal_available)
    model.addConstr(acid_alpha * x_alpha + acid_beta * x_beta <= acid_available)
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal objective value
    obj = int(model.objVal)
    
    return obj