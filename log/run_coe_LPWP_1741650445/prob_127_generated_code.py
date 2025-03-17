import gurobipy as gp
from gurobipy import GRB

def prob_127(cashews, almonds, _200, _20, _300, _25, twice, _15, _12, _10000, _800):
    """
    Args:
        cashews: an integer
        almonds: an integer
        _200: an integer
        _20: an integer
        _300: an integer
        _25: an integer
        twice: an integer
        _15: an integer
        _12: an integer
        _10000: an integer
        _800: an integer
    Returns:
        obj: an integer
    """
    # Create a new model
    model = gp.Model("diet_problem")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="x")  # Number of servings of almonds
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="y")  # Number of servings of cashews

    # Set objective function
    model.setObjective(15*x + 12*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(200*x + 300*y >= 10000, "Calories")
    model.addConstr(20*x + 25*y >= 800, "Protein")
    model.addConstr(x >= 2*y, "Almonds_Constraint")

    # Optimize the model
    model.optimize()

    # Return the objective value
    return model.objVal