def prob_148(pill, shot):
    """
    Args:
        pill: an integer, the number of pill vaccines administered
        shot: an integer, the number of shot vaccines administered
    Returns:
        obj: an integer, the maximum number of patients vaccinated
    """
    # Administer 30 pill vaccines
    pill_time = 30 * 10  # 30 pill vaccines * 10 minutes each
    
    # Calculate remaining time for shots
    remaining_time = 10000 - pill_time
    
    # Calculate the maximum number of shots that can be administered
    max_shots = remaining_time // 20  # 20 minutes per shot
    
    # Ensure at least 3 times as many shots as pills are administered
    max_pills = min(max_shots // 3, 30)  # At least 30 pills and 3 times as many shots
    
    # Calculate the total number of patients vaccinated
    total_patients = max_pills + max_shots
    
    return total_patients