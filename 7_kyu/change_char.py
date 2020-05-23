def change(st):
    """
    Search for letters Kata
    https://www.codewars.com/kata/52dbae61ca039685460001ae
    """
    return ''.join('1' if a in st.lower() else '0' for a in map(chr, range(97, 123)))