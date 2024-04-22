# Task 1 Which students are in both lists

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

print("Alice attended class and submitted assignment" if "Alice" in submitted and "Alice" in attended else "Alice either didn't submit assignemnt or attend class")
print("Bob attended class and submitted assignment" if "Bob" in submitted and "Bob" in attended else "Bob either didn't submit assignemnt or attend class")
print("Charlie attended class and submitted assignment" if "Charlie" in submitted and "Charlie" in attended else "Charlie either didn't submit assignemnt or attend class")
print("David attended class and submitted assignment" if "David" in submitted and "David" in attended else "David either didn't submit assignemnt or attend class")
print("Eve attended class and submitted assignment" if "Eve" in submitted and "Eve" in attended else "Eve either didn't submit assignemnt or attend class")
print("Frank attended class and submitted assignment" if "Frank" in submitted and "Frank" in attended else "Frank either didn't submit assignemnt or attend class")

print("\nAlice and Charlie were the only two students to both attend class and submit their assignments.")

'''
I used the power of shorthand if statements to as succinctly as possible check for the name 
of each student in both lists. I was careful with the placement of parenthesis for my print 
function, as well as the syntax of "string value" in list for both lists named 
before and after the "and" operator. After examining the output I made another
print statement singling out Alice and Charlie after a "\n" line break to clean up the output.
'''

# Task 2 Check if lists are identical in terms of content regardless of order
# I'm trying to figure out if this prompt is testing for comprehension of is operator or if using sort followed by == so I will test using both
print("\n")

if submitted is attended:
    print("The two lists submitted are identical")
else:
    print("The lists are not identical even if they share content.")

# This method checks if the two lists are identical by having the same object assignment (i.e. list_1 = list_2)

if submitted.sort() == attended.sort():
    print("The two lists are identical even after accounting for order")
else:
    print("The two lists aren't identical evem after accounting for order")

# This method checks if the lists are identical by using the == comparison operator after sorting both lists to ensure order isn't throwing the results off.

# Task 3 remove students from attended who did not submit
# From Task 1 I already know I have to remove Eve and Frank from the list

print("\n")
attended.remove("Eve")
attended.remove("Frank")
print(attended)

# I used the list.remove("value") method to remove Eve and Frank from attended