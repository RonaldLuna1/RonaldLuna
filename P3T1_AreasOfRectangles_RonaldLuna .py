# Area of Rectangles 
# CTI 110
# Ronald Luna
# 3-11-2020
# This code tells the user which rectangle has the greater area.

# Rectangle 1 dimentions.

length1 = int(input('Enter the lenght of rectangle 1: '))
width1 = int(input ('Enter the width of rectangle 1: '))


# Rectangle 2 dimentions.

length2 = int(input('Enter the lenght of rectangle 2: '))
width2 = int(input ('Enter the width of rectangle 2: '))

# Calculate area of the rectangles.

area1 = length1 * width1
area2 = length2 * width2

# Determine which has the greather area.

if area1 > area2:

    print ('Rectangle 1 has the greater area.')

else:

    if area2 > area1:

        print ('Rectangle 2 has the greater area.')

    else:

        print ('Both have the same area.')

        




