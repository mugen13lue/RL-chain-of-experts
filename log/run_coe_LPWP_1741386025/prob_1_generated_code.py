import gurobipy as gp
from gurobipy import GRB

def prob_1(color_printers, bw_printers):
    """
    Args:
        color_printers: an integer representing the number of color printers
        bw_printers: an integer representing the number of black and white printers
    
    Returns:
        obj: an integer representing the optimal objective value (profit)
    """
    # Create a new model
    model = gp.Model("printer_production")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="color_printers")
    y = model.addVar(vtype=GRB.INTEGER, name="bw_printers")

    # Set objective function
    model.setObjective(200*x + 70*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(x <= 20)
    model.addConstr(y <= 30)
    model.addConstr(x + y <= 35)

    # Optimize the model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj