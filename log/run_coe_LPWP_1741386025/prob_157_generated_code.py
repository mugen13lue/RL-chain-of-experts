import gurobipy as gp
from gurobipy import GRB

def prob_157(containers, trucks, Max_Trucks, Min_Oil_Units, Min_Containers):
    """
    Args:
        containers: an integer, the number of containers used.
        trucks: an integer, the number of trucks used.
        Max_Trucks: an integer, maximum number of trucks allowed.
        Min_Oil_Units: an integer, minimum number of oil units to be transported.
        Min_Containers: an integer, minimum number of containers required.

    Returns:
        Total_Containers_Trucks: an integer, the minimum total number of containers and trucks needed.
    """
    # Create a new model
    model = gp.Model("oil_transportation")

    # Define decision variables
    x = model.addVar(lb=Min_Containers, vtype=GRB.INTEGER, name="containers")
    y = model.addVar(lb=0, ub=Max_Trucks, vtype=GRB.INTEGER, name="trucks")

    # Set objective function
    model.setObjective(x + y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(30*x + 40*y >= Min_Oil_Units, "oil_units")
    model.addConstr(y <= 0.5*x, "trucks_constraint")

    # Optimize the model
    model.optimize()

    # Get the total number of containers and trucks needed
    Total_Containers_Trucks = model.objVal

    return Total_Containers_Trucks