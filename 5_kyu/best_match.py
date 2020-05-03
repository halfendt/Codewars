def best_match(goals1, goals2):
    """
    Simple Fun #166: Best Match Kata
    https://www.codewars.com/kata/58b38256e51f1c2af0000081
    """
    match_dict = {ind: tup[0]-tup[1] for ind, tup in enumerate(zip(goals1, goals2))}
    best_score = min(list(match_dict.values()))
    if list(match_dict.values()).count(best_score) == 1:
        return min(match_dict.keys(), key=(lambda ke: match_dict[ke]))
    else:
        high_dict = {i: goals2[i] for i in [key for key, value in match_dict.items() if value == best_score]}
        return max(high_dict.keys(), key=(lambda ke: high_dict[ke]))