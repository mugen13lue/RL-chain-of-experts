import gurobipy as gp
from gurobipy import GRB

def prob_212(supplement_A, supplement_B, constraint1, constraint2, cost_per_supplement_A, cost_per_supplement_B):
    """
    Args:
        supplement_A: an integer, the quantity of supplement A
        supplement_B: an integer, the quantity of supplement B
        constraint1: an integer, the value of the first constraint
        constraint2: an integer, the value of the second constraint
        cost_per_supplement_A: an integer, the cost per pill of supplement A
        cost_per_supplement_B: an integer, the cost per pill of supplement B
    Returns:
        costs: an integer, the objective value (minimized costs)
    """
    
    # Create a new model
    model = gp.Model("supplement_problem")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")
    y = model.addVar(vtype=GRB.INTEGER, name="y")
    
    # Set objective function
    model.setObjective(cost_per_supplement_A * x + cost_per_supplement_B * y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(5*x + 4*y >= constraint1)
    model.addConstr(10*x + 15*y >= constraint2)
    
    # Optimize the model
    model.optimize()
    
    # Get the minimized costs
    costs = model.objVal
    
    return costs