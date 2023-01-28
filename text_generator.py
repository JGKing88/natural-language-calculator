import random

plus = lambda a, b: a + b
minus = lambda a, b: a - b
mult = lambda a, b: a * b
div = lambda a, b: a / b
ops = {0: plus, 1: minus, 2: mult, 3: div}
opsign = {0: "+", 1: "-", 2: "*", 3: "/"}

text = ""

for _ in range(100000):
    a = random.randint(0, 10000)
    b = random.randint(1, 10000)
    op = random.randint(0, 3)
    c = ops[op](a, b)
    c = round(c, 9)
    eq = str(a) + " " + opsign[op] + " " + str(b) + " = " + str(c) + "\n"
    text += eq

with open('input.txt', 'w') as f:
    f.write(text)