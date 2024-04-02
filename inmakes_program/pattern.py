n=5
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()
print("............... increasing triangle.................")

n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

print("............... decreasing triangle.................")

n=5
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()

print("............... right sided triangle.................")

n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()

print("............... right sided  triangle.................")

n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n):
        print("*",end="")

    print()

print("............... hill triangle.................")

n =5
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    for j in range(i+1):
        print("*",end="")

    print()

print("............... decreasing hill  triangle.................")

n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n-1):
        print("*",end="")
    for j in range(i,n):
        print("*",end="")
    print()


print("............... decreasing/increasing hill triangle.................")

n =5
for i in range(n-1):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    for j in range(i+1):
        print("*",end="")

    print()

for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n-1):
        print("*",end="")
    for j in range(i,n):
        print("*",end="")
    print()
