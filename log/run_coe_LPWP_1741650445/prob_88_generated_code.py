import gurobipy as gp
from gurobipy import GRB

def prob_88(glass, plastic, glass_capacity, plastic_capacity, glass_min, glass_to_plastic_ratio, available_water):
    """
    Args:
        glass: an integer, representing the number of glass bottles
        plastic: an integer, representing the number of plastic bottles
        glass_capacity: an integer, representing the capacity of a glass bottle in ml
        plastic_capacity: an integer, representing the capacity of a plastic bottle in ml
        glass_min: an integer, representing the minimum number of glass bottles
        glass_to_plastic_ratio: an integer, representing the ratio of plastic bottles to glass bottles
        available_water: an integer, representing the available water in ml

    Returns:
        obj: an integer, representing the maximum number of bottles
    """
    
    # Create a new model
    model = gp.Model("water_bottles")
    
    # Define decision variables
    glass_bottles = model.addVar(lb=glass_min, vtype=GRB.INTEGER, name="glass_bottles")
    plastic_bottles = model.addVar(lb=0, vtype=GRB.INTEGER, name="plastic_bottles")
    
    # Set objective function
    model.setObjective(glass_bottles + plastic_bottles, sense=GRB.MAXIMIZE)
    
    # Add constraints
    model.addConstr(glass_capacity*glass_bottles + plastic_capacity*plastic_bottles <= available_water, "water_constraint")
    model.addConstr(glass_bottles >= glass_min, "min_glass_constraint")
    model.addConstr(plastic_bottles >= glass_to_plastic_ratio*glass_bottles, "min_plastic_constraint")
    
    # Optimize model
    model.optimize()
    
    # Get the optimal objective value
    obj = model.objVal
    
    return obj