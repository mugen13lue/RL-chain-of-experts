import gurobipy as gp
from gurobipy import GRB

def prob_38():
    """
    Returns:
        obj: an integer, value of the objective function
    """
    # Create a new model
    model = gp.Model("vitamin_mix")

    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.INTEGER, name="x")  # Number of cups of drink A
    y = model.addVar(lb=0, vtype=GRB.INTEGER, name="y")  # Number of cups of drink B

    # Set objective function: minimize the amount of Vitamin K
    model.setObjective(4*x + 12*y, sense=GRB.MINIMIZE)

    # Add constraints
    model.addConstr(8*x + 15*y >= 150, "vitamin_A_constraint")
    model.addConstr(6*x + 2*y >= 300, "vitamin_D_constraint")
    model.addConstr(10*x + 20*y <= 400, "vitamin_E_constraint")

    # Optimize the model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj

# Call the function and print the result
result = prob_38()
print("Optimal value of the objective function:", result)