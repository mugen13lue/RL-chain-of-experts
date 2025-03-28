import gurobipy as gp
from gurobipy import GRB

def prob_101(alpha, omega):
    """
    Args:
        alpha: an integer representing the number of alpha brand drinks
        omega: an integer representing the number of omega brand drinks
    Returns:
        obj: an integer representing the objective value (minimized sugar intake)
    """
    
    # Create a new model
    model = gp.Model("diet_problem")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="alpha_drinks")
    y = model.addVar(vtype=GRB.INTEGER, name="omega_drinks")
    
    # Set objective: Minimize sugar intake
    model.setObjective(20*x + 15*y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(30*x + 20*y >= 100, "protein_constraint")
    model.addConstr(350*x + 300*y >= 2000, "calories_constraint")
    model.addConstr(y <= 0.35*(x + y), "omega_limit_constraint")
    
    # Optimize the model
    model.optimize()
    
    # Get the objective value
    obj = model.objVal
    
    return obj