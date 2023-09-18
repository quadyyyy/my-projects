n = int(input())

a = 10 * (n % 10)
n = n // 10

a += n % 10
n = n // 10

a -= n

print(1 - a)