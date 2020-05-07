def encode_resistor_colors(ohms_string):
    """
    Resistor Color Codes, Part 2 Kata
    https://www.codewars.com/kata/5855777bb45c01bada0002ac
    """
    rest_dict = {'0': 'black', '1': 'brown', '2': 'red', '3': 'orange', '4': 'yellow', 
                 '5': 'green', '6': 'blue', '7': 'violet', '8': 'gray', '9': 'white'}
    first, second, *power = str(int(eval(ohms_string.replace('M', '*1000k').replace('k', '*1000').split()[0])))
    return '{} {} {} gold'.format(rest_dict[first], rest_dict[second], rest_dict[str(len(power))])