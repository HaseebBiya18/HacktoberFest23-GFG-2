import random as r
n = int(input("Give size of the array: "))
if n==0:
  n = int(input("Please give a valid input: "))
a = [int(input()) for i in range(n)]
print(max(a))
