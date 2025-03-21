import gurobipy as gp
from gurobipy import GRB

def prob_235(molars, canines):
    """
    Args:
        molars: an integer, the number of molars
        canines: an integer, the number of canines
    
    Returns:
        obj: an integer, the amount of pain killer needed
    """
    # Create a new model
    model = gp.Model("dentist_problem")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="x")  # Number of cavities filled in molars
    y = model.addVar(vtype=GRB.INTEGER, name="y")  # Number of cavities filled in canines

    # Set objective function
    model.setObjective(3*x + 2.3*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(20*x + 15*y <= 3000, "resin_constraint")
    model.addConstr(3*x + 2.3*y <= molars*3 + canines*2.3, "pain_killer_constraint")
    model.addConstr(x >= 45, "molar_reservation_constraint")
    model.addConstr(y >= 0.6*(x+y), "canine_percentage_constraint")

    # Optimize the model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj