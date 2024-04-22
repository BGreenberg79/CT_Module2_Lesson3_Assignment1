# Task 1 Descending Sort

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)
print(grades)

'''
The grades were sorted in order through the sort method, but as that defaults to an ascending
order I had to specify it as descending through using the reverse=True parameter 
'''

# Task 2 Mean Average

mean = sum(grades) / len(grades)
print(mean)

'''
The variable mean is created and assigned to identify the mean average of the grades list.
The variable uses the sum function to add up all of the grades listed and is divided by the
total number of values found in the list, which is identified by the len funchtion.
'''

# Task 3 Replace values under 80 with Failed

print(len(grades))
grades[7:10] = "Failed", "Failed", "Failed"
print(grades)

'''
I printed the len function to quickly count how many values were in the list and 
was able to use my earlier reverse sort to find out I only had to replace the last three values.
From those two pieces of information I was able to figure out that the slice and index 
functions I were using would start at index 7 and end at 10 given Python's rules where 
index starts counting from 0 and the end of slice adds 1. I then realized that to replace all 
three grades I would need to type out the "Failed" string three times so there was one value
for each replaced grade. Otherwise python woud have tried to evenly distribute the string for 
all three values and it would create an errant bug.
'''