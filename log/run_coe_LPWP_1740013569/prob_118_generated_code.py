import gurobipy as gp
from gurobipy import GRB

def prob_118(vitamin_shots, pills, var1, var2, var3, var4, var5, var6):
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
    model = gp.Model("vitamin_supply")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of batches of vitamin shots
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of batches of vitamin pills

    # Set objective function
    model.setObjective(10*x + 7*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(var1*x + var3*y <= 1200, "Vitamin_C_constraint")
    model.addConstr(var2*x + var4*y <= 1500, "Vitamin_D_constraint")
    model.addConstr(x <= var5, "Number_of_shots_constraint")
    model.addConstr(y >= x, "Pills_must_be_more_than_shots_constraint")

    # Optimize the model
    model.optimize()

    # Get the optimal objective value
    obj = int(model.objVal)

    return obj