import re

def arithmetic_arranger(problems, solve=False):
    # from this:
    # ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

    # To this:
    #      32      3801      45      123
    #   + 698    -    2    + 43    +  49
    #   -----    ------    ----    -----

    # Input:
    # [['3801 - 2', '123 + 49']]
    # Output:
    # '  3801      123\n'
    # '-    2    +  49\n'
    # '------    -----',
    if len(problems) > 5:
        return "Error: Too many problems."

    first = ""
    second = ""
    lines = ""
    result = ""
    output = ""

    for problem in problems:
        if re.search("[^\s0-9.+-]", problem):
            if re.search("[/]", problem) or re.search("[*]", problem):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."

        firstNumber = problem.split(" ")[0]
        operator = problem.split(" ")[1]
        secondNumber = problem.split(" ")[2]

        if len(firstNumber) >= 5 or len(secondNumber) >= 5:
            return "Error: Numbers cannot be more than four digits."

        result1 = ""
        if operator == "+":
            result1 = str(int(firstNumber) + int(secondNumber))
        elif operator == "-":
            result1 = str(int(firstNumber) - int(secondNumber))

        length = max(len(firstNumber), len(secondNumber)) + 2
        top = str(firstNumber).rjust(length)
        bottom = operator + str(secondNumber).rjust(length-1)
        line = ""
        res = str(result1).rjust(length)
        for s in range(length):
            line += "-"

        if problem != problems[-1]:
            first += top + '    '
            second += bottom + "    "
            lines += line + "    "
            result += res + "    "
        else:
            first += top
            second += bottom
            lines += line
            result += res

    if solve:
        output = first + "\n" + second + "\n" + lines + "\n" + result
    else:
        output = first + "\n" + second + "\n" + lines
    return output

