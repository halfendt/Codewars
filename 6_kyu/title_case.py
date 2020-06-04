def title_case(title, minor_words=''):
    """
    Title Case Kata
    https://www.codewars.com/kata/5202ef17a402dd033c000009
    """
    return ' '.join(c if c in minor_words.lower().split() else c.title() for c in title.capitalize().split())