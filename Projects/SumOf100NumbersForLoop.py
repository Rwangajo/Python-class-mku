m = input('Enter number to calculate sum ')
m = int (m)
total = 0
for num in range(m+1):
    total = total+num
    print(total)
print('Sum of first ', m, 'numbers is: ', total)
