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
    
    # Create a new model
    model = gp.Model("salesman_diet")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="ramen")
    y = model.addVar(vtype=GRB.INTEGER, name="fries")

    # Set objective function: minimize sodium intake
    model.setObjective(100*x + 75*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(400*x + 300*y >= 3000, "Calories")
    model.addConstr(20*x + 10*y >= 80, "Protein")
    model.addConstr(100*x + 75*y <= gp.GRB.INFINITY, "Sodium")
    model.addConstr(x <= 0.3*(x+y), "RamenPercentage")

    # Optimize model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj