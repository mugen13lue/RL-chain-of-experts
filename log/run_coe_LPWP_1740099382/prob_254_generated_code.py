import gurobipy as gp
from gurobipy import GRB

def prob_254(large_bags, tiny_bags):
    """
    Args:
        large_bags: an integer, the number of large bags of grain
        tiny_bags: an integer, the number of tiny bags of grain
    Returns:
        obj: an integer, the maximum amount of grain in weight
    """
    
    # Create a new model
    model = gp.Model("grain_transport")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of large bags
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of tiny bags

    # Set objective function
    model.setObjective(25*x + 6*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(4*x + 1.5*y <= 110, "energy_constraint")
    model.addConstr(x >= 2*y, "large_bags_constraint")
    model.addConstr(y >= 20, "tiny_bags_constraint")

    # Optimize model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj