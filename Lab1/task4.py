import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-W", type=int)
parser.add_argument("-w", type=int, nargs="+")

args = parser.parse_args()

knapsack = args.W
bars_weight = args.w

sums = []

def formula(bars_weight, knapsack, partial=[]):
    
    s = sum(partial)
    if s <= knapsack:
        sums.append(s)
    for i in range(len(bars_weight)):
        n = bars_weight[i]
        remaining = bars_weight[i + 1:]
        formula(remaining, knapsack, partial + [n])

formula(bars_weight, knapsack)

print(max(sums))