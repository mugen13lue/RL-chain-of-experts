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
    model = gp.Model("carbon_dioxide_production")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")
    y = model.addVar(vtype=GRB.INTEGER, name="y")

    # Set objective function
    model.setObjective(15*x + 18*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(10*x + 15*y <= 300, "wood_constraint")
    model.addConstr(20*x + 12*y <= 300, "oxygen_constraint")
    model.addConstr(x >= 0, "non_negativity_x")
    model.addConstr(y >= 0, "non_negativity_y")

    # Optimize the model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj