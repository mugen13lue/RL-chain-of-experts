import gurobipy as gp
from gurobipy import GRB

def prob_129():
    model = gp.Model("Clinic Swab Optimization")
    
    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="throat_swabs")
    y = model.addVar(vtype=GRB.INTEGER, name="nasal_swabs")
    
    # Set objective
    model.setObjective(x, sense=GRB.MAXIMIZE)
    
    # Constraints
    model.addConstr(5*x + 3*y <= 20000, "time_constraint")
    model.addConstr(y >= 30, "min_nasal_swabs")
    model.addConstr(x >= 4*y, "throat_swabs_constraint")
    
    # Optimize model
    model.optimize()
    
    # Get the optimal number of throat swabs
    optimal_throat_swabs = model.getAttr('X', x)
    
    # Calculate the total number of patients seen
    total_patients = optimal_throat_swabs + 30
    
    return int(total_patients)