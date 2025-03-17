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
    x1 = m.addVar(vtype=GRB.CONTINUOUS, name="x1")  # Raspberries from old farm
    x2 = m.addVar(vtype=GRB.CONTINUOUS, name="x2")  # Blueberries from old farm
    x3 = m.addVar(vtype=GRB.CONTINUOUS, name="x3")  # Strawberries from old farm
    y1 = m.addVar(vtype=GRB.CONTINUOUS, name="y1")  # Raspberries from new farm
    y2 = m.addVar(vtype=GRB.CONTINUOUS, name="y2")  # Blueberries from new farm
    y3 = m.addVar(vtype=GRB.CONTINUOUS, name="y3")  # Strawberries from new farm

    # Objective function: minimize cost
    m.setObjective(old * (x1 + x2 + x3) + new_farm * (y1 + y2 + y3), GRB.MINIMIZE)

    # Constraints
    m.addConstr(x1 + y1 == constraint1)  # Raspberries constraint
    m.addConstr(x2 + y2 == constraint2)  # Blueberries constraint
    m.addConstr(x3 + y3 == constraint3)  # Strawberries constraint
    m.addConstr(2*x1 + 4*y1 >= constraint4)  # Raspberries weight constraint
    m.addConstr(2*x2 + y2 >= constraint5)  # Blueberries weight constraint
    m.addConstr(4*x3 + 2*y3 >= constraint6)  # Strawberries weight constraint

    # Optimize the model
    m.optimize()

    # Return the objective value
    return m.objVal