def prob_121(ramen, fries):
    """
    Args:
        ramen: an integer, the number of packs of ramen
        fries: an integer, the number of packs of fries
    Returns:
        obj: an integer, the value of the objective function
    """
    obj = 75*ramen + 100*fries
    return obj