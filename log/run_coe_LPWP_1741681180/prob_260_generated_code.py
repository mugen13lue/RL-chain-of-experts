import gurobipy as gp
from gurobipy import GRB

def prob_260(method_A, method_B, required_fabric, required_plastic, available_special_element):
    """
    Solve the problem to minimize the total time needed.

    Args:
        method_A: an integer representing the number of executions of Method A
        method_B: an integer representing the number of executions of Method B
        required_fabric: an integer representing the minimum required units of fabric
        required_plastic: an integer representing the minimum required units of plastic
        available_special_element: an integer representing the available units of the special element

    Returns:
        objective_value: an integer representing the minimized total time needed
    """
    # Create a new model
    model = gp.Model("fabric_plastic_production")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="method_A_hours")
    y = model.addVar(vtype=GRB.INTEGER, name="method_B_hours")

    # Set objective function: minimize total time
    model.setObjective(60*x + 65*y, GRB.MINIMIZE)

    # Add constraints
    model.addConstr(25*x + 45*y >= required_fabric, "fabric_constraint")
    model.addConstr(14*x + 25*y >= required_plastic, "plastic_constraint")
    model.addConstr(60*x + 65*y <= available_special_element, "special_element_constraint")

    # Optimize the model
    model.optimize()

    # Get the optimized objective value
    objective_value = model.objVal

    return objective_value