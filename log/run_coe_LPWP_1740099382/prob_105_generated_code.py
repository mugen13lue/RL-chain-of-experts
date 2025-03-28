import gurobipy as gp
from gurobipy import GRB

def prob_105(cleansing_chemical, odor_removing_chemical):
    """
    Args:
        cleansing_chemical: an integer, the units of cleansing chemical used
        odor_removing_chemical: an integer, the units of odor-removing chemical used
    Returns:
        obj: an integer, the total time it takes for a house to be cleaned
    """
    model = gp.Model("house_cleaning")

    # Variables
    cleansing_chemical_units = model.addVar(name="cleansing_chemical")
    odor_removing_chemical_units = model.addVar(name="odor_removing_chemical")

    # Constraints
    model.addConstr(4*cleansing_chemical_units >= 100, name="Cleansing_Chemical_Constraint")
    model.addConstr(4*cleansing_chemical_units + 6*odor_removing_chemical_units <= 300, name="Total_Chemical_Constraint")
    model.addConstr(cleansing_chemical_units <= 2*odor_removing_chemical_units, name="Ratio_Constraint")

    # Objective
    model.setObjective(4*cleansing_chemical_units + 6*odor_removing_chemical_units, GRB.MINIMIZE)

    # Optimize model
    model.optimize()

    # Get the total time
    obj = model.objVal

    return obj