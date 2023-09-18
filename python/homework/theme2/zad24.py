h = int(input())
a = int(input())
b = int(input())

print((h - a) // (a - b) + 1 + 1 % ((h - a) % (a - b) + 1))