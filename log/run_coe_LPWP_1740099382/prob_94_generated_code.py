import gurobipy as gp
from gurobipy import GRB

def prob_94(chemical_reaction_A, chemical_reaction_B):
    """
    Args:
        chemical_reaction_A: an integer, represents the number of reactions of chemical reaction A
        chemical_reaction_B: an integer, represents the number of reactions of chemical reaction B
    Returns:
        objective: a float, representing the amount of rare compound produced
    """
    
    # Create a new model
    model = gp.Model("chemical_reactions")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.CONTINUOUS, name="x")  # Number of reactions of type A
    y = model.addVar(vtype=GRB.CONTINUOUS, name="y")  # Number of reactions of type B
    
    # Set objective function
    model.setObjective(10*x + 8*y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(5*x + 7*y <= 1000, "rare_inert_gas_constraint")
    model.addConstr(6*x + 3*y <= 800, "treated_water_constraint")
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal objective value
    objective = model.objVal
    
    return objective