"""
3) Write a program to get the tuple elements in a single line separated by spaces and print the number of elements in the given tuple.
Sample Input:
10 20 30
Sample Output:
3

"""
a=int(input("enter tuple elements"))
b=tuple(map(a.split()))
print(b)
