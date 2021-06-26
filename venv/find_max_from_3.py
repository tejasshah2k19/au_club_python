a = int(input("Enter no"))
b = int(input("Enter no"))
c = int(input("Enter no"))

# or

if a >b and a>c:
    print(a," is max")
elif b>a and b>c:
    print(b," is max")
elif c>a and c>b:
    print(c," is max")
else:
    print("All Are Same")