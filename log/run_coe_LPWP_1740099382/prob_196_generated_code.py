import gurobipy as gp
from gurobipy import GRB

def prob_196(large_ships, small_ships):
    """
    Args:
        large_ships: an integer, number of large ships
        small_ships: an integer, number of small ships
    Returns:
        objective_value: an integer, the objective value
    """
    model = gp.Model("shipping_problem")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")
    y = model.addVar(vtype=GRB.INTEGER, name="y")

    # Constraints
    model.addConstr(x <= y, "constraint1")
    model.addConstr(500*x + 200*y >= 3000, "constraint2")
    model.addConstr(x >= 0, "constraint3")
    model.addConstr(y >= 0, "constraint4")

    # Objective
    model.setObjective(x + y, GRB.MINIMIZE)

    # Solve the model
    model.optimize()

    objective_value = int(model.objVal)

    return objective_value