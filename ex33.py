#i = 0
first = int(input("Enter beginning> "))
last = int(input("Enter last> "))
increment = int(input("Enter interval> "))
numbers = []

def appendix(i):
    for i in range(first,last,increment):
        print(f"At the top i is {i}")
        numbers.append(i)
        #i = i+increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
"""while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i+1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")"""
appendix(first)
print ("The numbers: ")

for num in numbers:
    print(num)
