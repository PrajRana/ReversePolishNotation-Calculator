def get_data():
    hold_data = []
    hold_operators = ['+', '-', '*', '/']
    with open("input_RPN.txt", "r") as all_lines:
        # gets all lines from the file
        for text in all_lines:
            # if the line is not empty in file then do all the calculations
            if text != "\n":
                # removes the new line form every line
                wor = text.strip("\n")
                # loop for ever line in the file
                for a in wor:
                    # do not store space or operators in stack
                    if " " != a and a not in hold_operators:
                        # convert string into int
                        d = int(a)
                        hold_data.append(d)
                        # print("first:", hold_data)
                    elif a in hold_operators:
                        # pop the first(last 2 values stored in stacks for calculation)
                        val1 = hold_data.pop()
                        val2 = hold_data.pop()
                        total = 0
                        if a == "*":
                            total = val2 * val1
                        elif a == "+":
                            total = val2 + val1
                        elif a == "-":
                            total = val2 - val1
                        elif a == "/":
                            total = val2 / val1
                        else:
                            print("invalid operand")
                        # store the value in stack
                        hold_data.append(total)
                # print the final value
                print("Calculated value:", hold_data)
                hold_data.pop()  # empties the stack for another RPN to store data from another line



get_data()

