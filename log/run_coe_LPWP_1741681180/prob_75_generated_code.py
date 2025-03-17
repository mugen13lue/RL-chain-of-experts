import gurobipy as gp
from gurobipy import GRB

def prob_75(traditional_machine, modern_machine):
    """
    Args:
        traditional_machine: an integer, represents the number of acres to be used for traditional machine
        modern_machine: an integer, represents the number of acres to be used for modern machine
    Returns:
        obj: an integer, represents the maximum amount of tea leaves that can be picked
    """
    
    # Create a new model
    model = gp.Model("Tea Leaves Picking")
    
    # Define decision variables
    acres_traditional = model.addVar(lb=0, vtype=GRB.INTEGER, name="acres_traditional")
    acres_modern = model.addVar(lb=0, vtype=GRB.INTEGER, name="acres_modern")
    
    # Set objective function
    model.setObjective(30 * acres_traditional + 40 * acres_modern, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(20 * acres_traditional + 15 * acres_modern <= 9000, "fuel_constraint")
    model.addConstr(10 * acres_traditional + 15 * acres_modern <= 6000, "waste_constraint")
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal objective value
    obj = int(model.objVal)
    
    return obj