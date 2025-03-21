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
    
    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="gummies")
    y = model.addVar(vtype=GRB.INTEGER, name="pills")
    
    # Objective function: maximize zinc intake
    model.setObjective(4*x + 5*y, sense=GRB.MAXIMIZE)
    
    # Constraints
    model.addConstr(3*x + 2*y <= constraint1)  # Magnesium constraint
    model.addConstr(4*x + 5*y <= constraint2)  # Zinc constraint
    model.addConstr(y >= 10)  # Minimum number of pills
    model.addConstr(x >= 3*y)  # Preference for gummies
    model.addConstr(3*x + 2*y <= constraint3)  # Additional constraint
    model.addConstr(4*x + 5*y <= constraint4)  # Additional constraint
    model.addConstr(5*x + 3*y <= constraint5)  # Additional constraint
    
    # Optimize the model
    model.optimize()
    
    # Get the maximum zinc intake
    obj = model.objVal
    
    return obj