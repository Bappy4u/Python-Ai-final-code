
def product(a: int, b: int) -> int:

    if a * b > 1000:
        return a + b

    return a * b


x = int(input("Enter the number 1: "))
y = int(input("Enter the number 2: "))

print(product(x, y))
