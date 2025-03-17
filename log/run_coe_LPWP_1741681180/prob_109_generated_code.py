import gurobipy as gp
from gurobipy import GRB

def prob_109(automatic_machine, manual_machine):
    """
    Args:
        automatic_machine: an integer, representing the number of patients using the automatic machine
        manual_machine: an integer, representing the number of patients using the manual machine

    Returns:
        obj: an integer, representing the maximum number of patients whose blood pressure can be taken
    """
    # Create a new model
    model = gp.Model("clinic_optimization")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of patients processed by the automatic machine
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of patients processed by the manual machine

    # Set objective function: maximize z = x + y
    model.setObjective(x + y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(x <= 20, "constraint_1")
    model.addConstr(y >= 2*x, "constraint_2")
    model.addConstr(10*x + 15*y <= 20000, "constraint_3")

    # Optimize the model
    model.optimize()

    # Get the optimal objective value
    obj = int(model.objVal)

    return obj