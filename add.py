#!/usr/bin/env python3
print()
print('changing of variables in an array')
a =[1, 2, 3]   
print('the given array is')
print(a)
print('the array changed : ')                       

a[0] = 5                  
a[2]=8
print(a)

print()
print()

print('addition of two numbers')
num1=input('enter the first number :  ')
num2=input('enter the second number :  ')
sum=float(num1)+float(num2)
print('sum of {0} and {1} is {2}'.format(num1,num2,sum))

print()
print()

print('prime numbers in an interval')

lower=1
upper=100
print('prime numbers between', lower, 'and', upper, 'are :  ')
for num in range(lower,upper+1):
 if num>1:
  for i in range(2,num):
    if(num % i) == 0:
      break
  else:
    print(num) 
