import gurobipy as gp
from gurobipy import GRB

def prob_104(orange_juice, apple_juice):
    """
    Args:
        orange_juice: an integer (number of orange juice boxes)
        apple_juice: an integer (number of apple juice boxes)
    Returns:
        objective_value: an integer (total vitamin D intake)
    """
    
    # Constants for vitamin content in each juice box
    vitamin_d_orange = 10
    vitamin_c_orange = 8
    vitamin_d_apple = 12
    vitamin_c_apple = 6
    
    # Constraints
    min_orange_juice = 3
    min_apple_juice = 3
    max_vitamin_c = 300
    
    # Initialize model
    model = gp.Model("juice_problem")
    
    # Decision variables
    orange = model.addVar(vtype=GRB.INTEGER, name="orange")
    apple = model.addVar(vtype=GRB.INTEGER, name="apple")
    
    # Objective function
    model.setObjective(vitamin_d_orange * orange + vitamin_d_apple * apple, sense=GRB.MAXIMIZE)
    
    # Constraints
    model.addConstr(orange >= min_orange_juice)
    model.addConstr(apple >= min_apple_juice)
    model.addConstr(vitamin_c_orange * orange + vitamin_c_apple * apple <= max_vitamin_c)
    model.addConstr(apple >= 3 * orange)
    
    # Optimize model
    model.optimize()
    
    # Get objective value
    objective_value = int(model.objVal)
    
    return objective_value