import gurobipy as gp
from gurobipy import GRB

def prob_45(blueberries, raspberries, constraint1, constraint2, constraint3):
    """
    Args:
        blueberries: an integer, representing the number of acres for blueberries.
        raspberries: an integer, representing the number of acres for raspberries.
        constraint1: an integer, representing the limit for total acres.
        constraint2: an integer, representing the limit for watering cost.
        constraint3: an integer, representing the limit for labor days.

    Returns:
        obj: an integer, representing the objective value (profit).
    """
    
    # Create a new model
    model = gp.Model("berry_farm")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="blueberries")
    y = model.addVar(vtype=GRB.INTEGER, name="raspberries")
    
    # Set objective function
    model.setObjective(56*x + 75*y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(6*x + 3*y <= constraint3, "labor_constraint")
    model.addConstr(22*x + 25*y <= constraint2, "watering_constraint")
    model.addConstr(x + y <= constraint1, "total_acres_constraint")
    
    # Optimize the model
    model.optimize()
    
    # Get the objective value
    obj = model.objVal
    
    return obj