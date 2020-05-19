def no_space(x):
    """
    Remove String Spaces Kata
    https://www.codewars.com/kata/57eae20f5500ad98e50002c5
    """
    return x.replace(' ','')
    
    #or
    
    return ''.join(x.split())