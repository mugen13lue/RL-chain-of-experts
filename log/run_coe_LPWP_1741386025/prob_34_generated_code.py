from scipy.optimize import linprog

def prob_34(amount_fertilizer_C, amount_fertilizer_Y, cost_fertilizer_C, cost_fertilizer_Y, nitrous_oxide_fertilizer_C, vitamin_mix_fertilizer_C, nitrous_oxide_fertilizer_Y, vitamin_mix_fertilizer_Y):
    """
    Ayse produces a plant growth compound by mixing two types of fertilizer: C and Y.
    This growth compound must contain at least 5 units of nitrous oxide and 8 units of vitamin mix.
    Fertilizer C and Y cost $2 and $3 per kg respectively.
    Fertilizer C contains 1.5 units of nitrous oxide per kg and 3 units of vitamin mix per kg.
    Fertilizer Y contains 5 units of nitrous oxide per kg and 1 unit of vitamin mix per kg.
    Determine the minimum cost of Ayse's compound.

    Args:
        amount_fertilizer_C: an integer, the amount of Fertilizer C (in kg)
        amount_fertilizer_Y: an integer, the amount of Fertilizer Y (in kg)
        cost_fertilizer_C: an integer, the cost of Fertilizer C (in $ per kg)
        cost_fertilizer_Y: an integer, the cost of Fertilizer Y (in $ per kg)
        nitrous_oxide_fertilizer_C: a float, the nitrous oxide content of Fertilizer C (in units per kg)
        vitamin_mix_fertilizer_C: an integer, the vitamin mix content of Fertilizer C (in units per kg)
        nitrous_oxide_fertilizer_Y: an integer, the nitrous oxide content of Fertilizer Y (in units per kg)
        vitamin_mix_fertilizer_Y: an integer, the vitamin mix content of Fertilizer Y (in units per kg)

    Returns:
        obj: an integer, the minimum cost of Ayse's compound
    """
    
    # Define the coefficients of the objective function
    c = [cost_fertilizer_C, cost_fertilizer_Y]
    
    # Define the coefficients of the inequality constraints
    A = [[-nitrous_oxide_fertilizer_C, -nitrous_oxide_fertilizer_Y], [-vitamin_mix_fertilizer_C, -vitamin_mix_fertilizer_Y]]
    b = [-5, -8]
    
    # Define the bounds for the variables
    x_bounds = (0, None)
    y_bounds = (0, None)
    
    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')
    
    return res.fun