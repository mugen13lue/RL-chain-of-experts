def prob_22(regular_glass_pane, tempered_glass_pane, regular_glass_cooling_time, tempered_glass_cooling_time, regular_glass_profit, tempered_glass_profit):
    """
    Args:
        regular_glass_pane: an integer, the time required in the heating machine for one regular glass pane
        tempered_glass_pane: an integer, the time required in the heating machine for one tempered glass pane
        regular_glass_cooling_time: an integer, the time required in the cooling machine for one regular glass pane
        tempered_glass_cooling_time: an integer, the time required in the cooling machine for one tempered glass pane
        regular_glass_profit: an integer, the profit per pane of regular glass
        tempered_glass_profit: an integer, the profit per pane of tempered glass
    Returns:
        obj: an integer, the maximum profit
    """
    from scipy.optimize import linprog

    c = [regular_glass_profit, tempered_glass_profit]  # Adjusted to positive profit values
    A = [[regular_glass_pane, tempered_glass_pane], [regular_glass_cooling_time, tempered_glass_cooling_time]]
    b = [300, 300]
    x_bounds = (0, None)
    y_bounds = (0, None)

    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

    return res.fun  # Return the maximum profit without negation of the result.