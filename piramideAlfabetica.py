N, P = input().split(" ")
N = int(N)
if P == "maiusculas":
    z = 0
elif P == "minusculas":
    z = 32
    
for i in range(N):
    for j in range(26 - (i + 1)):
        print(".", end='')
    for q in range(i+1):
        print(chr(65+q+z), end="")
    print()