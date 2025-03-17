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
    x = model.addVar(vtype=GRB.CONTINUOUS, name="x")
    y = model.addVar(vtype=GRB.CONTINUOUS, name="y")
    
    # Set objective
    model.setObjective(x + y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(n_plastic*x + w_plastic*y <= 60000)
    model.addConstr(n_factory*x + w_factory*y >= n_anti_itch)
    model.addConstr(n_factory*x + w_factory*y >= n_topical_cream)
    
    # Optimize model
    model.optimize()
    
    # Get the minimum total time needed
    obj = model.objVal
    
    return obj