def likes(names):
    """
    Who likes it? Kata
    https://www.codewars.com/kata/5266876b8f4bf2da9b000362
    """
    formats = {
               0: "no one likes this",
               1: "{} likes this",
               2: "{} and {} like this",
               3: "{}, {} and {} like this",
               4: "{}, {} and {others} others like this"
              }
    n = len(names)
    return formats[min(n,4)].format(*names, others=n-2)