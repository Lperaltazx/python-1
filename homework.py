#Exercise 1

cube = 1000
for i in range(1001):
    if i == 5:
        continue
    print(i)

#exercise 2

for Number in range (1, 102):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break
    if (count == 0 and Number != 1):
        print(" %d" %Number, end = ' ')

#Exercise 3

age = int(input("how old are you"))
if age <= 17:
    print("kids")
elif age >17 and age <= 65:
    print("adult")
else:
    print("seniors")