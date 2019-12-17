import re
import sys

# Error with "- 743 * X^0  = 2 * X^1 - 4 * X^2"
# Error with more than one expression on right hand side

def absoluteValue(x):
    if (x < 0):
        x *= -1
    return x

def squareRoot(x, PRECISION=0.000001):
    y=1.0
    while (absoluteValue(x / y - y) > PRECISION):
        y = (y + x / y) / 2.0
    return y

def squared(number):
    return number * number

def main():

    # Getting the equation
    equation = sys.argv[1]

    # Splitting the equation in between the rhs and lhs, with '=' as delimiter
    lhs = equation.split('=')[0]
    rhs = equation.split('=')[1]

    # Then I slice my lhs with '+' as a delimiter
    sliced_lhs = lhs.split("+")

    # And finally I loop through the slices and try to find a '-' sign
    final_lhs = []
    for s in sliced_lhs:
        # If I find one I split the string and I add a minus in front
        if "-" in s:
            l = s.split('-')
            l[1] = "-" + l[1]
        else:
            l = s.split('-')
        final_lhs += l

    # Then I do the same thing for the rhs except if I inverse the value of the number by adding a minus
    final_rhs = []
    sliced_rhs = rhs.split("+")
    for s in sliced_rhs:
        if "-" in s:
            s = s[s.find('-'):]
            l = s.split('-')
        else:
            s = "-" + s
            l = [s]
        final_rhs += l

    # Setting a, b and c to infinity by default
    a = float("inf")
    b = float("inf")
    c = float("inf")

    # Then I loop through each element of each side of the equal side
    # and I try to find the values of a, b and c
    for element in final_lhs:
        element = element.strip().replace(" ", "")
        if "X^" in element:
            degree = int(element[element.find("^") + 1])
            if degree is 0:
                c = int(element[:element.find("*")])
            elif degree is 1:

                b = int(element[:element.find("*")])

            elif degree is 2:
                a = int(element[:element.find("*")])

    for element in final_rhs:
        element = element.strip().replace(" ", "")
        if "X^" in element:
            degree = int(element[element.find("^") + 1])
            if degree is 0:
                c = int(element[:element.find("*")])
            elif degree is 1:
                b = int(element[:element.find("*")])
            elif degree is 2:
                a = int(element[:element.find("*")])

    if (a == float("inf")):
        form = str(b) + " * X + " + str(c) 
        if "+ -" in form:
            form = form.replace("+ -", "- ")
        print("Reduced form: " + form + " = 0")
        print("Polynomial degree: 1")
        print("One solution:")
        discriminant = squared(b) - (4 * a * c)
        sol = float(-c) / float(b)
        print(sol)
    else:
        form = str(a) + " * X^2 + " + str(b) + " * X^1 + " + str(c)
        if "+ -" in form:
            form = form.replace("+ -", "- ")
        print("Reduced form: " + form + " = 0")
        print("Polynomial degree: 2")
        discriminant = squared(b) - (4 * a * c)
        if (discriminant > 0):
            print("Two solutions:")
            sol1 = (-b + squareRoot(discriminant)) / (2 * a)
            sol2 = (-b - squareRoot(discriminant)) / (2 * a)
            print(sol1)
            print(sol2)
        elif discriminant == 0:
            print("One solution:")
            sol = -b / (2 * a)
            print(sol)
        else:
            print("No solutions")

main()