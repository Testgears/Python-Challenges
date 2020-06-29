#This is a welcome message for the user
print ("Welcome!\nThis is an Armstrong number Checking Machine.\n")

#This is a function to ensure that the user enters only integers
def inputNumber(message):
    while True:
        try:
       	    userInput = int(input(message))       
        except ValueError:
       	    print("This is not a number! Try again.")
       	    continue
        else:
       	    return userInput 
       	    break 

#This is asking for the user input
number = inputNumber("Enter the number that you want to check:")

#This is converting the integer received from the user input to a string. So that the string function can be called on it.
s_number = str(number)

#This is getting the number of digits
exponent = len(s_number)

#This is creating an empty list. We would add the numbers to be added to this list.
adding_list = []

'''This for loop block is doing the following
1. Converting each character from 's_number' variable back to an integer.
2. Raising each converted integer by the exponent and storing in variable 'power'.
3. Adding the contents of the power variable into the 'adding_list' list.
'''
for d in s_number:
	digit = int(d)
	power =  digit ** exponent
	
	adding_list.append(power)

#This is calling the sum function on this list to find the sum of the items in this list.
result = sum(adding_list)

#Thus is to check if the sum is equal to the given number
if result == number:
	print ("Congratulations! This is an Armstrong number")
else:
	print ("Sorry, This is not an Armstrong number! Try again")