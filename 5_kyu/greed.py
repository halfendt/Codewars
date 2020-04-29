from collections import Counter

def score(dice):
    """
    Greed is Good Kata
    https://www.codewars.com/kata/5270d0d18625160ada0000e4
    """
    score = 0
    str_dict = {str(key): val for key, val in dict(Counter(dice)).items()}
    for k, v in str_dict.items():
        if k == '1' and v >= 3:
            score += 1000
            str_dict[k] -= 3
            if str_dict[k] >= 1:
                score += 100 * str_dict[k]
        elif k == '6' and v >= 3:
            score += 600
        elif k == '5' and v >= 3:
            score += 500
            str_dict[k] -= 3
            if str_dict[k] >= 1:
                score += 50 * str_dict[k]
        elif k == '4' and v >= 3:
            score += 400
        elif k == '3' and v >= 3:
            score += 300
        elif k == '2' and v >= 3:
            score += 200
        elif k == '1' and v >= 1:
            score += 100 * v
        elif k == '5' and v >= 1:
            score += 50 * v
    return score