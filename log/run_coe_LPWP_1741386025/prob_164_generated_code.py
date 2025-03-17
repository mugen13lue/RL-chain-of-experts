import gurobipy as gp
from gurobipy import GRB

def prob_164():
    """
    Solve the sand delivery problem and maximize the amount of sand that can be delivered.

    Returns:
        objective_value: the amount of sand that can be delivered (objective value of the problem)
    """
    # Create a new model
    model = gp.Model("sand_delivery")

    # Define variables
    x = model.addVar(lb=5, ub=100, vtype=GRB.INTEGER, name="small_containers")
    y = model.addVar(lb=3, ub=100, vtype=GRB.INTEGER, name="large_containers")

    # Set objective function
    model.setObjective(20*x + 50*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(x == 3*y, "small_large_relation")

    # Optimize model
    model.optimize()

    # Get the objective value
    objective_value = model.objVal

    return objective_value