import gurobipy as gp
from gurobipy import GRB

def prob_169(camels, horses):
    """
    Args:
        camels: an integer indicating the number of camels
        horses: an integer indicating the number of horses
    Returns:
        obj: an integer, the minimal number of animals
    """
    obj = 1e9
    
    # Create a new model
    model = gp.Model("animal_delivery")
    
    # Define decision variables
    num_camels = model.addVar(vtype=GRB.INTEGER, name="num_camels")
    num_horses = model.addVar(vtype=GRB.INTEGER, name="num_horses")
    
    # Set objective function
    model.setObjective(num_camels + num_horses, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(50*num_camels + 60*num_horses >= 1000)
    model.addConstr(20*num_camels + 30*num_horses <= 450)
    model.addConstr(num_horses <= num_camels)
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal solution
    if model.status == GRB.OPTIMAL:
        obj = int(num_camels.x + num_horses.x)
    
    return obj