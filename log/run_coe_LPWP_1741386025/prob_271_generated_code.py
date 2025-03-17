import gurobipy as gp
from gurobipy import GRB

def prob_271(n_factory, w_factory, n_anti_itch, n_topical_cream, w_anti_itch, w_topical_cream, n_plastic, w_plastic):
    """
    Args:
        n_factory: an integer, the production rate of anti-itch injections by the northern factory per hour.
        w_factory: an integer, the production rate of topical cream by the western factory per hour.
        n_anti_itch: an integer, the minimum required quantity of anti-itch injections.
        n_topical_cream: an integer, the minimum required quantity of topical cream.
        w_anti_itch: an integer, the production rate of anti-itch injections by the western factory per hour.
        w_topical_cream: an integer, the production rate of topical cream by the western factory per hour.
        n_plastic: an integer, the quantity of plastic required by the northern factory per hour.
        w_plastic: an integer, the quantity of plastic required by the western factory per hour.

    Returns:
        obj: an integer, the minimum total time needed.
    """
    
    # Create a new model
    model = gp.Model("factory_optimization")
    
    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x")  # Hours northern factory is run
    y = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="y")  # Hours western factory is run
    
    # Set objective function
    model.setObjective(x + y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(40*x + 35*y <= 60000, "plastic_constraint")
    model.addConstr(800*x + 650*y <= 800000, "anti_itch_constraint")
    model.addConstr(700*x + 750*y <= 700000, "topical_cream_constraint")
    
    # Optimize model
    model.optimize()
    
    # Get the minimum total time needed
    obj = model.objVal
    
    return obj