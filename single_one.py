# Given an array of integers, every element appears twice except for one.
# Implement a program that will print that single one.

# Example: [1,1,2,2,3,3,4,5,5,6,6,7,7] - 4 would be the odd man out

# Note:
# Your algorithm should have a linear runtime complexity.


# *** your code here ***
######### single one
listOfNum = [1,1,2,2,3,3,4,5,5,6,6,7,7]

def filterNums(numList):
  print(list(filter(lambda x: x == 4, numList)))

filterNums(listOfNum)

################
def filterNums2(numList,y):
  print(list(filter(lambda x: x == y, numList)))

filterNums2(listOfNum,4)

################
## steves solution
def find_odd(a):
    return [x for x in a if a.count(x) <2][0]

print(find_odd(listOfNum))
