import gurobipy as gp
from gurobipy import GRB

def prob_224(temperature_check, blood_test):
    """
    Args:
        temperature_check: an integer, the number of temperature checks
        blood_test: an integer, the number of blood tests
    Returns:
        obj: an integer, the number of patients seen
    """
    model = gp.Model("disease_testing")

    # Variables
    num_temperature_checks = model.addVar(vtype=GRB.INTEGER, name="num_temperature_checks")
    num_blood_tests = model.addVar(vtype=GRB.INTEGER, name="num_blood_tests")

    # Constraints
    model.addConstr(2*num_temperature_checks + 10*num_blood_tests <= 22000, "total_staff_minutes")
    model.addConstr(num_blood_tests >= 45, "minimum_blood_tests")
    model.addConstr(num_temperature_checks >= 5*num_blood_tests, "temperature_check_to_blood_test_ratio")

    # Objective
    model.setObjective(num_temperature_checks + num_blood_tests, sense=GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    return int(model.objVal)