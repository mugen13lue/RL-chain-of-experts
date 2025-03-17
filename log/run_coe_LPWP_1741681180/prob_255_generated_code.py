import gurobipy as gp
from gurobipy import GRB

def prob_255(automatic_electric_one, gas_powered_one):
    """
    Args:
       automatic_electric_one: an integer, the number of automatic electric car jacks
       gas_powered_one: an integer, the number of gas-powered car jacks
       
    Returns:
       amount_of_cars_processed_every_hour: an integer, the maximum amount of cars processed every hour
    """
    # Create a new model
    model = gp.Model("car_jacks_purchase")

    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="automatic_electric_jacks")
    y = model.addVar(vtype=GRB.INTEGER, name="gas_powered_jacks")

    # Set objective function
    model.setObjective(5*x + 4*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(x <= 15, "electric_jacks_limit")
    model.addConstr(6*x <= 50, "electricity_constraint")
    model.addConstr(7*y <= 80, "gas_constraint")

    # Optimize the model
    model.optimize()

    # Get the optimal solution
    amount_of_cars_processed_every_hour = model.objVal

    return amount_of_cars_processed_every_hour