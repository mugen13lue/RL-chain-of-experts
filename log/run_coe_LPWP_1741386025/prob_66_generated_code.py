import gurobipy as gp
from gurobipy import GRB

def prob_66(almond_croissants, pistachio_croissants, butter_units, flour_units, production_time):
    """
    Args:
        almond_croissants: an integer representing the number of almond croissants
        pistachio_croissants: an integer representing the number of pistachio croissants
        butter_units: an integer representing the total units of butter used
        flour_units: an integer representing the total units of flour used
        production_time: an integer representing the total production time
        
    Returns:
        obj: an integer representing the objective value (total production time)
    """
    # Create a new model
    model = gp.Model("croissants_production")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="almond_croissants")
    y = model.addVar(vtype=GRB.INTEGER, name="pistachio_croissants")

    # Set objective function
    model.setObjective(12*x + 10*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(5*x + 3*y <= butter_units, "butter_constraint")
    model.addConstr(8*x + 6*y <= flour_units, "flour_constraint")
    model.addConstr(x >= 3*y, "almond_ratio_constraint")

    # Optimize model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj