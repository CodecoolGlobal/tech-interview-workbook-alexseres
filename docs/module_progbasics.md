# Programming Basics questions

## Computer science

### Data structures

#### What is the purpose of a list (array in some programming languages) data structure? Name some methods of it!

List is a collection, A list is a data structure in Python that is mutable, ordered sequence of elements. Each element or value inside if a list called an item. Use [] square brackets. List are great to use when you want to work with many related values. They enable you to keep data together, condense you code, and perform the same methods and operations on multiple values at once.
methods : there are certain operation you can do witn lists. These opearation include indexing, slicing, adding, multiplying, checking for membership, even in Python with there some useful built in functions e.g.: finding the length of a seguence or finding largest or smallest element of the list 



#### What is the difference between a list/array and a set?

Sets unlike list, cannot have multiple occureences of the same element and it stores unordered value and not indexed.

#### What is the purpose and methods of a dictionary/map data structure?

Dictionary in Python is an unordered collection of data values, used to store data values like a map, which unlike other Data Types that hold only single value as an element,
 Dictionary holds key:value pair. Dictionary elements are accessed by the keys. Key value is provided in the dictionary to make it more optimized.
A dictionary maps a set of objects(keys) to another set of objects(value). The keys are unique, so its not ordered, and mutable. Each key-value pair maps the key to its associated value.
You can define a dictionary by enclosing a comma-separated list of key-value pairs in curly brackets. A colon seperarates eacg key from its associated value




### Algorithms

#### Fibonacci sequences. Write a method (or pseudo code), that generates the Fibonacci sequences.

There for way to perform Fibonacci sequence.: Iterative, naiveRecursive, RecursiveMemoizaition, tailRecursive
 
iterative
def f(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

recursiveMemoization:
factorial_memo = {}
def factorial(k):
    if k < 2: return 1
    if k not in factorial_memo:
        factorial_memo[k] = k * factorial(k-1)
    return factorial_memo[k



recursive: 
def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    elif n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 


#### How do you find a max value in a list/array if you can’t use any built-in functions?

def maximum(lst):
    maxi = lst[0]
    for num in lst:
        if maxi < num:
            maxi = num

 
#### How do you find the average of values in a list/array if you can’t use any built-in functions?

def average(lst):
    sum_of_list = 0
    len_of_list = 0
    for item in lst:
        sum_of_list += item
        len_of_list += 1
    average = sum_of_list/len_of_list
#### What do we call an *in-place* sort?

A sorting algorithm, which is only modifying the order of the elements within an object.

#### Explain an algorithm which sorts a list!

I define a list and I put in an empty list in the function, and I create a variable which is the first element of the defined list in a while loop. after I put the defined list in a for loop and looping thorugh all of its elements and I match the variable with all of its elements if is bigger. If is bigger, it will take the value of the elements. It takes the biggest valiue of the list, put into the empty list and remove it from the defined list.

def sort_list(lst):
    new_list = []
    while lst:
        minimum = lst[0]
        for x in lst:
            if x < minumum:
                minimum = x
        new_list.append(minimum)
        lst.remove(minimum)
    
    return new_list




### Programming paradigms - procedural

#### What is the call stack?

-The call stack is a dynamic Data structure maintained inside the computer's RAM by the operating system
A stack that stores details of the functions called by a program in sequence, so that each function can return on 
completion to the code that called it.A stack contains information about a function: name, parameter, execution.
its purpose to control the way procedures and function call each oter and control the way they pass parameters to each other
-sometimes it refered as machine stack, or execution stack or stack.

#### What is “Stack overflow”?
-Stack overflow is a runtime error that happens when a program runs out of memory in the call stack, 
and it is in danger over spilling and going into other
parts of the memory. Happens when recursive function hasnt got breaking point.

#### What are the main parts of a function?
-A function is a group of related statments that perform a specific task. It helps break our program into smaller and modular chunks
It consists a header and a body:
    -Header:
	-Keyword 'def' that makrs the start of the function header
	-a function name to uniquely identify the function. 
	-parameters(arguments) through which we pass values to a function. They are optional
	-A colon':' to mark the end of the function header	
    -Body:
	-optional documentation string docstring to describe what the function does
	-One or more pythin statemenrs that make up the function body
	-an optional return statement to return a value from the function
	



### Programming languages - Python  
#### How do you use a dictionary in Python?

-A dictionary is a collection which is unordered, changeable and indexed it consists
a key and value pair
-Each key is separated from its value by a colon(:), the items are separated by commas, and
the whole thing is enclosed in curly braces.Keys are unique within the dictionary while values may not be
The values of dictonary can be any type, but the keys must be of an immutable data type
such as strings, numbers. You can perform task such as access items: -by referring to its key name
	inside square prackets : x = thisdict["mode"]
	or change values: thisdict["year"] = 2020
	or even you can iterate though in a dict: for x in thisdict:
						      print(x) 	  
									





#### What does it mean that an object is immutable in Python?
-It means that after you create an object and assign some value to it, you cant modify that value.
Some immutable objects for example: string, tuple, integer, float.

#### What is conditional expression in Python?
-Conditional expression are features in Python, which perform different actions depending whether
a programmer-specified boolean condition evaluates to true or false. in Python conditional
expressions consist and if or/ and else, or if else.  
    example:
	if condition:
    	    x = true_value
	else:
	    x = false_value


#### What are different types of arguments in Python?
Default arguments:
    Sometimes we may want to use parameters in a function to provide a value for them. Default 
    arguments which assumes a default value if a value is not supplied as an argument while
    calling a function.
		deafult argument: func(a=2)

Keyword arguments:
    in function, the values passed through arguments are assigned to parameters in order by their position.
    With k.a. we can use the name of the parameter irrespective of its position while calling the function
    to supply the values. All the keyword arguments must match one of the arguments accepted by the function 
	keyword argument: func(a, b)
	    print (a + " and " + b + " are friends")

Variable-length arguments:
    Sometimes you may need more arguments to process function then you mentioned in the definition
    If we dont know in advance about the arguments needed in function, we can use v-l. a. also called
    arbitrary a.. For the asterisj is placed before a parameter in function definition which 
 	variable-lenght argument: func(* for_lists, ** for_dictionaries).


#### What is variable shadowing? (context: variable scope)
-It happens when we newly declared variable has the same name on the inner scope as on the outer scope. The program runs correctly,its a bad practice, it can be confusing.



#### What can happen if you try to delete/drop/add an item from a List, while you are iterating over it in Python?
If we delete/drop/add to a list while iterating over it the method might fail and we get a StopIteration or Runtime error, because we changed the number of elements in the list. 
The loop will skip through some elements, because it doesn't know that an elements was deleted/added, and advances to the next element.
-We can use list comprehension to avoid this problem by creating a new list variable or we can use slicing



#### What is the "golden rule" of variable scoping in Python (context: LEGB)? What is the lifetime of variables?
Scopes determine the accessibility of variables, and what kind of values they hold.

LEGB stands for Local, Enclosed, Global, Built-in. It is the hierarchy in which python is checking variables (and functions as well).

Variables have different lifetimes, depending on their definiton. For example a local variable exists only within the function, and when that function's execution is finished it doesn't exist anymore.

Golden rules: A variable should be only accessible where we use that certain variable: Using as much local variables as we can, and using global variables as little as we can.




#### If you need to access the iterator variable after a for loop, how would you do it in Python?§      // check with mentor
 

I would create an empty list and I would append with the iterables into it. and You can access any iterable variable in that list.


#### What type of elements can a list contain in Python?
A list can contain stirngs, integers, floats, tuples, dictionaries, sets.


#### What is slice operator in Python and how to use?

Returns the part of string or list  from the n'th character to the m'th character. Creates a slice object representing the set of indices specified by range(start, stop, step).
start: starting integer where the slicing of the object starts. 
stop: integer until whoch the slicing takes place.
step:integer a value which determines the increment between each index for
[start: stop: step]

#### What arithmetic operators (+,*,-,/) can be used on lists in Python? What do they do?
+ operator will add two lists together.
* operator will multiply a list, only integers in list.
- and / cannot be used.

#### What is the purpose of the in and not in membership operators in Python?
-Membership operators are operators used to validate the membership of a value
It test for membershop in a seqquence such as strings, lists or tuples.
	-'in' operator is used to check if value exists in a sequence or not. Evaluates to true if a variable
	 in the specified sequence and false otherwise
	-'not' operator- Evaluates to true if it does not finds a variable in the specified
	sequence and false otherwise.

#### What does the + operator mean when used with strings in Python?
-It will concatenate 2 string into one.
string1 = 'one'
string2 = 'two'
string3 = string1+string2
print(string3)
	onetwo

#### Explain f strings in Python?
F-string are only available in Python 3.It is a Literal String Interpolation, The f string is a string formatting program that lets us put variables into the string. We have to use f before the quotation 
mark and use curly brackets around the variables. f-strings are faster than the two most commonly used string formatting mechanisms, which are % formatting and str.format().

age = 17
print(f"My sister {age} years old.")

#### Name 4 iterable types in Python!
An iterator is an object that contains a countable number of values. It can be iterated upon, meaning that you can
traverse through all the values.


Iterable types: strings, tuples, lists, dictionaries


#### What is the difference between list/set/dictionary comprehension and a generator expression in Python?
-There is a lot of work in building an iterator in Python. We have to implement a class with __iter__() and __next__() method, keep track of internal states, and raise StopIteration when there are no values to be returned.
This is both lengthy and counterintuitive. Generator comes to the rescue in such situations.
Python generators are a simple way of creating iterators. All the work we mentioned above are automatically handled by generators in Python.
-The generator yields one item at a time and generate only when it is used. it hasnt got return statement,instead it has a yield statement and it saves the state of the function.
 List comprehensions reserve memory for a whole list, dicti, etc. Generators are memory efficients.

#### Does the order of the function definitions matter in Python? Why?

No, it doesnt. all matters is that we declare all functions before we call any of them. It only gets executed when we call them. We can make an order as we put in the main function.

#### What does unpacking mean in Python?

when the length of the data type is very obvious, you can pass in the exact number of variables as the number of values in the data type to unpack values.

e.g.:
my_info = ["Alex", "Seres", 25, "Budapest"]

name, surname, age, place = my_info

# Result
>>> name
'Alex'
>>> surname
'Seres'
>>> age
25
>>> place
'Budapest'

#### What happens when you try to assign the result of a function which has no return statement to a variable in Python?

the variable's value will be None-type


## Software engineering

### Debugging

#### What techniques can you use while debugging a program in Python?

Doctest: defining tests for specific parts in-code.
Printing: you can print specific variables/lists/ect while running the code to see how they are changing real-time.
Rubber duck method: explaining the code line by line.
Debug tool: you can use it to go through the code line by line and track the things you think might cause the error.
linter = analyse source code to flag programming erros, bigs, and suspicious code

#### What does step over, step into and step out mean while using the debugger?

Step over: an action to take in the debugger that will step over a given  file. If the line contains a function, the function will be executed and the result returned without debugging each line.

Step into: an action to take in the debugging. If the line doesnt contain a function it behaves the same as step over, but if it does the debugger will enter the called function and continue line. 

Step out: An action to take in the debugger that returns to the line where the current function was called
#### How can you start to debug a program from a certain line using the debugger?
You can put the breakpoint on the line. The program will run until the breakpoint and the debugger will start there.

### Version control

#### What are the advantages of using a version control system?
-Automatic backups: If you accidentally delete some file (or part of a file) you can undel
ete it. If you change something and want to undo it, the VCS can do so.
-Sharing on multiple computers: VCSes are designed to help multiple people 
collaboratively edit text files. This makes sharing between multiple computers (say your de
sktop and laptop) particularly easy. You do not need to bother if you always copied the new
est version; the VCS will do that for you. Even if you are offline and change files on 
both computers, the VCS will merge the changes intelligently once you are online.
-Version control and branching: Say you published some class notes as a pdf and
 want to fix some typos in them while simultaneously working on the notes for next 
year. No problem. And you only need to fix the typos once, the VCS will merge them to 
the other versions.


#### What is the difference between the working directory, the staging area and the repository in git?
-The working directory is simply, your current local directory that you are working on. e.g 
if you have master, dev and yourname-dev as your remote branches, if you checkout 
from dev to yourname-dev, yourname-dev is now your working directory if you checkout from this (yourname-dev) working directory to ano
ther say dev, dev is now your new working directory.
-In the staging area files are tracked, A staging step in git allows you to continue 
making changes to the working directory, and when you decide you wanna interact with version control, it allows you to record changes in small commits.
Repository: Is a file location where you are hold all the file related to your project.
#### What are remote repositories in git?
A remote in Git is a common repository that all team members use to exchange their changes. In most cases, such a remote repository is stored on a 
code hosting service like GitHub or on an internal server.

#### Why does a merge conflict occur?
-Conflicts generally arise when two people have changed the same lines in a file, or if one 
developer deleted a file while another developer was modifying it. In these cases, 
Git cannot automatically determine what is correct. Conflicts only affect the developer
 conducting the merge, the rest of the team is unaware of the conflict. 
Git will mark the file as being conflicted and halt the merging process. It is then the developers' responsibility to resolve the conflict.
#### Through what series of commands could you put a new file into a remote repository connected to your existing local repository?
touch newfile
git add newfile
git commit -m "message"
git push origin master
#### What does it mean atomic commits and descriptive commit messages?
Atomic commit means that you commit every logical block that you wrote. 
Descriptive commit messages describe the commit with details.
#### What’s the difference between git and GitHub?
Git is a version controll software, that is used for tracking changes in the code.
Github is an online server for hosting git repositories in the cloud.
"Its like difference between porn and pornhub" -I had to write this down, sorry.

## Software design

### Clean code

#### What does clean code mean?

It is a code which is easy to understand and easy to change. (DRY=dont repeat yourself)
It is easy to understand the execution flow of the entire application
It is easy to understand how the different objects collaborate with each other
It is easy to understand the role and responsibility of each class
It is easy to understand what each function does
It is easy to understand what is the purpose of each expression and variable

#### What steps do we usually do during a clean code refactoring?
step of the clean code:
    name functions and variables well
    remove magic numbers and comments
    apply each step of logic into function
    remove duplicate code

### Error handling

#### What is exception handling?
-An exception can be defined as an unusual condition in a program resulting in the interruption in the flow of program.
Whenever an exception occurs, the program stops the execution and thus the further code is not exexuted, therefore an
exception is the run-time errors that are unable to handle to Python script An exception is a Python object that represents
an error
-Python provides a way to handle the exception so that the code can be executed without interruption. If we do not
handle the exception, the interpretes doesnt execute all the code that exists after the exception.
#### What are the basics of exception handling in Python?
We use try and except blocks. The try block catches the exception. If the try cathes an exception it jumps to the except block. We can raise exceptions as well in the except block .

# import module sys to get the type of exception
import sys


randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)


#### In which case should we catch an exception? Why?
-Exceptions should be used for a situation where a certain method or dunction could not execute normally.
For example, when it encounters broken input or when a resource(e.g. a file) is unavailable. Use 
exceptions to signal the caller that you faced an error which you are unwilling or unable to handle. The exception
is then passed to the caller who has the chance to either handle the exception or pass it on.

#### What can/should we do with an exception in the ‘except’ block?
Because in the except block were are able to handle the error, whereares in the try block we are able to test.

#### What does the else and finally statement do in a try-except block in Python?

-the finally block runs after the try..exceplt block regardless if an error was catched or not.
-We should ise finally to make sure files or resources are closed or released regardless of whether an exception occurs, even if you dont catch the exception. 
## Software Development Methodologies

#### What is the main goal of a retrospective meeting?
Talking about the positive and negative things that occured during the week and getting an action item that we can focus on on the next week.
This is good to help teams improve their working culture.
## Programming environment

### Unix

#### What is MAC OS X and what is XNU?
The Mac OS X is the operating system of the Mac and the kernel of is the XNU kernel
    the kernel is the main component that control everything within OS.
    Mac OS X since 2001 has been derived from UNIX.
#### What do we call the shell in Mac OS X?

Mac OS X comes with the Bourne Again Shell (bash) as the default shell. We can call it Terminal. Also includes the Tenex C shell(csh), the Korn shell(ksh), and the Z shell (zsh)
#### What does root means in a Mac OS X environment?
A root is a user account to perform tasks that require access to all areas of the system. Called superuser. 
#### How do you access your personal files in Mac OS X?
Personal files are in the Home directory,  you can use cd ~. 
#### How can you install an application in Mac OS X?
You can install from the App Store. or from the web. 
#### What is package management in Mac OS X, what are repositories?
Package management keeps track of the users' software packages. It updates you about a new version of an installed software is available.

Mac OS X can use Homebrew as package manager. but not necceseraly.

The repository is storage location from where your OS updates itself, other softwares and installs new softwares. These repositories are hosted on remote servers and they are used for installing and updating software. 
#### How do you navigate in the filesystem with the command line?
pwd: print working directory
ls: list items
cd: change directory
#### What does the following commands do: mkdir, rm, cat, cp, touch?
make directory, new folder
delete folders
concatenate files and print on the standard output (read)
copy
create a new file
#### How can you look up what does a command do in Linux if you have no internet connection?
man command
#### What does the following commands do: head, tail, more, less?
head: print the first ten lines to standard output.
tail: print the last ten lines to standard output.
more: display contents of a text file
less: display contents of a file one page at a time
#### How do you download a file from internet using the terminal?
wget URL
