# Implement a program that prints out a half-pyramid of a specified height.

# Example: pyramid(6)
# input: (6) number of levels high
# output:
     #
    ##
   ###
  ####
 #####
######


# Challenge
# Implement a program that prints out a full-pyramid of a specified height.

# Example: pyramid(6)
# input: (6) number of levels high
# output:
     # #
    ## ##
   ### ###
  #### ####
 ##### #####
###### ######


# *** your code here ***
def pyramid(num):
  # outer loop is num of rows
  for i in range(0, num):
    # inner loop is num of cols
    for j in range(0, i+1):
      print('# ',end='')
    print("\r")

print(pyramid(6))

################
def pyramid2(num):
  # spaces
  k = 2 * num - 2
  # outer loop rows
  for i in range(0, num):
    # spaces
    for j in range(0, k):
      print(end=" ")
    k = k - 2
    # inner loop cols
    for j in range(0, i+1):
      print('# ',end='')
    print("\r")

print(pyramid2(6))

################
def pyramid3(num):
  # spaces
  k = 2 * num - 2
  # outer loop rows
  for i in range(0, num):
    # spaces
    for j in range(0, k):
      print(end=" ")
    k = k - 1
    # inner loop cols
    for j in range(0, i+1):
      print('# ',end='')
    print("\r")

print(pyramid3(6))
