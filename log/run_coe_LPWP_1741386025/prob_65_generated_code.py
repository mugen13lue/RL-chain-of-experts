import gurobipy as gp
from gurobipy import GRB

def prob_65(small_oil_well, large_oil_well):
    """
    Args:
        small_oil_well: an integer, number of acres to be used for small oil wells
        large_oil_well: an integer, number of acres to be used for large oil wells

    Returns:
        Total_Production_of_Oil: an integer, total production of oil
    """
    # Create a new model
    model = gp.Model("oil_production")

    # Decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="small_oil_well_acres")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="large_oil_well_acres")

    # Set objective
    model.setObjective(2*x + 5*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(2*x + 5*y <= 300, "production_constraint")
    model.addConstr(5*x + 10*y <= 2500, "drill_bits_constraint")
    model.addConstr(10*x + 20*y <= 4500, "pollution_constraint")

    # Optimize model
    model.optimize()

    return int(model.objVal)  # Return the total production of oil as an integer