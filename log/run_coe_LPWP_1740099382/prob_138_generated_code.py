from gurobipy import *

def prob_138(medicine_A, medicine_B):
    """
    Args:
        medicine_A: number of doses for medicine A (integer)
        medicine_B: number of doses for medicine B (integer)
    Returns:
        obj: maximum number of people that can be treated (integer)
    """
    m = Model()

    # Variables
    x = m.addVar(vtype=GRB.INTEGER, name="x")
    y = m.addVar(vtype=GRB.INTEGER, name="y")

    # Constraints
    m.addConstr(30*x + 40*y <= 300, "imported_material_constraint")
    m.addConstr(50*x + 30*y <= 400, "mRNA_constraint")
    m.addConstr(x <= 5, "max_doses_A_constraint")
    m.addConstr(y >= x, "doses_B_greater_than_A_constraint")
    m.addConstr(x == medicine_A, "doses_A_input_constraint")
    m.addConstr(y == medicine_B, "doses_B_input_constraint")

    # Objective
    m.setObjective(12*x + 8*y, GRB.MAXIMIZE)

    m.optimize()

    return int(m.objVal)