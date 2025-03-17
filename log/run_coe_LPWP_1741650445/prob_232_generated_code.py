import gurobipy as gp
from gurobipy import GRB

def prob_232(circular_tables, rectangular_tables):
    """
    Args:
        circular_tables: an integer, the number of circular tables
        rectangular_tables: an integer, the number of rectangular tables
    Returns:
        objective: an integer, the maximum number of catered guests
    """
    
    # Create a new model
    model = gp.Model("science_fair_optimization")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="circular_tables")
    y = model.addVar(vtype=GRB.INTEGER, name="rectangular_tables")
    
    # Set objective function
    model.setObjective(8*x + 12*y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(4*x + 4*y <= 500, "participants_constraint")
    model.addConstr(4*x + 5*y <= 300, "poster_boards_constraint")
    model.addConstr(15*x + 20*y <= 1900, "space_constraint")
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal objective value
    objective = model.objVal
    
    return objective