"""a, b = map(int,input().split())

if a >= b:
    print(int(True))
else:
    print(int(False))

if a > b:
    print(int(True))
else:
    print(int(False))

if  a <= b:
    print(int(True))
else:
    print(int(False))

if a < b:
    print(int(True))
else:
    print(int(False))

if a == b:
    print(int(True))
else:
    print(int(False))

if a != b:
    print(int(True))
else:
    print(int(False))
"""
input = input()
arr = input.split()
a = int(arr[0])
b = int(arr[1])

print(int(a >= b))
print(int(a > b))
print(int(a <= b))
print(int(a < b))
print(int(a == b))
print(int(a != b))