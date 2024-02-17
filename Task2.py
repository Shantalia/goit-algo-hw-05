from typing import Callable
from decimal import Decimal, getcontext
import re

def generator_numbers(text: str): 
    for st in text.split(' '):
        if re.fullmatch(r"\d+[.]\d+", st):
            yield float(st)

def sum_profit(text: str, func: Callable):
        summa = 0
        getcontext().prec = 6
        for num in func:
            summa += Decimal(num)
        return summa
             
text = "Загальний дохід працівника складається з декількох частин: 1000.01\
      як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers(text))
print(f"Загальний дохід: {total_income}")