import gurobipy as gp
from gurobipy import GRB

def prob_231(throwing_games, climbing_games, constraint_1, constraint_2, constraint_3):
    """
    Args:
        throwing_games: an integer, representing the number of throwing games
        climbing_games: an integer, representing the number of climbing games
        constraint_1: an integer, representing the constraint value for "twice_as_many_throwing_games_as_climbing_games"
        constraint_2: an integer, representing the constraint value for "at_least_5_climbing_games"
        constraint_3: an integer, representing the constraint value for "at_most_100_prizes_per_hour"
    
    Returns:
        total_number_of_customers_attracted_every_hour: an integer, representing the objective value
    """
    model = gp.Model("amusement_park")

    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="throwing_games")
    y = model.addVar(vtype=GRB.INTEGER, name="climbing_games")

    # Objective function
    model.setObjective(15*x + 8*y, sense=GRB.MAXIMIZE)

    # Constraints
    model.addConstr(x >= 2*y, name="twice_as_many_throwing_games_as_climbing_games")
    model.addConstr(y >= 5, name="at_least_5_climbing_games")
    model.addConstr(2*x + 3*y <= 100, name="at_most_100_prizes_per_hour")

    # Optimize the model
    model.optimize()

    total_number_of_customers_attracted_every_hour = model.objVal

    return total_number_of_customers_attracted_every_hour