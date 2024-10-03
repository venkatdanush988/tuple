"""
7) Write a program to get the tuple values in a single line separated by space and count the nuber of times the given x value is present in the given tuple.
Sample Input:
1 2 3 1 2 3 4 1 2 1
1
Sample Output:
4

"""
n = int(input("Enter the number of tuple elements: "))
elements = []

for _ in range(n):
    element = int(input("Enter element: "))
    elements.append(element)

tuple_elements = tuple(elements)
x=int(input("enter a number to count the no of times is repeated"))
y = tuple_elements.count(x)
print(f"{x} is repeated {y} times")
