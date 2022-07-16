<center> <h1> Python Guide </h1> </center>

# Index
### Modules
* [Sys Module](#Sys)
* [Timeit Module](#Timeit)
### Data types
* [Lists](#Lists)
* [Tuples](#Tuples)
* [Dictionary](#Dictionary)
* [Sets](#Sets)
* [Strings](#Strings)
* [Collections](#Collections)
* [Itertools](#Itertools)
* [Lambda functions](#Lambda)
* [Exceptions and errors](#Exceptions)
* [Logging](#)
* [JSON](#)
* [Random Numbers](#)
* [Decorators](#)
* [Generators](#)
* [Threading vs Multiprocessing](#)
* [Multithreading](#)
* [Multiprocessing](#)
* [Function Arguments](#)
* [Shallow vs Deep Copying](#)
* [Asterisk (*) Operator](#)
* [Context Managers](#)
---
# Modules
<center> <h1 id="Sys"> SYS Module </h1> </center>

```python
Input:
    import sys
    sys.getsizeof(,'bytes')

Output:
    n bytes
```
[Back to Index](#)
<center> <h1 id="Timeit"> Timeit Module </h1> </center>

```python
Input:
    from timeit import default_timer as timer
    
    start = timer()
    #code
    stop = timer()
    #The following print statement will return the time it takes to run the code between start and stop
    print(stop-start)

Output:
    #time it took to run
    
```
# Data Types
[Back to Index](#)
<center> <h1 id="Lists"> Lists  </h1> </center>

* Ordered
* Mutable

Common list functions: 
* append()
* insert()
* pop()
* remove()
* clear()
* reverse()
* sort() 

```python
A = [1,2,3]
B = A
B.append(4)
# This does not create a new list, it just assings B to the same list inside the memory
# To fix this you can cast B  'B = list(A)' or do 'B = A.copy()' 
>>> print(A)
[1,2,3,4] 
```
[Back to Index](#)
<center> <h1 id="Tuples"> Tuples  </h1> </center> 

* Ordered
* Immutable 

```python
Input:
    my_tuple = ('a','e','p','p')
    print(my_tuple.count('p'))

Output:
    2
```
[Back to Index](#)
<center> <h1 id="Dictionary"> Dictionary  </h1> </center>

* Key - Value pairs 
* Unordered 
* Mutable
```python
#Keys
mydict.keys() #Returns a list with all the keys inside the dict

#Values
mydict.values() #Returns a list of values inside the dict

#Key and Value
mydict.items() #Returns a lis of key - value pairs

Input:
    #Access values
    mydict = {'key1':'valor','key2':2}
    print(mydict['key2'])

Output:
    2

#Deleting values
del mydict['key']
mydict.pop('key')
```
 [Back to Index](#)
<center> <h1 id="Sets"> Sets  </h1> </center>

* Unordered 
* Mutable
* No Duplicates
```python
#Create an immutable set
frozenset()

Input:
    myset = {1,2,3,4,4}
    print(myset)

Output:
    2,3,1,4 #Is unordered and unique

#Add
myset.add()

#Remove
myset.remove() #This functions fails if the item you are trying to remove is not found on the set
myset.discard()
myset.clear()

#Union, intersection and difference
myset.union(other_set)
myset.intersection(other_set)
myset.symmetric_difference(other_set) #Returns outer join

```

[Back to Index](#)
<center> <h1 id="Strings"> Strings  </h1> </center>

* Ordered
* Immutable

Common String functions:
* strip()
* upper()
* lower()
* startswith() - returns a boolean
* endswith() - returns a boolean
* find() - returns the index where it found the parameter, it will return -1 if the parameter is not on the string
* count() - counts the number of times it can find the parameter on the string
* replace() - returns a new string
* split() - returns a list with every word on the string as an element, the default delimiter is a space


```python
Input:
    #Turn a list into a string
    my_string = 'Hello world, this is a string'
    my_list = my_string.split()
    new_string = ' '.join(my_list)
    #This concatenates each element on the list and puts whatever is on the ' ' between the elements of the list
    print(new_string)

Output:
    'Hello world, this is a string'

#Formatted Strings
#This is a way to input variables in a string
Input:
    var = 'World'
    var2 = 'String'
    print(f'Hello {var}, this is a {var2}')
Output:
    'Hello World, this is a String'
```

[Back to Index](#)
<center> <h1 id="Collections"> Collections  </h1> </center>
