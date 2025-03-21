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
    x = m.addVar(lb=0, ub=40000, vtype=GRB.CONTINUOUS, name="laminate_planks")
    y = m.addVar(lb=0, ub=20000, vtype=GRB.CONTINUOUS, name="carpets")
    
    # Set objective function
    m.setObjective(2.1*x + 3.3*y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    m.addConstr(x + y >= 50000, "shipping_contract_constraint")
    m.addConstr(x >= 15000, "laminate_planks_demand_constraint")
    m.addConstr(y >= 5000, "carpets_demand_constraint")
    
    # Optimize model
    m.optimize()
    
    # Get the optimal objective value
    obj = m.objVal
    
    return obj