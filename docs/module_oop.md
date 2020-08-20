# OOP questions


## Software design

### Error handling

#### What does 'fail fast' mean in terms of exception handling? Why is it a good practice?
-A fail-fast system is nothing but immediately report any failure that is likely to lead to failure. When a problem occurs, a fail-fast system fails immediately. In Java, we can find this behavior with iterators. Incase, you have called iterator on a collection object, and another thread tries to modify the collection object, then concurrent modification exception will be thrown. This is called fail-fast.


## Computer Science

### Data structures

#### How to find the middle element of singly linked list in O(n)?
-Use two pointer slow and fast and initialize both to head of linkedlist. -> move fast pointer by two step and slow pointer by one step in each iteration-> when fast pointer reaches at the end of a linked list, then the slow pointer will be pointing to the middle element of a linked list.

Node slow = head;
Node fast = head;
 
while (fast != null && fast.next != null) {

      slow = slow.next;
      fast = fast.next.next;
}

#### Given an array of integers going from 1 to 100 (both inclusive) there is a duplicated entry. How to find it?
duplicates = false;
for (j=0;j<zipcodeList.length;j++){
  for(k=j+1; k<zipcodeList.length;k++){
    if (ziocodeList[j] == zipcodeList[k])
      return true
  }
}
#### What is a linked list? How to find if a linked list has a loop?
-Similar to arrays in JAva, LinkedList is a linear data structure. However LinkedList elements are not stored in contiguous locations like arrays, they are linked with each other using pointers(stored in runtime). Each element of the LinkedList has the reference(address/pointer) to the next element of the LinkedList.

-Fast/slow solution to find the loop:
boolean hasLoop(Node first){
  Node slow = first;
  Node fast = first;

  while (fast!=null && fast.next !=null){
    slow=slow.next;
    fast=fast.next.next;
    if(slow == fast)return true
  }

}

#### What is the Big O time complexity of the common operations in an ArrayList, LinkedList, HashMap? And of a bubble sort, quicksort, finding items in a Binary Search tree?

ArrayList:
Random access takes O(1) time.
Adding/Deleting element takes average O(n) time.
Searching:
For sorted elements: O(log n) time
For non-sorted elements: O(n).

LinkedList
Adding and removing element take an O(1) constant-time insertion at any position.
Getting an element or check whether it contains a specified element takes O(n) time.
HashMap

Inserting and retrieving takes O(1) on average.
Checking whether a key exists: O(1).
Checking whether a value exists within a HashMap: O(n) because in this case it's necessary to iterate over the elements.
During HashMap collision because of the LinkedHashMap, it's element lookup worst-case scenario from O(n) to O(log(n)) time.

Bubble-sort:
Worst-case performance:
Comparison: O(n2)
Swaps: O(n2)
Best-case performance:
Comparison: O(n)
Swapping: O(1) -Average performance is the same as worst-case.

Quick-sort:
Worst-case performance: O(n2)
Best-case:
Simple partition: O(n log n)
Three-way partition with equal keys: O(n)
Average: O(n)
Binary-search tree:

The worst case for access, search, insertion, deletion is O(n).
Average for the same operations: O(log(n))

#### How does HashMap work?
-A HashMap is a map used to store mappings of key-value pairs. 
-It uses a technique called hashing. HashMap contatins an array of the nodes, and the node is represented as a class. It uses an array and linkedList data structure internally for storing Key and Value.
-There are 4 fields in HashMap: 
Node<K,V>
1. int hash
2. K Key
3. V Value
4. Node<K,V> next

-equals(): it checks the equality of two objects. It compares the Key, whether they are equal or not. It is method of the Object class. It can be overriden. If you override the equals() method, then it is mandatory to override the hashCode() method.

-hashCode(): This is the method of the object class. It returns the memory reference of the object in integer form. The value received from the method is used as the bucket number. The bucket number is the address of the element inside the map. Hash code of null Key is 0

-Bucket: Array of the node is called buckets. Each node has a data structure like a LinkedList. More than one node can share the same bucket. It may be different in capacity




#### Why is it important for keys in a map to have an immutable type? (Consider String for example.)
Because HashMap will search for the bucket according to the hash code of the key. If we change the key we change it's hash code so the map will search in the wrong bucket.
### Other

#### What is a garbage collector, in a nutshell?
In computer science, garbage collection (GC) is a form of automatic memory management. The garbage collector, or just collector, attempts to reclaim garbage, or memory occupied by objects that are no longer in use by the program.
## Programming paradigms

### Procedural

#### What is casting? What is the difference between up vs downcasting?
-Casting is the process of making a variable behaves as a variable of another type.
-Upcasting (Generalization or Widening) is casting to a parent type in simple words casting individual type to one common type is called upcasting while downcasting (specialization or narrowing) is casting to a child type or casting common type to individual type 

-Upcasting:
Casting from subclass to superclass.
For reference variables it means that the the list of methods and properties available to the corresponding object will less. In their case we distinguish:
Implicit conversion (Done by the compiler):
Body leg = new Leg();
And Explicit Conversion:
body = (Body) leg;

Downcasting:
It’s the casting from a superclass to a subclass. But only those object can be downcasted that are really instances of a subclass (e.g. Leg).
((Leg) body).walk();

#### Which order should we catch the exceptions? Why?
-if the exceptions have parent-child relationship, the catch blocks must be sorted by the most specific exceptions first, then by the most general one(RunTimeException or Exception). Why? it is because if we handle the most general exception first, the more specific ecceptions will be omitted, which is not good, as Java encourages handling exceptions as much specific as possible

try {
  s.charAt(10);
} catch ( NullPointerExeption e ) {
  System.out.println("null");
  e.printStackTrace();
} catch ( StringIndexOutOfBoundsException e ) {
  System.out.println("String index error!");
  e.printStackTrace();
} catch ( RuntimeException e ) {
  System.out.println("runtime exception!");
  e.printStackTrace();
}


### Object-oriented

#### What is a class?
-a class is a user defined blueprint or prototype from which objects are created. It represents the set of properties or methods that are common to all objects of one type.
#### What is an object?
-Object is an instance of a class and it is a basic unit of Object Oriented Programming and represents the real life entities. A typical Java program creates many objects, which as you know, interact by invoking methods. An object consist of a:
    -state: it is represented by attributes of an object. it also reflects the properties of an object.
    -behavior: it is represented by methods of an object. It also reflects the response of an object with other objects.
    -identity: it gives a unique name to an object and enables one object to interact with other objects.
#### What is a constructor?
-A Java constructor is special method that is called when an object is instantiated. In other words, when you use the new keyword. The purpose of a Java constructor is to initializes the newly created object before it is used. There are two types of constructor in java: no-arg constructor, and parameterized constructor.
#### Do we require parameter for constructors?
-Not every case. A constructor without parameter is the default constructor.if we want to initalize fields of the class with your own values, then use a parametized constructor.
#### What is an interface?
- An interface is a reference type in Java. It is similar to class. It is a collection of abstract methods.
    -interfaces specify what a class must do and not how. It is the blueprint of the class.
    -it specifies a set of methods that the class has to implement.
    -if a class implements an interfface and does not provide method bodies for all functions specified in the interface then the class must be declared abstract

-Interfaces are important because they seperate what a class does from how it does it. The contract defining what a client can expect leaves the developer free to implement it any way they choose, as long as they uphold the contract.


Classes can implement more than one interface but extend only one class

It is a way to fulfill an OOP Principle, polymorphism.

A simple example of interface:
public class Marinaring implements FoodMaker {

  @Override
  public String cook() {
      //implementation
  }       

public interface FoodMaker {
    cook();
}    
}

In Java, only the following Types can implement interface:
Class
Abstract class
Nested class
Enum
Dynamic Proxy
Interface elements:


#### What are access modifiers?
they are to specify the accessibility or scope of a field, method, constructor or class. We can change the access level of fields, constructors, methods, and class by applying the access modifier on it.
-Private: is accessible only within the class. 
-default : when no access modifier is specified for a class, method or data member. it is only accessible withtin the same package.
-protected: is specified using the keyword protected. The methods or data members declared as protected are accessible within the same package or sub classes in different package
-public: it has the wildest scope among all modifiers. Classes, methods, or data members which are declared as public are accessible from every where in the program. 
#### What is data hiding?
is a technique to hide internal object details(data members). Data hiding ensures exclusive data access to class members and protects object integrity by preventing unintended or intended changes. Also it refers to the fact that tose part of a computer program that may change must not be accessible from other modules/from clients.
#### Can a static method use non-static members?
-in static method can only access only static data members and static method of another class or same class but cannot access non-static methods or variables. 


#### What is the difference between hiding a static method and overriding an instance method?
-if a subclass defines a static method with the same signature as a static method in the superclass, then the method in the subclass hides the one in the superclass.
- if both method in parent class and child class are an instance method, it called overrides.
-One method cant be static in parent and and as an instance in the child. and visa versa.




#### Define the following terms: Instantiation, Attribute, Method
-Simple meaning of instantiate is creating an instance of an object from the class= ClassName obj = new ClassName();
- attribute is an another term for a field. Its typically a public constant or a public variable that can be accessed directly.
-Method is a block of code which runs when it is caledd. you can pass parameters into the method. it performs certain actions, they like functions


#### Could we access a static variable (or method) from a non-static method? Why?
A non-static method can access any static method or variable without creating an instance of the class becaise the static variable or method belongs to the class.


#### Could we access a non-static variable (or method) from a static method? Why?
- a static method can call only static methods, to acces a non static method from a static method, create an instance of the class.

#### How many instances you have of a static variable of a given class?
- a static variable is common to all the instances of the class because it is a class level variable. Memory allocation for such variables only happens once when the class is loaded in the memory. known as class variables.


#### Why is it not a good practice to write a lot of static methods?
-static members are always part of memory whether they are in use or not
- and it cannot override it
-they are hard to test to
-simply put, they break the assumptions of object-oriented programming 
#### What are the features of static attributes and static methods of a class? What are the benefits, when to use them?
-static attributes can be defined without taking additional memory(one for each class)
- static attributes and methods can be accessed without an instantiation of the class
- use when a particular piece of code is to be shared by all the instance methods.
#### What is the ‘this’ reference?
'this' is a reference variable which refers to the current object.
#### What are base class, subclass and superclass?
-subclass(child) - the class that inherits from another class(it can inherit properties and behaviours )
-base class is also called superclass
-superclass(parent) - the class being inherited from
    - to inherint from a class use the 'extends' keyword
#### Draw an object oriented family (as entities, with relations) on the whiteboard.
-find photo attached in 


#### Difference between overloading and overriding?
-overloading happens at compile time while overriding happens at runtime
-static method can be overloaded, non static can override 
-Overloading is being done in the same class while for overriding base and child class are required. Overriding is all about giving a specific implementation to the inherited method of parent class 
-in overloading parameter must be different, in overriding parameter must be the same
-
#### What are the Object Oriented Principles? Explain the concepts with realistic examples!
-There are 4 major principles in OOP. These are Encapsulation, Abstraction, Polymorphism and Inheritence. Also known as four pillars of OOP.

-Encapsulation is the mechanism of hiding data implementation by restricting access to public methods. Instance variables are kept private and accessor methods are public to achieve this
  e.g:public class Employee {
    private String name;
    private Date dob;
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public Date getDob() {
        return dob;
    }
    public void setDob(Date dob) {
        this.dob = dob;
    }
}
-Absraction: -Abstract means a concept or an Idea which is not associated with any particular instance. Using abstract class/Interface we express the intent of the class rather than the actual implementation. In a way, one class should not know the inner details of another in order to use it, just knowing hte interfaces should be good enough.
- Inheritance in Java is a mechanism in which one object acquires all the properties and behaviours of a parent object. Inheritance expresses "is-a" realationship between two object.
-Polymorphism is the ability of an object to take on many forms. The most common use occurs when a parent class refernce is esed to refer a child class object. Inheritance lets us inherit different attributes and methods from another class. Polumorphism uses those methods to perform different tasks. this allows us to perform a single action in different ways.
  - e. g.:class Animal {
  public void animalSound() {
    System.out.println("The animal makes a sound");
  }
}

class Pig extends Animal {
  public void animalSound() {
    System.out.println("The pig says: wee wee");
  }
}

class Dog extends Animal {
  public void animalSound() {
    System.out.println("The dog says: bow wow");
  }
}

class MyMainClass {
  public static void main(String[] args) {
    Animal myAnimal = new Animal();
    Animal myPig = new Pig();
    Animal myDog = new Dog();
        
    myAnimal.animalSound();
    myPig.animalSound();
    myDog.animalSound();
  }
}
#### What is method overloading?
-Overloading allows different methods to have the same name but different signatures where the signature can differ by the number of input parameters or type of input parameters or both. Overloading is realated to compile-time (or static) polymorphism.

e.g.:public class Sum { 
  
    // Overloaded sum(). This sum takes two int parameters 
    public int sum(int x, int y) 
    { 
        return (x + y); 
    } 
  
    // Overloaded sum(). This sum takes three int parameters 
    public int sum(int x, int y, int z) 
    { 
        return (x + y + z); 
    } 
  
    // Overloaded sum(). This sum takes two double parameters 
    public double sum(double x, double y) 
    { 
        return (x + y); 
    } 
  
    // Driver code 
    public static void main(String args[]) 
    { 
        Sum s = new Sum(); 
        System.out.println(s.sum(10, 20)); 
        System.out.println(s.sum(10, 20, 30)); 
        System.out.println(s.sum(10.5, 20.5)); 
    } 

#### What is method overriding?
If a subclass has the same method as declared in the parent class it is known as method overriding in Java.Method overriding is ised to provide specific implementation of a method which already provided by its superclass. Method overriding is used for runtime polymorphism.

#### Explain how object oriented languages attempt to simplify memory management for Programmers.   //not sure
E.G Java garbage collection is the process by which Java programs perform automatic memory management. Java programs compile to bytecode that can be run on a Java Virtual Machine. When Java programs run the JVM, objects are created on the heap, which is a portion of memory dedicated to the program. Eventually, some objects will no longer be needed. The garbage collectior finds these unused objects and deletes them to free up memory.


#### Explain the “Single Responsibility” principle!
-this principle stats that each class have one responsibility, one singlie purpose. and it should have only one reason to change. OBject should not have much unrelated behaviors because they are harder to maintain. If an error occurs, it is easier to find 

#### What is an object oriented program? Explain, show.
-OOP is a computer programming model that organizes software design around date, or objects, rather than functions and logic. An object can be defined as data field that has unique attributes and behaviour.

-OOP focuses on the objects that developers want to manipulate rather than the logic required to manipulate them. This approach to programming is well suited for programs that are large, complex, and actively updated or maintained .



#### How do you make a class immutable? What do you need to watch out for?
requirements:
-The class must be declared as final(child classes cant be created)
-Data members in the class must be declared as final
-parameterized constructor
-Getter method for all the variables in it
-No setters



#### How many instances can be created for an abstract class?
-We cant create, we can create all other classes extending that class. 


## Programming languages

### Java

#### What is autoboxing and unboxing?
-Autoboxing: converting a primitive value into an object of the corresponding wrapper class. e.g.: char to Character. Character gfg = 'a'; 
-unboxing: converting an object of a wrapper type to its corresponding primitive value. e.g.: // creating an Integer Object 
        // with value 10. 
        Integer i = new Integer(10); 
  
        // unboxing the Object 
        int i1 = i;  




#### If you have a variable, that shall store a positive whole number between 0 and 200, what primitive type would you use to store it?
int or short



#### What is the "golden rule" of variable scoping in Java? What is the lifetime of variables?   // not sure 
-The golden rule is that static code cannot access non-static members by their simple names. Static code is not executed in the context of an object, therefore the references this and super are not available. An object has knowledge of its class, therefore, static members are always accessable for non-static context.

  Variable Type              Scope          Lifetime
Instance variable   Throughout the class    Until the object is available in the memory
                    except in static        
                    methods

Class variable      Throughout the class    Untill the end of the program


Local Variable      Whithin the block       Until the control leaves the block in which is in declared
                    which it is declared

#### What is the purpose of the ‘equals()’ method?
-It determines whether the Object or string or number equals to the object string int is passed as an argument, return value is boolean
#### What is the difference between '==' and 'equals()'?
- == is an operator, equals() is a method. operators are generally used for primitive type comparisons thus == is used for memory address comparisson and equals methods is used for comparing objects.
#### What does the ‘static’ keyword mean?
-it is used for memory management mainly. we can apply it to variables, methods, blocks and nested classes.
-when a member is declared static, it can be accessed before any object of its class are created without reference to any object
#### Why is the main() method declared as static? Explain.
-Because the compiler can it without the creation of an object. the main() method is the starting point where the compiler starts program execution

#### What is the default access modifier in a class?
- when no access modifier is specified for a class, it is to be vaing the default access modifier by default.

#### What is the JVM?
-Java Virtual Machine that enables a computer to run Java programs as well as programs written in other languages. It is a specification that provides runtime environment in which java bytecode can be executed.
#### What is the difference between the JRE and the JDK?
-JDK(Java Development Kit) is a software development kit whereares JRE(Java Runtime Environment) is a software bundle that allows Java program to run
-JDK contains tools for developing, debugging . JRE contains class libraries and other supporting files 

-Usually, if you only care about running Java programs on computer you will only install the JRE. It's all you need. On the other hand, if you are planning to do some Java programming, you need to install the JDK instead.

#### What is the difference between long and Long?
-long is a primitive which must have a value
-Long is an object so it can be null, it can be passed to a method that accepts anObject, it canbe used for generic datatype, it can be serialized
#### Can a long store bigger numbers than a Long?   //not sure
-yes it can

#### What kind of packages do you know under java.util.* ? Bring at least 3 examples.
-java.util.Arrays
-java.util.Scanner
-java.util.LinkedList



#### What are the access modifiers in Java? Which one could we use for class?
-private: the acces level is only within the class
-Default: only within the package
-protected: within the package and outside the package through child class 
-public: everywhere

we could use Public or default for a class
#### Can an “enum” contain methods in Java? Explain.
yes it can. we should use enums, when we have values that arent going to change. It represents a group of constans(unchangeable variables, liike final variables)
#### When would you use a private/protected/public attribute? What is the difference?
- if we want to keep our attributes not accessible from outside class, we should use private to provides Encapsulation. its an advantage where we know they are not ued anywhere else in the code. it helps also in debugging 
- protected, we should use when my class is designed for inheritance, and the class proves special functionality to its derived classes that must not be visible to other class
-public we should use when we want access anywhere in the programm and its visible.
#### How do you prevent developers from subclassing a class?
-I would be using final keyword in class declaration.
#### How do you prevent developers from overriding a method in a subclass?
-I would be using private, static and final keyword in method, because they cant be overriden.
#### How do you prevent developers from changing the value of a variable?
-using final keyword
#### Think about money ;) How would you store a currency value, that shall support decimal parts? Think it through again, and try to think outside of the box!  // not sure
I would be using float, because currency can change, and the given value can be broken to longer decimal.

#### What happens if you try to call something, that you have no access to, because of data hiding?  // not sure
-you just cant refer to that data, it cant be seen if that is available in the class you want to call.

#### What happens if you try to delete/drop an item from an array, while you are iterating over it?
-You will get a ConcurrentModificationException
#### What happens if you try to delete/drop/add an item from a List, while you are iterating over it?    // not sure
-ConcurrentModificationError you get.
#### What happens if you try to add an item to the end of an array, while you are iterating over it?
-the size of array cant be modified. if you want to bigger, you have to create a new one.
#### If you need to access the iterator variable after a for loop, how would you do it?
- I would create an arraylist and I would fill with the iterable variable.
#### Which interfaces extend the Collection interface in Java. Which classes?
- just saying, Collection in Java is a framework that provides an architecture to store and manipulate the group of objects.

-Set, List, Queue, Deque are the interfaces, and the classes are ArrayList, Vector, LinkedList, HashSet and etc.



#### What is the connection between equals() and hashCode()? How are they used in HashMap?
-If two objects are equal according to the equals(Object) method, then calling the hashcode() method on each of the two objects must produce the same integer result
-Because in HashMap 2 or more object might be the same object, but different hashCode. we cant distinct with equals(). ----> The default implementation of hashCode() in Object class returns distinct integers for different objects. and Each object has different hash code

#### What is the difference between checked exceptions and unchecked exceptions? Could you bring example for each?
-The main difference between checked and unchecked exception is that the checked exceptions are checked at compile-time while unchecked e. are checked at runtime.


unchecked exceptions: NullPoitnerException, ArrayIndexOutOfBoundsException
checked exceptions:IOExceotion, ClassNotFoundException
#### What is Error in Java and how does it relate to Exception?  
-Error is a subclass of Throwable class like Exception that indicates serious problem that reasonable application should not try to catch. ERROR type:java.lang.StackOverflowError, java.lang.OutOfMemoryError

#### When does 'finally' block run? What it is used for? Could you give an example from your projects when you would use 'finally'?   // not sure
-finally block gets always executed, the purpose of it can close a file or connection at the end, to avoid stack overflow 

#### What is the largest number you can work with in Java?
-double	(2-2^-52)·2^1023

#### When you use method overriding, can you change the access level of the method, from protected to public? Why?When you use method overriding, can you change the access level of the method, from public to protected? Why?
Yes, an overriden method can have a different access modifier but it cannot lower the access scope. 
  -Methods declared public in a superclass also must be in al subclasses.
  -Methods declared protected in a superclass must either be protected or public in suclasses:they cannot be private 


#### Can the main method be overridden? Explain your answer
We cannot override main method, because static method cannot be overriden. The static method in java is associated with the class whereas the non-static method is associated with an object.
#### When you use method overriding, can you throw fewer exceptions in the subclass than in the parent class? Why?   //not solved


#### When you use method overriding, can you throw more exceptions in the subclass than in the parent class? Why?   //not sure
-Yes if it is unchecked exception.A method is overriden in a more specialiced subclass so that it is more complex and, for this reason, more probable to throwing new exceptions.
#### What does "final" mean in case of a variable, method or a class?
-final in class cannot be extended.
-final in method cannot be overriden.
-final in variable cannot be changed.

#### What is the super keyword?
-the super keyword refers to superclass (parent) objects.
-It is used to call superclass methods, and to access the superclass constructor.
-If we create the instance of subclass, an instance of parent class is created implicitly which is referred by super reference variable.

#### What are “generics”? When to use? Show examples.
-Generics add a way to specify concrete types to general purpose classes and methods that operated on Object before. With its use the compiler  an enforce the type at compile time, so we dont have to cast explicitly and it could catch errors in compile time.
-Using Java Generic concept, we might write a generic method for sorting an array of objects, then invoke the generic method with Integer arrays, Double arrays, String arrays and so on to sort the array elements
It can be useful several different times:
If we want to use specific types, e.g.: List<Integer> list = new ArrayList<>();
If we want to upper bound public <T extends Number> List<T> fromArrayToList(T[] a) or lower bound.
If we want to deal with multiple bounds. In this case we can also determine the order of the list of bounds <T extends Number & ComparableClass>


#### What is the benefit of having “generic” containers?  //not sure
It the types of it's containing classes can be bounded as subclasses of parentclass and it can hold more different types from other superclasses.
#### Given two Java programs on two different machines. How can you communicate between the two? What are the possible ways?
- We should establish connections on the server side socket(socket connection means that two machines have information about each other;s network locatation(IP Address) and TransmissionClientProtocol port).
-Socket socket = new Socket(“127.0.0.1”, 5000)
  -first argument is IP address of server, second is TCP Port- number representing which application run on server

-to communicate over a socket connection, streams are used to both input and output the data.



- A Java program for a Client :
import java.net.*; 
import java.io.*; 
  
public class Client 
{ 
    // initialize socket and input output streams 
    private Socket socket            = null; 
    private DataInputStream  input   = null; 
    private DataOutputStream out     = null; 
  
    // constructor to put ip address and port 
    public Client(String address, int port) 
    { 
        // establish a connection 
        try
        { 
            socket = new Socket(address, port); 
            System.out.println("Connected"); 
  
            // takes input from terminal 
            input  = new DataInputStream(System.in); 
  
            // sends output to the socket 
            out    = new DataOutputStream(socket.getOutputStream()); 
        } 
        catch(UnknownHostException u) 
        { 
            System.out.println(u); 
        } 
        catch(IOException i) 
        { 
            System.out.println(i); 
        } 
  
        // string to read message from input 
        String line = ""; 
  
        // keep reading until "Over" is input 
        while (!line.equals("Over")) 
        { 
            try
            { 
                line = input.readLine(); 
                out.writeUTF(line); 
            } 
            catch(IOException i) 
            { 
                System.out.println(i); 
            } 
        } 
  
        // close the connection 
        try
        { 
            input.close(); 
            out.close(); 
            socket.close(); 
        } 
        catch(IOException i) 
        { 
            System.out.println(i); 
        } 
    } 
  
    public static void main(String args[]) 
    { 
        Client client = new Client("127.0.0.1", 5000); 
    } 
} 
On the server side:

-A serverSocket which waits for the client request(when a client makes new Socket())

import java.net.*; 
import java.io.*; 
  
public class Server 
{ 
    //initialize socket and input stream 
    private Socket          socket   = null; 
    private ServerSocket    server   = null; 
    private DataInputStream in       =  null; 
  
    // constructor with port 
    public Server(int port) 
    { 
        // starts server and waits for a connection 
        try
        { 
            server = new ServerSocket(port); 
            System.out.println("Server started"); 
  
            System.out.println("Waiting for a client ..."); 
  
            socket = server.accept(); 
            System.out.println("Client accepted"); 
  
            // takes input from the client socket 
            in = new DataInputStream( 
                new BufferedInputStream(socket.getInputStream())); 
  
            String line = ""; 
  
            // reads message from client until "Over" is sent 
            while (!line.equals("Over")) 
            { 
                try
                { 
                    line = in.readUTF(); 
                    System.out.println(line); 
  
                } 
                catch(IOException i) 
                { 
                    System.out.println(i); 
                } 
            } 
            System.out.println("Closing connection"); 
  
            // close connection 
            socket.close(); 
            in.close(); 
        } 
        catch(IOException i) 
        { 
            System.out.println(i); 
        } 
    } 
  
    public static void main(String args[]) 
    { 
        Server server = new Server(5000); 
    } 
} 


#### What is an annotation? What can be annotated and how? Show examples.
-Java annotattion is a tag that represents the metadata i.e. attached with class, interface, methods or fields to indicate some additional information which can be used by java compiler.
-Annotations can be applied to the classes, interfaces, methods and fields. For example the below annotation is being applied to the method.

@Ovveride annotation assures that the subclass method is overriding the parent class method. If it is not so, compile time error occurs.

class ParentClass
{
	public void displayMethod(String msg){
		System.out.println(msg);
	}
}
class SubClass extends ParentClass
{
	@Override
	public void displayMethod(String msg){
		System.out.println("Message is: "+ msg);
	}
	public static void main(String args[]){
		SubClass obj = new SubClass();
		obj.displayMethod("Hey!!");
	}
}

### Database

#### How can you connect your application to a database server? What are the possible ways?
sing intelliJ's database connection tab (it is advised to use environmental variables for the database's access datas and use DAO pattern class which communicates directly with the database).
Using environmental variables and JDBC.
#### What do you know about database normalization?
-Normalization is the process of organizing the data in the database.
-it is used the minimize redundancy from a relation or set of relations.
-It divides the larger table into the smaller table and links them using relationship.

There are 3 types of normalization:
First Normal Form (1NF) sets the very basic rules for an organized database:

Create separate set of tables for each group of related data and identify each row with a unique columns (primary key) or set of columns (composite key)
Eliminate duplicate columns from the table
Second Normal Form (2NF) further addresses the concept of removing duplicate data:

Meet all the requirements of the first normal form
Remove subsets of data that apply to multiple rows of a table and place them in separate tables
Create relationships between these new tables and their predecessors through the use of foreign keys
Third normal form (3NF)*

Meet all the requirements of the second normal form.
Remove columns that are not dependent upon the primary key.
It's advantages are:
Data can be stored as small atomic pieces - it saves space and increases speed
Reduces data anomalies
Easy to maintain
