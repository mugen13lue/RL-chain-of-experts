def prob_218():
    """
    Returns:
        obj: an integer, the maximum profit
    """
    import gurobipy as gp
    from gurobipy import GRB

    # Create a new model
    model = gp.Model("taco_stand")

    # Define decision variables
    x1 = model.addVar(vtype=GRB.INTEGER, name="regular_tacos")
    x2 = model.addVar(vtype=GRB.INTEGER, name="deluxe_tacos")

    # Set objective function: maximize profit
    model.setObjective(2.50*x1 + 3.55*x2, sense=GRB.MAXIMIZE)

    # Add constraints
    model.addConstr(x1 <= 50, "regular_tacos_limit")
    model.addConstr(x2 <= 40, "deluxe_tacos_limit")
    model.addConstr(x1 + x2 <= 70, "total_tacos_limit")

    # Optimize the model
    model.optimize()

    # Get the maximum profit
    obj = model.objVal

    return obj