from gurobipy import *

def prob_111(crab_cakes, lobster_roll, constraint1, constraint2, constraint3, constraint4, constraint5, constraint6):
    """
    Args:
        crab_cakes: an integer, representing the number of crab cakes to eat
        lobster_roll: an integer, representing the number of lobster rolls to eat
        constraint1: an integer, representing the first constraint threshold
        constraint2: an integer, representing the second constraint threshold
        constraint3: a float, representing the third constraint threshold
        constraint4: an integer, representing the fourth constraint threshold
        constraint5: an integer, representing the fifth constraint threshold
        constraint6: an integer, representing the sixth constraint threshold
    Returns:
        obj: an integer, representing the minimized unsaturated fat intake
    """
    m = Model("diet_problem")

    # Variables
    x = m.addVar(vtype=GRB.CONTINUOUS, name="crab_cakes")
    y = m.addVar(vtype=GRB.CONTINUOUS, name="lobster_roll")

    # Constraints
    m.addConstr(5*x + 8*y >= constraint1)
    m.addConstr(7*x + 4*y >= constraint2)
    m.addConstr(y <= 0.4*(x + y))
    m.addConstr(x >= constraint4)
    m.addConstr(y >= constraint5)

    # Objective
    m.setObjective(4*x + 6*y, GRB.MINIMIZE)

    m.optimize()

    return m.objVal