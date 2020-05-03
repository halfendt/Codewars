def my_languages(results):
    """
    My Languages Kata
    https://www.codewars.com/kata/5b16490986b6d336c900007d
    """
    return [key for key, value in sorted(results.items(), key=lambda item: item[1], reverse=True) if value >= 60]