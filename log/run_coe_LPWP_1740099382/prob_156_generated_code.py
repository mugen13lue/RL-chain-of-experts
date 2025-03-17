import gurobipy as gp
from gurobipy import GRB

def prob_156(vans, trucks):
    """
    Args:
        vans: an integer, number of vans
        trucks: an integer, number of trucks
        
    Returns:
        obj: an integer, the minimum number of vans that can be used
    """
    # Create a new model
    model = gp.Model("shoe_transportation")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="vans")
    y = model.addVar(vtype=GRB.INTEGER, name="trucks")

    # Set objective function: minimize the number of vans used
    model.setObjective(x, GRB.MINIMIZE)

    # Add constraints
    model.addConstr(50*x + 100*y >= 2000, "min_pairs_constraint")
    model.addConstr(y <= x, "truck_constraint")

    # Optimize model
    model.optimize()

    # Get the minimum number of vans used
    obj = model.getAttr(GRB.Attr.X, x)

    return int(obj) if obj is not None else None