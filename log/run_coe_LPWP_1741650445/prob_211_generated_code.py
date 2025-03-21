import gurobipy as gp
from gurobipy import GRB

def prob_211(laminate_planks, carpets):
    """
    Args:
        laminate_planks: an integer (number of laminate planks produced weekly)
        carpets: an integer (number of carpets produced weekly)

    Returns:
        obj: a float (maximum profit achieved)
    """
    # Create a new model
    model = gp.Model("profit_maximization")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="laminate_planks")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="carpets")

    # Set objective function
    model.setObjective(2.1*x + 3.3*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(x >= 15000, name="demand_laminate_planks")
    model.addConstr(y >= 5000, name="demand_carpets")
    model.addConstr(x + y >= 50000, name="shipping_contract")
    model.addConstr(x <= 40000, name="raw_material_laminate_planks")
    model.addConstr(y <= 20000, name="raw_material_carpets")

    # Optimize the model
    model.optimize()

    # Get the maximum profit achieved
    obj = model.objVal

    return obj