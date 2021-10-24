i = 0
def S():
    global i
    if (s[i] == '('):
        print(f"{s[i:]} \t S -> (L)\n")
        i = i + 1
        if (L()):
            if (s[i] == ')'):
                i = i + 1
                return 1
            else:
                return 0
        else:
            return 0
    elif (s[i] == 'a'):
        print(f"{s[i:]} \t S -> a\n")
        i = i + 1
        return 1 
    else:
        return 0
def L():
    global i
    print(f"{s[i:]} \t L -> ST\n")
    if (S()):
        if (T()):
            return 1 
        else:
            return 0
    else:
        return 0
def T():
    global i
    if (s[i] == ','):
        print(f"{s[i:]} \t T -> ,ST\n")
        i = i + 1
        if (S()):
            if (T()):
                return 1
            else:
                return 0
        else:
            return 0
    else:
        print(f"{s[i:]} \t T -> ^\n")
        return 1

s = input("Enter the string: ")
print("Input \t Action\n")
if (S() and i == len(s)):
    print("String is successfully parsed")
else:
    print("Error in parsing string")