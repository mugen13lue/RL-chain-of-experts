import gurobipy as gp
from gurobipy import GRB

def prob_90(part_time_workers, full_time_workers):
    """
    Args:
        part_time_workers: an integer, the number of part time workers
        full_time_workers: an integer, the number of full time workers

    Returns:
        Total_Number_of_Workers: an integer, the total number of workers
    """
    # Create a new model
    model = gp.Model("worker_scheduling")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="full_time_workers")
    y = model.addVar(vtype=GRB.INTEGER, name="part_time_workers")

    # Set objective function: minimize total number of workers
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(8*x + 4*y >= 500, "total_hours_constraint")
    model.addConstr(300*x + 100*y <= 15000, "budget_constraint")

    # Optimize model
    model.optimize()

    # Get the total number of workers scheduled
    Total_Number_of_Workers = int(x.x + y.x)

    return Total_Number_of_Workers