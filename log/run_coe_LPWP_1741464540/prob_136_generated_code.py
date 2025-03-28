import gurobipy as gp
from gurobipy import GRB

def prob_136(lab_1, lab_2, constraint1, constraint2, constraint3):
    """
    Args:
        lab_1: an integer representing the number of hours to run lab 1
        lab_2: an integer representing the number of hours to run lab 2
        constraint1: an integer representing the available worker hours
        constraint2: an integer representing the minimum number of heart medication pills
        constraint3: an integer representing the minimum number of lung medication pills
    Returns:
        obj: an integer representing the total time needed
    """
    
    # Create a new model
    model = gp.Model("pharmaceutical_company")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x")  # hours lab 1 is run
    y = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="y")  # hours lab 2 is run

    # Set objective function
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(3*x + 5*y <= constraint1, "worker_hours")
    model.addConstr(20*x + 30*y >= constraint2, "heart_medication")
    model.addConstr(30*x + 40*y >= constraint3, "lung_medication")

    # Optimize the model
    model.optimize()

    # Get the total time needed
    obj = model.objVal

    return obj