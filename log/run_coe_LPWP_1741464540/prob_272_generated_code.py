import gurobipy as gp
from gurobipy import GRB

def prob_272(medication_patches, anti_biotic_creams):
    """
    Args:
        medication_patches: an integer, number of medication patches
        anti_biotic_creams: an integer, number of anti-biotic creams
    Returns:
        number_of_people: an integer, number of people that can be treated
    """
    model = gp.Model("hospital_problem")
    
    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="medication_patches")
    y = model.addVar(vtype=GRB.INTEGER, name="anti_biotic_creams")
    
    # Constraints
    model.addConstr(3*x + 5*y <= 400, "time_constraint")
    model.addConstr(5*x + 6*y <= 530, "material_constraint")
    model.addConstr(x + y <= 100, "batch_limit_constraint")
    model.addConstr(y >= 2*x, "min_anti_biotic_constraint")
    
    # Objective
    model.setObjective(3*x + 2*y, sense=GRB.MAXIMIZE)
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal solution
    number_of_people = int(model.objVal)
    
    return number_of_people