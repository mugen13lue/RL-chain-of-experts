import gurobipy as gp
from gurobipy import GRB

def prob_241(vars, constraints):
    """
    Args:
        vars: a dictionary with keys 'cart' and 'hand', representing the number of deliveries by cart and hand.
        constraints: a list of dictionaries representing the constraints.

    Returns:
        obj: the total number of refills per hour.
    """
    # Extract variables
    x = vars['cart']
    y = vars['hand']

    # Create a new model
    model = gp.Model("delivery_optimization")

    # Define decision variables
    cart = model.addVar(vtype=GRB.INTEGER, name="cart")
    hand = model.addVar(vtype=GRB.INTEGER, name="hand")

    # Set objective: minimize total number of refills per hour
    model.setObjective(5 * cart + 20 * hand, GRB.MINIMIZE)

    # Add constraints
    model.addConstr(70 * cart + 85 * hand == 4000, "customer_interactions")
    model.addConstr(cart >= 0.7 * (cart + hand), "cart_constraint")
    model.addConstr(hand >= 3, "hand_constraint")

    # Optimize model
    model.optimize()

    # Get the total number of refills per hour
    obj = model.objVal

    return obj