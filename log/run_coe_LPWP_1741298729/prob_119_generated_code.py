import gurobipy as gp
from gurobipy import GRB

def prob_119(electronic_thermometer, regular_thermometer, electronic_constraint, regular_constraint, time_constraint):
    """
    Args:
        electronic_thermometer: an integer representing the number of patients checked with the electronic thermometer
        regular_thermometer: an integer representing the number of patients checked with the regular thermometer
        electronic_constraint: an integer representing the required number of patients checked with the electronic thermometer
        regular_constraint: an integer representing the required number of patients checked with the regular thermometer
        time_constraint: an integer representing the maximum time the office is open
    Returns:
        number_of_patients: an integer representing the maximum number of patients whose temperature can be taken
    """
    model = gp.Model("patients_temperature")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")
    y = model.addVar(vtype=GRB.INTEGER, name="y")

    # Constraints
    model.addConstr(x >= 2*y)
    model.addConstr(y >= regular_constraint)
    model.addConstr(3*x + 2*y <= time_constraint)

    # Objective
    model.setObjective(x + y, sense=GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    number_of_patients = int(model.objVal)

    return number_of_patients