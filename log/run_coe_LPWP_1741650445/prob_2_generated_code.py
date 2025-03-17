from gurobipy import *

def prob_2(senior_accountants, junior_accountants):
    """
    Minimize Wage Bill problem
    
    Args:
        senior_accountants: an integer, number of senior accountants
        junior_accountants: an integer, number of junior accountants
    
    Returns:
        obj: an integer, minimized wage bill
    """
    m = Model("Minimize_Wage_Bill")
    
    # Variables
    num_senior_accountants = m.addVar(vtype=GRB.INTEGER, name="num_senior_accountants")
    num_junior_accountants = m.addVar(vtype=GRB.INTEGER, name="num_junior_accountants")
    
    # Constraints
    m.addConstr(num_senior_accountants + num_junior_accountants >= 100, "Minimum_number_of_accountants")
    m.addConstr(num_senior_accountants >= 5, "Minimum_number_of_senior_accountants")
    m.addConstr(num_senior_accountants >= num_junior_accountants/3, "Ratio_of_senior_to_junior_accountants")
    m.addConstr(3000*num_senior_accountants + 1000*num_junior_accountants <= 150000, "Weekly_wage_bill_constraint")
    
    # Objective
    m.setObjective(3000*num_senior_accountants + 1000*num_junior_accountants, GRB.MINIMIZE)
    
    # Solve the model
    m.optimize()
    
    # Return the minimized wage bill
    obj = m.objVal
    return obj