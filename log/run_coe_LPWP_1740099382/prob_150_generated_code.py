import gurobipy as gp
from gurobipy import GRB

def prob_150(small_bottles, large_bottles):
    """
    Args:
        small_bottles: an integer, the number of small bottles
        large_bottles: an integer, the number of large bottles
        
    Returns:
        amount_of_honey: an integer, the maximum amount of honey that can be transported
    """
    model = gp.Model("Honey_Transport")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="small_bottles")
    y = model.addVar(vtype=GRB.INTEGER, name="large_bottles")

    # Constraints
    model.addConstr(x <= 300, "Total small bottles")
    model.addConstr(y <= 100, "Total large bottles")
    model.addConstr(x >= 2*y, "Twice as many small bottles as large bottles")
    model.addConstr(x + y <= 200, "Total bottles")
    model.addConstr(y >= 50, "Minimum large bottles")

    # Objective
    model.setObjective(5*x + 20*y, sense=GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    amount_of_honey = int(model.objVal)

    return amount_of_honey