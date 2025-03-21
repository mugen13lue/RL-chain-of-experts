import gurobipy as gp
from gurobipy import GRB

def prob_276(spinach, soybeans):
    """
    Args:
        spinach: an integer, number of cups of spinach
        soybeans: an integer, number of cups of soybeans
    Returns:
        obj: an integer, the maximum caloric intake
    """
    model = gp.Model("caloric_intake")

    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="spinach")
    y = model.addVar(vtype=GRB.INTEGER, name="soybeans")

    # Objective function: maximize total caloric intake
    model.setObjective(30*x + 100*y, sense=GRB.MAXIMIZE)

    # Constraints
    model.addConstr(100*x + 80*y >= 12000, "fibre_constraint")
    model.addConstr(5*x + 12*y >= 300, "iron_constraint")
    model.addConstr(x > y, "spinach_soybeans_constraint")

    # Solve the model
    model.optimize()

    # Get the optimal objective value
    obj = int(model.objVal)

    return obj