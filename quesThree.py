

lst1 = []
lst2 = []

# for adding numbers of list use space between numbers. Input: 2 4 6 7 8 9
lst1 = [int(item) for item in input("Enter the list1 of numbers : ").split()]
lst2 = [int(item) for item in input("Enter the list1 of numbers : ").split()]

print("Odd numbers of list1")
for l in lst1:
    if l % 2 != 0:
        print(l)

print("Even numbers of list2")
for l in lst2:
    if l % 2 != 1:
        print(l)

