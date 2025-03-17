import gurobipy as gp
from gurobipy import GRB

def prob_34(C, Y, Fertilizer_C_cost, Fertilizer_Y_cost, Fertilizer_C_nitrous_oxide, Fertilizer_C_vitamin_mix, Fertilizer_Y_nitrous_oxide, Fertilizer_Y_vitamin_mix):
    """
    Ayse produces a plant growth compound by mixing two types of fertilizer: C and Y.
    This growth compound must contain at least 5 units of nitrous oxide and 8 units of vitamin mix.
    Fertilizer C and Y cost $2 and $3 per kg respectively.
    Fertilizer C contains 1.5 units of nitrous oxide per kg and 3 units of vitamin mix per kg.
    Fertilizer Y contains 5 units of nitrous oxide per kg and 1 unit of vitamin mix per kg.
    Determine the minimum cost of Ayse's compound.

    Args:
        C: an integer, the amount of Fertilizer C (in kg)
        Y: an integer, the amount of Fertilizer Y (in kg)
        Fertilizer_C_cost: an integer, the cost of Fertilizer C (in $ per kg)
        Fertilizer_Y_cost: an integer, the cost of Fertilizer Y (in $ per kg)
        Fertilizer_C_nitrous_oxide: a float, the nitrous oxide content of Fertilizer C (in units per kg)
        Fertilizer_C_vitamin_mix: an integer, the vitamin mix content of Fertilizer C (in units per kg)
        Fertilizer_Y_nitrous_oxide: an integer, the nitrous oxide content of Fertilizer Y (in units per kg)
        Fertilizer_Y_vitamin_mix: an integer, the vitamin mix content of Fertilizer Y (in units per kg)

    Returns:
        obj: an integer, the minimum cost of Ayse's compound
    """
    # Create a new model
    model = gp.Model("Ayse's Compound")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x")  # Amount of Fertilizer C in kg
    y = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="y")  # Amount of Fertilizer Y in kg

    # Set objective function
    model.setObjective(Fertilizer_C_cost * x + Fertilizer_Y_cost * y, GRB.MINIMIZE)

    # Add constraints
    model.addConstr(Fertilizer_C_nitrous_oxide * x + Fertilizer_Y_nitrous_oxide * y >= 5, "Nitrous Oxide")
    model.addConstr(Fertilizer_C_vitamin_mix * x + Fertilizer_Y_vitamin_mix * y >= 8, "Vitamin Mix")

    # Optimize the model
    model.optimize()

    # Get the minimum cost
    obj = model.objVal

    return obj