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
    # Create a new model
    model = gp.Model("hospital_pills")

    # Define variables
    x = model.addVar(vtype=GRB.INTEGER, name="prevention_pills")
    y = model.addVar(vtype=GRB.INTEGER, name="treatment_pills")

    # Set objective
    model.setObjective(y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(15*x + 25*y <= 10000, "budget_constraint")
    model.addConstr(x >= 2*y, "prevention_demand_constraint")
    model.addConstr(y >= 50, "treatment_demand_constraint")

    # Optimize model
    model.optimize()

    # Get the maximum number of patients treated
    obj = int(model.objVal)

    return obj