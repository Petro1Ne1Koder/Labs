import argparse


parser = argparse.ArgumentParser()

parser.add_argument("Number_1", type=int)
parser.add_argument("Operator", type=str)
parser.add_argument("Number_2", type=int)

args = parser.parse_args()

if args.Operator not in ("+", "-", "*", "/"):
    print("Not math symbol")
elif args.Operator in ("+" or "-" or "*"):
    print("Result is:", eval(str(args.Number_1) + args.Operator + str(args.Number_2)))
elif args.Operator == "/" and args.Number_2 == "0":
    print("Division by zero")
else:
    print(eval(str(args.Number_1) + args.Operator + str(args.Number_2)))