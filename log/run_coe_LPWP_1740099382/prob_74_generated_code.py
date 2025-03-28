import gurobipy as gp
from gurobipy import GRB

def prob_74(with_a_catalyst, without_a_catalyst):
    """
    Args:
        with_a_catalyst: an integer (number of process with a catalyst),
        without_a_catalyst: an integer (number of process without a catalyst),

    Returns:
        obj: an integer (amount of carbon dioxide produced),
    """
    # Create a new model
    m = gp.Model("carbon_dioxide_production")

    # Define decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="x")  # Number of processes with a catalyst
    y = m.addVar(vtype=GRB.INTEGER, name="y")  # Number of processes without a catalyst

    # Set objective function
    m.setObjective(15*x + 18*y, sense=GRB.MAXIMIZE)

    # Add constraints
    m.addConstr(10*x + 15*y <= 300, "wood_constraint")
    m.addConstr(20*x + 12*y <= 300, "oxygen_constraint")
    m.addConstr(x >= 0, "non_negativity_x")
    m.addConstr(y >= 0, "non_negativity_y")

    # Optimize model
    m.optimize()

    # Get the optimal objective value
    obj = m.objVal

    return obj