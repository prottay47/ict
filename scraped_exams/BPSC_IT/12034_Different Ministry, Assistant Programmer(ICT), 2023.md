# Different Ministry, Assistant Programmer(ICT), 2023

- **Original URL:** [https://it.jobqns.com/different-ministry-assistant-programmerict-2023/](https://it.jobqns.com/different-ministry-assistant-programmerict-2023/)
- **Date:** 2026-02-13T19:14:09
- **Categories:** BPSC IT Job Solution, BPSC IT Job Solution 2023, Job Solution 2023

---

#### Different Ministry
Post: Assistant Programmer (ICT) Exam Date: 19.07.2023,  Exam Taker: BPSC



1. (a) Mention two basic differences between 'Call by Value' and 'Call by Reference'. Write a simple program in C to swap two integer values using 'Call by value'.

C Program to Swap Two Integers Using Call by Value

```
#include <stdio.h>
void swap(int a, int b) {
int temp = a;
a = b;
b = temp;
printf("Inside swap function: a = %d, b = %d\n", a, b);
}
int main() {
int x = 10, y = 20;
printf("Before swap in main: x = %d, y = %d\n", x, y);
swap(x, y);
printf("After swap in main: x = %d, y = %d\n", x, y); // Values remain unchanged
return 0;
}
```

**🎥 Video Solution:**  Call by value vs Call by reference

1. (b) What is the diamond problem of multiple inheritance in C++?

**Diamond Problem in C++ (Conceptual Explanation)** The  **Diamond Problem**  in C++ occurs in multiple inheritance when two or more parent classes inherit from the same base class, and a child class inherits from those parent classes. This creates ambiguity in accessing the base class members.

**Inheritance Structure** • Class  **A**  is the base class• Class  **B**  and Class  **C**  both inherit from Class  **A** • Class  **D**  inherits from both Class  **B**  and Class  **C**

**Inheritance Diagram**

```
A
/ \
/   \
B     C
\   /
\ /
D
```

**Why the Problem Occurs** Class  **D**  receives two separate copies of Class  **A** —one through Class  **B**  and another through Class  **C** . When Class D tries to access a member of Class A, the compiler cannot determine which copy should be used, causing ambiguity.

**Result** This ambiguity is known as the Diamond Problem and is a common issue in multiple inheritance without proper control.

**C++ এ Diamond Problem (ধারণাগত ব্যাখ্যা)** C++ এ  **Diamond Problem**  তখন ঘটে যখন multiple inheritance এ দুইটি বা তার বেশি parent class একই base class থেকে inherit করে এবং একটি child class সেই parent class গুলো থেকে inherit করে। এর ফলে base class এর member access করার সময় ambiguity তৈরি হয়।

**Inheritance Structure** • Class  **A**  হলো base class• Class  **B**  এবং Class  **C**  উভয়ই Class  **A**  থেকে inherit করে• Class  **D** , Class  **B**  এবং Class  **C**  থেকে inherit করে

**Inheritance Diagram**

```
A
/ \
/   \
B     C
\   /
\ /
D
```

**সমস্যা কেন হয়** Class  **D**  এর মধ্যে Class  **A**  এর দুইটি আলাদা copy তৈরি হয়—একটি B এর মাধ্যমে এবং অন্যটি C এর মাধ্যমে। যখন Class D থেকে A এর কোনো member access করতে হয়, তখন compiler বুঝতে পারে না কোন copy ব্যবহার করবে।

**ফলাফল** এই অনিশ্চয়তাকেই Diamond Problem বলা হয়, যা multiple inheritance এ একটি সাধারণ সমস্যা।

2. (a) Difference between interpreter and compiler. Write down the phases of a compiler.

**Difference between Interpreter and Compiler**  **Interpreter:**  An interpreter translates and executes the program line by line. It does not generate a separate executable file and stops execution immediately when an error is found. Examples include Python and JavaScript. **Compiler:**  A compiler translates the entire source program into machine code at once and generates an executable file. Errors are reported after compilation. Examples include C and C++.

**Phases of a Compiler** 1)  **Lexical Analysis:**  Converts source code into tokens.2)  **Syntax Analysis:**  Checks grammatical structure using parse trees.3)  **Semantic Analysis:**  Ensures meaningful correctness (type checking, scope).4)  **Intermediate Code Generation:**  Produces an intermediate representation of code.5)  **Code Optimization:**  Improves performance and efficiency of the code.6)  **Code Generation:**  Generates target machine code.

**Interpreter এবং Compiler এর পার্থক্য**  **Interpreter:**  Interpreter প্রোগ্রামটি line by line translate এবং execute করে। এটি আলাদা executable file তৈরি করে না এবং error পাওয়া মাত্র execution বন্ধ করে দেয়। উদাহরণ: Python, JavaScript। **Compiler:**  Compiler পুরো source program একসাথে machine code এ রূপান্তর করে এবং একটি executable file তৈরি করে। Compilation শেষে error দেখায়। উদাহরণ: C, C++।

**Compiler এর ধাপসমূহ** 1)  **Lexical Analysis:**  Source code কে token এ রূপান্তর করে।2)  **Syntax Analysis:**  Program এর grammar সঠিক কিনা পরীক্ষা করে।3)  **Semantic Analysis:**  Meaningful correctness নিশ্চিত করে (type checking, scope)।4)  **Intermediate Code Generation:**  Intermediate code তৈরি করে।5)  **Code Optimization:**  Code এর efficiency এবং performance বাড়ায়।6)  **Code Generation:**  Final machine code তৈরি করে।

2 (b) Define the following terms-
(i) Chromatic number
(ii) Bipartite Graph:
(iii) Clique:  **(i) Chromatic Number**
**(i) Chromatic Number**
একটি graph এর chromatic number হলো সেই graph এর vertex গুলোকে এমনভাবে রঙ করতে যে কোনো দুটি adjacent vertex এর রঙ একই না হয়—এই কাজের জন্য প্রয়োজনীয়  **সর্বনিম্ন রঙের সংখ্যা** ।

**(ii) Bipartite Graph**
Bipartite graph হলো এমন একটি graph যার vertex গুলোকে  **দুটি আলাদা সেটে**  ভাগ করা যায়, যেখানে একই সেটের কোনো দুটি vertex এর মধ্যে edge থাকে না।
**(iii) Clique**
Clique হলো graph এর এমন একটি vertex এর উপসেট যেখানে  **প্রতিটি vertex অন্য সব vertex এর সাথে সরাসরি connected**  থাকে।

3. (a) State De-Morgan's law with an appropriate example.

De Morgan’s Laws are a pair of fundamental transformation rules in Boolean algebra and set theory that help simplify expressions involving complements, intersections, and unions. These laws are essential tools for reducing complex logical expressions, making calculations more manageable and enabling easier problem-solving.

**De Morgan’s Laws:**

- **Complement of the Union** : The complement of the union of two sets is equal to the intersection of their individual complements. ¬(A∪B)=¬A∩¬B
- **Complement of the Intersection** : The complement of the intersection of two sets is equal to the union of their individual complements. ¬(A∩B)=¬A∪¬B

Example:



3. (b) Simplify the following Boolean function using K-map.
Y = A'B'C'D' + A'B'CD' + A'BCD' + A'BCD + AB'C'D'+ AB'CD' + ABCD' + ABCD

**Representing function in k-map**

Making Group:

**Now Simplification:**

**Result:**  BC+B’D’



4. (a) Differentiate between half-duplex and full duplex transmission.

4 (b) Distinguish between routing and forwarding. What are the advantages of net specific routing over host specific routing?

**Difference between Routing and Forwarding**  **Routing:**  Routing is the process of selecting the best path for data packets to travel from source to destination across a network. It is a control-plane function and is performed using routing algorithms and routing tables (e.g., OSPF, RIP, BGP). **Forwarding:**  Forwarding is the process of moving a packet from an incoming interface to the correct outgoing interface based on the forwarding table. It is a data-plane operation and happens very fast inside the router.

**Key Distinction** Routing decides  **which path**  to take, while forwarding decides  **how to send**  the packet on that path.

**Advantages of Network-Specific Routing over Host-Specific Routing**  **1) Smaller Routing Table:**  Network-specific routing stores routes for entire networks instead of individual hosts, reducing routing table size. **2) Faster Lookup:**  Fewer entries in the routing table make route lookup faster and more efficient. **3) Better Scalability:**  It scales well for large networks like the Internet where millions of hosts exist. **4) Lower Overhead:**  Less memory and processing power are required compared to host-specific routing. **5) Easier Management:**  Network administrators can manage routes more easily by handling networks instead of individual hosts.

**Routing এবং Forwarding এর পার্থক্য**  **Routing:**  Routing হলো source থেকে destination পর্যন্ত data packet যাওয়ার জন্য সবচেয়ে ভালো পথ নির্ধারণ করার প্রক্রিয়া। এটি control-plane এর কাজ এবং routing algorithm ও routing table ব্যবহার করে সম্পন্ন হয় (যেমন OSPF, RIP, BGP)। **Forwarding:**  Forwarding হলো router এর incoming interface থেকে packet কে সঠিক outgoing interface এ পাঠানোর প্রক্রিয়া। এটি data-plane এর কাজ এবং খুব দ্রুত ঘটে।

**মূল পার্থক্য** Routing সিদ্ধান্ত নেয়  **কোন পথে**  packet যাবে, আর forwarding কাজ করে সেই পথে packet  **পাঠানোর**  জন্য।

**Host-Specific Routing এর তুলনায় Network-Specific Routing এর সুবিধা**  **1) ছোট Routing Table:**  Network-specific routing এ পুরো network এর জন্য entry থাকে, আলাদা আলাদা host এর জন্য নয়। **2) দ্রুত Lookup:**  Routing table ছোট হওয়ায় route খোঁজা দ্রুত হয়। **3) ভালো Scalability:**  Internet এর মতো বড় network এ এটি ভালোভাবে কাজ করে। **4) কম Overhead:**  কম memory ও processing power প্রয়োজন হয়। **5) সহজ ব্যবস্থাপনা:**  Individual host এর বদলে network ধরে routing করা সহজ।

5. (a) What is deadlock in operating system (OS)? What are the four necessary and sufficient conditions behind deadlock?

**Deadlock**  in an operating system occurs when two or more processes are stuck and cannot proceed because they are each waiting for a resource that another process holds. Essentially, the processes are in a “waiting loop,” and none can continue because they are all waiting for each other to release resources.

**Example:**  Imagine two people on a narrow staircase. One is going up, and the other is going down. Neither can move because the other person is blocking their path, and neither is willing to back up. They are stuck, waiting for the other to move first, which will never happen.

Necessary condition for occuring deadlock / Coffman Conditions

For a deadlock to happen, four conditions must all be true at the same time. These are called the Coffman conditions, named after the researchers who explained them.

- **Mutual Exclusion** : A resource can only be used by one process at a time. If a process is using a resource, no other process can use it until the first process releases it.
- **Hold and Wait** : A process is holding at least one resource and is waiting for additional resources that are currently held by other processes.
- **No Preemption** : Resources cannot be taken away from a process forcefully. A process can only release resources voluntarily when it is no longer needed.
- **Circular Wait** : A cycle exists where each process in the cycle is waiting for a resource that the next process holds. For example, Process A is waiting for Process B’s resource, Process B is waiting for Process C’s resource, and Process C is waiting for Process A’s resource.

**🎥 Video Solution:** Deadlock & its Necessary Condition

5.  (b) What is the difference between micro kernel and macro kernel in the context of OS?

5. (c) Define paging and trashing in the context of OS.

**Paging** Paging is a memory management technique used by the operating system where a process’s logical memory is divided into fixed-size blocks called  **pages** , and physical memory is divided into  **frames** . Pages are loaded into frames as needed, allowing non-contiguous memory allocation and efficient use of RAM.

**Thrashing** Thrashing is a condition in a demand-paged system where the operating system spends most of its time handling  **page faults**  (swapping pages in and out of memory) instead of executing processes. This happens when there are not enough frames to hold the working sets of active processes, leading to very low CPU utilization and poor performance.

**Paging** Paging হলো operating system এর একটি memory management technique যেখানে process এর logical memory কে সমান আকারের  **page**  এ ভাগ করা হয় এবং physical memory কে  **frame**  এ ভাগ করা হয়। প্রয়োজন অনুযায়ী page গুলো frame এ load করা হয়, ফলে memory efficiently ব্যবহার করা যায়।

**Thrashing** Thrashing হলো demand-paged system এর এমন একটি অবস্থা যেখানে operating system অধিকাংশ সময়  **page fault**  handle করতে ব্যয় করে এবং process execute করার সময় খুব কম পায়। এটি ঘটে যখন active process গুলোর জন্য পর্যাপ্ত frame থাকে না, ফলে CPU utilization কমে যায় এবং system performance খারাপ হয়।

6. (a) Discuss the main role of Address Resolution Protocol (ARP) in the network layer of TCP/IP protocol suite.

**Role of Address Resolution Protocol (ARP) in TCP/IP** Address Resolution Protocol (ARP) is used to map a logical IP address to a physical MAC address within a local network. Although ARP works closely with the network layer, it operates between the  **Network Layer**  and the  **Data Link Layer**  of the TCP/IP protocol suite.

**Main Functions of ARP**  **1) IP to MAC Mapping:**  ARP finds the MAC address corresponding to a given IP address so that data can be delivered on the local network. **2) ARP Request:**  When a device wants to send data, it broadcasts an ARP request asking, “Who has this IP address?” **3) ARP Reply:**  The device with the matching IP address responds with its MAC address. **4) ARP Cache:**  The resolved IP–MAC pairs are stored temporarily to reduce future ARP requests and improve efficiency.

**Importance of ARP** Without ARP, devices would not be able to communicate over a local network because physical delivery of packets requires MAC addresses.

**TCP/IP এ Address Resolution Protocol (ARP) এর ভূমিকা** Address Resolution Protocol (ARP) ব্যবহার করা হয় local network এর মধ্যে একটি  **IP address**  কে তার সংশ্লিষ্ট  **MAC address**  এ রূপান্তর করার জন্য। যদিও ARP network layer এর সাথে সম্পর্কিত, এটি মূলত Network Layer এবং Data Link Layer এর মাঝামাঝি কাজ করে।

**ARP এর প্রধান কাজসমূহ**  **1) IP থেকে MAC Mapping:**  নির্দিষ্ট IP address এর জন্য সঠিক MAC address খুঁজে বের করে। **2) ARP Request:**  কোনো device data পাঠানোর আগে broadcast করে জিজ্ঞেস করে—“এই IP address কার?” **3) ARP Reply:**  যেই device এর কাছে সেই IP থাকে, সে তার MAC address পাঠিয়ে দেয়। **4) ARP Cache:**  IP–MAC mapping সাময়িকভাবে সংরক্ষণ করা হয় যাতে বারবার ARP request পাঠাতে না হয়।

**ARP এর গুরুত্ব** ARP ছাড়া local network এ data delivery সম্ভব নয়, কারণ physical network এ data পাঠাতে MAC address অপরিহার্য।

6. (b) Define following terms: (i) Bandwidth (ii) Latency (iii) MAC Address (iv) IP address

**(i) Bandwidth** Bandwidth refers to the maximum amount of data that can be transmitted over a network channel in a given amount of time. It is usually measured in bits per second (bps).

**(ii) Latency** Latency is the time delay between sending data from the source and receiving it at the destination. It is commonly measured in milliseconds (ms).

**(iii) MAC Address** A MAC (Media Access Control) address is a unique physical identifier assigned to a network interface card (NIC) by the manufacturer. It is used for communication within a local network.

**(iv) IP Address** An IP (Internet Protocol) address is a logical address assigned to a device on a network that identifies it uniquely and enables communication across networks.

**(i) Bandwidth** Bandwidth হলো একটি network channel দিয়ে নির্দিষ্ট সময়ে সর্বোচ্চ কত পরিমাণ data পাঠানো যায় তার পরিমাপ। এটি সাধারণত bits per second (bps) এ মাপা হয়।

**(ii) Latency** Latency হলো source থেকে destination এ data পৌঁছাতে যে সময় বিলম্ব ঘটে। এটি সাধারণত millisecond (ms) এ পরিমাপ করা হয়।

**(iii) MAC Address** MAC (Media Access Control) address হলো প্রতিটি network interface card (NIC) এর জন্য manufacturer কর্তৃক দেওয়া একটি unique physical address। এটি local network এ communication এর জন্য ব্যবহৃত হয়।

**(iv) IP Address** IP (Internet Protocol) address হলো একটি logical address যা network এ কোনো device কে uniquely identify করে এবং বিভিন্ন network এর মধ্যে যোগাযোগ সম্ভব করে।

7. (a) What is ACID mean in database system?

**ACID in Database System** ACID represents a set of properties that ensure reliable processing of database transactions. It helps maintain data consistency and integrity in a database system.

**A – Atomicity** Atomicity ensures that a transaction is treated as a single unit. Either all operations of the transaction are completed successfully, or none of them are applied to the database.

**C – Consistency** Consistency ensures that a transaction brings the database from one valid state to another valid state, following all defined rules and constraints.

**I – Isolation** Isolation ensures that multiple transactions executed concurrently do not interfere with each other. Each transaction appears to be executed independently.

**D – Durability** Durability guarantees that once a transaction is committed, its changes are permanently saved in the database, even in case of system failure.

**Database System এ ACID** ACID হলো কিছু গুরুত্বপূর্ণ property এর সমষ্টি যা database transaction কে নির্ভরযোগ্য ও নিরাপদ করে। এটি data consistency এবং integrity বজায় রাখতে সাহায্য করে।

**A – Atomicity** Atomicity নিশ্চিত করে যে একটি transaction সম্পূর্ণভাবে execute হবে অথবা একেবারেই হবে না। মাঝপথে আংশিক execution গ্রহণযোগ্য নয়।

**C – Consistency** Consistency নিশ্চিত করে যে transaction শেষে database একটি valid অবস্থায় থাকে এবং সব নিয়ম ও constraint মেনে চলে।

**I – Isolation** Isolation নিশ্চিত করে যে একাধিক transaction একসাথে চললেও তারা একে অপরকে প্রভাবিত করে না। প্রতিটি transaction আলাদাভাবে execute হওয়ার মতো আচরণ করে।

**D – Durability** Durability নিশ্চিত করে যে transaction commit হওয়ার পর তার পরিবর্তন স্থায়ীভাবে database এ সংরক্ষিত থাকে, system failure হলেও।

7. (b) A system has P processes each needing a maximum of m resources and a total of r resources available. Which conditions must hold to make the system deadlock free?

**Condition for a Deadlock-Free System** To ensure that a system is free from deadlock, the following condition must be satisfied:

**r ≥ P × (m − 1) + 1**

**Where:** •  **P**  = Number of processes•  **m**  = Maximum number of resources each process may request•  **r**  = Total number of available resources

**Explanation** In the worst-case scenario, each process may request up to  **m**  resources but is currently holding only  **m − 1**  resources and waiting for one more.So,• One process holds (m − 1) resources• P processes together hold  **P × (m − 1)**  resources

To avoid deadlock, there must be at least  **one extra resource**  available so that at least one process can obtain all required resources, complete its execution, and release the resources for others.

Therefore, the system will be deadlock-free if: **r ≥ P × (m − 1) + 1**

**Deadlock-Free System এর শর্ত** একটি system কে deadlock-free রাখতে হলে নিচের শর্তটি পূরণ হতে হবে:

**r ≥ P × (m − 1) + 1**

**যেখানে:** •  **P**  = Process এর সংখ্যা•  **m**  = প্রতিটি process সর্বোচ্চ যতটি resource চাইতে পারে•  **r**  = মোট available resource এর সংখ্যা

**ব্যাখ্যা** Worst-case অবস্থায় প্রতিটি process সর্বোচ্চ  **m**  টি resource চাইতে পারে, কিন্তু বর্তমানে  **m − 1**  টি resource ধরে রেখে আরও ১টির জন্য অপেক্ষা করে।তাহলে,• ১টি process ধরে রাখে (m − 1) টি resource• P টি process একসাথে ধরে রাখে  **P × (m − 1)**  টি resource

Deadlock এড়ানোর জন্য system এ অন্তত  **১টি অতিরিক্ত resource**  থাকতে হবে, যাতে কোনো একটি process তার সব resource পেয়ে কাজ শেষ করতে পারে এবং পরে resource গুলো release করতে পারে।

সুতরাং system টি deadlock-free হবে যদি: **r ≥ P × (m − 1) + 1**

8. (a) Define function overloading and function overriding with examples.

**Function Overloading** Function overloading is a concept where multiple functions have the same name but different parameters (either in number or type). It is resolved at  **compile-time** , so it is also called compile-time polymorphism.

**Example**

```
class Math {
public:
int add(int a, int b) { return a + b; }
float add(float a, float b) { return a + b; }
};
```

In this example, the add() function is overloaded to work with both integer and float values.

**Function Overriding** Function overriding allows a derived class to provide its own implementation of a function that is already defined in its base class. It is resolved at  **runtime**  and requires inheritance and virtual functions.

**Example**

```
class Base {
public:
virtual void display() { cout << "Base class display"; }
};

class Derived : public Base {
public:
void display() override { cout << "Derived class display"; }
};
```

Here, the display() function in the derived class overrides the base class version.

**Function Overloading** Function overloading হলো এমন একটি ধারণা যেখানে একই নামের একাধিক function থাকে, কিন্তু তাদের parameter এর সংখ্যা বা type আলাদা হয়। এটি  **compile-time**  এ resolve হয়, তাই একে compile-time polymorphism বলা হয়।

**উদাহরণ**

```
class Math {
public:
int add(int a, int b) { return a + b; }
float add(float a, float b) { return a + b; }
};
```

এই উদাহরণে add() function টি integer এবং float দুই ধরনের data এর জন্য কাজ করে।

**Function Overriding** Function overriding তখন ঘটে যখন একটি derived class তার base class এ থাকা কোনো function এর নতুন implementation প্রদান করে। এটি  **runtime**  এ resolve হয় এবং এর জন্য inheritance ও virtual function প্রয়োজন।

**উদাহরণ**

```
class Base {
public:
virtual void display() { cout << "Base class display"; }
};

class Derived : public Base {
public:
void display() override { cout << "Derived class display"; }
};
```

এখানে derived class, base class এর display() function টি override করেছে।

8. (b) Write a program in C using recursion to find the factorial of an integer.
```
#include <stdio.h>
long int multiplyNumbers(int n);
int main() {
int n;
printf("Enter a positive integer: ");
scanf("%d", &n);
printf("Factorial of %d = %ld", n, multiplyNumbers(n));
return 0;
}

long int multiplyNumbers(int n) {
if (n >= 1)
return n * multiplyNumbers(n - 1);
else
return 1;
}
```

```
Sample I/O:
Enter a positive integer: 5
Factorial of 5 = 120
=== Code Execution Successful ===
```

🔗 **Run Online:**  Factorial using recursion
