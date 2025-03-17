import gurobipy as gp
from gurobipy import GRB

def prob_137(oranges, grapefruit):
    """
    Args:
        oranges: an integer, the number of oranges to eat
        grapefruit: an integer, the number of grapefruit to eat
    Returns:
        obj: an integer, the minimum sugar intake
    """
    model = gp.Model("diet_problem")

    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="oranges")
    y = model.addVar(vtype=GRB.INTEGER, name="grapefruit")

    # Objective function
    model.setObjective(5*x + 6*y, sense=GRB.MINIMIZE)

    # Constraints
    model.addConstr(5*x + 7*y >= 80, "vitamin_c_constraint")
    model.addConstr(3*x + 5*y >= 70, "vitamin_a_constraint")
    model.addConstr(x >= 2*y, "preference_constraint")

    # Solve the model
    model.optimize()

    # Get the optimal solution
    obj = model.objVal

    return obj