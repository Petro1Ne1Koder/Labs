import argparse
import operator
import math

parser = argparse.ArgumentParser()

parser.add_argument("Operator", type=str)
parser.add_argument("Number", type=int, nargs="+")

args = parser.parse_args()

def func(oper, *args) -> str:
    
    try:
        func = getattr(operator, oper)
        return func(*args)
    except Exception:
        try:
            func1 = getattr(math, oper)
            return func1(*args)
        except Exception:
            return "Error"

print(func(args.Operator, *args.Number))