"""
10) Write the program to count the number of times the given number (x) is present in the given tuple list and print it's factorial value without using factorial() method.
Sample Input:
1 2 3 4 1 5 1
1
Sample Output:
6

"""
input_data = input("Enter numbers separated by spaces: ")
numbers = tuple(map(int, input_data.split()))
x = int(input("Enter the number to count: "))
count_x = numbers.count(x)

factorial = 1
for i in range(1, count_x + 1):
    factorial *= i

print(factorial)
