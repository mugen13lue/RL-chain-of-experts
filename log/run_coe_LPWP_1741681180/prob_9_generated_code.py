def prob_9(carrots, cucumbers):
    """
    Args:
        carrots: an integer, the number of carrots sold each month
        cucumbers: an integer, the number of cucumbers sold each month

    Returns:
        obj: an integer, the maximum profit
    """
    max_profit = 0
    max_carrots = 0
    max_cucumbers = 0

    for c in range(300, 501):
        for cu in range(0, min(c//3, (500-c*0.30)//0.50) + 1):
            if c*0.30 + cu*0.50 <= 500:
                profit = c*0.75 + cu*0.80
                if profit > max_profit:
                    max_profit = profit
                    max_carrots = c
                    max_cucumbers = cu

    return max_profit, max_carrots, max_cucumbers