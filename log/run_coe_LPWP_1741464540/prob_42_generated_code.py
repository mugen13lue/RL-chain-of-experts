import gurobipy as gp
from gurobipy import GRB

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
    # Create a new model
    m = gp.Model("berry_farm")

    # Decision variables
    x1 = m.addVar(name="x1")  # kg of raspberries harvested at the old farm
    x2 = m.addVar(name="x2")  # kg of blueberries harvested at the old farm
    x3 = m.addVar(name="x3")  # kg of strawberries harvested at the old farm
    y1 = m.addVar(name="y1")  # kg of raspberries harvested at the new farm
    y2 = m.addVar(name="y2")  # kg of blueberries harvested at the new farm
    y3 = m.addVar(name="y3")  # kg of strawberries harvested at the new farm

    # Objective function
    m.setObjective(old*(x1 + x2 + x3) + new_farm*(y1 + y2 + y3), GRB.MINIMIZE)

    # Constraints
    m.addConstr(x1 + y1 >= constraint1)
    m.addConstr(x2 + y2 >= constraint2)
    m.addConstr(x3 + y3 >= constraint3)
    m.addConstr(x1 >= constraint4)
    m.addConstr(x2 >= constraint5)
    m.addConstr(x3 >= constraint6)

    # Optimize the model
    m.optimize()

    # Return the objective value
    return m.objVal