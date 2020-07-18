num = int(input("Enter a number greater than 1: "))
primarylist = []

if num > 1:
    for i in range(2, num+1):
        primary = True
        for ii in range(2, i):
            if i % ii == 0:
                primary = False
        if primary:
            primarylist.append(i)
else:
    print(f"{num} is not a proper number!")
    
print(primarylist)