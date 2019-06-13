# input
a = input()
b = input()
c = input()

# compare
if a > b:
    if a > c:
        max_number = a
    else:
        max_number = c
else:
    if b > c:
        max_number = b
    else:
        max_number = c

# outout
print(max_number)
