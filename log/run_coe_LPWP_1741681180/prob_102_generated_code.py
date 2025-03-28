from gurobipy import *

def prob_102(beaker_1, beaker_2, constraint1, constraint2, constraint3, constraint4, constraint5, constraint6):
    """
    Args:
        beaker_1: an integer, number of units of flour used by beaker 1
        beaker_2: an integer, number of units of flour used by beaker 2
        constraint1: an integer, limit on total units of flour available
        constraint2: an integer, limit on total units of special liquid available
        constraint3: an integer, limit on total units of waste produced
        constraint4: an integer, limit on units of waste produced by beaker 1
        constraint5: an integer, limit on units of waste produced by beaker 2
        constraint6: an integer, limit on units of slime produced by beaker 1

    Returns:
        amount_of_slime: an integer, maximum amount of slime that can be produced
    """
    m = Model("Slime Production")

    # Decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="x")
    y = m.addVar(vtype=GRB.INTEGER, name="y")

    # Objective function
    m.setObjective(constraint6 * x + 3 * y, GRB.MAXIMIZE)

    # Constraints
    m.addConstr(beaker_1 * x + beaker_2 * y <= constraint1, "flour_constraint")
    m.addConstr(6 * x + 3 * y <= constraint2, "special_liquid_constraint")
    m.addConstr(constraint4 * x + constraint5 * y <= constraint3, "waste_constraint")

    m.optimize()

    amount_of_slime = int(m.objVal)

    return amount_of_slime