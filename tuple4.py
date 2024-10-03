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
a=input("enter elements for total sum")
b=tuple(map(int,a.split())
sum=0
for i in b:
  sum+=i
print("the sum is",sum)
  
