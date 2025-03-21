import gurobipy as gp
from gurobipy import GRB

def prob_207(graph_paper, music_paper):
    """
    Args:
        graph_paper: an integer, number of reams of graph paper to produce
        music_paper: an integer, number of reams of music paper to produce
    Returns:
        objective_value: an integer, maximum profit
    """
    m = gp.Model("Forest_Paper")

    # Decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="graph_paper")
    y = m.addVar(vtype=GRB.INTEGER, name="music_paper")

    # Constraints
    m.addConstr(3*x + 1.5*y <= 350, "printing_machine_constraint")
    m.addConstr(5.5*x + 3*y <= 350, "scanning_machine_constraint")
    m.addConstr(x >= 0, "non_negativity_constraint_x")
    m.addConstr(y >= 0, "non_negativity_constraint_y")

    # Objective function
    m.setObjective(4*x + 2.5*y, GRB.MAXIMIZE)

    # Optimize model
    m.optimize()

    # Get the optimal objective value
    objective_value = m.objVal

    return objective_value