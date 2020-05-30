from re import search

def domain_name(url):
    """
    Extract the domain name from a URL Kata
    https://www.codewars.com/kata/514a024011ea4fb54200004b
    """
    return search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')