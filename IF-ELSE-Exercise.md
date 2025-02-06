Key takeaways: continued

Exercise 1

What is the output of the following snippet?

x = 5
y = 10
z = 8

print(x > y)
print(y > z)


Check
Exercise 2

What is the output of the following snippet?

x, y, z = 5, 10, 8

print(x > z)
print((y - 5) == x)


Check
Exercise 3

What is the output of the following snippet?

x, y, z = 5, 10, 8
x, y, z = z, y, x

print(x > z)
print((y - 5) == x)


Check
Exercise 4

What is the output of the following snippet?

x = 10

if x == 10:
    print(x == 10)
if x > 5:
    print(x > 5)
if x < 10:
    print(x < 10)
else:
    print("else")


Check


Exercise 5

What is the output of the following snippet?

x = "1"

if x == 1:
    print("one")
elif x == "1":
    if int(x) > 1:
        print("two")
    elif int(x) < 1:
        print("three")
    else:
        print("four")
if int(x) == 1:
    print("five")
else:
    print("six")


Check
Exercise 6

What is the output of the following snippet?

x = 1
y = 1.0
z = "1"

if x == y:
    print("one")
if y == int(z):
    print("two")
elif x == y:
    print("three")
else:
    print("four")


Check
Prev Next