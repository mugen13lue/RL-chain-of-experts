from gurobipy import *

def prob_185(labradors, golden_retrievers):
    """
    Args:
        labradors: an integer, the number of labradors used
        golden_retrievers: an integer, the number of golden retrievers used

    Returns:
        obj: an integer, the maximum number of newspapers that can be delivered
    """
    
    # Create a new model
    m = Model("newspaper_delivery")
    
    # Define decision variables
    x = m.addVar(vtype=GRB.INTEGER, name="labradors")
    y = m.addVar(vtype=GRB.INTEGER, name="golden_retrievers")
    
    # Set objective function
    m.setObjective(7*x + 10*y, sense=GRB.MAXIMIZE)
    
    # Add constraints
    m.addConstr(5*x + 6*y <= 1500, "bone_treats_constraint")
    m.addConstr(y >= 50, "golden_retriever_constraint")
    m.addConstr(x <= 0.6*(x + y), "labrador_constraint")
    
    # Optimize the model
    m.optimize()
    
    # Return the objective value
    return int(m.objVal)