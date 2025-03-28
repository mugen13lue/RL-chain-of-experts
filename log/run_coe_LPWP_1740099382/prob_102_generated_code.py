import gurobipy as gp
from gurobipy import GRB

def prob_102(constraint1, constraint2, constraint3, constraint4, constraint5, constraint6):
    """
    Args:
        constraint1: an integer, limit on total units of flour available
        constraint2: an integer, limit on total units of special liquid available
        constraint3: an integer, limit on total units of waste produced
        constraint4: an integer, limit on units of waste produced by beaker 1
        constraint5: an integer, limit on units of waste produced by beaker 2
        constraint6: an integer, limit on units of slime produced by beaker 1

    Returns:
        amount_of_slime: an integer, maximum amount of slime that can be produced
    """
    # Create a new model
    model = gp.Model("summer_camp")

    # Create variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="beaker_1")
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="beaker_2")

    # Set objective function
    model.setObjective(5*x + 3*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(4*x + 6*y <= constraint1, "flour_constraint")
    model.addConstr(6*x + 3*y <= constraint2, "special_liquid_constraint")
    model.addConstr(4*x + 2*y <= constraint3, "waste_constraint")
    model.addConstr(x <= constraint4, "waste_beaker_1_constraint")
    model.addConstr(y <= constraint5, "waste_beaker_2_constraint")
    model.addConstr(5*x <= constraint6, "slime_beaker_1_constraint")

    # Optimize model
    model.optimize()

    # Get the maximum amount of slime produced
    amount_of_slime = model.objVal

    return amount_of_slime