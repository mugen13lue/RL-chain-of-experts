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
    # Create a new model
    m = gp.Model("transportation")

    # Define decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="carts")
    y = m.addVar(vtype=GRB.INTEGER, name="trolleys")

    # Set objective function
    m.setObjective(2*x + 4*y, sense=GRB.MINIMIZE)

    # Add constraints
    m.addConstr(5*x + 7*y >= 100, "equipment_constraint")
    m.addConstr(2*x + 4*y == carts + 4*trolleys, "worker_constraint")
    m.addConstr(y >= 12, "min_trolley_constraint")
    m.addConstr(y <= 0.4*(x + y), "max_trolley_constraint")

    # Optimize the model
    m.optimize()

    # Get the total number of workers
    obj = m.objVal

    return obj