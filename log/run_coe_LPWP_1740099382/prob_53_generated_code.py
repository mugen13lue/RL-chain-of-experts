import gurobipy as gp
from gurobipy import GRB

def prob_53(process_A, process_B):
    """
    Args:
        process_A: an integer, number of processes of type A
        process_B: an integer, number of processes of type B
    Returns:
        obj: an integer, total number of coins that can be plated
    """
    
    # Create a new LP model
    model = gp.Model("coin_plating")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of processes of type A
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of processes of type B
    
    # Set objective function
    model.setObjective(5*x + 7*y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(3*x + 5*y <= 500, "gold_constraint")
    model.addConstr(2*x + 3*y <= 300, "wires_constraint")
    
    # Non-negativity constraints
    model.addConstr(x >= 0, "non_negativity_x")
    model.addConstr(y >= 0, "non_negativity_y")
    
    # Optimize model
    model.optimize()
    
    # Get the total number of coins that can be plated
    obj = model.objVal
    
    return obj