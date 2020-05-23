def greet(language):
    """
    Welcome! Kata
    https://www.codewars.com/kata/577ff15ad648a14b780000e7
    """
    greet_dict = {'english': 'Welcome', 'czech': 'Vitejte', 'danish': 'Velkomst', 
    'dutch': 'Welkom', 'estonian': 'Tere tulemast', 'finnish': 'Tervetuloa', 
    'flemish': 'Welgekomen', 'french': 'Bienvenue', 'german': 'Willkommen',
    'irish': 'Failte', 'italian': 'Benvenuto', 'latvian': 'Gaidits', 'lithuanian': 'Laukiamas',
    'polish': 'Witamy', 'spanish': 'Bienvenido', 'swedish': 'Valkommen', 'welsh': 'Croeso'}
    return greet_dict.get(language, 'Welcome')