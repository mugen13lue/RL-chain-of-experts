import gurobipy as gp
from gurobipy import GRB

def prob_109(automatic_machine, manual_machine):
    """
    Args:
        automatic_machine: an integer, representing the number of patients using the automatic machine
        manual_machine: an integer, representing the number of patients using the manual machine

    Returns:
        obj: an integer, representing the maximum number of patients whose blood pressure can be taken
    """
    
    # Create a new model
    model = gp.Model("clinic_optimization")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # number of patients processed by the automatic machine
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # number of patients processed by the manual machine
    
    # Set objective function
    model.setObjective(x + y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(10*x + 15*y <= 20000)
    model.addConstr(y >= 2*x)
    model.addConstr(x <= 20)
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal objective value
    obj = int(model.objVal)
    
    return obj