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
    
    # Create variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="x")  # Number of hours the northern factory is run
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="y")  # Number of hours the western factory is run
    
    # Set objective
    model.setObjective(x + y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(800*x + 650*y >= n_anti_itch)
    model.addConstr(700*x + 750*y >= n_topical_cream)
    model.addConstr(40*x + 35*y <= n_plastic)
    
    # Optimize model
    model.optimize()
    
    # Get the minimum total time needed
    obj = model.objVal
    
    return obj