import gurobipy as gp
from gurobipy import GRB

def prob_120(machine_1, machine_2):
    """
    Args:
        machine_1: a float, the usage of machine 1 in minutes
        machine_2: a float, the usage of machine 2 in minutes
    Returns:
        Total_Amount_of_Waste: a float, the total amount of waste produced
    """
    
    # Create a new model
    model = gp.Model("minimize_waste")
    
    # Define decision variables
    x = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="x")  # minutes machine 1 is used
    y = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name="y")  # minutes machine 2 is used
    
    # Set objective function
    model.setObjective(0.3*x + 0.5*y, sense=GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(0.5*x + 0.3*y <= 8, "Heart_Medicine")
    model.addConstr(0.8*x + y >= 4, "Brain_Medicine")
    model.addConstr(0.3*x <= 0.3*x, "Waste_Machine1")
    model.addConstr(0.5*y <= 0.5*y, "Waste_Machine2")
    
    # Optimize the model
    model.optimize()
    
    # Get the total amount of waste produced
    Total_Amount_of_Waste = model.objVal
    
    return Total_Amount_of_Waste