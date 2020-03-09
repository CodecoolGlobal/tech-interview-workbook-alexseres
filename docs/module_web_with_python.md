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
a
#### What is BubbleSort? Describe the main logic of this sorting algorithm.
#### Explain the process of finding the maximum and minimum value in a list of numbers!
#### Explain the process of calculating the average value in an array of numbers!
#### What is Big O complexity? Explain time and space complexity!
#### Explain the process of calculating the average value in a linked list of numbers!

### Procedural
#### How the CASE condition works in SQL?
#### How the switch-case condition works in JavaScript?
#### How to achieve a switch-case-like structure in Python?
#### Explain variable scoping in Python!
#### What’s the difference between const and var in JavaScript?
#### How the list comprehension looks like in Python?
#### How the “ternary expression” looks like in Python?
#### How the ternary expression looks like in JavaScript?
#### How to import a function from another module in Python?
#### How to import a function from another module in JavaScript?

### Functional
#### What is recursion?
#### Write a recursive function which calculates the Fibonacci numbers!
#### How to store a function in a variable in Python?
#### List the ways of defining a callable logical unit in JavaScript!
#### What is an event listener? How to attach one?
#### How to trigger an event in JavaScript?
#### What is a callback function? Tell some examples of its usage.
#### What is a Python decorator? How does it work? Tell some examples of its usage.
#### What is the difference between synchronous and asynchronous execution?

## Programming languages

### SQL

#### How can you connect your application to a database server? What are the possible ways?
#### When do you use the DISTINCT keyword in SQL?
#### What are aggregate functions in SQL? Give 3 examples.
#### What kind of JOIN types do you know in SQL? Could you give examples?
#### What are the constraints in sql?
#### What is a cursor in SQL? Why would you use one?
#### What are database indexes? When to use?
#### What are database transactions? When to use?
#### What kind of database relations do you know? How to define them?
#### You have a table with an “address” field which contains data like “3525, Miskolc, Régiposta 9.” (postcode, city, street name and address). How would you query all records related to Miskolc?
#### How would you keep track of what kind of data has changed after an UPDATE or DELETE operation in a table?

### HTML & CSS

#### What’s the difference between XML, XHTML and HTML?
#### How to include a JavaScript file in a webpage?
#### How to include a CSS file in a webpage?
#### How to select an element using its id in CSS?
#### How to select elements using their class in CSS?
#### How to select elements which have the ‘alpha’ and ‘beta’ classes in CSS?
#### How to select all list items in all ordered lists on the page in CSS?
#### How to select elements using their attributes in CSS?
#### What are UX and UI?
#### Please list some points that an application should fulfill to have good UX.
#### What is XML, XSLT, DTD?
#### What is the difference between HTML and XML?

### Javascript

#### What is javascript?
#### When to use AJAX? Bring examples of its usage.
#### What is DOM and how to manipulate it from Javascript?
#### What are events and how/why to use them in Javascript?
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
