"""
Calculating with Functions Kata
https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39
"""
def zero(oper=None): return expression(0, oper)
def one(oper=None): return expression(1, oper)
def two(oper=None): return expression(2, oper)
def three(oper=None): return expression(3, oper)
def four(oper=None): return expression(4, oper)
def five(oper=None): return expression(5, oper)
def six(oper=None): return expression(6, oper)
def seven(oper=None): return expression(7, oper)
def eight(oper=None): return expression(8, oper)
def nine(oper=None): return expression(9, oper)

def plus(b): return lambda a: a + b
def minus(b): return lambda a: a - b
def times(b): return lambda a: a * b
def divided_by(b): return lambda a: a // b

def expression(num, oper): return num if not oper else oper(num)