import gurobipy as gp
from gurobipy import GRB

def prob_277(mechanical, standard_keyboards):
    """
    Args:
        mechanical: an integer, the number of mechanical keyboards
        standard_keyboards: an integer, the number of standard keyboards

    Returns:
        obj: an integer, the maximum total number of keyboards manufactured
    """
    # Create a new model
    model = gp.Model("keyboard_manufacturing")

    # Define decision variables
    x = model.addVar(lb=30, vtype=GRB.INTEGER, name="standard_keyboards")
    y = model.addVar(vtype=GRB.INTEGER, name="mechanical_keyboards")

    # Set objective function
    model.setObjective(x + y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(2*x + 5*y <= 1000)
    model.addConstr(x + 2*y <= 250)

    # Optimize model
    model.optimize()

    # Get the optimal objective value
    obj = int(model.objVal)

    return obj