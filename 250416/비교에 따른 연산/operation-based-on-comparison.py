inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])
c = b/a

if a > b:
    print(a*b)
else:
    print(f'{c:.0f}')