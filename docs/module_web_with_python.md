# Web with Python questions

## Software design

### Clean code

#### Point out 5 suggestions, how to format an SQL query!
- 1. Avoid giving the same name to both a table and column.
- 2. Use a new line for each seperate query and to use a new line for each separate column after a comma.
- 3. incule the AS keyword for creating aliases, becaise this makes the code more readable
- 4. The name of an obhect in a database for a table or a column should be unique and not too long. Avoid special charactetrs, use only letters, numbers and underscores.
- 5. If the name of the table or column must consist of more than one word, use an underscore to connect them e. g. :person_age


e.g.:


SELECT p.person_id,
       p.first_name,
       p.last_name,
       p.name
  FROM Person AS p 
 WHERE p.Name = 'New York'
    OR p.Name = 'Chicago';


#### What layers can you name in a simple web application?       /not sure
    -Presentation tier: os built in HTML5, can be containing CSS(stylesheets) or Javascript. it communicates with other tiers in application program interface(API).
    -Application tier : can be named as logic tier, is written by a programming language such as Python, and it contains the business logic thats supports the application functions
    -Data tier: the data tier consists of a database and a program managing read and write access to a database. Can be named as the storage tier, such as PostreQSL



### Error handling
#### What error can occur, when an array does not have an element on the requested index?               // not sure
-indexError


#### What is the “finally” block, and how would you use it?
- the finally keyword is used in try..except blocks. It defines a block of code to run when the try...except...else block is final
-the finally block will be executed no matter if the try block raises an error or not
-useful to close objects and clean up resources


#### Why should we catch special exception types?     //notsure
- Use exceptions to signal the caller that you faced an error which you are unwilling or unable to handle. SQL injections attacks allow attackers to steal, modify, delete data informations.  



### Security
#### What is SQL injection? How to protect an application against it?
- is an attack in data-driven applications, which malicious SQL statements are inserted into an entry field field for execution
-Prevention:
    -parameterized queries are a menas of pre-compliling a SQL statement so that you can then supply the parameters in order for the statement to be executed. This method makes it posiible for the database to recognise the code and distingush it from input data. 
    - use command parameters: they are defined by adding placeholder names in SQL commands, which will be later replaced by user input. ASP.NET has a very intuitive and easy-to-use set of APIs for this purpose. 
    -use stored procedures: stored procedures are frequent SQL operations that are stored on the database itself, varying only with their arguments. Stored procedures make it much more difficult for attackers to execute their malicioius SQL, as it is unable to be dynamically inserted within queries
    -use a web application firewall: you can protect against generic SQL injections with a web application by firewall. By filtering potentially dangeruous web requests, web application firewalls can catch and prevent SQL injections




#### What is XSS? How to protect an application against it?
-Cross-site Scripting(XSS) is a web security vulnerabilitu that allows an attacker to compromise the interactions that users have with vulnerable application. It allows an attacker to find the same origin policy, which is designed to segregate different websites from each other .

-Prevention: 
    -escaping user input: taking the data an application has received and ensuring its secure before rendering it for the end user. By escaping iuser input, key characters in the data received by a web page will be prevented from being interpreted in any malicious way. 
    - validation input: is the process pf ensuring an applicaton is rendering the correct data and preventing malicious data frpm doing harm to the site, database, users. 
    -sanitize user input: is allow HTML markup, to ensure data received can do no harm to users as well as your database by scruibbing the date clean of potentially harmful markup, changing unacceptable user input to an acceptable format.

#### How to properly store passwords?
- hash and salt it on the server. 
#### What is HTTPS?
-Hypertext transfre protocol secure(HTTPS) is the sercure version of HTTP, which is the primary protocol used to send data between a web browser and a website. HTTPS is encrypted in order to increase security of data transfer. THis is particularly important when users transmit sensitive data, such as by logging into a back account.
#### What is encryption and decryption?
-encryption: a text gets encoded into an unreadable text.
decryption: Transforming the unreadable text into readable format again. 
#### What is hashing?
in one way, a process where text gets converted into ficed length fignerprint. Hash is a secure way to store data to not be able to be stolen.
#### What is the difference between encryption and hashing? When would you use which?
Hashing is one way only, while encrzption has two way. Encryption can be reversed, hashed data cannot.
#### What encryption methods do you know?
AES: Advanced Encryption Standard, it is a symmetric encryption algorithm that encrypts fixed blocks of data (of 128bits) at a time. The keys used to decipher the text can be 128, 192 256 bit long. 

RSA, is a public-key encryption algorithm and the standard data sent over the internet.

#### What hashing methods do you know?
MD5: 128 bit. not the savest
SHA256: generates an almost-unique, fixed size 256 bit (32-byte) hash. very safe.

#### How/where would you store sensitive data (like db password, API key, ...) of your application?
I would put data like password, or API key in my environment variables. It is very hard to steal 


## Computer science

### Algorithms

#### What is the difference between Stack and Queue data structure?
Stack follows the LIFO principle: Last In First Out, push;pop<br>
- Programs runs like this most of the time.

Queue follows the first in first out principle. enqueue;dequeue
- Login queues work like this.
#### What is BubbleSort? Describe the main logic of this sorting algorithm.
BubbleSort loops through a list multiple times (1 loop for the list, 1 for the elements).
This sort compares 2 elements and if they're not in the correct order it swaps the 2 elements.
The highest element will "bubble" its way to the end of the list, hence the name.
```python
def bubblesort(lst):
    iterations = 1
    N = len(lst)
    while iterations < N:
        j = 0
        while j <= N-2:
            if lst[j] > lst[j+1]:
                temp = lst[j+1]
                lst[j+1] = lst[j]
                lst[j] = temp
            j += 1
        iterations += 1
    return lst
```
#### Explain the process of finding the maximum and minimum value in a list of numbers!
You declare the first number of the list to be the smallest number and you loop through the list.<br>
If the loop finds an element that is smaller than our declared variable it reassigns
that number to the variable.
```python
def _min(_list):
    smallest_value = _list[0]
    for element in _list:
        if smallest_value > element:
            smallest_value = element
    return smallest_value
```

Maximum:
You declare the first element of the list to be the biggest number and you loop through the list.
If if the loop finds an element that is bigger than our variable it reassigns the variable to that number.
```python
def _max(_list):
    biggest_value = _list[0]
    for element in _list:
        if biggest_value < element:
            biggest_value = element

    return biggest_value
```
#### Explain the process of calculating the average value in an array of numbers!
```python
def my_avg(_list):
    my_sum = 0
    element_number = 0
    for element in _list:
        my_sum += element
        element_number += 1
    average = my_sum / element_number

    return average
```
It loops through a list, adds every element to the sum, and adds one to the element_number after
each iteration. This way if you divide the sum with the number of iterations you get the average.
#### What is Big O complexity? Explain time and space complexity!
It is the relation between runtime and input size.
```python
def _length(_list):
    list_length = 0
    for _ in _list:
        list_length += 1
    return list_length
# O(n) complexity
```
Space complexity:<br>
This is the amount of memory used in the algorithm. The more elements the more memory usage.
#### Explain the process of calculating the average value in a linked list of numbers!
Linked lists are linear collection of data elements, where every node has a value and a pointer to the next node, so
order is not determined by the physical placement in the memory
- Create a length and sum variable
- Iterate through the list incrementing the length and adding the current node's value to the sum<br>
- return sum/length
### Procedural
#### How the CASE condition works in SQL?
The CASE statement is similar to an if/else statement.
It goes through the selected columns, if the WHEN condition is true then the THEN statement replaces
the value of that cell.
You can also use ELSE in the CASE statement that works the same way as typical if/else statement.
```postgresql
SELECT name, age,
CASE
    WHEN age < 18 THEN
        "Can't drink legally"
    WHEN age > 70 THEN
        "Shouldn't drink"
    ELSE 
        "Can drink legally"
END
FROM people;
```
#### How the switch-case condition works in JavaScript?
The expression in the switch argument gets executed and its value is checked against cases.
If the case matches a value it starts executing and we need to break out of it in order to stop
We can use a default value in the end which gets executed it no cases were matched.
```javascript
switch(expression){ // This expression will be checked against the values
    case value:     // If the value matches the expression value it starts executing
        expression;
        break;      // We need to break it, so it won't execute anything else

    case value:
        expression;
        break;

    default:        // If no case matches this block gets executed
        Expression;
                    // No need to break since it's the end of the block
}
```
#### How to achieve a switch-case-like structure in Python?
With if else and elif.
```python
fruit = 'banana'

if fruit == 'orange':
    print('This is an orange')
elif fruit == 'banana':
    print('This is a banana')
elif fruit == 'apple':
    print('This is an apple')
else: #This would be the default in Javascript
    print('Some other fruit')
```
#### Explain variable scoping in Python!
LEGB: Local, Enclosed, Global, Built-in
Scope determines the accessibility of our variables, and what values do they hold.
It is the hierarchy in which python looks for variables (and functions as well).
Variables have different lifetimes, depending on their definition. For example a local variable exists only within
the function, and when that function's execution is finished it does not exist anymore.
#### What’s the difference between const and var in JavaScript?
const creates a block scope variable, so it can be only accessed in the block that it was declared in and its value
can not be changed.
var creates a global scope (or function scope) variable.
let creates a block scope variable same as const, but its value can be changed.
#### How the list comprehension looks like in Python?
numbers = [number for number in range(1, 11)] # Creates a list with numbers from 1 to 10
#### How the “ternary expression” looks like in Python?
I think python's if-else statements are pretty simple and ternary expressions look a bit weird here compared to
other languages.
So I would stick with the normal if-else statement.
```python
number = 3
return_value = 'Number is 3.' if number==3 else 'Number is not 3.'
```
#### How the ternary expression looks like in JavaScript?
condition ? expressionIfTrue : expressionIfFalse
```javascript
let number = 3;
let returnValue = (number===3) ? 'Number is 3.' : 'Number is not 3.';
console.log(returnValue);
```
#### How to import a function from another module in Python?
import /origin/my_module without the .py part. If the file is in the same directory it is not
necessary to provide the origin.
So either:
import module
or
from module import function
#### How to import a function from another module in JavaScript?
If we use more functions we need the curly brackets.
import {function1, function2} from module
or
import module
These are the ones I use but there are 9 other ways if your taste requires something else.
### Functional
#### What is recursion?
A function calling itself.
#### Write a recursive function which calculates the Fibonacci numbers!
def fibonacci(seq_index):
    if seq_index <= 1:
        return seq_index
    else:
        return fibonacci(seq_index - 1) + fibonacci(seq_index - 2)
#### How to store a function in a variable in Python?
When you assign a function to a variable you don't use the () but simply the name of the function.
In your case given def x(): ..., and variable silly_var you would do something like this:
silly_var = x
and then you can call the function either with
x()
or
silly_var()
#### List the ways of defining a callable logical unit in JavaScript!
function one() {
    return 'one';
}

const two = function() {
    return 'two';
}

const three =  () => 'three';

const four = singleParameter => singleParameter+'four';

const five = (number1, number2) => {
    let result = number1 + number2;
    return result; // It's dumb but it wants to show that you have to use {} for multiline arrow function
}


six: function () {
  return 'six';
}
#### What is an event listener? How to attach one?
An even listener watches for our defined event to occur at a given DOM object. The event handler function is called when the event is triggered.

const buttonOne = querySelector('#btn1');
buttonOne.addEventListener('click', function() {
  buttonOne.remove();
})
#### How to trigger an event in JavaScript?
We either listen for the predefined user interaction or we wait for events that occur by deafult.
For example: windows.onload or mouseover 
#### What is a callback function? Tell some examples of its usage.
A callback function is a function that is passed into another function as argument, which
is then called, hence its name.
- Event listeners
- Asynchronous calls
#### What is a Python decorator? How does it work? Tell some examples of its usage.
Decorators are functions that extend other functions, they basically wrap around the
original function.
- On databases.py-s extending a connection handler
- In flask on routes.
#### What is the difference between synchronous and asynchronous execution?
Synchronous execution happens line-by line in order, while in asynchronous execution one thread
can execute other lines of code while the other thread waits for the data to load.
## Programming languages

### SQL

#### How can you connect your application to a database server? What are the possible ways?
With a database adapter, in our case python's psycopg2.
#### When do you use the DISTINCT keyword in SQL?
DISTINCT statement is used to return only distinct (different) values
#### What are aggregate functions in SQL? Give 3 examples.
Instead of returning every value, with this function you can return a single value COUNT, AVG, MAX 
#### What kind of JOIN types do you know in SQL? Could you give examples?
LEFT JOIN: Represents every value from the table after the FROM even if it has null value.
RIGHT JOIN: Represents every value from the table after the JOIN even if it has a null value.
FULL JOIN: Represents everything from every table even if the values are null
INNER JOIN: Represents only the values on which it can join together two tables ON a given clause.
No null values!

#### What are the constraints in sql?
Constraints are the rules enforced on the data columns of a table. These are used to limit the type of data that can go into a table. e. g.: Primary KEY, UNIQUE
#### What is a cursor in SQL? Why would you use one?
It is a database object is used to retrieve, store information from the database and to manipulate this data.

#### What are database indexes? When to use?
Indexes are special lookup tables that the database search engine can use to speed up data retrieval. Simply put, an index is a pointer to data in a table. An index in a database is very similar to an index in the back of a book.
#### What are database transactions? When to use?     *
A transaction represents a change in the database and they are generally used with DML commands.
It is usually used to catch an error, and in that case the transaction is aborted and it rolls back the changes.
If the transaction doesn't catch an error it is saved to the database(commit). Transactions work independently to each other.
#### What kind of database relations do you know? How to define them!
One to One: Each table contain one primary key of the relation.
For example:
In the students table every student has one student_id and in the addresses table one address has one student_id,
One to Many: A table has a record that relates to many records in the other table.
For example:
In the teachers table one teacher has one teacher_id but in the classes table more classes can have the same teacher_id.
Many to Many: In both tables any record can relate to any record in the other table.
For example:
In the classes table one class can have many students and in the students table one student can have many classes
I consider this solution messy, so I like to break many-to-many relations into One-to-Many relations with an Intermediary junction table.
#### You have a table with an “address” field which contains data like “3525, Miskolc, Régiposta 9.” (postcode, city, street name and address). How would you query all records related to Miskolc?
SELECT address
FROM table
WHERE address LIKE "%Miskolc%"
#### How would you keep track of what kind of data has changed after an UPDATE or DELETE operation in a table?
Adding the records of the changes to another table.
So first I'd insert my record of a deletion/update to the new table then I'd alter/delete the row.<br>
Or I'd insert the returning into Clause to a new table. You can also create a a trigger for this, and save the
record to the new table.

### HTML & CSS

#### What’s the difference between XML, XHTML and HTML?
HTML : is the HyperText Markup language, which is designed to create structured documents and provide for semantic meaning behind the documents(the skeleton of the website)

XML : is the Extensible Markup Language which provides rules for storing, creating, structuring and encoding documents

XHTML : is an XML-based HTML. it serves the same function as HTML, but with the same functionas XML documents
#### How to include a JavaScript file in a webpage?
We can use script tage in HTML with src attribute :
<script src="script.js" type="text/javascript" defer></script>
#### How to include a CSS file in a webpage?

If we are talking about External files, we just have to put link tag with href atrribute and type attribute like that : <link href="myCSSfile.css" rel="stylesheet" type="text/css">
#### How to select an element using its id in CSS?
Gotta put hashtag
#id{
    backgroundcolor: red;
}
#### How to select elements using their class in CSS?
Gotta put full-stop
.class{
    backgroundcolor: green;
}
#### How to select elements which have the ‘alpha’ and ‘beta’ classes in CSS?
.alpha.beta {
    backgroundcolor: purple;
}
#### How to select all list items in all ordered lists on the page in CSS?
ol li {
    backgroundcolor: yellow;
}
#### How to select elements using their attributes in CSS?
smt[target]{
    color:green;
}
#### What are UX and UI?
UI: User Interface. Graphical layout of the of the page/application, It is basically the graphic design.
UX: User eXperience. It is about the user interaction with the application/page. 
"If you imagine a product as the human body, the bones represent the code which give it structure. The organs represent the UX design: measuring and optimizing against input for supporting life functions. And UI design represents the cosmetics of the body; its presentation, its senses and reactions"
#### Please list some points that an application should fulfill to have good UX.
- Understandable: You know how to navigate on the site immediately.
- Responsive: Either on mobile or on PC the experience is nearly the same.
- Smoothness: The app doesn't require 5G to load in a minute.
#### What is XML, XSLT, DTD?
XML is eXtensible Markup Language used for storing data.
XSLT is ((eXtensible Stylesheet Language) Transformation) used for styling XML.
DTD is Document Type Definition used for defining the structure and attributes of XML.
#### What is the difference between HTML and XML?
There are many.
1.HTML is used to display data, XML is used to store, transport
2.HTML is a markup language,XML provides framework to define markup language
3.HTML is not necceseray to use closing tags, in XML is mandatory
### Javascript

#### What is javascript?
JavaScript is a scripting programming language for the Web. JS can update, and change both HTML and CSS. JS can calculate, namipulate and validate data. Can be backend and frontend.
#### When to use AJAX? Bring examples of its usage.
AJAX stands for Asynchronous Javascript and XML. The most valuable feaute of AJAX is allow to refresh, update datathe webpage without reloading.
#### What is DOM and how to manipulate it from Javascript?
It stands for Document Object Model. With DOM, Js can access and change all the elements of the HTML content. Each branch is a node and these nodes contain objects. For example you can access and manipulate html element : document.getElementById("demo").innerHTML = "Hello World!";
#### What are events and how/why to use them in Javascript?
HTML events are the 'things' that happen HTML elements.
When JS is used HTML pages, JS can react on these events. User interacton e.g.: click, hover, keydown, etc. You can attach eventlisteners where you want to wair, and you can make a function on is
#### What is event bubbling/capturing? How would you use it?

#### What is JSON and how do we use it?

## Software engineering

### Version control

#### What type of branching strategy would you use?
#### What would you do if you find a bug on the production code (master branch)?
#### How can you move changes from one branch to another in GIT?
#### How does a VCS help with code reviews?
#### What is your favorite git command? Why?
#### What does remote/local mean in Git? 

### DevOps

#### Why is it good to use a package manager software?
#### Why is it good to use a virtual environment for a project?

### Networks

#### What kind of HTTP status codes do you know?
#### What is a API?
#### What is REST API?
#### What is JSON? When to use?
#### What is TCP/IP? What layers does it define, what are they responsible for?
#### What’s the difference between TCP and UDP?
#### How does an HTTP Request look like? What are the most relevant HTTP header fields?
#### How does an HTTP Response look like? What are the most relevant HTTP header fields?
#### What is DNS? How does it work?
#### What is a web server?
#### Explain the client-server architecture.
#### What would you use a session for?
#### What would you use a cookie for?

## Software Development Methodologies

#### What kind of software development methodologies do you know? What are the main features of these?
#### What are the SCRUM roles?
#### What are the SCRUM ceremonies?
#### What are the SCRUM artifacts?
#### What is the main goal of a retrospective meeting?
#### Explain, when would you recommend to use the waterfall methodology?
