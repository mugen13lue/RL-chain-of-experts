def prob_139(spit_tests, swabs):
    """
    Args:
        spit_tests: an integer, the number of spit tests
        swabs: an integer, the number of swabs
    Returns:
        obj: an integer, the objective value
    """
    total_time = spit_tests * 10 + swabs * 15
    if total_time > 8000 or spit_tests < 2 * swabs or swabs < 20:
        return 0
    
    return spit_tests + swabs