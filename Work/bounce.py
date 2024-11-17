#!/usr/bin/python.py
# bounce.py
# A rubber ball is dropped from a height of 100 meters and each time it hits 
# the ground, it bounces back up to 3/5 the height it fell. Write a program 
# bounce.py that prints a table showing the height of the first 10 bounces.
# Exercise 1.5

print("10 Bounce heights \r\n")

# Setup Variables
start_height = input("Enter a height for the ball to be dropped from in Meters: ")
bounced_height = float(start_height)

print('The ball is dropped from a height of: ', start_height)

# iterate 10 times
for a_cnt in range(10): 
    # calculate next bounce height
    bounced_height = bounced_height * ( 3 / 5 )
    # print the result
    print("Bounce number ", a_cnt, "comes up", round(bounced_height,2), "M")

