def goodVsEvil(good, evil):
    """
    Good vs Evil Kata
    https://www.codewars.com/kata/52761ee4cffbc69732000738
    """
    good_list = [int(num) for num in good.split(' ')]
    evil_list = [int(num) for num in evil.split(' ')]
    good_dict = {'Hobbits': 1, 'Men': 2, 'Elves': 3, 'Dwarves': 3, 'Eagles': 4, 'Wizards': 10}
    evil_dict = {'Orcs': 1, 'Men': 2, 'Wargs': 2, 'Goblins': 2, 'Uruk Hai': 3, 'Trolls': 5, 'Wizards': 10}
    good_sum = sum([num1 * num2 for num1, num2 in zip(list(good_dict.values()), good_list)])
    evil_sum = sum([num1 * num2 for num1, num2 in zip(list(evil_dict.values()), evil_list)])
    if good_sum > evil_sum:
        return 'Battle Result: Good triumphs over Evil'
    elif good_sum < evil_sum:
        return 'Battle Result: Evil eradicates all trace of Good'
    else:
        return 'Battle Result: No victor on this battle field'