def decode_resistor_colors(bands):
    """
    Resistor Color Codes Kata
    https://www.codewars.com/kata/57cf3dad05c186ba22000348
    
    First and second bands indicates the first two digits of the ohms value
    Third band indicates the power of ten to multiply them by
    
    Args:
        bands(list): list of strings of the color bands of a resistor
    
    Returns:
        res(str): string giving the resistance of the resistor in ohms, with the percent tolerance
        
    Example:
        decode_resistor_colors("brown black brown gold") --> "100 ohms, 5%"  i.e. 10*10**1 ohms
    """
    rest_dict = {'black': '0', 'brown': '1', 'red': '2', 'orange': '3', 'yellow': '4', 
                 'green': '5', 'blue': '6', 'violet': '7', 'gray': '8', 'white': '9'}
    tol_dict = {'gold': ', 5%', 'silver': ', 10%'}
    
    colors = bands.split()
    res = int(rest_dict[colors[0]] + rest_dict[colors[1]]) * 10**int(rest_dict[colors[2]])
    if res % 10**6 == 0:
        res //= 10**6
        res = str(res)+'M ohms'
    elif res > 10**6:
        res /= 10**6
        res = str(res)+'M ohms'
    elif res % 10**3 == 0:
        res //= 10**3
        res = str(res)+'k ohms'
    elif res > 10**3:
        res /= 10**3
        res = str(res)+'k ohms'
    else:
        res = str(res)+' ohms'

    if len(colors) == 4:
        res += tol_dict[colors[3]]
    else:
        res += ', 20%'
    return res
