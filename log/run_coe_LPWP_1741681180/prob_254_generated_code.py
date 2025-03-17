def prob_254(large_bags, tiny_bags):
    """
    Args:
        large_bags: an integer, the number of large bags of grain
        tiny_bags: an integer, the number of tiny bags of grain
    Returns:
        obj: an integer, the maximum amount of grain in weight
    """
    obj = 1e9
    # Objective function: Maximize total weight of grain
    obj = 25 * large_bags + 6 * tiny_bags
    
    # Constraints
    energy_constraint = 4 * large_bags + 1.5 * tiny_bags <= 110
    large_tiny_relation = large_bags == 2 * tiny_bags
    min_tiny_bags = tiny_bags >= 20
    
    if energy_constraint and large_tiny_relation and min_tiny_bags:
        return obj
    else:
        return 0  # Return 0 if constraints are not met

# Example usage
# print(prob_254(10, 5))  # Output: 250