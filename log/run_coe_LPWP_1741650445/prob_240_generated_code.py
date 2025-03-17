import gurobipy as gp
from gurobipy import GRB

def prob_240(prevention, treatment):
    """
    Args:
        prevention: an integer, number of prevention pills to purchase
        treatment: an integer, number of treatment pills to purchase
    Returns:
        obj: an integer, maximum number of patients that can be treated
    """
    model = gp.Model("hospital_pills")

    # Decision variables
    num_prevention_pills = model.addVar(vtype=GRB.INTEGER, name="num_prevention_pills")
    num_treatment_pills = model.addVar(vtype=GRB.INTEGER, name="num_treatment_pills")

    # Set objective
    model.setObjective(num_treatment_pills, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(15*num_prevention_pills + 25*num_treatment_pills <= 10000, "budget_constraint")
    model.addConstr(num_prevention_pills >= 2*num_treatment_pills, "prevention_demand_constraint")
    model.addConstr(num_treatment_pills >= 50, "treatment_demand_constraint")

    # Optimize model
    model.optimize()

    # Get the maximum number of patients treated
    obj = int(model.objVal)

    return obj