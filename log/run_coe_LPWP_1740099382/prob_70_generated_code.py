import gurobipy as gp
from gurobipy import GRB

def healthcare_scheduling(num_nurses, num_pharmacists, total_hours_needed, budget):
    # Create a new model
    model = gp.Model("healthcare_scheduling")
    
    # Define decision variables
    nurses = model.addVar(vtype=GRB.INTEGER, name="nurses")
    pharmacists = model.addVar(vtype=GRB.INTEGER, name="pharmacists")
    
    # Set objective function
    model.setObjective(nurses + pharmacists, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(5*nurses + 7*pharmacists == total_hours_needed, "total_hours_constraint")
    model.addConstr(250*nurses + 300*pharmacists <= budget, "budget_constraint")
    
    # Optimize model
    model.optimize()
    
    # Get the objective value
    obj = model.objVal
    
    return obj