import gurobipy as gp
from gurobipy import GRB

def prob_223(Pi_TV, Beta_Video, Gamma_Live):
    """
    Args:
        Pi_TV: an integer, representing the number of commercials to run on Pi TV
        Beta_Video: an integer, representing the number of commercials to run on Beta Video
        Gamma_Live: an integer, representing the number of commercials to run on Gamma Live
    Returns:
        obj: an integer, representing the maximum audience
    """
    m = gp.Model("commercial_optimization")

    # Decision variables
    x1 = m.addVar(vtype=GRB.INTEGER, name="x1")
    x2 = m.addVar(vtype=GRB.INTEGER, name="x2")
    x3 = m.addVar(vtype=GRB.INTEGER, name="x3")

    # Constraints
    m.addConstr(x1 + x2 + x3 <= 8, "beta_video_limit")
    m.addConstr(x3 <= (1/3)*(x1 + x2 + x3), "gamma_live_limit")
    m.addConstr(x1 >= 0.2*(x1 + x2 + x3), "pi_tv_min")
    m.addConstr(1200*x1 + 2000*x2 + 4000*x3 <= 20000, "budget_constraint")

    # Objective
    m.setObjective(2000*x1 + 5000*x2 + 9000*x3, GRB.MAXIMIZE)

    # Optimize model
    m.optimize()

    # Return maximum audience
    return int(m.objVal)