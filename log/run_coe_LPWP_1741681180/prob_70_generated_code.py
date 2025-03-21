import gurobipy as gp
from gurobipy import GRB

def healthcare_scheduling():
    # Create a new model
    model = gp.Model("healthcare_scheduling")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="nurses")
    y = model.addVar(vtype=GRB.INTEGER, name="pharmacists")
    
    # Set objective function: minimize Z = 0
    model.setObjective(0, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(5*x + 7*y == 200, "hours_constraint")
    model.addConstr(250*x + 300*y <= 9000, "budget_constraint")
    model.addConstr(x >= 0, "non_negativity_nurses")
    model.addConstr(y >= 0, "non_negativity_pharmacists")
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal objective value
    obj = model.objVal
    
    return obj

# Call the function to solve the healthcare scheduling problem
optimal_workers = healthcare_scheduling()
print("Optimal number of nurses and pharmacists scheduled to minimize total workers:", optimal_workers)