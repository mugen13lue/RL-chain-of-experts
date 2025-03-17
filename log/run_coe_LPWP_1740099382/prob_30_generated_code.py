from gurobipy import *

def prob_30(phones, laptops, labor_hours_phones, labor_hours_laptops, cost_sqft_phones, cost_sqft_laptops, revenue_sqft_phones, revenue_sqft_laptops):
    """
    Args:
        phones: an integer, representing the number of phones
        laptops: an integer, representing the number of laptops
        labor_hours_phones: an integer, representing the labor hours required for phones
        labor_hours_laptops: an integer, representing the labor hours required for laptops
        cost_sqft_phones: an integer, representing the cost per sq. foot for phone production
        cost_sqft_laptops: an integer, representing the cost per sq. foot for laptop production
        revenue_sqft_phones: an integer, representing the net revenue per sq. foot for phones
        revenue_sqft_laptops: an integer, representing the net revenue per sq. foot for laptops

    Returns:
        obj: an integer, the optimal revenue
    """
    m = Model("FactoryLayout")

    # Define variables
    x = m.addVar(vtype=GRB.CONTINUOUS, name="x")  # sq. feet allocated for phone production
    y = m.addVar(vtype=GRB.CONTINUOUS, name="y")  # sq. feet allocated for laptop production

    # Set objective
    m.setObjective(revenue_sqft_phones*x + revenue_sqft_laptops*y, sense=GRB.MAXIMIZE)

    # Add constraints
    m.addConstr(x + y <= 100, "SpaceConstraint")
    m.addConstr(labor_hours_phones*x + labor_hours_laptops*y <= 2000, "LaborConstraint")
    m.addConstr(cost_sqft_phones*x + cost_sqft_laptops*y <= 5000, "BudgetConstraint")
    m.addConstr(x >= 0, "NonNegativity_x")
    m.addConstr(y >= 0, "NonNegativity_y")

    # Optimize model
    m.optimize()

    return int(m.objVal)