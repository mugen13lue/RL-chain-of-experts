import gurobipy as gp
from gurobipy import GRB

def prob_170(small_suitcases, large_suitcases):
    """
    Args:
        small_suitcases: an integer, the number of small suitcases
        large_suitcases: an integer, the number of large suitcases
    Returns:
        number_of_snacks: an integer, the maximum number of snacks that can be delivered
    """
    # Create a new model
    model = gp.Model("snack_exporter")

    # Define decision variables
    x = model.addVar(lb=0, ub=70, vtype=GRB.INTEGER, name="small_suitcases")
    y = model.addVar(lb=15, ub=50, vtype=GRB.INTEGER, name="large_suitcases")

    # Set objective function
    model.setObjective(50*x + 80*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(x >= 2*y, "twice_as_many_small_suitcases")
    model.addConstr(x + y <= 70, "total_suitcases_limit")

    # Optimize model
    model.optimize()

    # Get the optimal solution
    number_of_snacks = int(model.objVal)

    return number_of_snacks