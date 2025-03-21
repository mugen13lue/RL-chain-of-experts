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

    # Set objective function: Minimize 3000x + 1000y
    model.setObjective(3000*x + 1000*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(x + y >= 100, "min_num_accountants")
    model.addConstr(x >= 5, "min_num_senior_accountants")
    model.addConstr(x >= (1/3)*y, "senior_to_junior_ratio")
    model.addConstr(3000*x + 1000*y <= 150000, "weekly_wage_bill_constraint")

    # Optimize the model
    model.optimize()

    # Get the minimized wage bill
    obj = model.objVal

    return obj