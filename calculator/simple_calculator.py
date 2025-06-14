var1, op, var2 = input("Enter Equation: ").strip().split()

operations = {

    "+": lambda x, y: float(x) + float(y),
    "-": lambda x, y: float(x) - float(y),

    "*" : lambda x, y: float(x) * float(y),
    "x" : lambda x, y: float(x) * float(y),

    "/" : lambda x, y: float(x) / float(y)
        if y != 0 else "Error, division by zero"

}

if op in operations:

    result = operations[op](var1, var2)

    print(f"{result:.2f}")
