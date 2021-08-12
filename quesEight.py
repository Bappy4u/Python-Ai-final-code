
def fact(x: int) -> int:
    if x==0:
        return 0

    res = 1
    for i in range(1, x+1):
        res = res * i

    return res


x = (int(input("Enter the number to get factorial of the number: ")))

print("Factorial of", x, "is",  fact(x))