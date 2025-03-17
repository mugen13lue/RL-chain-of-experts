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
    morphine_per_painkiller = 10
    digestive_medicine_per_painkiller = 3
    morphine_per_sleeping_pill = 6
    digestive_medicine_per_sleeping_pill = 5
    
    m = gp.Model("pharmacy_problem")
    
    # Decision variables
    x1 = m.addVar(vtype=GRB.INTEGER, name="painkillers")
    x2 = m.addVar(vtype=GRB.INTEGER, name="sleeping_pills")
    
    # Objective function
    m.setObjective(digestive_medicine_per_painkiller * x1 + digestive_medicine_per_sleeping_pill * x2, GRB.MINIMIZE)
    
    # Constraints
    m.addConstr(morphine_per_painkiller * x1 + morphine_per_sleeping_pill * x2 <= 3000)
    m.addConstr(x1 >= 50)
    m.addConstr(x2 >= 0.7 * (x1 + x2))
    
    m.optimize()
    
    amount_of_digestive_medicine = m.objVal
    
    return amount_of_digestive_medicine