from gurobipy import *

def prob_201(refrigerators, stoves):
    """
    Solve the problem to maximize profit.

    Args:
        refrigerators: an integer representing the number of refrigerators to sell.
        stoves: an integer representing the number of stoves to sell.
    Returns:
        profit: an integer representing the maximum profit achievable.
    """
    # Create a new model
    model = Model("Appliance_Profit_Maximization")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="refrigerators")
    y = model.addVar(vtype=GRB.INTEGER, name="stoves")

    # Set objective function: maximize profit
    model.setObjective(400*x + 260*y, GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(60*x + 45*y <= 20000, "mover_time_constraint")
    model.addConstr(20*x + 25*y <= 13000, "setup_time_constraint")

    # Optimize the model
    model.optimize()

    # Get the optimal solution
    profit = model.objVal

    return profit