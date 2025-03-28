import gurobipy as gp
from gurobipy import GRB

def prob_246(LED_fixture, fluorescence_lamp):
    """
    Args:
        LED_fixture: an integer, the number of LED fixtures to be installed
        fluorescence_lamp: an integer, the number of fluorescence lamps to be installed

    Returns:
        obj: an integer, the total number of light changes
    """
    # Create a new model
    model = gp.Model("lighting_problem")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="LED_fixtures")
    y = model.addVar(vtype=GRB.INTEGER, name="fluorescence_lamps")

    # Set objective function
    model.setObjective(3*x + 4*y, GRB.MINIMIZE)

    # Add constraints
    model.addConstr(5*x + 8*y <= 2000, "electricity_constraint")
    model.addConstr(x + y >= 300, "min_fixtures_constraint")
    model.addConstr(y >= 0.3*(x + y), "min_percentage_constraint")

    # Optimize the model
    model.optimize()

    # Get the total number of light changes
    obj = model.objVal

    return obj