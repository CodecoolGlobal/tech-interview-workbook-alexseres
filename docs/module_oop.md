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


### C#

#### Explain the purpose of IL and how does it relate to CLR?
  -Intermediate language(IL) is an oop language designed to be used by compilers for the .NET Framework before static or dynamic compilation to machine code. The IL is used by the .NET Framework to generate machine-independent code as the output of compilation of the source code written in any .NET programming language

  -The .NET Framwrowk provides a run-tiome environment called the Common Language Runtime(CLR), which runs the code and helps in making the development process easier by providing the various services.  It is responsible for managing the execiton of .NET programs regardless of any .NET programming language. CLR provides also memory management, type safety, etc.

  explain:
    -suppose you have written a c# program and save it in a file which is the source code
    - Language specific compiler compiles the sourcedoe int the IL  along with its metadata and CLR provides the servide and runtime enviromnent to IL code. CLR also uses the .NET Framework Library.Metadata provides information about the programming language, environment, version, class libraries to the CLR 


#### What does “managed code” mean?
  -Manage code is a code whose execution is managed by the Common Language Runtime(CLR). It gets the managed code and compiles it into machine code. After that,the code is executed.
#### What is an assembly?
  An assembly is a file that is automatically generated by the compiler upon successful compilation of every .NET application. It can be either a Dynamic Link Library or an executable file like (.exe). It is generated only once for an application and upon each subsequent compilation the assembly gets updated. It can store metadata, manifest information, string , bitmap etc.

#### What is the difference between an EXE and a DLL?
  -The term EXE is shortedned version of executable as it identifies the file as a program. DLL stands for Dynamic Link Library, which commonly contains functions and procedures that can be used by other programs.
  -DLL is a library and therefore cannot be executable. Exe can be executed. Exe always runs in its own address apce i.e., its a seperate process. The purpose of exe is to launch a seperate application of its own. DLL always needs a host exe to run
  . The purpose of DLL is to have a collection fo methods/classes which can be re-used from some other application
#### What is strong-typing versus weak-typing? Which is preferred? Why?    //not sure
  -Strong type means that the type check is done at compile time and weak typing that the type check is done at runtime.
  -In C# is used a strongly typed manner, meaning : a variable is declared of a specific Type (either string, int etc) and cannot later be assigned avalue of different type. However we can use explicit conversion.

  - if you want to have fixed length data type that cannot be changed after compilation, you use strongly-typing

#### What is a namespace?
  -Namespaces are used in C# to organize and provide a level of separation of codes, purpose of writing clenaer codes and managing larger projects. They can be considered as a container which consists of other namespaces, classes, etc.
#### Explain sealed class in C#?
  -Sealed classes are used to restrict the users from inheriting the class.
  -A class can be sealed by using the 'sealed' keyword. The keyword tells the compiler that the class is sealed and therefore cannot be extended. 
  -The main purpose of a sealed class is to take away the inheritance feature from class users so they cannot derive a class from it. One of the best usage of a sealed classes when you have a class with static members
#### What is explicit vs. implicit conversion? Give examples of both of them.
  -Conversion happens when we assign the value of one data type to another. if the data types are compatible then we can do implicit conversion. If not, then they need to be converted explicitly.
  -No special syntax is required because the conversion always succeeds and no data will be list
  -Explicit conversion require cast expression. Casting is required when information might be lost in the conversion. 


  -implicit: 
    int i = 2;
    long l = i;
  -explicit:
    double d = 12.21;
    int i = (int)d;


#### Is a struct stored on the heap or stack?
-struct is the value type data type that represents data structures
-srtuct is a value type, and valu types always stored in the stack.
- if the struct instance is a class member, its memory will be allocated contigiuosly as part of the class instances memory on the heap

#### Can a struct have methods?
  Yes of course, also they can have constructor too.
#### Can DateTimes be null?
  -Datetime is a structure of value Type. 
  -If you use DateTime nullable type. you can assign the null literal to the Datetime type. : DateTime?
#### List out the differences between Array and ArrayList in C#?
  Arrays:
    -Arrays are strongly-typed collections of the same data type and have a fixed length that cannot be changed during run-time.
    -We can access the Array elements by numeric index.
    -Arrays cannot be null
     
  ArrayList:
    -non-generic collection of object whose size increases dynamically. 
    -Arraylist can be used to add unknown data where you dount know the types and the size of the data 
    - You can add and remove items for a specific position using index, also allows dynamic memory allocation, searching, and sorting


#### How is the using() pattern useful? What is IDisposable? How does it support deterministic finalization?
  -The using statement simplify the code that you must write to cleanup an object. The using statement obtains one or more resources executes the statements that you specify and automatically disposes of the object. However the using statement is useful only for objects that are used within the scope of the method in which they are constructed

    using (MyManagedClass mnObj = new MyManagedClass())  
    {  
    ......  
    mnObj.Use(); //use the mnObj object  
    ......  
    } //The compiler will dispose the mnObj object now  
    ......  

    -The using keyword makes sure that the Dispose() method on IDisposable gets called at the end of its scope.


  -THe CLR garbage collector reclaims the memory used by managed objects, but types that use unmanaged resources implement the IDisposable interface to allow the resources needed by these unmanaged resources to be recleimed

  -The IDisposable interface exists for deterministic destruction.
 

#### How can you make sure that objects using dedicated resources (database connection, files, hardware, OS handle, etc.) are released as early as possible?       // not yet implemented



#### Why to use keyword “const” in C#? Give an example.n 
  -If you want to avoid the change of the variable during the execution of the program.e.g. Its good idea to use for database connection
  -public const string ConnectionString = "YourConnectionString";

#### What is the difference between “const” and “readonly” variables in C#?
  -constants need to have a value at compile time, readonly can get value at runtime.(readonly is a runtime constant)
  -constant can be declared inside a method, readonly cant
  -readonly can be used static modifiers, const cannot
#### What is a property in C#?
  -A property in C# is a member of a class that provides a flexible mechanism for classes to expose private fields.
  -Internally, C# properties are special methods called accessors.
  -A property have two accessors, get property and set property accessor
  -a get access return a property value, and a set accessor assigns a new value
  -you should start with capital your property

  class MyClass  
{  
    private int x;  
    public int X  
    {  
        get  
        {  
            return x;  
        }  
        set  
        {  
            x = value;  
        }  
    }  
}  

#### List out two different types of errors in C#?
  -Syntax error occur during development, when you make type mistake in code. 
  bool flag=true;

  While (flag) //syntax error, since c# is case sensitive
  {
  //TO DO:
  }

  -Runtime errors occur during execution of the program. These are also called exceptions. This can be caused due to improper user inputs,design logic or system error

  int a = 5, b = 0;
  int result = a / b; // DivideByZeroException
  

#### What is the difference between “out” and “ref” parameters in C#?
  -ref tells the compiler that the object is initialized before entering the function, while out tells the compiler that the object will be initialized inside the function.

  -So while ref is two-ways, out is out-only.


#### Can we override private virtual method in C#?
  -A virtual method has an implementation in a bse class as well as derived the class. It is used when a methods basic functionality is the same but sometimes more functionality is needed in the derived class. A virtual method is created in the base class that can be overriden in the derived class. We create a virtual method in the bas class using the virtual keyword and that method us overriden in the derived class isong the override keyword

#### What's the difference between IEquatable and just overriding Object.Equals()?
  -There is no real functional difference. The main difference is performance. When generics were introduced in .NET 2.0 they were able to add a bunch of neat classes such as List<T>,Dictionary<K,V>, HashSet<T>, etc. These structures make heavy use of GetHashCode and Equals. But for value types this required boxing. IEquatable lets a structure implement a strongly typed Equals method so no boxing is required. Thus much better performance when using value types with generic collections.

  -Reference types dont benefit as much the IEquatable<T> implementation does let you avoid a cast from System.Object which can make a difference if its called frequently


#### Explain the differences between public, protected, private and internal. Explain access modifier – “protected internal” in C#!
  -All types and type members have an accessibility level. The accessibility level controls whether they can be used from other code in your assembly or other assemblies.
    -public: The type or member can be accessed by any other code in the same assembly or another assembly that references it
    -protected: The type or member can be accessed only by code in the same clss, or in class that derived from that class
    -private: -||- in the same class or struct
    -internal:  -||- in the same assembly, but not for other assemlby
    -protected internal: -||- any code on the assembly in which is declared. or from within a derived class in another assembly


#### What’s the difference between using `override` and `new` keywords when defining method in child class?
  -override: overrides the functionality of virtual method in a base class, providing different functionality
  -new: hides the original method (which aint have to be virtual), providing different functionality. This should only be used where it is absolutely necessary.

  When you hide a method, you can still access the original method by up casting to the base class. 

  public class Base
{
    public virtual void DoIt()
    {
    }
}

public class Derived : Base
{
    public new void DoIt()
    {
    }
}

Base b = new Derived();
Derived d = new Derived();

b.DoIt();                      // Calls Base.DoIt
d.DoIt();                      // Calls Derived.DoIt


#### Explain StringBuilder class in C#!
  The string is immutable. Every time you use one of the methods in System.String class. you createa a new string object in memory, which requires a new allocation of space for that new object. In situations where you need to perform repeated modifications to a string , the overhead associated with creating a new String object can be costly.
  
  --> The System.Text.StringBuilder class can be used when you want to modify a string without creating a new object. For example, using the StringBuilder class can boost performance when concatenating many strings together in a loop

  class GFG { 
  
    // Main Method 
    public static void Main() 
    { 
  
        // "20" is capacity 
        StringBuilder s = new StringBuilder("HELLO ", 20); 
          
        s.Append("GFG"); 
  
        // after printing "GEEKS" 
        // a new line append 
        s.AppendLine("GEEKS"); 
          
        s.Append("GeeksForGeeks"); 
        Console.WriteLine(s); 
    } 
} 
#### How we can sort the array elements in descending order in C#?
  int[] array = new int[]{3,1,4,5,2};
  Array.Sort<int>(array,
                  new Comparison<int>(
                    (i1,i2) => i2.CompareTo(i1)
                  ));
  or

  array = array.OrderByDescending(c => c).ToArray();

#### Can you use a value type as a generic type argument in C#? For example when implementing an interface like (IEquatable).     //not yet implemented 


#### What are Nullable Types in C#?    //complete it later
  -In C# the compiler doesnt allow you to a null value to a variable. The Nullable type allows you to assign a null value to a variable.
    -Nullable<data_type> variable_name = null;
    or a shorter:
    -datatype? variable_name = null;

#### Conceptually, what is the difference between early-binding and late-binding?
  -The compiler performs a process called binding when an object is assigned to an object variable. The early binding (static binding) refers to compile time binding and late binding  (dynamic binding) refers to a runtime binding.

#### What is delegate, event, callback, multicast delegate?
  -delegate:
    -A delegate is a reference type variable that holds the reference to a method. The reference can be changed at runtime. Delegates are especially used for implementing events and the callback methods.
    -Understanding delegates is by thinking  of a delegate to a method signature. It can be a placeholder to one or more method
  -event:
      -events enable a class or object to notify other classes or objects when something of interest occurs. The class sends (or raises) the event is called the publisher and the classes that receive(or handle) the event are called subscribers.
  -callback:  
    -A callback is a function that will be called when a process is done executing a specific task. The usage of callback is usually in asynchrnous logic.

  -multicast delegate:
    It is a delegate that holds the reference of more than one function. When we invoke the multicast delegate, then all the functions which are referenced by the delegate are going to be invoked. 
    using System;

    // Define a custom delegate that has a string parameter and returns void.
    delegate void CustomDel(string s);

    class TestClass
    {
        // Define two methods that have the same signature as CustomDel.
        static void Hello(string s)
        {
            Console.WriteLine($"  Hello, {s}!");
        }

        static void Goodbye(string s)
        {
            Console.WriteLine($"  Goodbye, {s}!");
        }

        static void Main()
        {
            // Declare instances of the custom delegate.
            CustomDel hiDel, byeDel, multiDel, multiMinusHiDel;

            // In this example, you can omit the custom delegate if you
            // want to and use Action<string> instead.
            //Action<string> hiDel, byeDel, multiDel, multiMinusHiDel;

            // Create the delegate object hiDel that references the
            // method Hello.
            hiDel = Hello;

            // Create the delegate object byeDel that references the
            // method Goodbye.
            byeDel = Goodbye;

            // The two delegates, hiDel and byeDel, are combined to
            // form multiDel.
            multiDel = hiDel + byeDel;

            // Remove hiDel from the multicast delegate, leaving byeDel,
            // which calls only the method Goodbye.
            multiMinusHiDel = multiDel - hiDel;

            Console.WriteLine("Invoking delegate hiDel:");
            hiDel("A");
            Console.WriteLine("Invoking delegate byeDel:");
            byeDel("B");
            Console.WriteLine("Invoking delegate multiDel:");
            multiDel("C");
            Console.WriteLine("Invoking delegate multiMinusHiDel:");
            multiMinusHiDel("D");
        }
      }
      /* Output:
      Invoking delegate hiDel:
        Hello, A!
      Invoking delegate byeDel:
        Goodbye, B!
      Invoking delegate multiDel:
        Hello, C!
        Goodbye, C!
      Invoking delegate multiMinusHiDel:
        Goodbye, D!
      */



    "I just met you,
    and this is crazy,
    but here's my number(delegate),
    So if something happens(event),
    Call me, maybe(callback)?"

#### What is enum in C#?
  -C# enum is a value type with a set of related named constans often referred as an enumerator list. The C# enum keyword is used to declare an enumeration. It is a primitive data type, enumeration contains its own values and cannot inherit or cannot pass inheritance. The main benefit of this that constants can be referred to in a consistent, expressive and type safe way.

  enum Season
{
    Spring,
    Summer,
    Autumn,
    Winter
}
#### What is null-conditional operator?
  -THe null-conditional operator ?. will immediately return null if the expression on its left-hand side evaluates to null, instead of throwing a NullReferenceException. If its left-hand side evaluates to a non-null value, it is treated just like a normal . operator. It might return null, its return type is always a nullable type. That means that for a struct or primitive type, it is wrapped into a Nullable<T>.

  -int? length = people?.Length; // null if people is null

#### What is null-coalescing operator?
  -THe null-coalescing operator ?? returns the value of its left-hand operand if it isn't nulll; otherwise, it evauates the right-hand operand and returns its result. The ?? operator doesnt evaluate its right-hand operand if the left-hand operand evaluates to non-null

  static void Main(string[] args)
  {
    string name = null;
    string myname=name ?? "Laxmi";
    Console.WriteLine(myname);
    // Output : Laxmi
  }

#### What is serialization?
  - Serialization is the process of converting an object into a stream of bytes to store the object or transmit it tio a memory, database, or a file. Its main purpose is to save the state of an object in order to be able to recreate it when needed. The reverse process is called deserialization.
  - The object is serlialized to a stream carries the data. The stream may also have information about the object's type, such as its version, culture, and assembly name. 

  -Through serialization, a developer can perform actions such:
    -Sending the object to a remote application by using a web service
    -Passing an object from one domain to another
    -Passing an object through a firewall as a JSON or XML string
    -Maintaining security or user-specific information across applications

  -In C# you can achieve JSON, Binary and XML serialization
  -Binary serialization:
    -Binary serialization uses binary encoding to produce compact serialization for uses such as stroage or socked based network streams. In binary serialization, all members, even members that are read-only are serialized and performance is enchanced.

    static void Serialize()
    {
        // Create a hashtable of values that will eventually be serialized.
        Hashtable addresses = new Hashtable();
        addresses.Add("Jeff", "123 Main Street, Redmond, WA 98052");
        addresses.Add("Fred", "987 Pine Road, Phila., PA 19116");
        addresses.Add("Mary", "PO Box 112233, Palo Alto, CA 94301");

        // To serialize the hashtable and its key/value pairs,
        // you must first open a stream for writing.
        // In this case, use a file stream.
        FileStream fs = new FileStream("DataFile.dat", FileMode.Create);

        // Construct a BinaryFormatter and use it to serialize the data to the stream.
        BinaryFormatter formatter = new BinaryFormatter();
        try
        {
            formatter.Serialize(fs, addresses);
        }
        catch (SerializationException e)
        {
            Console.WriteLine("Failed to serialize. Reason: " + e.Message);
            throw;
        }
        finally
        {
            fs.Close();
        }
    } 
#### What is the difference between Finalize() and Dispose() methods?
  -The Finalize() method(also called destructor to the class)  is used to perform any neccessary final clean-up when a class instance is being collected by the garbage collector

  using System;

  public class Destroyer
  {
    public override string ToString() => GetType().Name;

    ~Destroyer() => Console.WriteLine($"The {ToString()} destructor is executing.");
  }

  The finalizer implicitly calls Finalize on the bass class of the object. Therefore a finalizer is implicitly translated to:
    protected override void Finalize()  
    {  
    try  
    {  
        // Cleanup statements...  
    }  
    finally  
    {  
        base.Finalize();  
    }  
    }  
  


  -The Dispose() method in the other hand is meant to be called by the code that created your class so that you can clean up and release any sources you have acquired (unmanaged data, database connections, file handles, etc) the moment the code is done with you object
#### How do you inherit a class from another class in C#?
  -Inheritance is one of the fundemental attributes of object oriented programming. It allows you to define a child class that reuses(inherits), extends, or modifies the behaviour of a parent class. The class whose members are inherited is called the base class. 

  using System;

namespace InheritanceApplication {
   class Shape {
      public void setWidth(int w) {
         width = w;
      }
      public void setHeight(int h) {
         height = h;
      }
      protected int width;
      protected int height;
   }

   // Derived class
   class Rectangle: Shape {
      public int getArea() { 
         return (width * height); 
      }
   }
   class RectangleTester {
      static void Main(string[] args) {
         Rectangle Rect = new Rectangle();

         Rect.setWidth(5);
         Rect.setHeight(7);

         // Print the area of the object.
         Console.WriteLine("Total area: {0}",  Rect.getArea());
         Console.ReadKey();
      }
   }
  }

#### What is difference between “is” and “as” operators in C#?
  -The is operator is used to check if the run-time type of an object is compatible with the give type or not whereares as operator is used to perform conversion between compatible reference types or Nullable types
  -The is is a boolean type, as not
  -the is operator returns false if the given object is not of the same type whereares as operator return null if the conversion is not possible
  -The is operator is used for only reference, boxing and unboxing, whereares as operator used for only nullable, reference and boxing conversions
  -Using as will not throw a cast exception, but simply return null if the cast fails.

#### What are indexers in C# .NET?
  -Indexers allow instances of a class or struct to be indexed as an arrays. The indexed value can be set or retrieved without explicitly specifying a type or instance member. Indexers resemble properties except that their acccessors take parameters. A user can retrieve or set the indexed value without pointing an instance or a type member. 

  using System;

  class SampleCollection<T>
  {
    // Declare an array to store the data elements.
    private T[] arr = new T[100];

    // Define the indexer to allow client code to use [] notation.
    public T this[int i]
    {
        get { return arr[i]; }
        set { arr[i] = value; }
    }
  }

  class Program
  {
    static void Main()
    {
        var stringCollection = new SampleCollection<string>();
        stringCollection[0] = "Hello, World";
        Console.WriteLine(stringCollection[0]);
    }
  }
  // The example displays the following output:
  //    

#### What is the difference between returning IQueryable<T> vs. IEnumerable<T>?
  -The difference is that IQueryable<T> is the interface that allows LINQ-to-SQL(LINQ to anything ) to work. So if you further refine your query on an IQuerable<T>, that query will be executed in the database if possible.
  -For the IEnumerable<T> case, it will be LINQ-to-object, meaning that all objects matching the original query will have to be loaded into memory from database.

#### What is LINQ? Explain the idea of extension methods.
  -LINQ stands for Language Integrated Query is the name for a set of technologies based on the integration of query capabilities directly into the C# language.
  -Traditionally, queries against data are ecxpressed as simple strings without type checking at compile time.
  -FOr developer who writes queiroes, the most visible language integrated part of LINQ is the query expression. Query expressions are written in a declerative query syntax. By using query syntax, you can perform filtering, ordering, grouping operatins on data sources with a minimum of code 

    class LINQQueryExpressions
  {
      static void Main()
      {

          // Specify the data source.
          int[] scores = new int[] { 97, 92, 81, 60 };

          // Define the query expression.
          IEnumerable<int> scoreQuery =
              from score in scores
              where score > 80
              select score;

          // Execute the query.
          foreach (int i in scoreQuery)
          {
              Console.Write(i + " ");
          }
      }
  }
  // Output: 97 92 81

#### What are the advantages and disadvantages of lazy loading?  // not sure
  -Lazy loading is initializing the member the first time it is referenced. 

      private string _someField;

    public string SomeField
    {
        get 
        {
            // we'd also want to do synchronization if multi-threading.
            if (_someField == null)
            {
                _someField = new String('-', 1000000);
            }

            return _someField;
        }
    }

-advantage:
  -minimizes start up time of the application.
  -application consumes less memory because on-demand loading
  -unnecessary database SQL execution is avoided 
-disadvantage:
  -the code can become complicated

#### How to use of “yield” keyword? Mention at least one practical scenario where it can be used?
  -basic idea: if you want a collection that you can use "foreach" on, but gathering the items into the collection is expensive for some reason (like querying them out of a database), and you will often not need the entire collection, then you create a function that builds the collection one item at a time and yields it back to the consumer( who can then terminate the collection effort early).

  -Think of it this way: You go to the meat counter and want to buy a pound of sliced ham. The butcher takes a 10-pound ham to the back, puts it on the slicer machine, slices the whole thing, then brings the pile of slices back to you and measures out a pound of it. (OLD way). With yield, the butcher brings the slicer machine to the counter, and starts slicing and "yielding" each slice onto the scale until it measures 1-pound, then wraps it for you and you're done. The Old Way may be better for the butcher (lets him organize his machinery the way he likes), but the New Way is clearly more efficient in most cases for the consumer.


#### What are attributes in C#? Give some examples of usage of them.
  -Attributes provide a powerful method of associationg metadata or declarative information with code(assemblies, types, methods, properties, and so forth).
  -Attributes add metadata to your program. Metadata is information about the types defined in a program. ALL .NET assemblies contain a specified set of metadata that describes the types and type members defined in the assembly
  -Attributes can be placed on most any declaration, though a specific attribute might restrict the types of declarations on which it is valid
  -in C# you specify an attribute by placing the name of the attribute enclosed in square brackets
    -[Serializable]
    public class SampleClass
    {
        // Objects of this type can be serialized.
    }

#### By what mechanism does NUnit know what methods to test?
  -Testadapter
#### What is the GAC? What problem does it solve?
  -Each computer where the Common Language Runtime is installed has a machine-wide code cache called the Global Assembly Cache. It stores assemblies specifically designated to be shared by several applications on the computer
  -main benefit :  way to keep DLLs globally accessible without worrying about conflicts. No more DLL Hell. Each architecture and version gets it's own place to live.
  -So the GAC must be a place to store code libraries so they are accessible to all applications running on the machine
#### What is the largest number you can work with in C#?
ulong: Holds 64-bit unsigned integers. The u in ulong stands for unsigned. The smallest possible value of a ulong variable is 0; the largest possible value is 18,446,744,073,709,551,615


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
