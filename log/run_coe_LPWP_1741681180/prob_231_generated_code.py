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
    throw = model.addVar(vtype=GRB.INTEGER, name="throw")
    climb = model.addVar(vtype=GRB.INTEGER, name="climb")

    # Objective function
    model.setObjective(15*throw + 8*climb, sense=GRB.MAXIMIZE)

    # Constraints
    model.addConstr(throw >= 2*climb)
    model.addConstr(climb >= 5)
    model.addConstr(2*throw + 3*climb <= constraint_3)

    model.optimize()

    total_number_of_customers_attracted_every_hour = model.objVal

    return total_number_of_customers_attracted_every_hour