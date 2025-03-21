import gurobipy as gp
from gurobipy import GRB

def prob_141(turkey_dinner, tuna_salad_sandwich):
    """
    Args:
        turkey_dinner: an integer,
        tuna_salad_sandwich: an integer,
    Returns:
        obj: an integer,
    """
    # Create a new model
    model = gp.Model("diet_problem")

    # Define decision variables
    turkey_dinner_count = model.addVar(lb=0, vtype=GRB.INTEGER, name="turkey_dinner")
    tuna_salad_count = model.addVar(lb=0, vtype=GRB.INTEGER, name="tuna_salad_sandwich")

    # Set objective function
    model.setObjective(12*turkey_dinner_count + 8*tuna_salad_count, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(20*turkey_dinner_count + 18*tuna_salad_count >= 150)
    model.addConstr(30*turkey_dinner_count + 25*tuna_salad_count >= 200)
    model.addConstr(turkey_dinner_count <= 0.4*(turkey_dinner_count + tuna_salad_count))

    # Optimize model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj