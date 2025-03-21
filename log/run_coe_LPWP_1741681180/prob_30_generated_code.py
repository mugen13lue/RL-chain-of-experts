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
    x1 = model.addVar(vtype=GRB.INTEGER, name="phones_space")
    x2 = model.addVar(vtype=GRB.INTEGER, name="laptops_space")

    # Set objective function
    model.setObjective(var5*x1 + var6*x2, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(var1*x1 + var2*x2 <= 2000, "labor_constraint")
    model.addConstr(var3*x1 + var4*x2 <= 5000, "cost_constraint")
    model.addConstr(x1 + x2 <= 100, "space_constraint")

    # Optimize model
    model.optimize()

    # Get the optimal revenue
    obj = model.objVal

    return obj