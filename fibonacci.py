def fibo(n):
  first = 0
  second = 1
  while n>0:
    third = first + second
    first =second
    second = third
    n-=1
    print(third,end=" ")
n= int(input("Enter the number: "))
print("Fibonacci series: ",end=" ")
fibo(n)