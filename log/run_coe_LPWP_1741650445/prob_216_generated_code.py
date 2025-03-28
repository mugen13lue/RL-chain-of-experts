import gurobipy as gp
from gurobipy import GRB

def prob_216(crepe_cakes, sponge_cakes, birthday_cakes):
    """
    Maximizes the profit of a small bakery by determining the number of each cake to make.

    Args:
        crepe_cakes: Integer, the number of crepe cakes to make.
        sponge_cakes: Integer, the number of sponge cakes to make.
        birthday_cakes: Integer, the number of birthday cakes to make.
        
    Returns:
        profit: Float, the maximum profit achievable.
    """
    # Create a new model
    model = gp.Model("cake_production")

    # Decision variables
    x1 = model.addVar(vtype=GRB.INTEGER, name="crepe_cakes")
    x2 = model.addVar(vtype=GRB.INTEGER, name="sponge_cakes")
    x3 = model.addVar(vtype=GRB.INTEGER, name="birthday_cakes")

    # Set objective
    model.setObjective(12*x1 + 10*x2 + 15*x3, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(400*x1 + 500*x2 + 450*x3 <= 20000, "batter_constraint")
    model.addConstr(200*x1 + 300*x2 + 350*x3 <= 14000, "milk_constraint")

    # Optimize model
    model.optimize()

    # Get the optimal solution
    profit = model.objVal

    return profit