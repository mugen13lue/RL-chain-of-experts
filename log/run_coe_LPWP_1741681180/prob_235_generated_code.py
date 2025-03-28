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
    resin_molars = 20
    resin_canines = 15
    pain_killer_molars = 3
    pain_killer_canines = 2.3
    
    # Create a new model
    model = gp.Model("dentist_problem")
    
    # Define decision variables
    x_molars = model.addVar(vtype=GRB.INTEGER, name="x_molars")
    x_canines = model.addVar(vtype=GRB.INTEGER, name="x_canines")
    
    # Set objective function
    model.setObjective(pain_killer_molars * x_molars + pain_killer_canines * x_canines, GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(resin_molars * x_molars + resin_canines * x_canines <= 3000, "resin_constraint")
    model.addConstr(x_canines >= 0.6 * (x_molars + x_canines), "canine_percentage_constraint")
    model.addConstr(x_molars >= 45, "molars_constraint")
    
    # Optimize the model
    model.optimize()
    
    # Get the optimal objective value
    obj = model.objVal
    
    return obj