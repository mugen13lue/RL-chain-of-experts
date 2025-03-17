from scipy.optimize import linprog

def prob_42(cost_old_farm, cost_new_farm, raspberries_req, blueberries_req, strawberries_req, raspberries_old, blueberries_old, strawberries_old):
    """
    A berry farmer has two farms, an old and new farm, where he grows raspberries, blueberries, and strawberries.
    He has a contract to provide a local store with 10 kg of raspberries, 9 kg of blueberries, and 15 kg of strawberries.
    At his old farm, it costs $300 to operate per day and he can harvest and deliver 2 kg of raspberries,
    2 kg of blueberries, and 4 kg of strawberries in a day.
    At his new farm, it costs $200 to operate per day and he can harvest and deliver 4 kg of raspberries,
    1 kg of blueberries, and 2 kg of strawberries in a day.
    Formulate a LP to meet his contract while minimizing his cost.

    Args:
        cost_old_farm: An integer, the cost to operate at the old farm per day.
        cost_new_farm: An integer, the cost to operate at the new farm per day.
        raspberries_req: An integer, the limit for the raspberries to be provided.
        blueberries_req: An integer, the limit for the blueberries to be provided.
        strawberries_req: An integer, the limit for the strawberries to be provided.
        raspberries_old: An integer, the weight of raspberries provided by the old farm per day.
        blueberries_old: An integer, the weight of blueberries provided by the old farm per day.
        strawberries_old: An integer, the weight of strawberries provided by the old farm per day.

    Returns:
        obj: An integer, the objective value (minimum cost) to meet the contract.
    """
    c = [cost_old_farm, cost_new_farm]  # Coefficients of the objective function to minimize cost

    A = [
        [-raspberries_old, -blueberries_old],  # Coefficients for raspberries constraint
        [-raspberries_old, -strawberries_old],  # Coefficients for blueberries constraint
        [-2*raspberries_old, -2*strawberries_old]   # Coefficients for strawberries constraint
    ]

    b = [-raspberries_req, -blueberries_req, -strawberries_req]  # RHS of the constraints

    bounds = [(0, None), (0, None)]  # Bounds for the variables x1 and x2

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    return res.fun