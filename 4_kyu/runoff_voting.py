def runoff(voters):
    """
    Instant Runoff Voting Kata
    https://www.codewars.com/kata/52996b5c99fdcb5f20000004
    """
    first_choice = [voter[0] for voter in voters]  
    counts = {cand: first_choice.count(cand) for cand in voters[0]}
    perc_dict = {cand: num_votes / total_votes for total_votes in (sum(counts.values()),) for cand, num_votes in counts.items()}
    max_key_val = max(perc_dict.items(), key=lambda x: x[1])
    min_key_val = min(perc_dict.items(), key=lambda x: x[1])
    if max_key_val[1] <= 0.5:
        for key, value in perc_dict.items():
            if value == min_key_val[1]:
                [voter.remove(key) for voter in voters]
        if len(voters[0]) == 0:
            return None
        else:
            return runoff(voters)
    else:
        return max_key_val[0]