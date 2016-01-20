from fractions import Fraction
def isint(input):
    return input.isdigit()

def isfloat(input):
    try:
        return float(input) != None;
    except ValueError:
        return False;


def isfraction(input):
    try:
        return Fraction(input) != None;
    except ValueError:
        return False;


def isstr(input):
    if not isint(input) and not isfloat(input):
        return True
    return False

print isint("3.14")
print isfloat("-5.3")
print isstr("3.14")
print isfraction("3242342/22222")