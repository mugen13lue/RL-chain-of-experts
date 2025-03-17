import gurobipy as gp
from gurobipy import GRB

def prob_247(_35, _65000, _1000, _1250, three_times):
    """
    Args:
        _35: an integer, at least 35 sets of small packets should be filled
        _65000: an integer, total amount of jam available in ml
        _1000: an integer, ml of jam in a set of small packets
        _1250: an integer, ml of jam in a jug
        three_times: an integer, at least three times as many jugs must be used than sets of small packets
    Returns:
        total_number_of_units: an integer, total number of units (sets of small packets and jugs) to maximize sales
    """
    
    # Create a new model
    model = gp.Model("jam_business")

    # Define decision variables
    x = model.addVar(lb=_35, vtype=GRB.INTEGER, name="small_packets")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="jugs")

    # Set objective function
    model.setObjective(x + y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(x * _1000 + y * _1250 <= _65000, "jam_constraint")
    model.addConstr(y >= three_times * x, "jugs_constraint")

    # Optimize model
    model.optimize()

    total_number_of_units = int(model.objVal)

    return total_number_of_units