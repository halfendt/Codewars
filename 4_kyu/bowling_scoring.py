def bowling_score(frames):
    """
    Ten-Pin Bowling Kata
    https://www.codewars.com/kata/5531abe4855bcc8d1f00004c    
    """
    frames_list = frames.split()
    score = 0
    for ind, frame in enumerate(frames_list[:9]):
        if 'X' in frame:
            if 'X' in frames_list[ind+1][0]:
                score += 20
                try:
                    if 'X' in frames_list[ind+2][0]:
                        score += 10
                    else:
                        score += int(frames_list[ind+2][0])
                except:
                    if 'X' in frames_list[ind+1][1]:
                        score += 10
            elif '/' in frames_list[ind+1][1]:
                score += 20
            else:
                score += 10 + int(frames_list[ind+1][0]) + int(frames_list[ind+1][1])
        elif '/' in frame:
            if 'X' in frames_list[ind+1][0]:
                score += 20
            else:
                score += 10 + int(frames_list[ind+1][0])
        else:
            score += sum(int(digit) for digit in frame)
    if 'XXX' == frames_list[9]:
        score += 30
    elif 'XX' in frames_list[9]:
        score += 20 + int(frames_list[9][2])
    elif 'X' in frames_list[9][0]:
        if '/' in frames_list[9][2]:
            score += 20
        else:
            score += 10 + int(frames_list[9][1]) + int(frames_list[9][2])
    elif '/' in frames_list[9][1]:
        if 'X' in frames_list[9][2]:
            score += 20
        else:
            score += 10 + int(frames_list[9][2])
    else:
        score += sum(int(digit) for digit in frames_list[9])
    return score