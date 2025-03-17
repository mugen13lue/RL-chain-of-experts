import gurobipy as gp
from gurobipy import GRB

def prob_109():
    """
    Returns:
        obj: an integer, representing the maximum number of patients whose blood pressure can be taken
    """
    
    # Create a new model
    model = gp.Model("patient_blood_pressure")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of patients processed by the automatic machine
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of patients processed by the manual machine

    # Set objective function
    model.setObjective(x + y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(x <= 20, "constraint_1")
    model.addConstr(y >= 2*x, "constraint_2")
    model.addConstr(10*x + 15*y <= 20000, "constraint_3")

    # Optimize the model
    model.optimize()

    # Get the maximum number of patients whose blood pressure can be taken
    obj = int(model.objVal)

    return obj