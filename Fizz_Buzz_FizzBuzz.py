# Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz"
# instead of the number and for multiples of five print "Buzz". For numbers that are multiples of three and five,
# print "FizzBuzz".
# Sample Output :
# 1
# 2
# fizz
# 4
# buzz

i = 1
while (i <= 50):
    if (i % 3) == 0:
        print("Fizz")
    elif (i % 5) == 0:
        print("Buzz")
    elif (i % 3) == 0 and (i % 5) == 0:
        print("FizzBuzz")
    else:
        print(i)
    i = i + 1
