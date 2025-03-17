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
    obj = 4 * cleansing_chemical + 6 * odor_removing_chemical
    return obj

def optimize_cleaning_time():
    model = gp.Model("cleaning_time")

    # Decision variables
    cleansing_chemical = model.addVar(lb=100, vtype=GRB.INTEGER, name="cleansing_chemical")
    odor_removing_chemical = model.addVar(lb=0, ub=150, vtype=GRB.INTEGER, name="odor_removing_chemical")

    # Objective function
    model.setObjective(4 * cleansing_chemical + 6 * odor_removing_chemical, sense=GRB.MINIMIZE)

    # Constraints
    model.addConstr(cleansing_chemical + odor_removing_chemical <= 300, "total_chemical_limit")
    model.addConstr(cleansing_chemical <= 2 * odor_removing_chemical, "cleansing_odor_ratio")

    # Optimize model
    model.optimize()

    # Retrieve optimal values
    optimal_cleansing = model.getAttr('x', cleansing_chemical)
    optimal_odor_removing = model.getAttr('x', odor_removing_chemical)
    min_time = model.objVal

    print("Optimal units of cleansing chemical:", optimal_cleansing)
    print("Optimal units of odor-removing chemical:", optimal_odor_removing)
    print("Minimum total time:", min_time)

optimize_cleaning_time()