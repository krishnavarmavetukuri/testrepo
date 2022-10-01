'''
1. Write a program to separate student names belonging to a class alphabetically.
Use appropriate python data type (Should make use of lists and sorting).
a. Test case: Enter student names: ravi, ameen, saraf, rahul, kanaka
b. Student names sorted: [“ameen”, “kanaka”, “rahul”, “ravi”, “saraf”]
(moderate)
'''

stu = input("Enter student names: ")
l = stu.split(",")
l.sort()
print(l)
