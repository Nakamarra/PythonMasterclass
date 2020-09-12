age = 26
print("My age is {} years.".format(age))
print(f"My age is {age} years.") # f strings only for python 3.6 and above


print()
print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}""".format(28, 30, 31))


for i in range(1, 13):
	print("No. {0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))


print()

# Add formating to space out the digits (right align)

for i in range(1, 13):
	print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))


print()

# Left Align

for i in range(1, 13):
	print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))


print()

# Center Align

for i in range(1, 13):
	print("No. {0:^2} squared is {1:^3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))

print()

# Formatting after the decimal

print("Pi is approximately {0:12}".format(22/7))
print("Pi is approximately {0:12f}".format(22/7))
print("Pi is approximately {0:12.50f}".format(22/7))
print("Pi is approximately {0:52.50f}".format(22/7))
print("Pi is approximately {0:62.50f}".format(22/7))
print("Pi is approximately {0:72.50f}".format(22/7))

print()

print(f"Pi is approximately {22 / 7:12.50f}.")

pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}.")

print()

item1 = 13.34
item2 = 4.995
item3 = 98.995
total = item1 + item2 + item3 
print("Hello {0}, your total is ${1:6.2f}.".format("Zander", total))

