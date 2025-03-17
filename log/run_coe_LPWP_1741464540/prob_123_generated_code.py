import gurobipy as gp
from gurobipy import GRB

def prob_123(painkillers, sleeping_pills):
    """
    Args:
        painkillers: an integer, representing the number of painkiller pills
        sleeping_pills: an integer, representing the number of sleeping pills
    Returns:
        amount_of_digestive_medicine: an integer, representing the total amount of digestive medicine needed  
    """
    model = gp.Model("pharmacy_problem")
    
    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="painkiller_pills")
    y = model.addVar(vtype=GRB.INTEGER, name="sleeping_pills")
    
    # Constraints
    model.addConstr(10*x + 6*y <= 3000, "morphine_constraint")
    model.addConstr(3*x + 5*y >= 0, "digestive_medicine_constraint")
    model.addConstr(x >= 50, "painkiller_pills_constraint")
    model.addConstr(y >= 0.7*(x + y), "sleeping_pills_constraint")
    
    # Objective
    model.setObjective(3*x + 5*y, GRB.MINIMIZE)
    
    # Optimize model
    model.optimize()
    
    # Return total amount of digestive medicine needed
    return int(model.objVal)