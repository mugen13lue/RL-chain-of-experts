import gurobipy as gp
from gurobipy import GRB

def prob_214(basketball_tournament, horse_race, soccer_game, limit_1, limit_2):
    """
    Args:
        basketball_tournament: an integer, representing the amount of money to put on basketball tournament.
        horse_race: an integer, representing the amount of money to put on horse race.
        soccer_game: an integer, representing the amount of money to put on soccer game.
        limit_1: an integer, representing the limit for the sum of all bets.
        limit_2: a float, representing the limit for the average chance of losing money.

    Returns:
        obj: a float, representing the maximum average payout.
    """
    m = gp.Model("gambling")

    # Variables
    x1 = m.addVar(lb=0, ub=basketball_tournament, name="x1")
    x2 = m.addVar(lb=0, ub=horse_race, name="x2")
    x3 = m.addVar(lb=0, ub=soccer_game, name="x3")

    # Constraints
    m.addConstr(x1 + x2 + x3 <= 100000, "total_money_constraint")
    m.addConstr(0.5*x1 + 0.25*x2 + 0.1*x3 <= 0.3 * (x1 + x2 + x3), "average_chance_constraint")

    # Objective
    m.setObjective(1.2*x1 + 0.5*x2 + 0.1*x3, GRB.MAXIMIZE)

    m.optimize()

    return m.objVal