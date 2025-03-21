def maximize_fish_catch(net_acres, line_acres, sum_in_a, bait_available, pain_tolerance):
    max_fish = 0
    
    for n in range(net_acres + 1):
        for f in range(line_acres + 1):
            if (n * 8 + f * 5) > max_fish and (n * 4 + f * 3) <= bait_available and (n * 2 + f) <= pain_tolerance:
                max_fish = n * 8 + f * 5
    
    return max_fish