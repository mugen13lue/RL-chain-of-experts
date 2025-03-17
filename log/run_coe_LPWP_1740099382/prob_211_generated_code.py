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
    obj = 0
    
    # Create a new model
    m = gp.Model("flooring_production")
    
    # Define decision variables
    x = m.addVar(lb=0, ub=40000, vtype=GRB.INTEGER, name="laminate_planks")
    y = m.addVar(lb=0, ub=20000, vtype=GRB.INTEGER, name="carpets")
    
    # Set objective function
    m.setObjective(2.1*x + 3.3*y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    m.addConstr(x + y >= 15000)
    m.addConstr(y >= 5000)
    m.addConstr(x + y >= 50000)
    
    # Optimize model
    m.optimize()
    
    if m.status == GRB.OPTIMAL:
        obj = m.objVal
    
    return obj