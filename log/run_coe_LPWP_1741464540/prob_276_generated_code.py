import gurobipy as gp
from gurobipy import GRB

def prob_276(spinach, soybeans):
    """
    Args:
        spinach: an integer, number of cups of spinach
        soybeans: an integer, number of cups of soybeans
    Returns:
        obj: an integer, the maximum caloric intake
    """
    
    # Create a new model
    model = gp.Model("senior_home_snacks")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="spinach")
    y = model.addVar(vtype=GRB.INTEGER, name="soybeans")

    # Set objective function
    model.setObjective(30*x + 100*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(100*x + 80*y >= 12000, "Fibre")
    model.addConstr(5*x + 12*y >= 300, "Iron")
    model.addConstr(x >= y, "Spinach_Soybeans")
    model.addConstr(x >= 0, "Non-negativity_x")
    model.addConstr(y >= 0, "Non-negativity_y")

    # Optimize the model
    model.optimize()

    # Get the maximum caloric intake
    obj = model.objVal

    return obj