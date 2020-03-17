# CTI-110
# P3HW1 - Color Mixer
# Ronald Luna
# Date: 3-16-2020


# User enters 2 primary colors
primaryColor1 = input ("Enter primary color 1:")
primaryColor2 = input ("Enter primary color 2:")

# Program mix the color 
if ( primaryColor1 == "red" and primaryColor2 == "blue" ) or ( primaryColor1 == "blue" and primaryColor2 == "red" ):
# Program print the color results    
     print( primaryColor1 + " mixed with " + primaryColor2 + " is purple" )

elif ( primaryColor1 == "red" and primaryColor2 == "yellow" ) or ( primaryColor1 == "yellow" and primaryColor2 == "red" ):
    
     print ( primaryColor1 + " mixed with " + primaryColor2 + " is orange" )

elif ( primaryColor1 == "blue" and primaryColor2 == "yellow" ) or ( primaryColor1 == "yellow" and primaryColor2 == "blue" ):

     print ( primaryColor1 + " mixed with " + primaryColor2 + " is green" )
# Program print error if not a primary color is entered
else:
     print( "One of the colors you entered, " + primaryColor1 + " or " + primaryColor2 + ", is not a primaryColor" ) 



# Pseudocode

# the user enter two primary colors.
# computer process the two entered color. 
# the computer prints the result of the two mixed colors.
# program print an error if one of the numbers is not a primary color.




