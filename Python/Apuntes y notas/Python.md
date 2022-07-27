<center> <h1> Python Guide </h1> </center>

# Index
### Modules
* [Sys Module](#Sys)
* [Timeit Module](#Timeit)
* [Regular Expression](#Regex) 
### Data types
* [Lists](#Lists)
* [Tuples](#Tuples)
* [Dictionary](#Dictionary)
* [Sets](#Sets)
* [Strings](#Strings)
* [Lambda Functions](#Lambda)
* [Exceptions and errors](#Exceptions)
* [Logging](#Logging)
* [JSON](#JSON)
* [Decorators](#Decorators)
* [Generators](#Generators)
* [Yield Statement](#Yield)
* [Multithreading](#Multithreading)
* [Function Arguments](#Arguments)
* [Context Managers](#Context)
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
<center> <h1 id="Regex"> Regular Expression </h1> </center>
A Regular Expression (RegEx) is a sequence of characters that defines a search pattern.  

<br/>
MetaCharacters: are characters that are interpreted in a special way by a RegEx engine.

* []  Square brackets: Square brackets specifies a set of characters you wish to match.
* .  Period: A period matches any single character (except newline '\n').
* ^  Caret: The caret symbol ^ is used to check if a string starts with a certain character.
* \$  Dollar: The dollar symbol $ is used to check if a string ends with a certain character.
* \* Star: The star symbol * matches zero or more occurrences of the pattern left to it.
* \+ Plus: The plus symbol + matches one or more occurrences of the pattern left to it.


```python

import re
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
#Turn a list into a string
Input:
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
<center> <h1 id="Lambda"> Lambda Functions  </h1> </center>

A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression. It is commonly used to define subfunctions.

```python
#add 10
lambda x: x + 10

#multiply
lambda x,y: x*y

```
[Back to Index](#)
<center> <h1 id="Exceptions"> Exceptions  </h1> </center>
Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. Errors detected during execution are called exceptions and are not unconditionally fatal.

The try statement works as follows:

* First, the try clause (the statement(s) between the try and except keywords) is executed.

* If no exception occurs, the except clause is skipped and execution of the try statement is finished.

* If an exception occurs during execution of the try clause, the rest of the clause is skipped. Then, if its type matches the exception named after the except keyword, the except clause is executed, and then execution continues after the try/except block.

* If an exception occurs which does not match the exception named in the except clause, it is passed on to outer try statements; if no handler is found, it is an unhandled exception and execution stops.

```python
#Basic structure
try:
    a = 5/0
except:
    print('Division by 0 is not posible')

#You can get the type of exception
try:
    a = 5/0
except Exception as e:
    print(e)

#You can specify the type of exception you want to catch
except (RuntimeError, TypeError, NameError):

#One try statement can have multiple exception clauses
try:
    a = 5/1
    b = a + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)

#Finally clause is used as a piece of code that should always run at the end
Input:
    try:
        a = 5/0
    except Exception as e:
        print(e)
    finally:
        print('This will always run')

Output:
    'division by zero'
    'This will always run'
```

[Back to Index](#)
<center> <h1 id="Logging"> Logging  </h1> </center>
Built in module

There are 5 different logging levels:
* debug
* info
* warning
* error
* critical

Only the warning, error and critical levels are printed by default.

```python
import logging
logging.debug('This is a debug message')
logging.info('This is a info message')
logging.warning('This is a warning message')
logging.error('This is a error message')
logging.critical('This is a critical message')
```

[Back to Index](#)
<center> <h1 id="JSON"> JSON  </h1> </center>
JSON stands for JavaScript Object Notation.

Python has a built in Json module to work with it.
Converting python to json converts the python datatypes into their json equivalent.
| Python    | JSON      |
|:----------|:----------|
|dict       | Object    |
|list       | Array     |
|tuple      | Array     |
|str        | String    |
|int        | Number    |
|float      | Number    |
|True       | true      |
|False      | false     |
|None       | null      |

```python
#Convert a dictionary into json 
import json

person = {'name':'Luis', 'Age':25, 'City': 'Mexico city'}
personJSON = json.dumps(person)
```

[Back to Index](#)
<center> <h1 id="Decorators"> Decorators  </h1> </center>
A decorator is a function that takes another function as argument and extends the behavi or of the function without modifying it.
 
```python
Input:
    def start_end_decorator(func):
        def wrapper(*args, **kwargs):
            print('Start')
            func(*args, **kwargs)
            print('end')
        return wrapper

    # The @ sign calls the start_end_decorator function as a decorator for the print_name function and modifies its behavior 
    @start_end_decorator
    def print_name():
        print('name')

    print_name()

Output:
     Start
     name
     end
```
[Back to Index](#)
<center> <h1 id="Generators"> Generators  </h1> </center>
Generator functions are a special kind of function that use the 'yield' statement instead of the 'return' statement. They generate lazy iterators. These are objects that you can loop over like a list. However, unlike lists, lazy iterators do not store their contents in memory.

```python
# Memory benefit of using Generators
Input:
    import sys

    def firstn(n):
        nums = []
        num = 0
        while num < n:
            nums.append(num)
            num += 1
        return nums

    def firstn_generators(n):
        num = 0
        while num < n:
            yield num
            num += 1

    print(sys.getsizeof(firstn(10000)))
    print(sys.getsizeof(firstn_generators(10000)))
Output:
    87616
    112

 # Generating an infinite sequence, however, will require the use of a generator, since your computer memory is finite
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
```

[Back to Index](#)
<center> <h1 id="Yield"> Yield Statement </h1> </center>
The yield statement suspends function’s execution and sends a value back to the caller, but retains enough state to enable function to resume where it is left off.
When resumed, the function continues execution immediately after the last yield run.

This allows its code to produce a series of values over time, rather than computing them at once and sending them back like a list.

We should use yield when we want to iterate over a sequence, but don’t want to store the entire sequence in memory.

```python
Input:
    # A Simple Python program to demonstrate working
    # of yield
    
    # A generator function that yields 1 for the first time,
    # 2 second time and 3 third time
    def simpleGeneratorFun():
        yield 1
        yield 2
        yield 3
    
    # Driver code to check above generator function
    for value in simpleGeneratorFun(): 
        print(value)
Output:
    1
    2
    3
```

[Back to Index](#)
<center> <h1 id="Multithreading"> Multithreading </h1> </center>
A thread is an entity within a process that can be scheduled for execution. Also, it is the smallest unit of processing that can be performed in an OS (Operating System). In simple words, a thread is a sequence of such instructions within a program that can be executed independently of other code. For simplicity, you can assume that a thread is simply a subset of a process!

**Multithreading** is defined as the ability of a processor to execute multiple threads concurrently.
```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor() as executor:
    executor.map(function, iterable)
```

[Back to Index](#)
<center> <h1 id="Arguments"> Function Arguments </h1> </center>
A parameter with an * in a function means you can pass any number of positional arguments.

A paratemer with two ** means you can pass any number of kewyword arguments to the function.

```python
Input:
    def greeting(*args, **kwargs):
        for arg in args:
            print(f'Hello{arg}')

    greeting('tom','bob','tim')

Output:
    Hello, tom
    Hello, bob
    Hello, tim

```
[Back to Index](#)
<center> <h1 id="Context"> Context Managers </h1> </center>
Context managers allow you to automatically handle the setup and teardown phases whenever you’re dealing with external resources or with operations that require those phases.

One common problem you’ll face in programming is how to properly manage external resources, such as files, locks, and network connections. Sometimes, a program will retain those resources forever, even if you no longer need them. This kind of issue is called a memory leak because the available memory gets reduced every time you create and open a new instance of a given resource without closing an existing one.

```python
with expression as target_var:
    do_something(target_var)

#Example:
with open("hello.txt", mode="w") as file:
    file.write("Hello, World!") 
```