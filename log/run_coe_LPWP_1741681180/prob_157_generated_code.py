import gurobipy as gp

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
    m = gp.Model("oil_transportation")

    # Decision variables
    x = m.addVar(vtype=gp.GRB.INTEGER, name="containers")
    y = m.addVar(vtype=gp.GRB.INTEGER, name="trucks")

    # Objective function: minimize total number of containers and trucks
    m.setObjective(x + y, sense=gp.GRB.MINIMIZE)

    # Constraints
    m.addConstr(30*x + 40*y >= Min_Oil_Units, "min_oil_units")
    m.addConstr(x >= Min_Containers, "min_containers")
    m.addConstr(y <= Max_Trucks, "max_trucks")
    m.addConstr(y <= 0.5*x, "trucks_containers_ratio")

    m.optimize()

    Total_Containers_Trucks = m.objVal

    return Total_Containers_Trucks