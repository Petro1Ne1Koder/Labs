import argparse


def check(formula):
    
    if (formula):
        if formula[0] in ("+" or "-" or "0") and formula[1].isnumeric():
            # First place operation
            error()
        elif formula[len(formula) - 1] in ("+" or "-"):
            # Last place operation
            error()
        else:
            for i in range(len(formula) + 1):
                if len(formula) == i:
                    #Printing Result
                    solving(formula)
                    break
                elif formula[len(formula) - 1 - i] not in ("+", "-") \
                        and formula[len(formula) - 1 - i].isdigit() == 0:
                    #Using not included symbols
                    error()
                    break
                elif formula[len(formula) - 1 - i] in ("+" or "-") and formula[len(formula) - 2 - i] in ("+" or "-"):
                    #Reusing operations
                    error()
                    break
                elif formula[len(formula) - 2 - i] in ("+" or "-") \
                        and formula[len(formula) - 1 - i] == '0' and formula[len(formula) - i].isnumeric():
                    #0 on first place of number
                    error()
                    break
    else:
        error()
        #If line is empty


def solving(formula):
    print("True,", eval(formula))


def error():
    print("False, None")


parser = argparse.ArgumentParser()
parser.add_argument("formula", nargs = "?", type = str)
args = parser.parse_args()
check(args.formula)