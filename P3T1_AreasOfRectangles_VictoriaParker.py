##This program will calculate the area of two rectangles.
##3/12/2020
##CTI-110 P3T1-Areas Of Rectangles
##Victoria Parker

#Dimensions of rectangle 1.
lenght1 = int(input('Enter the lenght of rectangle 1: '))
width1 = int(input('Enter the width of rectangle 1: '))

#Dimensions of rectangle 2.
lenght2 = int(input('Enter the lenght of rectangle 2: '))
width2 = int(input('Enter the width of rectangle 2: '))

#Calculate the variables.
area1 = lenght1 * width1
area2 = lenght2 * width2

#Output
if area1 > area2:
    print('Rectangle 1 has the larger area.')
else:
    if area2 > area1:
        print('Rectangle 2 has the larger area.')
    else:
        print('Both rectangles have equal area.')
