import gurobipy as gp
from gurobipy import GRB

def prob_104(num_orange_juice, num_apple_juice):
    """
    Args:
        num_orange_juice: an integer (number of orange juice boxes)
        num_apple_juice: an integer (number of apple juice boxes)
    Returns:
        objective_value: an integer (total vitamin D intake)
    """
    model = gp.Model("juice_problem")
    
    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="orange_juice")
    y = model.addVar(vtype=GRB.INTEGER, name="apple_juice")
    
    # Constraints
    model.addConstr(10*x + 12*y <= 120, "vitamin_d_limit")  # Total Vitamin D intake limit
    model.addConstr(8*x + 6*y <= 300, "vitamin_c_limit")
    model.addConstr(x >= 3, "min_orange_juice")
    model.addConstr(y >= 3*x, "min_apple_juice")
    
    # Objective
    model.setObjective(10*x + 12*y, sense=GRB.MAXIMIZE)
    
    # Optimize model
    model.optimize()
    
    objective_value = int(model.objVal)
    
    return objective_value