from gurobipy import *

def prob_25(apartments, townhouses):
    """
    
    Args:
        apartments: an integer, amount of money invested in apartments
        townhouses: an integer, amount of money invested in townhouses
    
    Returns:
        profit: an integer, maximum profit
    """
    
    # Create a new model
    m = Model("RealEstateInvestment")
    
    # Define decision variables
    x = m.addVar(vtype=GRB.CONTINUOUS, name="apartments")
    y = m.addVar(vtype=GRB.CONTINUOUS, name="townhouses")
    
    # Set objective function
    m.setObjective(0.10*x + 0.15*y, GRB.MAXIMIZE)
    
    # Add constraints
    m.addConstr(x + y == 600000, "TotalInvestment")
    m.addConstr(x <= 200000, "MaxApartmentsInvestment")
    m.addConstr(x >= 0.5*y, "MinInvestmentRatio")
    
    # Optimize model
    m.optimize()
    
    # Get the optimal solution
    profit = m.objVal
    
    return profit