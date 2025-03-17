import gurobipy as gp
from gurobipy import GRB

def optimize_commercials():
    """
    Returns:
        obj: an integer, representing the maximum audience
    """
    # Define the model
    model = gp.Model("commercial_optimization")

    # Decision variables
    Commercials_Pi_TV = model.addVar(vtype=GRB.INTEGER, name="Commercials_Pi_TV")
    Commercials_Beta_Video = model.addVar(vtype=GRB.INTEGER, name="Commercials_Beta_Video")
    Commercials_Gamma_Live = model.addVar(vtype=GRB.INTEGER, name="Commercials_Gamma_Live")

    # Set objective
    model.setObjective(2000 * Commercials_Pi_TV + 5000 * Commercials_Beta_Video + 9000 * Commercials_Gamma_Live, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(0.2 * (Commercials_Pi_TV + Commercials_Beta_Video + Commercials_Gamma_Live) <= Commercials_Pi_TV)
    model.addConstr(Commercials_Gamma_Live <= 0.33 * (Commercials_Pi_TV + Commercials_Beta_Video + Commercials_Gamma_Live))
    model.addConstr(1200 * Commercials_Pi_TV + 2000 * Commercials_Beta_Video + 4000 * Commercials_Gamma_Live <= 20000)
    model.addConstr(Commercials_Beta_Video <= 8)

    # Optimize the model
    model.optimize()

    # Get the maximum audience
    obj = model.objVal

    return obj