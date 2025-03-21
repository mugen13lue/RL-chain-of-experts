def prob_131(bananas, mangoes):
    """
    Args:
        bananas: an integer, number of bananas
        mangoes: an integer, number of mangoes
    Returns:
        obj: an integer, minimum sugar intake
    """
    obj = 10 * bananas + 8 * mangoes  # Calculate total sugar intake
    
    # Constraints
    total_calories = 80 * bananas + 100 * mangoes
    total_potassium = 20 * bananas + 15 * mangoes
    
    # Check if constraints are met
    if total_calories < 4000 or total_potassium < 150 or mangoes > 0.33 * (bananas + mangoes):
        return 1e9  # Return a large value if constraints are not met
    
    return obj