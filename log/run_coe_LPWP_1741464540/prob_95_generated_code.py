import gurobipy as gp
from gurobipy import GRB

def prob_95(heap_leaching, vat_leaching):
    """
    Args:
        heap_leaching: an integer, the proportion of lands that use heap leaching technique
        vat_leaching: an integer, the proportion of lands that use vat leaching technique
    Returns:
        obj: an float, the maximum daily production of rare earth oxide
    """
    
    # Create a new model
    model = gp.Model("mining_optimization")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.CONTINUOUS, name="x")  # Proportion of land using heap leaching technique
    y = model.addVar(vtype=GRB.CONTINUOUS, name="y")  # Proportion of land using vat leaching technique
    
    # Set objective function
    model.setObjective(3*x + 5*y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(3*x + 5*y <= 100)  # Production Constraint
    model.addConstr(8*x + 17*y <= 90)  # Wastewater Constraint
    model.addConstr(10*x + 20*y <= 100)  # Machine Constraint
    model.addConstr(x + y == 1)  # Proportion Constraint
    
    # Optimize model
    model.optimize()
    
    # Return the maximum daily production of rare earth oxide
    return model.objVal