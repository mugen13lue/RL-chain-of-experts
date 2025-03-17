import gurobipy as gp
from gurobipy import GRB

def prob_150(small_bottles, large_bottles):
    """
    Args:
        small_bottles: an integer, the number of small bottles
        large_bottles: an integer, the number of large bottles
        
    Returns:
        amount_of_honey: an integer, the maximum amount of honey that can be transported
    """
    # Create a new model
    model = gp.Model("bee_farm_transport")

    # Define decision variables
    x = model.addVar(lb=0, ub=300, vtype=GRB.INTEGER, name="small_bottles")
    y = model.addVar(lb=0, ub=100, vtype=GRB.INTEGER, name="large_bottles")

    # Set objective function
    model.setObjective(5*x + 20*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(5*x + 20*y <= 300)
    model.addConstr(x >= 2*y)
    model.addConstr(y >= 50)

    # Optimize the model
    model.optimize()

    # Get the optimal solution
    amount_of_honey = model.objVal

    return amount_of_honey