"""
6) Write a program to get n number of values from user in separate line and print the minimum value of the given tuple.
Sample Input:
3
20
30
10
Sample Output:
10

"""
n = int(input("Enter the number of tuple elements: "))
elements = []

for _ in range(n):
    element = int(input("Enter element: "))
    elements.append(element)

tuple_elements = tuple(elements)
min_element = min(tuple_elements)
print("The minimum element is", min_element)
