def longest_consec(strarr, k):
    """
    Consecutive strings Kata
    https://www.codewars.com/kata/56a5d994ac971f1ac500003e
    """
    return max(["".join(strarr[i:k+i]) for i in range(len(strarr)-k+1)], key=len) if strarr and 0 < k <= len(strarr) else ""