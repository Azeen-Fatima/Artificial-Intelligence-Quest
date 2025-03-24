Python 3.8.8rc1 (tags/v3.8.8rc1:dfd7d68, Feb 17 2021, 11:01:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> #While loop
>>> count=0
>>> while(count<3):
	count=count+1
	print("Hello Geek")

	
Hello Geek
Hello Geek
Hello Geek
>>> 
>>> #for in loop
>>> print("List Iteration")
List Iteration
>>> l=["geeks","for","geeks"]
>>> for i in l:
	print(i)

	
geeks
for
geeks
>>> #similarly
>>> print("\nTuple Iteration")

Tuple Iteration
>>> t=("Geeks","for","Geeks")
>>> for i in t:
	print(i)

	
Geeks
for
Geeks
>>> #similarly for strings
>>> print("\nString Iterations")

String Iterations
>>> s="Geeks")
SyntaxError: unmatched ')'
>>> s="geeks"
>>> for index in s:
	print(index)

	
g
e
e
k
s
>>> 
>>> #Iterating by index of Sequences
SyntaxError: invalid syntax
>>> 
>>> list=["geeks","for","geeks"]
>>> for index in range(len(list)):
	print(list[index])

	
geeks
for
geeks
>>> #Loop control statement
>>> #Continue statement
>>> 
>>> #Print all letters except 'e' and 's'
>>> for letter in 'geeksforgeeks':
	if letter=='e' or letter=='s':
		continue
	print('Current Letter : ',letter)

	
Current Letter :  g
Current Letter :  k
Current Letter :  f
Current Letter :  o
Current Letter :  r
Current Letter :  g
Current Letter :  k
>>> 
>>> #Break statement
>>> #break loop as soon as it see 'r'
>>> for letter in 'geeksforgeeks':
	if letter=='r':
		break
	print('Current Letter : ',letter)

	
Current Letter :  g
Current Letter :  e
Current Letter :  e
Current Letter :  k
Current Letter :  s
Current Letter :  f
Current Letter :  o
>>> 
>>> #Creating functions
>>> def my_Function():
	print("Hello from function")

	
>>> my_Function()
Hello from function
>>> 
>>> #Function with parameters
>>> def my_function(fname):
	print(fname+"Refsnes")

	
>>> my_function("Emil")
EmilRefsnes
>>> my_function("Tobias")
TobiasRefsnes
>>> my_function("Linus")
LinusRefsnes
>>> 
>>> #Defult paramter value
>>> def my_funCtion(country="Norway"):
	print("I am from "+ country)

	
>>> my_funCtion("Pakistan")
I am from Pakistan
>>> my_funCtion()
I am from Norway
>>> 
>>> #Passing a list as parameter
>>> def My_function(food):
	for x in food:
		print(x)

		
>>> fruits=["apple","bnana","cherry"]
>>> My_function(fruits)
apple
bnana
cherry
>>> 
>>> #Return values
>>> def return_function(x):
	return 5*x

>>> return_function(3)
15
>>> return_function(9)
45
>>> return_function(0)
0
>>> #Keyword arguments
>>> def keyword_function(child1,child3,child2)
SyntaxError: invalid syntax
>>> def keyword_function(child1,child3,child2):
	print("The yougest child is " + child3)

	
>>> keyword_function(child1="Azeen",child2="Rubab",child3="Farwa")
The yougest child is Farwa
>>> 
>>> #Classes and Objects
>>> class MyClass:x=5

>>> p1=MyClass()print(p1.x)
SyntaxError: invalid syntax
>>> 