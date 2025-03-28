def prob_156(vans, trucks):
    """
    Args:
        vans: an integer, number of vans
        trucks: an integer, number of trucks
        
    Returns:
        obj: an integer, the minimum number of vans that can be used
    """
    # Minimum pairs of shoes constraint: 50x + 100y >= 2000
    # Number of trucks constraint: y <= x
    # Non-negativity constraint for vans: x >= 0
    # Non-negativity constraint for trucks: y >= 0
    
    # Since y = x, we can simplify the constraint to 150x >= 2000
    # Solve for x
    x = 2000 // 150
    if x * 150 < 2000:
        x += 1
    
    return x