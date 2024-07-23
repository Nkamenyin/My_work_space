def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b == 0:
        raise ZeroDivisionError("You can not divide by zero")
    return a/b

def cal(a,operator,b):
    if operator == "+":
        return add(a/b)
    elif operator == "-":
        return sub(a,b)
    elif operator == "*":
        return mul(a,b)
    elif operator == "/":
        return div(a,b)
    else:
        raise ValueError("invalid operation")
