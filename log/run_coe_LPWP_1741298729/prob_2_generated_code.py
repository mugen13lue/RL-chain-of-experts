import gurobipy as gp
from gurobipy import GRB

def prob_2(senior_accountants, junior_accountants):
    """
    Minimize Wage Bill problem
    
    Args:
        senior_accountants: an integer, number of senior accountants
        junior_accountants: an integer, number of junior accountants
    
    Returns:
        obj: an integer, minimized wage bill
    """
    # Create a new model
    model = gp.Model("minimize_wage_bill")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="senior_accountants")
    y = model.addVar(vtype=GRB.INTEGER, name="junior_accountants")
    
    # Set objective function: minimize total weekly wage bill
    model.setObjective(3000*x + 1000*y, GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(x + y >= 100)
    model.addConstr(x >= 5)
    model.addConstr(x >= y/3)
    model.addConstr(3000*x + 1000*y <= 150000)
    
    # Optimize the model
    model.optimize()
    
    # Get the minimized wage bill
    obj = model.objVal
    
    return obj