import gurobipy as gp
from gurobipy import GRB

def prob_115():
    """
    Returns:
        x: an integer, the number of units of fertilizer to be added
        y: an integer, the number of units of seeds to be added
    """
    
    # Create a new model
    model = gp.Model("lawn_optimization")
    
    # Define decision variables
    x = model.addVar(lb=50, ub=300, vtype=GRB.INTEGER, name="fertilizer")
    y = model.addVar(lb=0, ub=150, vtype=GRB.INTEGER, name="seeds")
    
    # Set objective function
    model.setObjective(0.5*x + 1.5*y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(x + y <= 300, "total_units_constraint")
    model.addConstr(x <= 2*y, "fertilizer_to_seeds_ratio_constraint")
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal values of x and y
    x = round(x.x)
    y = round(y.x)
    
    return x, y

# Get the optimal values of x and y
x_opt, y_opt = prob_115()
print(f"Optimal number of units of fertilizer: {x_opt}")
print(f"Optimal number of units of seeds: {y_opt}")