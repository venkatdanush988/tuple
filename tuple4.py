"""
4) Write a program to get n number of tuple elements from the user in separate lines and print the sum of their values using predefined method.
Sample Input:
3
10
20
30
Sample Output:
60

"""
n = int(input("Enter the number of tuple elements: "))
elements = []

for _ in range(n):
    element = int(input("Enter element: "))
    elements.append(element)

tuple_elements = tuple(elements)
total_sum = sum(tuple_elements)
print("The sum is", total_sum)
