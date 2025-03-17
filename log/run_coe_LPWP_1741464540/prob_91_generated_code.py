import gurobipy as gp
from gurobipy import GRB

def prob_91(A, B, _30, _100, _50, _120):
    """
    Args:
        A: an integer (not used)
        B: an integer (not used)
        _30: an integer (not used)
        _100: an integer (not used)
        _50: an integer (not used)
        _120: an integer (not used)
    Returns:
        obj: an integer
    """
    # Create a new model
    model = gp.Model("machine_allocation")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="x")  # Number of machines of type A
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="y")  # Number of machines of type B

    # Set objective function: minimize total number of machines
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(30*x + 50*y >= 1000, "Production_Constraint")
    model.addConstr(100*x + 120*y <= 3000, "Electricity_Constraint")
    model.addConstr(y <= 0.3*(x + y), "Machine_B_Constraint")
    model.addConstr(x >= 5, "Machine_A_Constraint")

    # Optimize the model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj