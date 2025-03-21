import gurobipy as gp
from gurobipy import GRB

def prob_195(carrier_pigeons, owls):
    """
    Args:
        carrier_pigeons: an integer, the number of carrier pigeons
        owls: an integer, the number of owls

    Returns:
        number_of_letters: an integer, the maximum number of letters that can be sent
    """
    model = gp.Model("letter_delivery")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="carrier_pigeons", lb=0)
    y = model.addVar(vtype=GRB.INTEGER, name="owls", lb=0)

    # Set objective function
    model.setObjective(2*x + 5*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(3*x + 5*y <= 1000, "number_of_treats_constraint")
    model.addConstr(y <= 0.4*(x + y), "percentage_of_owls_constraint")
    model.addConstr(x >= 20, "minimum_carrier_pigeons_constraint")

    # Optimize model
    model.optimize()

    # Get the optimal solution
    number_of_letters = int(model.objVal)

    return number_of_letters