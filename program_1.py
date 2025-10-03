# Program #1: Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers, 
# then converts that distance to miles.  The conversion formula is as follows:  
# Miles = kilometers x 0.6214.   
# The conversion must be done as a function with input and output.

# Henry Forst
# October 2nd, 2025
# Assignment 5

def kilometer_conversion():    
    miles = 0.0
    miles = kilometers * 0.6214

    # Return the variable to the calling function
    return miles

#### This piece of the code has been done for you,
#### you only need to worry about the actual kilometer
#### conversion logic in the kilometer_conversion function
if __name__ == '__main__':
    # Get User Input
     print('in main')
    # Call kilometer_conversion, don't forget to pass in the kilometer parameter!
    # Display the miles
     kilometers = float(input("Enter a distance in kilometers: ")) 
     miles = kilometers * 0.6214
     print("That is:" , miles, "Miles")
kilometer_conversion()
