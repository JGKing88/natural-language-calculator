import random
import torch

plus = lambda a, b: a + b
minus = lambda a, b: a - b
mult = lambda a, b: a * b
div = lambda a, b: a / b
ops = {0: plus, 1: minus, 2: mult, 3: div}
opsign = {0: "+", 1: "-", 2: "*", 3: "/"}

# here are all the unique characters that occur in this text
chars = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", " ", "-", "/", "*", "\n", "="]
vocab_size = len(chars)
# create a mapping from characters to integers
stoi = { ch:i for i,ch in enumerate(chars) }
itos = { i:ch for i,ch in enumerate(chars) }

def encode(s):
    return [stoi[c] for c in s] # encoder: take a string, output a list of integers

def decode(l):
    return ''.join([itos[i] for i in l]) # decoder: take a list of integers, output a string


def get_equation(block_size, output_size):
    a = random.randint(0, 100)
    b = random.randint(1, 100)
    op = random.randint(0, 3)
    c = ops[op](a, b)
    c = round(c)

    input = str(a) + " " + opsign[op] + " " + str(b) + " = "
    dif = block_size - len(input)
    input = torch.cat((torch.zeros(dif, dtype=torch.long), torch.tensor(encode(input), dtype = torch.long)))
    
    output = str(c)
    dif = output_size - len(output)
    output = torch.cat((torch.zeros(dif, dtype=torch.long) - 1, torch.tensor(encode(output), dtype = torch.long)))

    output = output.view(1, -1)
    input = input.view(1, -1)
    return input, output

if __name__ == "__main__":
    print(get_equation())