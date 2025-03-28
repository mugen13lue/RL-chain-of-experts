import gurobipy as gp
from gurobipy import GRB

def prob_211():
    """
    Returns:
        obj: a float (maximum profit achieved)
    """
    # Create a new model
    model = gp.Model("flooring_problem")

    # Define decision variables
    x = model.addVar(lb=0, ub=40000, vtype=GRB.CONTINUOUS, name="laminate_planks")
    y = model.addVar(lb=0, ub=20000, vtype=GRB.CONTINUOUS, name="carpets")

    # Set objective function
    model.setObjective(2.1*x + 3.3*y, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(x >= 15000, name="demand_laminate_planks")
    model.addConstr(y >= 5000, name="demand_carpets")
    model.addConstr(x + y >= 50000, name="shipping_contract")
    
    # Optimize model
    model.optimize()

    # Get the optimal objective value
    obj = model.objVal

    return obj