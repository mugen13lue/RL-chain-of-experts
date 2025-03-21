import gurobipy as gp
from gurobipy import GRB

def prob_286(wine, kombucha, _3, _8, _5, _7, _7000, _9000, _20_percent):
    """
    Args:
        wine: an integer representing the number of wine units
        kombucha: an integer representing the number of kombucha units
        _3: an integer representing the value 3
        _8: an integer representing the value 8
        _5: an integer representing the value 5
        _7: an integer representing the value 7
        _7000: an integer representing the value 7000
        _9000: an integer representing the value 9000
        _20_percent: an integer representing the value of 20% of the total units

    Returns:
        obj: an integer representing the objective value
    """
    # Create a new model
    model = gp.Model("brewery_problem")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="wine")
    y = model.addVar(vtype=GRB.INTEGER, name="kombucha")

    # Set objective function
    model.setObjective(_3*x + _5*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(_3*x + _5*y <= _9000, "Fruit")
    model.addConstr(_8*x <= _7000, "Water")
    model.addConstr(_7*y <= _9000, "Tea")
    model.addConstr(x >= y, "Wine_Kombucha_Ratio")
    model.addConstr(y >= _20_percent*x, "Kombucha_Minimum")

    # Optimize the model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj