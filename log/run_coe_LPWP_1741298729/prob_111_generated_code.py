import gurobipy as gp
from gurobipy import GRB

def prob_111():
    # Create a new model
    model = gp.Model("diet_problem")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="crab_cakes")
    y = model.addVar(vtype=GRB.INTEGER, name="lobster_roll")
    
    # Set objective function
    model.setObjective(4*x + 6*y, GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(5*x + 8*y >= 80, "vitamin_A")
    model.addConstr(7*x + 4*y >= 100, "vitamin_C")
    model.addConstr(y <= 0.4*(x + y), "lobster_roll_limit")
    
    # Optimize model
    model.optimize()
    
    # Get the minimized unsaturated fat intake
    obj = model.objVal
    
    return obj