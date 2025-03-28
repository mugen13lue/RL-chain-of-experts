import gurobipy as gp
from gurobipy import GRB

def maximize_people_supplied(vitamin_shots, pills, var1, var2, var3, var4, var5, var6):
    """
    Args:
        vitamin_shots: an integer, the number of batches of vitamin shots
        pills: an integer, the number of batches of vitamin pills
        var1: an integer, the number of units of vitamin C required for a batch of vitamin shots
        var2: an integer, the number of units of vitamin D required for a batch of vitamin shots
        var3: an integer, the number of units of vitamin C required for a batch of vitamin pills
        var4: an integer, the number of units of vitamin D required for a batch of vitamin pills
        var5: an integer, the maximum number of batches of vitamin shots
        var6: an integer, the number of people supplied by one batch of vitamin pills
    Returns:
        obj: an integer, the maximum number of people that can be supplied
    """
    m = gp.Model("vitamin_supply")

    # Define variables
    x = m.addVar(vtype=GRB.INTEGER, name="x")  # number of batches of vitamin shots
    y = m.addVar(vtype=GRB.INTEGER, name="y")  # number of batches of vitamin pills

    # Set objective
    m.setObjective(10*x + 7*y, sense=GRB.MAXIMIZE)

    # Add constraints
    m.addConstr(var1*x + var3*y <= var5, "vitamin_c_constraint")
    m.addConstr(var2*x + var4*y <= var6, "vitamin_d_constraint")
    m.addConstr(x <= vitamin_shots, "number_of_shots_constraint")
    m.addConstr(y >= x, "pills_more_than_shots_constraint")

    # Optimize model
    m.optimize()

    # Get the optimal objective value
    obj = m.objVal

    return obj