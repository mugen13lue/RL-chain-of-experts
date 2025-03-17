import gurobipy as gp
from gurobipy import GRB

def prob_268(in_vivo, ex_vivo, constraint1, constraint2):
    """
    Args:
        in_vivo: an integer, the number of in-vivo experiments
        ex_vivo: an integer, the number of ex-vivo experiments
        constraint1: an integer, the value of constraint 1
        constraint2: an integer, the value of constraint 2

    Returns:
        obj: an integer, the objective value of the problem
    """
    
    # Create a new model
    model = gp.Model("radiation_minimization")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="in_vivo")
    y = model.addVar(vtype=GRB.INTEGER, name="ex_vivo")
    
    # Set objective function
    model.setObjective(2*x + 3*y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(30*x + 45*y <= constraint1, "preparation_time")
    model.addConstr(60*x + 30*y <= constraint2, "execution_time")
    
    # Optimize the model
    model.optimize()
    
    # Get the objective value
    obj = model.objVal
    
    return obj