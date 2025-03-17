import gurobipy as gp
from gurobipy import GRB

def prob_284(heavy_duty_yard_machine, gas_lawn_mower):
    """
    Args:
        heavy_duty_yard_machine: an integer, the square feet to be cut using heavy duty yard machine
        gas_lawn_mower: an integer, the square feet to be cut using gas lawn mower

    Returns:
        obj: an integer, the objective value (time required)
    """
    # Create a new model
    model = gp.Model("grass_cutting")

    # Define variables
    heavy_duty_area = model.addVar(lb=0, vtype=GRB.INTEGER, name="heavy_duty_yard_machine")
    gas_area = model.addVar(lb=0, vtype=GRB.INTEGER, name="gas_lawn_mower")

    # Set objective
    model.setObjective(2*heavy_duty_area + 5*gas_area, GRB.MINIMIZE)

    # Add constraints
    model.addConstr(3*heavy_duty_area + 2*gas_area <= 450, "fuel_constraint")
    model.addConstr(12*heavy_duty_area + 10*gas_area <= 2000, "pollution_constraint")
    model.addConstr(heavy_duty_area + gas_area <= 2500, "land_constraint")
    
    # Optimize model
    model.optimize()

    # Get the objective value
    obj = model.objVal

    return obj