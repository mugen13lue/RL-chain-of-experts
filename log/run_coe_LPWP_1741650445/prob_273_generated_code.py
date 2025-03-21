from gurobipy import *

def prob_273(camel_caravans, desert_trucks):
    """
    Args:
        camel_caravans: an integer, the number of camel caravans
        desert_trucks: an integer, the number of desert trucks
        
    Returns:
        total_number_of_hours: an integer, the total number of hours required
    """
    
    # Create a new model
    m = Model("transportation_problem")
    
    # Define decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="camel_caravans")
    y = m.addVar(vtype=GRB.INTEGER, name="desert_trucks")
    
    # Set objective function: minimize total number of hours
    m.setObjective(12*x + 5*y, GRB.MINIMIZE)
    
    # Add constraints
    m.addConstr(50*x + 150*y >= 1500, "goods_constraint")
    
    # Optimize model
    m.optimize()
    
    # Get the total number of hours required
    total_number_of_hours = m.objVal
    
    return total_number_of_hours