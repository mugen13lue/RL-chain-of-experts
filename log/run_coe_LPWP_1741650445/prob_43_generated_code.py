import gurobipy as gp
from gurobipy import GRB

def prob_43(Kebabs, Rice):
    """
    Args:
        Kebabs: an integer, the number of servings of Kebabs
        Rice: an integer, the number of servings of Rice
        
    Returns:
        obj: a float, the value of the objective function (minimized cost)
    """
    # Create a new model
    model = gp.Model("diet_optimization")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="Rice")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="Kebab")

    # Set objective function: Minimize Cost
    model.setObjective(3*x + 2*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(300*x + 200*y >= 2200, "Calories")
    model.addConstr(4.5*x + 4*y >= 30, "Protein")

    # Optimize model
    model.optimize()

    # Get the minimized cost
    obj = model.objVal

    return obj