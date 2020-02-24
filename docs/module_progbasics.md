# Programming Basics questions

## Computer science

### Data structures

#### What is the purpose of a list (array in some programming languages) data structure? Name some methods of it!

A list is a data structure in Python that is mutable, ordered sequence of elements. Each element or value inside if a list called an item. Use [] square brackets. List are great to use when you want to work with many related values. They enable you to keep data together, condense you code, and perform the same methods and operations on multiple values at once.
methods : .sort(), .index(), .append(),

#### What is the difference between a list/array and a set?

Sets unlike list, cannot have multiple occureences of the same element and it stores unordered value and not indexed.

#### What is the purpose and methods of a dictionary/map data structure?

Use {} curly brackets to construct the dictionary and [] square brackets to index it. Seperate the key and value with colons with commas. 

A dictionary maps a set of objects(keys) to another set of objects(value). The keys are unique, so its not ordered, and mutable. Each key-value pair maps the key to its associated value.

"A dictionary consists of a collection of key-value pairs. Each key-value pair maps the key to its associated value."
### Algorithms

#### Fibonacci sequences. Write a method (or pseudo code), that generates the Fibonacci sequences.

 
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

A stack that stores details of the functions called by a program in sequence, so that each function can return on completion to the code that called it.A stack contains information about a function: name, parameter, execution.
its purpose to control the way procedures and function call each oter and control the way they pass parameters to each other


#### What is “Stack overflow”?

Where the amount of memory that the computer is allocated for the stach has run out, and it is in danger over spilling and going into other parts of the memory. Happens when recursive function hasnt got breaking point

#### What are the main parts of a function?
header and body.
header: Def statement, fuction name, parameters, colon. example: def func(parameter):
body: the actions of the function.

### Programming languages - Python  
#### How do you use a dictionary in Python?
Use {} curly brackets to construct the dictionary and [] square brackets to index it. Seperate the key and value with colons with commas. Keys have to be immutable type and unique.
dictionary = {'first_key': my_value, 'second_key': second_value}
#### What does it mean that an object is immutable in Python?
It cannot be changed after it is created.
Some immutable objects for example: string, tuple, integer, float.
#### What is conditional expression in Python?
Conditional expressions are operators that evaluate smt based on a condition being True or False.
#### What are different types of arguments in Python?
deafult argument: func(a=2), keyword argument: func(a, b), variable-lenght argument: func(* for_lists, ** for_dictionaries).
#### What is variable shadowing? (context: variable scope)
It happens when we newly declared variable has the same name on the inner scope as on the outer scope. The program runs correctly, but it can be confusing.
#### What can happen if you try to delete/drop/add an item from a List, while you are iterating over it in Python?
If we delete/drop/add to a list while iterating over it the method might fail, because we changed the number of elements in the list. The loop will skip through some elements, because it doesn't know that an elements was deleted/added, and advances to the next element.
#### What is the "golden rule" of variable scoping in Python (context: LEGB)? What is the lifetime of variables?
Scopes determine the accessibility of variables, and what kind of values they hold.

LEGB stands for Local, Enclosed, Global, Built-in. It is the hierarchy in which python is checking variables (and functions as well).

Variables have different lifetimes, depending on their definiton. For example a local variable exists only within the function, and when that function's execution is finished it doesn't exist anymore.

Golden rules: A variable should be only accessible where we use that certain variable: Using as much local variables as we can, and using global variables as little as we can.

#### If you need to access the iterator variable after a for loop, how would you do it in Python?§
list = []
for iterable in something:
    list.append(iterable)
print(list)

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
It returns True or False(boolen value) whether the value before the in/not in is in the string, list, dictionary so on.
#### What does the + operator mean when used with strings in Python?
it will concatenate 2 string into one.
#### Explain f strings in Python?
F-string are only available in Python 3. The f string is a string formatting program that lets us put variables into the string. We have to use f before the quotation mark and use curly brackets around the variables.

age = 17
print(f"My sister {age} years old.")

#### Name 4 iterable types in Python!

strings, tuples, lists, dictionaries
#### What is the difference between list/set/dictionary comprehension and a generator expression in Python?

The generator yields one item at a time and generate only when it is used. it hasnt got return statement and it saves the state of the function. List comprehensions reserve memory for a whole list, dicti, etc. Generators are memory efficients.

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

Step over: an action to take in the debugger that will step over a give file. If the line contains a function, the function will be executed and the result returned without debugging each line.

Step into: an action to take in the debugging. If the line doesnt contain a function it behaves the same as step over, but if it does the debugger will enter the called function and continue line. 

Step out: An action to take in the debugger that returns to the line where the current function was called
#### How can you start to debug a program from a certain line using the debugger?
You can put the breakpoint on the line. The program will run until the breakpoint and the debugger will start there.

### Version control

#### What are the advantages of using a version control system?
You can view the changes throughout a project, multiple people are able to work on the same code at the same time. You can read every commit and see what happend to the code. 


#### What is the difference between the working directory, the staging area and the repository in git?
Working directory contains the files which are untracked by git. Git doesn't pay attention to these files until you add them to the staging area.
In the staging area files are tracked, which means that git keeps track of the changes that has happened to that file.
Repository: Is a file location where you are hold all the file related to your project.
#### What are remote repositories in git?
Remote repositories are versions of a project in the cloud, e.g. GitHub.

#### Why does a merge conflict occur?
When two commits change the same line differently and the automatic merge can't resolve the issue.
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

## Software design

### Clean code

#### What does clean code mean?

It is a code which is easy to understand and easy to change. (DRY=dont repeat yourself)
#### What steps do we usually do during a clean code refactoring?
step of the clean code:
    name functions and variables well
    remove magic numbers and comments
    apply each step of logic into function
    remove duplicate code

### Error handling

#### What is exception handling?
When our code runs into a line that it couldn't run, instead of crashing, we handle the exception in a meaningful way.

#### What are the basics of exception handling in Python?
We use try and except blocks. The try block catches the exception. If the try cathes an exception it jumps to the except block. We can raise exceptions as well.

#### In which case should we catch an exception? Why?

if you have a suspecious code that may raise exception, you can defend your program by placing the suspecious code in a try block. afte you can put an except statement, followed by a block of code which handles the problem elegantly.

#### What can/should we do with an exception in the ‘except’ block?
when you think that you have a code which can produce an error or to avoid your program to be crashed.
#### What does the else and finally statement do in a try-except block in Python?

the finally clause is always ececuted before the try statement whether the statement is true or false. 
else is executed only if the statements in the try block doesnt raise an exception.

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
