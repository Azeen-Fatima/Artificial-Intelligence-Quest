Python 3.8.8rc1 (tags/v3.8.8rc1:dfd7d68, Feb 17 2021, 11:01:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello World!")
Hello World!
>>> 
>>> #this is a comment
>>> 
>>> x=1  #value of x i 1
>>> 
>>> #multiple statements on single line
>>> print("Hello");print("world")
Hello
world
>>> 
>>> #indentation concept
>>> if x>0:
 print("Single space indentation")
 print("Single space indentation")

Single space indentation
Single space indentation
>>> if x>0:
	 print("Space+tab indentation")
	 print("Space+tab indentation")

Space+tab indentation
Space+tab indentation
>>> 
>>> #data types
>>> a=123
>>> type(a)
<class 'int'>
>>> b=-0
>>> type(b)
<class 'int'>
>>> c=1.36
>>> type(c)
<class 'float'>
>>> d=-2.65
>>> type(d)
<class 'float'>
>>> e=1.25-10
>>> type(e)
<class 'float'>
>>> 
>>> #complex numbers
>>> y=complex(1,2)
>>> type(y)
<class 'complex'>
>>> print(y)
(1+2j)
>>> z=1+2j
>>> type(z)
<class 'complex'>
>>> z=1+2J
>>> type(z)
<class 'complex'>
>>> 
>>> #Boolean type
>>> 
>>> x=true
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    x=true
NameError: name 'true' is not defined
>>> x=True
>>> type(x)
<class 'bool'>
>>> x=False
>>> type(x)
<class 'bool'>
>>> 
>>> #strings
>>> str1="String1"  #string start and end with double quotes
>>> print(str1)
String1
>>> str2='string2'   #string start and end with single quote
>>> print(str2)
string2
>>> str3='azeen"   #start with single and end with double quotes
SyntaxError: EOL while scanning string literal
>>> str3="azeen'   #start with double and end with single quote
SyntaxError: EOL while scanning string literal
>>> 
>>> str4= 'Day"s'   #double quote within single quote
>>> print(str4)
Day"s
>>> str5="Day's"     #single quote within double quote
>>> print(str5)
Day's

>>> #special characters in strings
>>> print("This is a backslash (\\) mark")
This is a backslash (\) mark
>>> print("this is tab \t key")
this is tab 	 key
>>> print("These are \'single quotes\'")
These are 'single quotes'
>>> print("These are \"Double quotes\"")
These are "Double quotes"
>>> print("This is new line\nNew line")
This is new line
New line
>>> 
>>> #string indices and accessing elements
>>> string1=Azeen Fatima
SyntaxError: invalid syntax
>>> string1="Azeen Fatima"
>>> print(string1[0])  #print first element which is at 0th index
A
>>> print(string1[-11])	#first element from right counting
z
>>> print(string1[6])
F
>>> print(string1[20])	#out of range
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    print(string1[20])	#out of range
IndexError: string index out of range
>>> 
>>> #Creating lists
>>> my_list1 = {5,12,13,15}	#all integer values
>>> my_list2 = {'red','blue','green'}	#all strings
>>> my_list3 = {2,'yellow',12.6}	#mix values
>>> print(my_list1);print(my_list2);print(my_list3)
{13, 12, 5, 15}
{'red', 'green', 'blue'}
{'yellow', 2, 12.6}
>>> my_list=[]
>>> print(my_list)
[]
>>> 
>>> #list indices
>>> print(my_list1[1],my_list2[0])
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    print(my_list1[1],my_list2[0])
TypeError: 'set' object is not subscriptable
>>>  print(my_list1[1],my_list1[0])
 
SyntaxError: unexpected indent
>>> my_list1[0]
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    my_list1[0]
TypeError: 'set' object is not subscriptable
>>> color_list = ["red","black","white","yellow"]
>>> color_list[0]
'red'
>>> print(color_list[1],color_list[2])
black white
>>> print(color_list[-1])
yellow
>>> 
>>> #list slices
>>> print(color_list[:3])
['red', 'black', 'white']
>>> print(my_list1[1:4])
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    print(my_list1[1:4])
TypeError: 'set' object is not subscriptable
>>> print(color_list[:])
['red', 'black', 'white', 'yellow']
>>> 