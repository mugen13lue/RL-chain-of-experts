import gurobipy as gp
from gurobipy import GRB

def prob_155():
    """
    Solve the problem to maximize the total number of tricks that can be performed.

    Returns:
        obj: total number of tricks (integer)
    """
    model = gp.Model("aquarium_show")

    # Variables
    x = model.addVar(vtype=GRB.INTEGER, name="otters")
    y = model.addVar(vtype=GRB.INTEGER, name="dolphins")

    # Constraints
    model.addConstr(3*x + 5*y <= 200, "num_treats")
    model.addConstr(y >= 10, "min_dolphins")
    model.addConstr(x <= 0.3*(x+y), "max_otters")

    # Objective
    model.setObjective(3*x + y, sense=GRB.MAXIMIZE)

    # Optimize model
    model.optimize()

    obj = model.objVal

    return obj

# Call the function to solve the problem
result = prob_155()
print("Total number of tricks that can be performed:", result)