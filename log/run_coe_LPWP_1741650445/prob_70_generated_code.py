import gurobipy as gp
from gurobipy import GRB

def healthcare_scheduling():
    # Create a new model
    model = gp.Model("healthcare_scheduling")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="nurses")
    y = model.addVar(vtype=GRB.INTEGER, name="pharmacists")
    
    # Set objective function
    model.setObjective(x + y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(5*x + 7*y == 200, "hours_constraint")
    model.addConstr(250*x + 300*y <= 9000, "budget_constraint")
    
    # Optimize model
    model.optimize()
    
    # Get the optimal solution
    nurses = x.x
    pharmacists = y.x
    
    return nurses, pharmacists

# Call the function to get the optimal scheduling
nurses, pharmacists = healthcare_scheduling()
print("Number of nurses scheduled:", nurses)
print("Number of pharmacists scheduled:", pharmacists)