from gurobipy import *

def prob_142(experiment_1, experiment_2, constraint_1, constraint_2, constraint_3, constraint_4, constraint_5, constraint_6, constraint_7, constraint_8):
    """
    Args:
        experiment_1: an integer, number of experiments of type 1
        experiment_2: an integer, number of experiments of type 2
        constraint_1: an integer, constraint on the availability of red liquid for experiment 1
        constraint_2: an integer, constraint on the availability of blue liquid for experiment 1
        constraint_3: an integer, constraint on the availability of red liquid for experiment 2
        constraint_4: an integer, constraint on the availability of blue liquid for experiment 2
        constraint_5: an integer, constraint on the production of smelly gas for experiment 1
        constraint_6: an integer, constraint on the production of smelly gas for experiment 2
        constraint_7: an integer, constraint on the maximum total production of smelly gas
        constraint_8: an integer, constraint on the maximum total production of green gas

    Returns:
        obj: an integer, the objective value (total amount of green gas produced)
        experiment_1: an integer, number of experiments of type 1
        experiment_2: an integer, number of experiments of type 2
    """
    m = Model("green_gas_production")

    # Decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="experiment_1")
    y = m.addVar(vtype=GRB.INTEGER, name="experiment_2")

    # Constraints
    m.addConstr(3*x + 5*y <= constraint_1, "red_liquid_constraint_exp1")
    m.addConstr(4*x + 3*y <= constraint_2, "blue_liquid_constraint_exp1")
    m.addConstr(5*x + 3*y <= constraint_3, "red_liquid_constraint_exp2")
    m.addConstr(3*x + 2*y <= constraint_4, "blue_liquid_constraint_exp2")
    m.addConstr(x + y <= constraint_5, "smelly_gas_constraint_exp1")
    m.addConstr(2*x + 2*y <= constraint_6, "smelly_gas_constraint_exp2")
    m.addConstr(x + 2*y <= constraint_7, "total_smelly_gas_constraint")
    m.addConstr(5*x + 6*y <= constraint_8, "total_green_gas_constraint")

    # Objective function
    m.setObjective(5*x + 6*y, GRB.MAXIMIZE)

    m.optimize()

    obj = m.objVal

    return obj, int(x.x), int(y.x)