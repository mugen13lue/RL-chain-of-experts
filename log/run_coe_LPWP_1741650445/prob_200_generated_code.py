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
    hams_var = model.addVar(vtype=GRB.INTEGER, name="hams")
    pork_ribs_var = model.addVar(vtype=GRB.INTEGER, name="pork_ribs")

    # Set objective function
    model.setObjective(150*hams_var + 300*pork_ribs_var, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(4*hams_var + 2.5*pork_ribs_var <= 4000, "machine_slicer")
    model.addConstr(2*hams_var + 3.5*pork_ribs_var <= 4000, "machine_packer")
    model.addConstr(hams_var >= 0, "non_negativity_hams")
    model.addConstr(pork_ribs_var >= 0, "non_negativity_pork_ribs")

    # Optimize model
    model.optimize()

    # Get the optimal profit
    profit = model.objVal

    return profit