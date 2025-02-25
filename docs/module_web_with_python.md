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
- Use exceptions to signal the caller that you faced an error which you are unwilling or unable to handle.



### Security
#### What is SQL injection? How to protect an application against it?
SQL injections attacks allow attackers to steal, modify, delete data informations.  
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
You simply dont call the function and dont use ()brackets, just simply the name of the function
def x():
    print(20)
 y = x
 y() ---> output: 20   
#### List the ways of defining a callable logical unit in JavaScript!
function one() {
    return 'one';
}
const two = function() { //function expression
    return 'two';
}
const three =  () => 'three';  //lambda expression

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
LEFT JOIN: Returns all of the records from the left table, and the matched records from the right
RIGHT JOIN:returns all records from the right table, and the matched recors from the left table
FULL JOIN: returns all recrods when there is a match in either left or right table
INNER JOIN:  returns records that have matching values in both tables

#### What are the constraints in sql?
Constraints are the rules enforced on the data columns of a table. These are used to limit the type of data that can go into a table. e. g.: Primary KEY(a combination of a not null and UNIQUE. Uniquely identifies each row in the table),Foreign KEY(Uniquely indifies a row/records in another table), UNIQUE(Ensures that all values in a column different)

#### What is a cursor in SQL? Why would you use one?
It is a database object is used to retrieve, store information from the database and to manipulate this data.

#### What are database indexes? When to use?
Indexes are special lookup tables that the database search engine can use to speed up data retrieval. Simply put, an index is a pointer to data in a table. An index in a database is very similar to an index in the back of a book.

"Consider a "Book" of 1000 pages, divided by 10 Chapters, each section with 100 pages.

Simple, huh?

Now, imagine you want to find a particular Chapter that contains a word "Alchemist". Without an index page, you have no other option than scanning through the entire book/Chapters. i.e: 1000 pages."
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

#### You have a table with an “address” field which contains data like “3525, Miskolc, Régiposta 9.” (postcode, city, street name and address). How would you query all records related to Miskolc?
SELECT address
FROM table
WHERE address LIKE "%Miskolc%"
#### How would you keep track of what kind of data has changed after an UPDATE or DELETE operation in a table?
A foreign key with cascade delete means that if a record in the parent table is deleted, then the corresponding records in the child table will automatically be deleted. This is called a cascade delete in SQL Server
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
It stands for Document Object Model.When a web page is loaded, the browser creates a Document Object Model of the page. With DOM, Js can access and change all the elements of the HTML content. Each branch is a node and these nodes contain objects. For example you can access and manipulate html element : document.getElementById("demo").innerHTML = "Hello World!";
#### What are events and how/why to use them in Javascript?
HTML events are the 'things' that happen HTML elements.
When JS is used HTML pages, JS can react on these events. User interacton e.g.: click, hover, keydown, etc. You can attach eventlisteners where you want to wair, and you can make a function on it
#### What is event bubbling/capturing? How would you use it?
Event bubbling is when an aevent happens on an element, it first runs the handlers on it, then on its parent, then all the way up on the other ancestors.Use: <form onclick="alert('form')">FORM
                        <div onclick="alert('div')">DIV
                            <p onclick="alert('p')">P<p>
                        </div>
                    </form>


click on the inner <p> first runs onclick: on that<p>, then on the outer <div>, then the outer <form>, and so on


Event capturing is the event starts from top element to the target elements. It is the opposite of event bubbling, which starts from target element to the top element.
#### What is JSON and how do we use it?
JSON stands for JavaScript Object Notation.It is a lightweight format for storing and transporting data. It is used when date is sent from a server to a webpage or reverse.
example : {
   "book": [
	
      {
         "id":"01",
         "language": "Java",
         "edition": "third",
         "author": "Herbert Schildt"
      },
	
      {
         "id":"07",
         "language": "C++",
         "edition": "second",
         "author": "E.Balagurusamy"
      }
   ]
}
## Software engineering

### Version control

#### What type of branching strategy would you use?
My live code would be on the master branch, and my development would be on the development branch.
Each feature would have its own branch from development, and merged back to it when it's finished.
Before merging back to the branch I'd pull the branch which it was originated from to resolve the merge conflict there.
When i would like to bring the development code live I would review it, open a pull request, review it
with others, change my code according to the feedback, and merge the code to master.
#### What would you do if you find a bug on the production code (master branch)?
Create aother branch to solve that specific bug.
#### How can you move changes from one branch to another in GIT?
Cherry pick for one commit, rebase for more, merge for the entire.
#### How does a VCS help with code reviews?
Every little change can be seen with an exact history.
You can also see who wrote specific changes to the code.
#### What is your favorite git command? Why?
git status: it shows what files have to be committed, and which while is added to the stage area.
#### What does remote/local mean in Git? 
Local is in your computer, remote is on the web.

### DevOps

#### Why is it good to use a package manager software?
It is a convenient way to get updates for you existing packages, and to get new ones.
You don't have to google through everything.
#### Why is it good to use a virtual environment for a project?
It helps you to keep your code functional if something changes. For example a tool gets updated
and suddenly your code crashes, but with virtual environment your versions can stay the same.

### Networks

#### What kind of HTTP status codes do you know?
2xx for Success, 3xx for Redirection, 4xx for Failures, 5xx server errors.
202 accepted: the request is complete and a new resource is created
303 see other: the requested has moved temporarilay to a new url
404 Not Found: the server cannot find the requested page
505 HTTP Version Not Supported: the server does not support the 'http protocal' version

#### What is a API?
Application Programming Interface. It is the gateway that allows your code to communicate with other code/site.
You can imagine it like the backend is the kitchen, the food on the table is the frontend and the waiter is the API.
#### What is REST API?
REST API stands for Representational State Transfer Application Programming Interface.
REST determines how the API looks like. It is a set of rules that developers follow when they create their API. One of these rules states that you should be able to get a piece of data (called resource) when you link to a specific URL
#### What is JSON? When to use?
JSON stands for JavaScript Object Notation. 
The JSON format is syntactically identical to the code for creating JavaScript objects. JS program can easily convert JSON data into native JS objects, it consist a key value pairs. We use it the store and transport data,from server to webpage.
#### What is TCP/IP? What layers does it define, what are they responsible for?
TCP/IP (Transmission Control Protocol/Internet Protocol) is a set of protocols, that are used for data transmission over computer networks. 
It is a set of communication rules that defines how data should be transferred.(packeting, addressing, transferring, routing, receiving)
It.contains four layers :1. Process/Application Layer(HTTP, Browser), 2. Host-to-Host/Transport Layer(TCP, it packets the data with headers), 3. Internet Layer(IP, it knows where it comes from and where it goes), 4. Network Access/ Link Layer(receives and converts the data)
#### What’s the difference between TCP and UDP?
-TCP is a connection-roiented protocol, whereares UDP is a connectionless protocol
-The speed for TCP is slower while the speed of UDP is faster
-TCP uses handshake protocol like SYN, SYN-ACK, ACK while UDP uses no handshake protocols
-TCP does error checking and also makes error recovery, on the other hand,
UDP performs error checking, but it discards erroneous packets.
-TCP has acknowledgement segments, but UDP does not have any acknowledgement segment
-TCP is heavy-weight and UDP is lightweight
#### How does an HTTP Request look like? What are the most relevant HTTP header fields?
HTTP requests are messages sent by the client to initiate an action on the server.
http://developer.mozilla.org/en-US/docs/Web/HTTP/Messages HTTP/1.1) 1. An HTTP method, a verb (like GET, PUT or POST) or a noun (like HEAD or OPTIONS), that describes the action to be performed. 2. The request target, usually a URL, or the absolute path of the protocol, port, and domain are usually characterized by the request context. 3. The HTTP version, which defines the structure of the remaining message, acting as an indicator of the expected version to use for the response.
HTTP headers from a request follow the same basic structure of an HTTP header: a case-insensitive string followed by a colon (':') and a value whose structure depends upon the header. The whole header, including the value, consist of one single line, which can be quite long. There are numerous request headers available. They can be divided in several groups: 1. General headers, like Via, apply to the message as a whole. 2. Request headers, like User-Agent, Accept-Type, modify the request by specifying it further (like Accept-Language), by giving context (like Referer), or by conditionally restricting it (like If-None). 3. Entity headers, like Content-Length which apply to the body of the request. Obviously, there is no such header transmitted if there is no body in the request.
The final part of the request is its body. Not all requests have one: requests fetching resources, like GET, HEAD, DELETE, or OPTIONS, usually don't need one. Some requests send data to the server in order to update it: as often the case with POST requests (containing HTML form data). Bodies can be broadly divided into two categories: 1. Single-resource bodies, consisting of one single file, defined by the two headers: Content-Type and Content-Length. 2. Multiple-resource bodies, consisting of a multipart body, each containing a different bit of information. This is typically associated with HTML Forms.

Headers:
- host: domain
- method: GET, POST, DELETE, etc
- path: url path /feed
- cookies: user session etc
- user agent: browser, os
- content type: body's content type
#### How does an HTTP Response look like? What are the most relevant HTTP header fields?
Headers:
- Content-type
- Status code
Body:
- The site you receive
#### What is DNS? How does it work?
The Domain Name System (DNS) is the phonebook of the Internet. Humans access information online through domain names,
 like nytimes.com or espn.com. Web browsers interact through Internet Protocol (IP) addresses.
  DNS translates domain names to IP addresses so browsers can load Internet resources

#### What is a web server?
A web server is used for hosting websites. It usually runs on a dedicated hardware which stores data about the web page.
This can handle incoming requests and respond to them.
#### Explain the client-server architecture.
In this architecture a server can handle many connecting clients over a network. The server contains the data about the page.
They communicate through requests and responses. A request is made by the client, the server processes that request
(eg: Which page is to be loaded? Which cookies did you send?) and then it sends a response.
#### What would you use a session for?
I'd store login data with this. Is the user logged in or not.
#### What would you use a cookie for?
1. Personalised ads. Other: Saving forms, saving the state of the basket (any useful information that is not sensitive).
## Software Development Methodologies

#### What kind of software development methodologies do you know? What are the main features of these?
Waterfall methodology:It is very simple to understand and use. In a waterfall model, each phase must be completed before the next phase can begin and there is no overlapping in the phases..

Agile:It has a time boxed iterative approach to development. Analysis, design, etc.. are done contemporary.
It builds the software in small blocks instead of delivering
one huge block of software in the end. Because of this the software can be changed cost effectively throughout the
project. It is a good practice for codes where the requirements are not 100% clean at the start and where the codebase
needs to change during the development. Good for projects like a website.
#### What are the SCRUM roles?
- Product owner (PO)
- Scrum master
- Developer team

#### What are the SCRUM ceremonies?
- Sprint planning
- Daily stand ups
- Sprint review
- Retrospective meeting

#### What are the SCRUM artifacts?
- Product backlog: never ending<br>
- Sprint backlog: what the team thinks can be done in a sprint<br>
- Increment: All completed backlogs from the current sprint combined with the previous sprint's backlog.<br>
- Burn-Down Chart: An overview graph that can assume the team's and project's velocity. 

#### What is the main goal of a retrospective meeting?
A meeting that reflects the previous sprint. Discussing the positive and negative elements of the sprint.
Making an action item, that can be implemented in the next sprint. It needs to be Specific, Measurable, Action-oriented,
Realistic, )

#### Explain, when would you recommend to use the waterfall methodology?
When the requirements are clean and you can't really fix the software afterwards.
Most cars' system are designed this way. You can't really roll an update to the tempomat in a car.
.................