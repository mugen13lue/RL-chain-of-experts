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

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="throwing_games")
    y = model.addVar(vtype=GRB.INTEGER, name="climbing_games")

    # Constraints
    model.addConstr(x >= constraint_1*y, "twice_as_many_throwing_games_as_climbing_games")
    model.addConstr(y >= constraint_2, "at_least_5_climbing_games")
    model.addConstr(2*x + 3*y <= constraint_3, "at_most_100_prizes_per_hour")

    # Objective
    model.setObjective(15*x + 8*y, sense=GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    total_number_of_customers_attracted_every_hour = model.objVal

    return total_number_of_customers_attracted_every_hour