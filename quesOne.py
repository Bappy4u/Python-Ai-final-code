
lst = []

# for adding numbers of list use space between numbers. Input: 2 4 6 7 8 9
lst = [int(item) for item in input("Enter the list of numbers : ").split()]

for l in lst:
    if l > 150:
        break
    if l % 5 == 0:
        print(l)
