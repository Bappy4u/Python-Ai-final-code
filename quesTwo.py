
lst = []

# for adding numbers of list use space between numbers. Input: 2 4 6 7 8 9
lst = [int(item) for item in input("Enter the list of numbers : ").split()]

if lst[0] == lst[len(lst)-1]:
    print("Successful")
