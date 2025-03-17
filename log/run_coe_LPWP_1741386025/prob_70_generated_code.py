import gurobipy as gp
from gurobipy import GRB

def healthcare_scheduling():
    # Create a new model
    model = gp.Model("healthcare_scheduling")
    
    # Define decision variables
    nurses = model.addVar(vtype=GRB.INTEGER, name="nurses")
    pharmacists = model.addVar(vtype=GRB.INTEGER, name="pharmacists")
    
    # Set objective function
    model.setObjective(nurses + pharmacists, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(5*nurses + 7*pharmacists == 200, "total_hours_constraint")
    model.addConstr(250*nurses + 300*pharmacists <= 9000, "budget_constraint")
    
    # Optimize model
    model.optimize()
    
    # Get the optimal solution
    nurses_scheduled = nurses.x
    pharmacists_scheduled = pharmacists.x
    
    return nurses_scheduled, pharmacists_scheduled