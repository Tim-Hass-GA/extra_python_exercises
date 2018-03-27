# Reverse Strings in a Sentence

# Given a string, implement a program that will reverse the order of the characters
# in each word within a sentence while still preserving whitespaces and initial word order.

# Example:
# Input: "Let's do a coding challenge"
# Output: "s'teL od a gniedoc egnellahc"


# *** your code here ***
######## reverse
def reverse_string(string):
  new_sentence = string.split(" ")
  for i in new_sentence:
    new_sentence
  return new_sentence[::-1]

print(reverse_string("Let's do a coding challenge"))

# OUTPUT ['challenge', 'coding', 'a', 'do', "Let's"]

######## reverse
def reverse_string2(string):
  for i in string:
    new_sentence2 = string[::-1]
  return new_sentence2

print(reverse_string2("Let's do a coding challenge"))

# OUTPUT egnellahc gnidoc a od s'teL

######## reverse
def reverse_string3(string):
  words = string.split(" ")
  new_word = [word[::-1] for word in words]
  new_sentence3 = " ".join(new_word)
  return new_sentence3

print(reverse_string3("Let's do a coding challenge"))

# OUTPUT s'teL od a gnidoc egnellahc

def reverse_string4(string):
    return " ".join(word[::-1] for word in string.split(" "))
print(reverse_string4("Let's do a coding challenge"))
