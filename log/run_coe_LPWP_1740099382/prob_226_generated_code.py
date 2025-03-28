import gurobipy as gp
from gurobipy import GRB

def prob_226(carts, trolleys):
    """
    Solve the transportation problem.
    
    Args:
        carts: an integer, number of carts used
        trolleys: an integer, number of trolleys used
    
    Returns:
        obj: an integer, total number of workers
    """
    m = gp.Model("transportation")

    # Define decision variables
    x = m.addVar(name="carts")
    y = m.addVar(name="trolleys")

    # Set objective function
    m.setObjective(2*x + 4*y, GRB.MINIMIZE)

    # Add constraints
    m.addConstr(5*x + 7*y >= 100, "equipment_constraint")
    m.addConstr(2*x + 4*y >= 100, "worker_constraint")  # Updated to reflect equipment delivery rate
    m.addConstr(y >= 12, "min_trolley_constraint")
    m.addConstr(y <= 0.4*(x + y), "max_trolley_percentage_constraint")

    # Optimize model
    m.optimize()

    # Get the total number of workers
    obj = m.objVal

    return obj