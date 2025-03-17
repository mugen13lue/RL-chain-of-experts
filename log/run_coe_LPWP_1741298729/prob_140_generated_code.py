import gurobipy as gp
from gurobipy import GRB

def prob_140(Beam_1, Beam_2):
    """
    Args:
        Beam_1: an integer, the number of minutes of Beam 1 used
        Beam_2: an integer, the number of minutes of Beam 2 used

    Returns:
        obj: an integer, the minimized total radiation received by the pancreas
    """
    # Create a new model
    model = gp.Model("radiation_optimization")

    # Define decision variables
    minutes_beam_1 = model.addVar(lb=0, vtype=GRB.INTEGER, name="minutes_beam_1")  # minutes of Beam 1 used
    minutes_beam_2 = model.addVar(lb=0, vtype=GRB.INTEGER, name="minutes_beam_2")  # minutes of Beam 2 used

    # Set objective function
    model.setObjective(0.2*minutes_beam_1 + 0.1*minutes_beam_2, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(0.3*minutes_beam_1 + 0.2*minutes_beam_2 <= 4, "Pancreas_Dose")
    model.addConstr(0.6*minutes_beam_1 + 0.4*minutes_beam_2 >= 3, "Tumor_Dose")

    # Optimize the model
    model.optimize()

    # Get the minimized total radiation received by the pancreas
    obj = model.objVal

    return obj