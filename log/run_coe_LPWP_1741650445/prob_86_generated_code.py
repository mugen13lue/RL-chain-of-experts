from gurobipy import *

def prob_86(mocha_coffee_powder, mocha_milk, regular_coffee_powder, regular_milk, mocha_time, regular_time,
            mocha_regular_ratio, coffee_powder_limit, milk_limit):
    """
    Args:
        mocha_coffee_powder: an integer, the units of coffee powder required for each mocha.
        mocha_milk: an integer, the units of milk required for each mocha.
        regular_coffee_powder: an integer, the units of coffee powder required for each regular coffee.
        regular_milk: an integer, the units of milk required for each regular coffee.
        mocha_time: an integer, the time required to make a mocha in minutes.
        regular_time: an integer, the time required to make a regular coffee in minutes.
        mocha_regular_ratio: an integer, the minimum ratio between mochas and regular coffees to be made.
        coffee_powder_limit: an integer, the maximum units of coffee powder available.
        milk_limit: an integer, the maximum units of milk available.

    Returns:
        obj: an integer, the minimum total production time.
    """
    model = Model("coffee_shop")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="mochas")
    y = model.addVar(vtype=GRB.INTEGER, name="regular_coffees")

    # Constraints
    model.addConstr(mocha_coffee_powder * x + regular_coffee_powder * y <= coffee_powder_limit, "coffee_powder")
    model.addConstr(mocha_milk * x + regular_milk * y <= milk_limit, "milk")
    model.addConstr(x >= mocha_regular_ratio * y, "minimum_mochas")

    # Objective
    model.setObjective(mocha_time * x + regular_time * y, GRB.MINIMIZE)

    # Solve
    model.optimize()

    return int(model.objVal)