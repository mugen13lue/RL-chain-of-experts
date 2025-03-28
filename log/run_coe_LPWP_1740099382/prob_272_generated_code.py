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
    model = gp.Model("hospital_batches")

    # Decision variables
    num_medication_patches = model.addVar(vtype=GRB.INTEGER, name="num_medication_patches")
    num_antibiotic_creams = model.addVar(vtype=GRB.INTEGER, name="num_antibiotic_creams")

    # Constraints
    model.addConstr(3*num_medication_patches + 5*num_antibiotic_creams <= 400)
    model.addConstr(5*num_medication_patches + 6*num_antibiotic_creams <= 530)
    model.addConstr(num_medication_patches + num_antibiotic_creams <= 100)
    model.addConstr(num_antibiotic_creams >= 2*num_medication_patches)

    # Objective function
    model.setObjective(3*num_medication_patches + 2*num_antibiotic_creams, sense=GRB.MAXIMIZE)

    # Optimize the model
    model.optimize()

    number_of_people = 0
    if model.status == GRB.OPTIMAL:
        number_of_people = 3*num_medication_patches.x + 2*num_antibiotic_creams.x

    return number_of_people