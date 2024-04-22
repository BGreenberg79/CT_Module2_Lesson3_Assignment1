# Task 1 Extract Week 2

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]  
print(temperatures[7:14])

'''
The second week accounts of the 8th to 14th values and to get this 
output we need to account for python's index starting at 0 before the
colon and adding 1 after the colon
'''

# Task 2 Extract all temperatures above 100
# The values are already sorted ascending but if they weren't I would use the temperatures.sort() method

print(len(temperatures))
print(temperatures[-6:])

''' 
I print the len function to determine how long the list was and then after examining the 
prompt I realized that only the last 6 values  were above 100 so before the colon I listed -6 
and after the colon I left the slice blank.
'''

# Task 3 Reverse List and Days 5 to 10

temperatures.sort(reverse=True)
# This function now reverses the list to flip the days, which now makes them descending

print(temperatures[4:10])
'''
This print statement indexes the 5th to 10th day by starting the count from index 0
(giving us the 4 before the colon for the 5th day start) and stopping on the 10th day 
by adding 1 at the end [5th, 6th, 7th, 8th, 9th, 10th]
'''
