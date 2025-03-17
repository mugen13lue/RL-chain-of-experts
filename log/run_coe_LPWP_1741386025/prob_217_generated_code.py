import gurobipy as gp
from gurobipy import GRB

def prob_217(cat_paw, gold_shark, cat_paw_percentage_first_mix, gold_shark_percentage_first_mix,
             cat_paw_percentage_second_mix, gold_shark_percentage_second_mix, cat_paw_limit, gold_shark_limit,
             profit_first_mix, profit_second_mix):
    """
    Args:
        cat_paw: an integer, representing the amount of cat paw snacks (in kg) to be prepared
        gold_shark: an integer, representing the amount of gold shark snacks (in kg) to be prepared
        cat_paw_percentage_first_mix: a float, representing the percentage of cat paw snacks in the first mix
        gold_shark_percentage_first_mix: a float, representing the percentage of gold shark snacks in the first mix
        cat_paw_percentage_second_mix: a float, representing the percentage of cat paw snacks in the second mix
        gold_shark_percentage_second_mix: a float, representing the percentage of gold shark snacks in the second mix
        cat_paw_limit: an integer, representing the available amount of cat paw snacks in stock (in kg)
        gold_shark_limit: an integer, representing the available amount of gold shark snacks in stock (in kg)
        profit_first_mix: an integer, representing the profit per kg for the first mix
        profit_second_mix: an integer, representing the profit per kg for the second mix
    Returns:
        obj: an integer, representing the maximum profit
    """
    model = gp.Model("snack_mix")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x")  # kg of the first mix
    y = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="y")  # kg of the second mix

    # Set objective function
    model.setObjective(profit_first_mix * x + profit_second_mix * y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(cat_paw_percentage_first_mix * x + cat_paw_percentage_second_mix * y <= cat_paw, "cat_paw_constraint")
    model.addConstr(gold_shark_percentage_first_mix * x + gold_shark_percentage_second_mix * y <= gold_shark, "gold_shark_constraint")
    model.addConstr(x <= cat_paw_limit, "cat_paw_limit_constraint")
    model.addConstr(y <= gold_shark_limit, "gold_shark_limit_constraint")

    # Optimize model
    model.optimize()

    # Get the maximum profit
    obj = model.objVal

    return obj