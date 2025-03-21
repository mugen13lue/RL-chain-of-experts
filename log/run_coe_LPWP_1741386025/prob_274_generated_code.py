import gurobipy as gp
from gurobipy import GRB

def prob_274(first_dose, second_dose):
    """
    Args:
        first_dose: an integer, represents the number of first-dose vaccines to be made
        second_dose: an integer, represents the number of second-dose vaccines to be made
    Returns:
        obj: an integer, represents the minimized amount of gelatine used
    """
    model = gp.Model("vaccine_production")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")
    y = model.addVar(vtype=GRB.INTEGER, name="y")

    # Constraints
    model.addConstr(30*x + 65*y <= 35000, "antibiotics")
    model.addConstr(20*x + 60*y <= 20000, "gelatine")  # Assuming total gelatine available is 20,000 mg
    model.addConstr(x >= y, "first_dose_requirement")
    model.addConstr(y >= 40, "second_dose_minimum")

    # Objective
    model.setObjective(20*x + 60*y, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    return int(model.objVal)