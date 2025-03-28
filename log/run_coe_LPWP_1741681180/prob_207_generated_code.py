import gurobipy as gp
from gurobipy import GRB

def prob_207(graph_paper, music_paper):
    """
    Args:
        graph_paper: an integer, number of reams of graph paper to produce
        music_paper: an integer, number of reams of music paper to produce
    Returns:
        objective_value: an integer, maximum profit
    """
    
    # Create a new model
    model = gp.Model("Forest_Paper_Problem")
    
    # Decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="graph_paper")
    y = model.addVar(vtype=GRB.INTEGER, name="music_paper")
    
    # Set objective function
    model.setObjective(4*x + 2.5*y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(3*x + 1.5*y <= 350, "printing_machine_constraint")
    model.addConstr(5.5*x + 3*y <= 350, "scanning_machine_constraint")
    model.addConstr(x >= 0, "non_negativity_constraint_x")
    model.addConstr(y >= 0, "non_negativity_constraint_y")
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal objective value
    objective_value = model.objVal
    
    return objective_value