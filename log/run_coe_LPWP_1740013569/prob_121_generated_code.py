import gurobipy as gp
from gurobipy import GRB

def prob_121(ramen, fries):
    """
    Args:
        ramen: an integer, the number of packs of ramen
        fries: an integer, the number of packs of fries
    Returns:
        obj: an integer, the value of the objective function
    """
    obj = 0

    # Create a new model
    m = gp.Model("salesman_diet")

    # Define decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="ramen")
    y = m.addVar(vtype=GRB.INTEGER, name="fries")

    # Set objective function: minimize sodium intake
    m.setObjective(100*x + 75*y, sense=GRB.MINIMIZE)

    # Add constraints
    m.addConstr(400*x + 300*y >= 3000, "calories_constraint")
    m.addConstr(20*x + 10*y >= 80, "protein_constraint")
    m.addConstr(100*x + 75*y <= 2000, "sodium_constraint")  # Assuming maximum sodium intake of 2000 mg
    m.addConstr(x <= 0.3*(x+y), "ramen_percentage_constraint")

    # Optimize model
    m.optimize()

    # Get the optimal objective value
    obj = m.objVal

    return obj