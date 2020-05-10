def namelist(names):
    """
    Format a string of names like 'Bart, Lisa & Maggie' Kata
    https://www.codewars.com/kata/53368a47e38700bd8300030d
    """
    name_list = [h['name'] for h in names]
    if len(name_list) > 2:
        return ', '.join(name_list[:-1])+' & '+name_list[-1]
    elif len(name_list) == 2:
        return ' & '.join(name_list)
    else:
        return ''.join(name_list)