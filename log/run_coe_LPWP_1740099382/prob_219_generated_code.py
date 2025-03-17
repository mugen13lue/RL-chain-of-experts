import gurobipy as gp
from gurobipy import GRB

def prob_219(math_workbooks, english_workbooks):
    """
    Args:
        math_workbooks: an integer, representing the number of math workbooks to make
        english_workbooks: an integer, representing the number of English workbooks to make

    Returns:
        obj: an integer, representing the objective value (profit)
    """
    
    # Create a new model
    model = gp.Model("workbook_production")
    
    # Define decision variables
    x = model.addVar(lb=40, ub=140, vtype=GRB.INTEGER, name="math_workbooks")
    y = model.addVar(lb=60, ub=170, vtype=GRB.INTEGER, name="english_workbooks")
    
    # Set objective function
    model.setObjective(15*x + 17*y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(x + y >= 200, "total_workbooks")
    
    # Optimize the model
    model.optimize()
    
    # Get the objective value
    obj = model.objVal
    
    return obj