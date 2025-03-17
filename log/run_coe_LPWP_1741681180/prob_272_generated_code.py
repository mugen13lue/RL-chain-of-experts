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
    model = gp.Model("hospital_treatment")

    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="medication_patches")
    y = model.addVar(vtype=GRB.INTEGER, name="anti_biotic_creams")

    # Constraints
    model.addConstr(3*x + 5*y <= 400)
    model.addConstr(5*x + 6*y <= 530)
    model.addConstr(y >= 2*x)
    model.addConstr(x + y <= 100)

    # Objective function
    model.setObjective(3*x + 2*y, sense=GRB.MAXIMIZE)

    # Optimize the model
    model.optimize()

    number_of_people = 0
    if model.status == GRB.OPTIMAL:
        number_of_people = model.objVal

    return int(number_of_people)