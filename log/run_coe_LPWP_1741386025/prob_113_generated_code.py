import gurobipy as gp
from gurobipy import GRB

def prob_113(children_vaccines, adult_vaccines):
    """
    Args:
        children_vaccines: an integer representing the number of children's vaccines
        adult_vaccines: an integer representing the number of adult vaccines

    Returns:
        obj: an integer representing the objective value (amount of fever suppressant)
    """
    obj = 0

    # Create a new model
    model = gp.Model("vaccine_production")

    # Define decision variables
    x = model.addVar(lb=50, vtype=GRB.INTEGER, name="children_vaccines")
    y = model.addVar(vtype=GRB.INTEGER, name="adult_vaccines")

    # Set objective function
    model.setObjective(50*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(50*x + 75*y <= 20000, "mRNA_constraint")
    model.addConstr(y >= 0.7*(x+y), "adult_vaccine_percentage_constraint")
    model.addConstr(x >= 50, "min_children_vaccines_constraint")

    # Set children's and adult vaccines input values
    x_start = children_vaccines
    y_start = adult_vaccines

    # Set initial solution values
    model.addConstr(x == x_start)
    model.addConstr(y == y_start)

    # Optimize model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj