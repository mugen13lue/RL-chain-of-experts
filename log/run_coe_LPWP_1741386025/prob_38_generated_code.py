from gurobipy import *

def prob_38(A, B):
    """
    Args:
        A: an integer, number of cups of drink A
        B: an integer, number of cups of drink B
    Returns:
        obj: an integer, value of the objective function
    """
    # Create a new model
    model = Model("VitaminMix")

    # Define decision variables
    cups_A = model.addVar(lb=0, vtype=GRB.INTEGER, name="cups_A")
    cups_B = model.addVar(lb=0, vtype=GRB.INTEGER, name="cups_B")

    # Set objective function: minimize 4*cups_A + 12*cups_B (amount of Vitamin K)
    model.setObjective(4*cups_A + 12*cups_B, GRB.MINIMIZE)

    # Add constraints
    model.addConstr(8*cups_A + 15*cups_B >= 150, "VitaminA")
    model.addConstr(6*cups_A + 2*cups_B >= 300, "VitaminD")
    model.addConstr(10*cups_A + 20*cups_B <= 400, "VitaminE")

    # Optimize the model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj