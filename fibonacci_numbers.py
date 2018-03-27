# Fibonacci numbers   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

# Implment a program that will print a LIST of fibonacci numbers to a specified length.

# Example: fibonacci(10)
# input: number  (desired length of array)
# output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] - the first 10 numbers of the fibonacci sequence

# Hint:
# You may start your array like this:
# list = [0, 1]


# *** your code here ***
def fibonacci2(length):
  listFib = [0,1]
  for i in range(2, length):
    listFib.append(listFib[i-1] + listFib[i-2])
  return listFib

print(fibonacci2(10))


# add the previous two numbers
# 
