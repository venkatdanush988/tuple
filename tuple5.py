"""
5) Write a program to get n number of tuple elements from the user in separate line and print the maximum value of the given values.
Sample Input:
3
20
10
30
Sample Output:
30

"""
n = int(input("Enter the number of tuple elements: "))
elements = []

for _ in range(n):
    element = int(input("Enter element: "))
    elements.append(element)

tuple_elements = tuple(elements)
max_element = max(tuple_elements)
print("The maximum element is", max_element)
