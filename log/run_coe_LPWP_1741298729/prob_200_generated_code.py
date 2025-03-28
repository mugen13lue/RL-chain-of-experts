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
    num_hams = model.addVar(vtype=GRB.INTEGER, name="hams")
    num_pork_ribs = model.addVar(vtype=GRB.INTEGER, name="pork_ribs")

    # Set objective function
    model.setObjective(150*num_hams + 300*num_pork_ribs, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(4*num_hams + 2*num_pork_ribs <= 4000, "machine_slicer")
    model.addConstr(2.5*num_hams + 3.5*num_pork_ribs <= 4000, "machine_packer")

    # Optimize the model
    model.optimize()

    # Get the optimal profit
    profit = model.objVal

    return profit