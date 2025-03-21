def prob_25(apartments, townhouses):
    """
    
    Args:
        apartments: an integer, amount of money invested in apartments
        townhouses: an integer, amount of money invested in townhouses
    
    Returns:
        profit: an integer, maximum profit
    """
    
    # Constraints
    total_investment = apartments + townhouses
    if total_investment > 600000 or apartments > 200000 or apartments < townhouses / 2:
        return -1  # Invalid input
    
    # Calculate profit
    apartment_profit = apartments * 0.10
    townhouse_profit = townhouses * 0.15
    total_profit = apartment_profit + townhouse_profit
    
    return total_profit