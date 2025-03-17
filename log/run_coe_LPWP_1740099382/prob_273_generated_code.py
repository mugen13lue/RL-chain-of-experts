import gurobipy as gp
from gurobipy import GRB

def prob_273(camel_caravans, desert_trucks):
    """
    Args:
        camel_caravans: an integer, the number of camel caravans
        desert_trucks: an integer, the number of desert trucks
        
    Returns:
        total_number_of_hours: an integer, the total number of hours required
    """
    
    # Create a new model
    model = gp.Model("transportation_problem")
    
    # Define decision variables
    x = model.addVar(vtype=GRB.INTEGER, name="camel_caravans")
    y = model.addVar(vtype=GRB.INTEGER, name="desert_trucks")
    
    # Set objective function: minimize total number of hours
    model.setObjective(12*x + 5*y, GRB.MINIMIZE)
    
    # Add constraints
    model.addConstr(50*x + 150*y >= 1500, "goods_constraint")
    
    # Optimize model
    model.optimize()
    
    # Get total number of hours required
    total_number_of_hours = model.objVal
    
    return total_number_of_hours