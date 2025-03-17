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
    model = gp.Model("swab_optimization")
    
    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="throat_swabs", lb=throat_swabs)
    y = model.addVar(vtype=GRB.INTEGER, name="nasal_swabs", lb=nasal_swabs)
    
    # Constraints
    model.addConstr(5*x + 3*y <= 20000, "time_constraint")
    model.addConstr(y >= 30, "min_nasal_swabs")
    model.addConstr(x >= 4*y, "throat_swabs_constraint")
    
    # Objective
    model.setObjective(x + y, sense=GRB.MAXIMIZE)
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal solution
    number_of_patients = int(model.objVal)
    
    return number_of_patients