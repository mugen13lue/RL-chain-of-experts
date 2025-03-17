from gurobipy import *

def prob_247(small_packets, jugs, _1000, _1250, three_times, _35, _65000):
    """
    Args:
        small_packets: an integer,
        jugs: an integer,
        _1000: an integer,
        _1250: an integer,
        three_times: a string,
        _35: an integer,
        _65000: an integer,
    Returns:
        total_number_of_units: an integer,
    """
    m = Model("jam_business")

    # Define variables
    x = m.addVar(vtype=GRB.INTEGER, name="small_packets")
    y = m.addVar(vtype=GRB.INTEGER, name="jugs")

    # Set objective
    m.setObjective(x + y, sense=GRB.MAXIMIZE)

    # Add constraints
    m.addConstr(x >= _35)
    m.addConstr(y >= 3*x)
    m.addConstr(_1000*x + _1250*y <= _65000)

    # Optimize model
    m.optimize()

    total_number_of_units = int(m.objVal)

    return total_number_of_units