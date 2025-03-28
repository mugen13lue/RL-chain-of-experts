import gurobipy as gp
from gurobipy import GRB

def prob_124(gummies, pills, constraint1, constraint2, constraint3, constraint4, constraint5):
    """
    Args:
        gummies: an integer, representing the number of gummies to eat
        pills: an integer, representing the number of pills to take
        constraint1: an integer, representing the constraint parameter 1
        constraint2: an integer, representing the constraint parameter 2
        constraint3: an integer, representing the constraint parameter 3
        constraint4: an integer, representing the constraint parameter 4
        constraint5: an integer, representing the constraint parameter 5
    Returns:
        obj: an integer, representing the maximum zinc intake
    """
    model = gp.Model("diet_problem")
    
    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="gummies")
    y = model.addVar(vtype=GRB.INTEGER, name="pills")
    
    # Constraints
    model.addConstr(3*x + 2*y <= constraint1)
    model.addConstr(4*x + 5*y <= constraint2)
    model.addConstr(y >= constraint3)
    model.addConstr(x >= constraint4*y)
    
    # Objective
    model.setObjective(4*x + 5*y, sense=GRB.MAXIMIZE)
    
    # Solve the model
    model.optimize()
    
    # Get the maximum zinc intake
    obj = model.objVal
    
    return obj