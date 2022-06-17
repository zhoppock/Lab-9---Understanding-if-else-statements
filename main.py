# LargeSmall.py - This program calculates the largest and smallest of three integer values. 
# Declare and initialize variables here
firstNumber = -50;
secondNumber = 53;
thirdNumber = 78;

# Write assignment, if, or if else statements here as appropriate
if firstNumber > secondNumber:
  if firstNumber > thirdNumber:
    largest = firstNumber
    if secondNumber > thirdNumber:
      middle = secondNumber
      smallest = thirdNumber
    elif secondNumber < thirdNumber:
      middle = thirdNumber
      smallest = secondNumber
  elif firstNumber < thirdNumber:
    middle = firstNumber
    largest = thirdNumber
    smallest = secondNumber
    
elif firstNumber < secondNumber:
  if firstNumber > thirdNumber:
    middle = firstNumber
    largest = secondNumber
    smallest = thirdNumber
  elif firstNumber < thirdNumber:
    smallest = firstNumber
    if secondNumber > thirdNumber:
      middle = thirdNumber
      largest = secondNumber
    elif secondNumber < thirdNumber:
      middle = secondNumber
      largest = thirdNumber

# Output largest and smallest number. 
print("The largest value is " + str(largest))
print("The middle value is " + str(middle))
print("The smallest value is " + str(smallest))
