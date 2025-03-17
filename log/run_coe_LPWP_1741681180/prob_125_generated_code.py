def minimize_total_time(anxiety_medication, anti_depressants):
    """
    Args:
        anxiety_medication: an integer (number of units of anxiety medication)
        anti_depressants: an integer (number of units of anti-depressants)
    Returns:
        total_time_effective_medication: an integer (total time it takes for the medication to be effective)
    """
    total_time_effective_medication = anxiety_medication * 3 + anti_depressants * 5
    
    # Check if constraints are met
    if anxiety_medication < 30 or anxiety_medication > 2 * anti_depressants or anxiety_medication + anti_depressants < 100:
        return 1e9
    
    return total_time_effective_medication