from gurobipy import *

def prob_41(hardwood, vinyl_planks):
    """
    Args:
        hardwood: an integer, the quantity of hardwood flooring produced weekly
        vinyl_planks: an integer, the quantity of vinyl planks produced weekly
    Returns:
        profit: a float, the maximum profit that can be achieved
    """
    m = Model()

    # Define variables
    x = m.addVar(lb=0, ub=50000, vtype=GRB.CONTINUOUS, name="hardwood")
    y = m.addVar(lb=0, ub=30000, vtype=GRB.CONTINUOUS, name="vinyl_planks")

    # Set objective
    m.setObjective(2.5*x + 3*y, sense=GRB.MAXIMIZE)

    # Add constraints
    m.addConstr(x >= 20000, "Demand_constraint_hardwood")
    m.addConstr(y >= 10000, "Demand_constraint_vinyl")
    m.addConstr(x + y >= 60000, "Shipping_contract_constraint")
    m.addConstr(x <= 50000, "Production_limit_constraint_hardwood")
    m.addConstr(y <= 30000, "Production_limit_constraint_vinyl")

    # Optimize model
    m.optimize()

    return m.objVal