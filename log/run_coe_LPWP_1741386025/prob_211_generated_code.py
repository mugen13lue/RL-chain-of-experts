import gurobipy as gp
from gurobipy import GRB

def maximize_profit(laminate_planks, carpets):
    """
    Args:
        laminate_planks: an integer (number of laminate planks produced weekly)
        carpets: an integer (number of carpets produced weekly)

    Returns:
        obj: a float (maximum profit achieved)
    """
    obj = 0
    
    # Create a new model
    m = gp.Model("profit_maximization")
    
    # Define decision variables
    x = m.addVar(lb=0, vtype=GRB.INTEGER, name="laminate_planks")
    y = m.addVar(lb=0, vtype=GRB.INTEGER, name="carpets")
    
    # Set objective function
    m.setObjective(2.1*x + 3.3*y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    m.addConstr(x >= 15000, name="demand_laminate_planks")
    m.addConstr(y >= 5000, name="demand_carpets")
    m.addConstr(x + y >= 50000, name="shipping_contract")
    m.addConstr(x <= 40000, name="raw_material_laminate_planks")
    m.addConstr(y <= 20000, name="raw_material_carpets")
    
    # Optimize model
    m.optimize()
    
    if m.status == GRB.OPTIMAL:
        obj = m.objVal
    
    return obj