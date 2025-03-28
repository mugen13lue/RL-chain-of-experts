import gurobipy as gp
from gurobipy import GRB

def prob_111():
    # Create a new model
    model = gp.Model("diet_problem")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.CONTINUOUS, name="crab_cakes")
    y = model.addVar(vtype=GRB.CONTINUOUS, name="lobster_roll")
    
    # Set objective function
    model.setObjective(4*x + 6*y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(5*x + 8*y >= 80, "vitamin_A_constraint")
    model.addConstr(7*x + 4*y >= 100, "vitamin_C_constraint")
    model.addConstr(y <= 0.4*(x+y), "lobster_roll_limit_constraint")
    
    # Optimize model
    model.optimize()
    
    # Get the minimized unsaturated fat intake
    obj = model.objVal
    
    return obj