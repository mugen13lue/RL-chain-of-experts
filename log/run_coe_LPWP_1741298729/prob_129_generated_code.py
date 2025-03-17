import gurobipy as gp
from gurobipy import GRB

def prob_129(throat_swabs, nasal_swabs):
    """
    Args:
        throat_swabs: an integer, the number of throat swabs
        nasal_swabs: an integer, the number of nasal swabs
        
    Returns:
        number_of_patients: an integer, the number of patients
    """
    model = gp.Model("clinic_swabs")
    
    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="throat_swabs")
    y = model.addVar(vtype=GRB.INTEGER, name="nasal_swabs")
    
    # Constraints
    model.addConstr(5*x + 3*y <= 20000)
    model.addConstr(y >= 30)
    model.addConstr(x >= 4*y)
    
    # Objective
    model.setObjective(x + y, sense=GRB.MAXIMIZE)
    
    # Optimize the model
    model.optimize()
    
    # Return the optimal number of patients
    return int(model.objVal)