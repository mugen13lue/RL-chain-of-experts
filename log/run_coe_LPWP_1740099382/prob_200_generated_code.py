import gurobipy as gp
from gurobipy import GRB

def prob_200(hams, pork_ribs):
    """
    Solves the problem of maximizing profit for a meat processing plant.

    Args:
        hams: The number of batches of hams to produce (integer).
        pork_ribs: The number of batches of pork ribs to produce (integer).

    Returns:
        profit: The maximum profit that can be achieved (integer).
    """
    # Create a new model
    model = gp.Model("meat_processing")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="hams")
    y = model.addVar(vtype=GRB.INTEGER, name="pork_ribs")

    # Set objective function
    model.setObjective(150*x + 300*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(4*x + 2*y <= 4000, "machine_slicer_hours")
    model.addConstr(2.5*x + 3.5*y <= 4000, "machine_packer_hours")

    # Optimize the model
    model.optimize()

    # Get the optimal solution
    profit = model.objVal

    return profit