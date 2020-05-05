def delete_nth(order, max_e):
    """
    Delete occurrences of an element if it occurs more than n times Kata
    https://www.codewars.com/kata/554ca54ffa7d91b236000023
    """
    return [num for ind, num in enumerate(order) if order[:ind].count(num) < max_e]