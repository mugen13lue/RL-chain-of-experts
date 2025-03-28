import gurobipy as gp
from gurobipy import GRB

def prob_30(phones, laptops, var1, var2, var3, var4, var5, var6):
    """
    Args:
        phones: an integer, representing the number of phones
        laptops: an integer, representing the number of laptops
        var1: an integer, representing the labor hours required for phones
        var2: an integer, representing the labor hours required for laptops
        var3: an integer, representing the cost per sq. foot for phone production
        var4: an integer, representing the cost per sq. foot for laptop production
        var5: an integer, representing the net revenue per sq. foot for phones
        var6: an integer, representing the net revenue per sq. foot for laptops

    Returns:
        obj: an integer, the optimal revenue
    """
    # Create a new model
    model = gp.Model("factory_layout")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x")  # sq. feet allocated for phone production
    y = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="y")  # sq. feet allocated for laptop production

    # Set objective function
    model.setObjective(var5*x + var6*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(x + y <= 100, "space_constraint")
    model.addConstr(var1*x + var2*y <= 2000, "labor_constraint")
    model.addConstr(var3*x + var4*y <= 5000, "budget_constraint")

    # Optimize the model
    model.optimize()

    # Get the optimal revenue
    obj = model.objVal

    return obj