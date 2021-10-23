import re
if __name__ == "__main__":
    test_cases = int(input())

    for i in range(test_cases):
        # Get the expression
        expr = input()
        p = re.compile('^[(]?[-]?([0-9]+)[)]??([(]?([-+/*]([0-9]))?([.,][0-9]+)?[)]?)*$')
        if p.match(expr):
            parsed = []
            residual = []
            for char in expr:
                if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    residual.append(char)
                if char in ['+', '*', '-']:
                    # Check the previous number
                    if len(residual) > 0:
                        number = ''.join(residual)
                        number = int(number)
                        parsed.append(number)
                        parsed.append(char)
                        residual = []
                    else:
                        parsed.append(char)
                else:
                    pass
            if len(residual) > 0:
                        number = ''.join(residual)
                        number = int(number)
                        parsed.append(number)
                        residual = []
            if len(parsed) == 1:
                print(parsed[0])
            else:
                print(parsed)
        else:
            print('invalid')