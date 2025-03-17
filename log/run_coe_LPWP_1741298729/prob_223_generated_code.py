from gurobipy import *

def prob_223(Pi_TV, Beta_Video, Gamma_Live):
    """
    Args:
        Pi_TV: an integer, representing the number of commercials to run on Pi TV
        Beta_Video: an integer, representing the number of commercials to run on Beta Video
        Gamma_Live: an integer, representing the number of commercials to run on Gamma Live
    Returns:
        obj: an integer, representing the maximum audience
    """
    m = Model()

    # Decision variables
    Commercials_Pi_TV = m.addVar(vtype=GRB.INTEGER, name="Commercials_Pi_TV")
    Commercials_Beta_Video = m.addVar(vtype=GRB.INTEGER, name="Commercials_Beta_Video")
    Commercials_Gamma_Live = m.addVar(vtype=GRB.INTEGER, name="Commercials_Gamma_Live")

    # Objective function
    m.setObjective(2000 * Commercials_Pi_TV + 5000 * Commercials_Beta_Video + 9000 * Commercials_Gamma_Live, sense=GRB.MAXIMIZE)

    # Constraints
    m.addConstr(Commercials_Pi_TV + Commercials_Beta_Video + Commercials_Gamma_Live == Pi_TV + Beta_Video + Gamma_Live)
    m.addConstr(1200 * Commercials_Pi_TV + 2000 * Commercials_Beta_Video + 4000 * Commercials_Gamma_Live <= 20000)
    m.addConstr(Commercials_Gamma_Live <= (1/3) * (Pi_TV + Beta_Video + Gamma_Live))
    m.addConstr(Commercials_Pi_TV >= (1/5) * (Pi_TV + Beta_Video + Gamma_Live))

    m.optimize()

    obj = int(m.objVal)

    return obj