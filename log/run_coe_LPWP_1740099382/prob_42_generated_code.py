from gurobipy import *

def prob_42(old, new_farm, constraint1, constraint2, constraint3, constraint4, constraint5, constraint6):
    """
    A berry farmer has two farms, an old and new farm, where he grows raspberries, blueberries, and strawberries.
    He has a contract to provide a local store with 10 kg of raspberries, 9 kg of blueberries, and 15 kg of strawberries.
    At his old farm, it costs $300 to operate per day and he can harvest and deliver 2 kg of raspberries,
    2 kg of blueberries, and 4 kg of strawberries in a day.
    At his new farm, it costs $200 to operate per day and he can harvest and deliver 4 kg of raspberries,
    1 kg of blueberries, and 2 kg of strawberries in a day.
    Formulate a LP to meet his contract while minimizing his cost.

    Args:
        old: An integer, the cost to operate at the old farm per day.
        new_farm: An integer, the cost to operate at the new farm per day.
        constraint1: An integer, the limit for the raspberries to be provided.
        constraint2: An integer, the limit for the blueberries to be provided.
        constraint3: An integer, the limit for the strawberries to be provided.
        constraint4: An integer, the weight of raspberries provided by the old farm per day.
        constraint5: An integer, the weight of blueberries provided by the old farm per day.
        constraint6: An integer, the weight of strawberries provided by the old farm per day.

    Returns:
        obj: An integer, the objective value (minimum cost) to meet the contract.
    """
    m = Model("berry_farm")

    # Variables
    x1 = m.addVar(vtype=GRB.CONTINUOUS, name="x1")
    x2 = m.addVar(vtype=GRB.CONTINUOUS, name="x2")

    # Constraints
    m.addConstr(2*x1 + 4*x2 >= constraint1, "Raspberries")
    m.addConstr(2*x1 + x2 >= constraint2, "Blueberries")
    m.addConstr(4*x1 + 2*x2 >= constraint3, "Strawberries")

    # Objective
    m.setObjective(old*x1 + new_farm*x2, GRB.MINIMIZE)

    m.optimize()

    return m.objVal