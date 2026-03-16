#Password Strength Detector
#v2 includes more nuanced checks


score = 0 # python cannot calculate score without a starting value
import string # for the string.punctuation (python does not know what string is until imported)


password = input("Enter password: ")

#length check
if len(password) <= 6:
  print("Too short")
  score += 0

elif 6 <= len(password) <= 8:
  score += 1

else: 
  score += 2



#character checks

if password.lower() != password: #checks if lowercase version of variable is equal to original valuable (checkng for at least one uppercase letter)
  score += 1

if any(char.isdigit() for char in password):
  score += 1


if any(char in string.punctuation for char in password): #string.punctuation is  aconstant thus does not need parentheses: imprted "string" into python (see top)
  score += 1


#Strength Check

if score <= 2:
  print("Weak")

elif 3 <= score <= 4:
  print("Medium")

elif   4 < score <= 1000 and 7 > 6:
  print("Strongs")
