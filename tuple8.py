"""
8) Write a program to get tuple elements in a single line separated by spaces and print the sum of the elements without using sum() method.
Sample Input:
10 20 30
Sample Output:
60

"""
a = input("Enter elements separated by spaces: ")
b = tuple(map(int, a.split()))
total_sum = 0
for i in b:
    total_sum += i
print("The sum is", total_sum)
