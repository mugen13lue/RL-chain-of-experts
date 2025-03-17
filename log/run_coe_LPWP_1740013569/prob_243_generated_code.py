import gurobipy as gp
from gurobipy import GRB

def prob_243(original_meal, experimental_meal):
    """
    Args:
        original_meal: an integer representing the number of original meals
        experimental_meal: an integer representing the number of experimental meals
    Returns:
        obj: an integer representing the objective value, i.e., the minimized cooking time
    """
    
    # Create a new model
    model = gp.Model("meal_optimization")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of original combos
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of experimental combos
    
    # Set objective function
    model.setObjective(10*x + 15*y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(20*x + 25*y <= 800, "food_waste_constraint")
    model.addConstr(45*x + 35*y <= 900, "wrapping_waste_constraint")
    
    # Optimize the model
    model.optimize()
    
    # Get the minimized cooking time
    obj = model.objVal
    
    return obj