def solution(array_a, array_b):
    se = [(a - b)**2 for a, b, in zip(array_a, array_b)]
    mse = sum(se)/len(se)
    return mse