# Combined Bank, Senior Officer (IT), 2020

- **Original URL:** [https://it.jobqns.com/combined-bank-senior-officer-it-2020/](https://it.jobqns.com/combined-bank-senior-officer-it-2020/)
- **Date:** 2026-08-08T16:51:24
- **Categories:** Latest Post, Bank IT Job Solution, Bank IT Job Solution 2020, Field-Based Job Solution (MCQ+Written)

---

Senior Officer (IT) • Year 2020

Combined Bank

💼Post Name: Senior Officer (IT)

📅Exam Date: 03-Nov-2020

- ☆

1

Database Management System
Deadlock in DBMS

When does a Deadlock occur and how do you prevent it in a database?

**Techniques to Prevent Deadlock in DBMS**

A  **Deadlock**  occurs when two or more transactions wait indefinitely for resources held by each other. The following techniques can be used to prevent or handle deadlocks in a DBMS:

**1. Wait-Die and Wound-Wait Schemes:**
These schemes decide whether a transaction should wait or be aborted when a resource is requested. In the  **Wait-Die**  scheme, an older transaction may wait, while a younger transaction requesting a resource held by an older transaction is aborted. In the  **Wound-Wait**  scheme, an older transaction can preempt (abort) a younger transaction.

**2. Timeout Mechanism:**
A transaction is automatically aborted if it waits for a lock longer than a specified time. This prevents transactions from waiting indefinitely and helps reduce deadlocks.

**3. Resource Ordering:**
All transactions are required to request resources in a predefined order. This prevents the  **Circular Wait**  condition, which is one of the necessary conditions for deadlock.

**4. Preemptive Resource Allocation:**
If necessary, a resource can be released from a transaction that can safely be aborted. The resource is then allocated to another transaction, helping to avoid deadlock.

**5. Deadlock Detection Algorithms:**
The DBMS can periodically check for deadlocks using a  **Wait-for Graph** . If a cycle is detected in the graph, one of the transactions involved in the cycle can be aborted or rolled back to resolve the deadlock.

**Conclusion:**

Deadlocks can be prevented or resolved using  **Wait-Die/Wound-Wait schemes, Timeout, Resource Ordering, Preemptive Resource Allocation,**  and  **Deadlock Detection** . These techniques help maintain efficient and reliable database transaction processing.



**DBMS-এ Deadlock প্রতিরোধের কৌশলসমূহ**

যখন দুই বা ততোধিক Transaction একে অপরের দ্বারা ব্যবহৃত Resource-এর জন্য অনির্দিষ্টকাল অপেক্ষা করে, তখন  **Deadlock**  সৃষ্টি হয়। DBMS-এ Deadlock প্রতিরোধ বা নিয়ন্ত্রণের জন্য নিম্নলিখিত কৌশলগুলো ব্যবহার করা হয়:

**১. Wait-Die এবং Wound-Wait Scheme:**
এই Scheme-গুলো নির্ধারণ করে কোনো Transaction অপেক্ষা করবে নাকি Abort হবে।  **Wait-Die**  Scheme-এ পুরোনো Transaction অপেক্ষা করতে পারে, কিন্তু কোনো পুরোনো Transaction-এর কাছে থাকা Resource-এর জন্য অপেক্ষাকৃত নতুন Transaction Abort হয়।  **Wound-Wait**  Scheme-এ পুরোনো Transaction প্রয়োজনে নতুন Transaction-কে Abort করে Resource নিতে পারে।

**২. Timeout Mechanism:**
কোনো Transaction নির্দিষ্ট সময়ের বেশি Lock-এর জন্য অপেক্ষা করলে সেটিকে স্বয়ংক্রিয়ভাবে Abort করা হয়। এর ফলে Transaction অনির্দিষ্টকাল অপেক্ষা করতে পারে না এবং Deadlock-এর সম্ভাবনা কমে।

**৩. Resource Ordering:**
সকল Transaction-কে একটি নির্দিষ্ট ক্রম অনুযায়ী Resource Request করার নিয়ম করা হয়। এর ফলে  **Circular Wait**  Condition প্রতিরোধ করা যায়, যা Deadlock-এর একটি গুরুত্বপূর্ণ কারণ।

**৪. Preemptive Resource Allocation:**
যদি কোনো Transaction-কে নিরাপদে Abort করা যায়, তাহলে তার দখলে থাকা Resource Release করে অন্য Transaction-কে দেওয়া যেতে পারে। এর মাধ্যমে Deadlock এড়ানো যায়।

**৫. Deadlock Detection Algorithm:**
DBMS একটি  **Wait-for Graph**  ব্যবহার করে নিয়মিত Deadlock শনাক্ত করতে পারে। Graph-এ কোনো  **Cycle**  পাওয়া গেলে Cycle-এর একটি Transaction Abort বা Rollback করে Deadlock সমাধান করা হয়।

**উপসংহার:**

DBMS-এ  **Wait-Die/Wound-Wait Scheme, Timeout, Resource Ordering, Preemptive Resource Allocation**  এবং  **Deadlock Detection**  ব্যবহার করে Deadlock প্রতিরোধ বা সমাধান করা যায়। এগুলো Database Transaction Processing-কে কার্যকর ও নির্ভরযোগ্য রাখতে সাহায্য করে।

- ☆

2

Computer Network

What is the difference between packet sniffing (Snooping) and Packet spoofing?

**Packet Sniffing (Snooping)**  is the process of capturing and monitoring network packets as they travel through a network. An attacker or administrator uses a packet sniffer to observe network traffic and may obtain information such as IP addresses, protocols, or unencrypted data.

**Packet Spoofing**  is the process of creating or modifying network packets by using a forged source address or other information so that the packet appears to come from a trusted or different source.

Packet Sniffing (Snooping)
Packet Spoofing

Captures and monitors existing network packets.
Creates or modifies packets with false information.

Primarily used to  **observe or intercept**  network communication.
Primarily used to  **impersonate**  another device or source.

Does not necessarily modify the packets being observed.
Changes or forges packet information, such as the source IP address.

Example: Capturing network traffic using a packet analyzer.
Example: Sending a packet with a forged source IP address.

**Conclusion:**

In simple terms,  **Sniffing means listening to network traffic** , whereas  **Spoofing means pretending to be another source by using forged packet information** .



**Packet Sniffing (Snooping)**  হলো Network-এর মধ্য দিয়ে চলাচলকারী Data Packet Capture এবং Monitor করার প্রক্রিয়া। এর মাধ্যমে Network Traffic পর্যবেক্ষণ করে IP Address, Protocol এবং Unencrypted Data-এর মতো তথ্য সংগ্রহ করা যেতে পারে।

**Packet Spoofing**  হলো Network Packet তৈরি বা পরিবর্তন করে তাতে মিথ্যা Source Address বা অন্যান্য তথ্য ব্যবহার করার প্রক্রিয়া, যাতে Packet-টি কোনো Trusted বা অন্য Source থেকে এসেছে বলে মনে হয়।

Packet Sniffing (Snooping)
Packet Spoofing

বিদ্যমান Network Packet Capture এবং Monitor করে।
ভুয়া তথ্যসহ Packet তৈরি বা পরিবর্তন করে।

মূলত Network Communication  **Observe বা Intercept**  করার জন্য ব্যবহৃত হয়।
মূলত অন্য Device বা Source-এর পরিচয়  **Impersonate**  করার জন্য ব্যবহৃত হয়।

সাধারণত পর্যবেক্ষণ করা Packet পরিবর্তন করে না।
যেমন Source IP Address-এর মতো Packet-এর তথ্য পরিবর্তন বা জাল করতে পারে।

উদাহরণ: Packet Analyzer দিয়ে Network Traffic Capture করা।
উদাহরণ: Forged Source IP Address ব্যবহার করে Packet পাঠানো।

**উপসংহার:**

সহজভাবে বলা যায়,  **Sniffing হলো Network Traffic পর্যবেক্ষণ বা শোনা** , আর  **Spoofing হলো ভুয়া Packet Information ব্যবহার করে অন্য Source হিসেবে পরিচয় দেওয়া** ।



☆

3

Database Management System

Classify the failure of Database Management.

**Classification of Database Failures**

A  **Database Failure**  occurs when the database system cannot continue its normal operation or when committed data may be lost. Database failures can be classified into the following types:

**1. Transaction Failure:**
A transaction may fail because of logical errors, invalid data, constraint violations, or deadlock. The failed transaction is usually rolled back.

**2. System Failure:**
A system crash caused by power failure, hardware failure, or operating system failure may cause the contents of main memory to be lost. However, data stored on secondary storage generally remains safe.

**3. Disk Failure:**
Failure of a hard disk or other storage device can cause loss or corruption of database data stored on that device.

**4. Media Failure:**
Damage or corruption of storage media, such as disk crashes or bad sectors, can make database files inaccessible or permanently lost.

**5. Communication Failure:**
In a distributed database system, network failure or communication problems may prevent transactions from completing correctly between different sites.

**6. Catastrophic Failure:**
Events such as fire, flood, earthquake, or major hardware destruction can damage the entire database system and its storage.

**Conclusion:**

The major database failures are  **Transaction Failure, System Failure, Disk/Media Failure, Communication Failure,**  and  **Catastrophic Failure** . Backup, logging, recovery mechanisms, and fault-tolerant systems are used to recover from these failures.



**Database Failure-এর শ্রেণিবিভাগ**
যখন Database System স্বাভাবিকভাবে কাজ করতে পারে না অথবা Commit করা Data হারিয়ে যাওয়ার সম্ভাবনা থাকে, তখন তাকে  **Database Failure**  বলে। Database Failure-কে নিম্নলিখিতভাবে শ্রেণিবদ্ধ করা যায়:

**১. Transaction Failure:**
Logical Error, Invalid Data, Constraint Violation অথবা Deadlock-এর কারণে কোনো Transaction ব্যর্থ হতে পারে। সাধারণত ব্যর্থ Transaction-কে Rollback করা হয়।

**২. System Failure:**
Power Failure, Hardware Failure অথবা Operating System Failure-এর কারণে System Crash হলে Main Memory-এর Data হারিয়ে যেতে পারে। তবে Secondary Storage-এ সংরক্ষিত Data সাধারণত নিরাপদ থাকে।

**৩. Disk Failure:**
Hard Disk বা অন্য কোনো Storage Device নষ্ট হলে সেখানে সংরক্ষিত Database Data হারিয়ে যেতে বা Corrupt হতে পারে।

**৪. Media Failure:**
Disk Crash, Bad Sector অথবা Storage Media-এর ক্ষতির কারণে Database File Access করা সম্ভব নাও হতে পারে বা স্থায়ীভাবে Data হারিয়ে যেতে পারে।

**৫. Communication Failure:**
Distributed Database System-এ Network Failure বা Communication Problem-এর কারণে বিভিন্ন Site-এর মধ্যে Transaction সঠিকভাবে সম্পন্ন নাও হতে পারে।

**৬. Catastrophic Failure:**
Fire, Flood, Earthquake অথবা বড় ধরনের Hardware Destruction-এর মতো ঘটনায় সম্পূর্ণ Database System এবং Storage ক্ষতিগ্রস্ত হতে পারে।

**উপসংহার:**

Database-এর প্রধান Failure হলো  **Transaction Failure, System Failure, Disk/Media Failure, Communication Failure**  এবং  **Catastrophic Failure** । এসব Failure থেকে Recovery করার জন্য  **Backup, Logging, Recovery Mechanism**  এবং Fault-Tolerant System ব্যবহার করা হয়।



☆

4

Programming Concept

Write the different approaches of debugging a code.

**Different Approaches of Debugging a Code**

**Debugging**  is the process of finding, analyzing, and correcting errors or bugs in a computer program. The common approaches to debugging are:

**1. Brute Force Approach:**
In this approach, the programmer uses print statements, logs, memory dumps, or other diagnostic information to find where the error occurs.

**2. Backtracking:**
The programmer starts from the point where the error is observed and traces the program backward through previous statements to identify the source of the error.

**3. Cause Elimination:**
Possible causes of an error are identified and systematically eliminated one by one until the actual cause is found.

**4. Program Slicing:**
Only the statements or parts of the program that can affect a particular variable or incorrect output are examined. This reduces the amount of code that needs to be analyzed.

**5. Using a Debugger:**
A debugging tool is used to execute the program step-by-step, set breakpoints, inspect variables, and monitor program execution to locate the bug.

**Conclusion:**

The main debugging approaches are  **Brute Force, Backtracking, Cause Elimination, Program Slicing,**  and  **Debugger-based debugging** . These techniques help programmers identify and correct errors efficiently.



**Code Debugging-এর বিভিন্ন Approach**

**Debugging**  হলো Computer Program-এর Error বা Bug খুঁজে বের করা, বিশ্লেষণ করা এবং সংশোধন করার প্রক্রিয়া। Code Debugging-এর সাধারণ Approach-গুলো হলো:

**১. Brute Force Approach:**
এই পদ্ধতিতে  **Print Statement, Log, Memory Dump**  ইত্যাদি ব্যবহার করে Program-এর কোথায় Error ঘটছে তা খুঁজে বের করা হয়।

**২. Backtracking:**
যে স্থানে Error দেখা যায় সেখান থেকে Program-এর আগের Statement বা Execution ধাপে পিছনের দিকে গিয়ে Error-এর মূল কারণ খুঁজে বের করা হয়।

**৩. Cause Elimination:**
Error-এর সম্ভাব্য কারণগুলো চিহ্নিত করে একে একে বাদ দেওয়া হয়, যতক্ষণ না প্রকৃত কারণটি শনাক্ত করা যায়।

**৪. Program Slicing:**
কোনো নির্দিষ্ট Variable বা Incorrect Output-কে প্রভাবিত করতে পারে এমন Program-এর নির্দিষ্ট অংশগুলো বিশ্লেষণ করা হয়। এতে সম্পূর্ণ Program পরীক্ষা করার প্রয়োজন হয় না।

**৫. Using a Debugger:**
Debugger Tool ব্যবহার করে Program-কে Step-by-Step Execute করা, Breakpoint স্থাপন করা, Variable-এর Value পরীক্ষা করা এবং Program-এর Execution পর্যবেক্ষণ করে Bug খুঁজে বের করা হয়।

**উপসংহার:**

Debugging-এর প্রধান Approach হলো  **Brute Force, Backtracking, Cause Elimination, Program Slicing**  এবং  **Debugger-based Debugging** । এসব পদ্ধতি ব্যবহার করে Program-এর Error কার্যকরভাবে শনাক্ত ও সংশোধন করা যায়।



☆

5

Microprocessor & Computer Architecture

Why Heterogeneous Multicore Processor (HMP) gaining more popularity?

A  **Heterogeneous Multicore Processor (HMP)**  contains different types of CPU cores, typically high-performance cores and power-efficient cores. It is becoming more popular because it provides a better balance between performance and energy efficiency.

**1. Better Performance:**
High-performance cores can handle demanding applications and computationally intensive tasks efficiently.

**2. Lower Power Consumption:**
Power-efficient cores can handle lightweight tasks using less energy, which reduces overall power consumption.

**3. Improved Energy Efficiency:**
The processor can assign each task to the most suitable type of core, providing high performance when needed while saving energy for less demanding tasks.

**4. Better Thermal Management:**
Using efficient cores for lighter workloads reduces heat generation and helps maintain suitable operating temperatures.

**5. Suitable for Modern Devices:**
HMP is especially useful in smartphones, laptops, servers, and embedded systems where both high performance and long battery life or lower operating cost are important.

**Conclusion:**

HMP is gaining popularity because it provides  **high performance, lower power consumption, better energy efficiency, and improved thermal management**  by using different types of processor cores according to workload requirements.



**Heterogeneous Multicore Processor (HMP)** -এ বিভিন্ন ধরনের CPU Core থাকে। সাধারণত এতে High-Performance Core এবং Power-Efficient Core উভয়ই থাকে। এটি Performance এবং Energy Efficiency-এর মধ্যে ভালো ভারসাম্য তৈরি করে।

**১. উন্নত Performance:**
High-Performance Core ব্যবহার করে Computationally Intensive এবং কঠিন কাজ দ্রুত সম্পন্ন করা যায়।

**২. কম Power Consumption:**
সাধারণ বা হালকা কাজগুলো Power-Efficient Core দিয়ে সম্পন্ন করা যায়, ফলে কম Energy ব্যবহার হয়।

**৩. উন্নত Energy Efficiency:**
Processor প্রতিটি কাজের জন্য উপযুক্ত Core নির্বাচন করতে পারে। ফলে প্রয়োজনের সময় High Performance এবং সাধারণ কাজের সময় Energy Saving করা সম্ভব হয়।

**৪. উন্নত Thermal Management:**
হালকা কাজ Efficient Core-এ সম্পন্ন করলে কম Heat উৎপন্ন হয় এবং Processor-এর Temperature নিয়ন্ত্রণে রাখা সহজ হয়।

**৫. আধুনিক Device-এর জন্য উপযোগী:**
Smartphone, Laptop, Server এবং Embedded System-এ HMP বিশেষভাবে কার্যকর, কারণ এসব ক্ষেত্রে High Performance-এর পাশাপাশি কম Power Consumption গুরুত্বপূর্ণ।

**উপসংহার:**

HMP জনপ্রিয় হচ্ছে কারণ এটি বিভিন্ন ধরনের Core ব্যবহার করে  **উচ্চ Performance, কম Power Consumption, উন্নত Energy Efficiency**  এবং  **ভালো Thermal Management**  প্রদান করে।



☆

6

Design Analysis of Algorithm

Discuss Complexity factor of algorithm.

**Complexity Factors of an Algorithm**

The  **Complexity of an Algorithm**  refers to the amount of resources required by an algorithm as the size of the input increases. The main factors affecting algorithm complexity are:

**1. Time Complexity:**
It measures the amount of  **time or number of operations**  required by an algorithm to complete its execution for a given input size. It is commonly expressed using  **Big-O notation** , such as O(n), O(log n), and O(n²).

**2. Space Complexity:**
It measures the amount of  **memory or storage space**  required by an algorithm during execution. It includes memory used for variables, data structures, and temporary storage.

**3. Input Size:**
The complexity of an algorithm depends on the  **size of the input** . Generally, as the input size increases, the number of operations and required resources also increase.

**4. Nature of Input:**
The arrangement or characteristics of input data can affect the execution time. An algorithm may have different  **Best Case, Average Case,**  and  **Worst Case**  complexities.

**5. Data Structures Used:**
The choice of data structure, such as  **Array, Linked List, Stack, Queue,**  or  **Tree** , can significantly affect the efficiency and complexity of an algorithm.

**Conclusion:**

The major complexity factors are  **Time, Space, Input Size, Nature of Input,**  and  **Data Structures** . A good algorithm should use minimum time and memory while producing the correct result.



☆

7

Microprocessor & Computer Architecture

What is block and page? Draw simple block and page diagram in SSD (Solid State Drive).

In a  **Solid State Drive (SSD)** , data is stored in flash memory. The flash memory is organized into  **Pages**  and  **Blocks** .

**1. Page:**
A  **Page**  is the smallest unit of data that can normally be  **read or programmed (written)**  in NAND flash memory. A page typically contains several KB of data.

**2. Block:**
A  **Block**  is a group of multiple pages. The  **erase operation**  in NAND flash memory is normally performed at the block level.

```
SSD (NAND Flash Memory)
|
+----------------+----------------+
|                                 |
BLOCK 1                            BLOCK 2
|                                 |
+----+----+                       +----+----+
|    |    |                       |    |    |
Page 1 Page 2 Page 3 ...          Page 1 Page 2 Page 3 ...
|    |    |                       |    |    |
4 KB  4 KB  4 KB                  4 KB  4 KB  4 KB
```

**Page:**  A Page is the basic unit for reading and writing data in NAND flash memory.
**Block:**  A Block is a group of multiple Pages and is the basic unit for erase operations.

☆

8

Data Communication

What is GGSN? Write main function of GGSN.

**GGSN (Gateway GPRS Support Node)**

**GGSN**  stands for  **Gateway GPRS Support Node** . It is a major component of the GPRS/2.5G mobile packet-switched network. It acts as a gateway between the mobile network and external packet data networks such as the  **Internet** .

**Main Functions of GGSN:**

**1. Gateway to External Networks:**
Connects the GPRS/packet core network to external networks such as the Internet and private IP networks.

**2. IP Address Management:**
Assigns or manages IP addresses for mobile subscribers when they establish a data connection.

**3. Packet Routing:**
Routes data packets between the mobile user and external packet data networks.

**4. Authentication and Access Control:**
Works with other network components to support subscriber authentication and control access to packet data services.

**5. Charging and Data Usage:**
Collects information about packet data usage for charging and billing purposes.

**Conclusion:**

The main role of GGSN is to act as a  **gateway between the mobile packet network and external data networks** , while providing IP address management, packet routing, access control, and charging support.



**GGSN (Gateway GPRS Support Node)**

**GGSN** -এর পূর্ণরূপ হলো  **Gateway GPRS Support Node** । এটি GPRS/2.5G Mobile Packet-Switched Network-এর একটি গুরুত্বপূর্ণ Component। এটি Mobile Network এবং  **Internet**  বা অন্যান্য External Packet Data Network-এর মধ্যে Gateway হিসেবে কাজ করে।

**GGSN-এর প্রধান Functions:**

**১. External Network-এর সাথে সংযোগ:**
GPRS/Packet Core Network-কে Internet এবং Private IP Network-এর মতো External Network-এর সাথে সংযুক্ত করে।

**২. IP Address Management:**
Mobile Subscriber Data Connection স্থাপন করলে তার IP Address Assign বা Manage করতে সাহায্য করে।

**৩. Packet Routing:**
Mobile User এবং External Packet Data Network-এর মধ্যে Data Packet Route করে।

**৪. Authentication ও Access Control:**
অন্যান্য Network Component-এর সাথে কাজ করে Subscriber Authentication এবং Packet Data Service-এর Access Control-এ সহায়তা করে।

**৫. Charging ও Data Usage:**
Subscriber-এর Packet Data Usage-এর তথ্য সংগ্রহ করে, যা Charging এবং Billing-এর কাজে ব্যবহৃত হয়।

**উপসংহার:**

GGSN-এর প্রধান কাজ হলো  **Mobile Packet Network এবং External Data Network-এর মধ্যে Gateway হিসেবে কাজ করা** । এছাড়া এটি IP Address Management, Packet Routing, Access Control এবং Charging-এর মতো কাজেও সহায়তা করে।



☆

9

Data Communication

Describe Internet Exchange (IX) national and international level data communication function.

**Internet Exchange (IX) and Its Data Communication Functions**

An  **Internet Exchange (IX)** , also called an  **Internet Exchange Point (IXP)** , is a physical networking facility where different Internet Service Providers (ISPs), network operators, content providers, and other networks connect and exchange Internet traffic directly.

**1. Data Communication at National Level:**

At the national level, an IX allows different ISPs and networks within a country to exchange local Internet traffic directly. For example, traffic between two users or websites located in the same country can remain within the country's network instead of being routed through an international network.

**Functions at National Level:**
• Exchanges traffic between different national ISPs.
• Reduces dependence on international bandwidth.
• Reduces latency and improves Internet speed.
• Reduces the cost of international bandwidth.
• Improves local access to websites, cloud services, and content.

**2. Data Communication at International Level:**

At the international level, Internet networks exchange traffic through international IXPs, submarine cables, international transit providers, and other interconnected networks. This enables communication between users, servers, and services located in different countries.

**Functions at International Level:**
• Exchanges Internet traffic between networks of different countries.
• Provides connectivity to international Internet destinations.
• Supports international content and cloud services.
• Provides alternative network paths and improves reliability.
• Helps networks efficiently exchange large volumes of international traffic.

**Simple Working:(ধারণাগত)**

☆

10

Microprocessor & Computer Architecture

Write are the parameters that are being used to evaluate the performance of memory?

**Parameters Used to Evaluate Memory Performance**

The performance of a computer memory is evaluated using several important parameters:

**1. Access Time:**
It is the time required to locate and access a particular data item from memory. Lower access time means faster memory.

**2. Memory Cycle Time:**
It is the minimum time interval required between two successive memory operations.

**3. Transfer Rate:**
It indicates the amount of data that can be transferred between memory and the processor per unit of time. Higher transfer rate means better performance.

**4. Memory Capacity:**
It represents the total amount of data that the memory can store, usually measured in KB, MB, GB, or TB.

**5. Cost per Bit:**
It represents the cost of storing one bit of information. A lower cost per bit generally makes a memory technology more economical.

**6. Bandwidth:**
It represents the amount of data that can be transferred by the memory in a given period, usually expressed in bytes per second.

**Conclusion:**

The major parameters used to evaluate memory performance are  **Access Time, Memory Cycle Time, Transfer Rate, Capacity, Cost per Bit,**  and  **Bandwidth** .



**Memory-এর Performance মূল্যায়নের Parameters**

Computer Memory-এর Performance মূল্যায়নের জন্য কয়েকটি গুরুত্বপূর্ণ Parameter ব্যবহার করা হয়:

**১. Access Time:**
Memory থেকে নির্দিষ্ট Data খুঁজে বের করে Access করতে যে সময় লাগে তাকে Access Time বলে। Access Time কম হলে Memory দ্রুত কাজ করে।

**২. Memory Cycle Time:**
পরপর দুটি Memory Operation-এর মধ্যে প্রয়োজনীয় সর্বনিম্ন সময়কে Memory Cycle Time বলে।

**৩. Transfer Rate:**
প্রতি একক সময়ে Memory এবং Processor-এর মধ্যে কত পরিমাণ Data Transfer করা যায় তাকে Transfer Rate বলে। Transfer Rate বেশি হলে Performance ভালো হয়।

**৪. Memory Capacity:**
Memory সর্বমোট কত পরিমাণ Data সংরক্ষণ করতে পারে তাকে Memory Capacity বলে। এটি সাধারণত KB, MB, GB বা TB-তে প্রকাশ করা হয়।

**৫. Cost per Bit:**
এক Bit Data সংরক্ষণ করতে যে খরচ হয় তাকে Cost per Bit বলে। Cost per Bit কম হলে Memory তুলনামূলকভাবে বেশি সাশ্রয়ী।

**৬. Bandwidth:**
নির্দিষ্ট সময়ে Memory কত পরিমাণ Data Transfer করতে পারে তাকে Memory Bandwidth বলে। এটি সাধারণত Bytes per Second-এ প্রকাশ করা হয়।

**উপসংহার:**

Memory Performance মূল্যায়নের প্রধান Parameter হলো  **Access Time, Memory Cycle Time, Transfer Rate, Capacity, Cost per Bit**  এবং  **Bandwidth** ।



☆

11

Programming Concept

Write a program that check a number is Armstrong or not.

**C Program to Check Armstrong Number**

An  **Armstrong number**  is a number whose sum of each digit raised to the power of the total number of digits is equal to the original number. For example,  **153 = 1³ + 5³ + 3³ = 153** .

```
#include <stdio.h>

int main() {
int num, original, remainder, digits = 0;
int sum = 0, power, i;

printf("Enter a number: ");
scanf("%d", &num);

original = num;

/* Count the number of digits */
int temp = num;
while (temp != 0) {
digits++;
temp /= 10;
}

/* Calculate the sum of powers of digits */
temp = num;

while (temp != 0) {
remainder = temp % 10;
power = 1;

for (i = 0; i < digits; i++) {
power *= remainder;
}

sum += power;
temp /= 10;
}

if (sum == original)
printf("%d is an Armstrong number.\n", original);
else
printf("%d is not an Armstrong number.\n", original);

return 0;
}
```

**Example:**

For input  **153** :
153 = 1³ + 5³ + 3³ = 1 + 125 + 27 =  **153** .

Therefore,  **153 is an Armstrong number** .


☆

12

Miscellaneous

Ergonomics is study of characteristics of iteration. How to measure quality of sitting good chair (ergonomics)

**Ergonomics and Quality of Sitting in a Good Chair**

**Ergonomics**  is the study of how people interact with their workplace, tools, furniture, and environment. An ergonomically designed chair should provide comfort, proper body support, and reduce physical strain during prolonged sitting.

**Measures of a Good Ergonomic Chair:**

**1. Adjustable Seat Height:**
The seat height should allow the feet to rest flat on the floor and the knees to remain approximately at a right angle.

**2. Proper Back Support:**
The backrest should support the lower back (lumbar region) and maintain the natural curve of the spine.

**3. Comfortable Seat Depth and Width:**
The seat should provide sufficient support without pressing against the back of the knees.

**4. Adjustable Armrests:**
Armrests should allow the shoulders to remain relaxed and the elbows to stay close to the body.

**5. Proper Sitting Posture:**
The head should remain balanced, shoulders relaxed, back supported, and thighs approximately parallel to the floor.

**6. Comfortable and Stable Base:**
A stable five-point base with smooth movement provides better balance and reduces unnecessary body movement.

**7. Material and Cushioning:**
The seat should have adequate cushioning and breathable material to provide comfort during long periods of sitting.

**Conclusion:**

The quality of an ergonomic chair can be measured by its  **adjustability, lumbar support, comfort, stability, proper posture support,**  and ability to reduce fatigue and physical strain during prolonged sitting.



**Ergonomics এবং ভালো চেয়ারে বসার গুণমান**
**Ergonomics**  হলো মানুষ কীভাবে তার Workplace, Tools, Furniture এবং Environment-এর সাথে কাজ করে তার অধ্যয়ন। একটি Ergonomic Chair দীর্ঘ সময় বসার সময় আরাম, সঠিক Body Support এবং শারীরিক চাপ কমাতে সাহায্য করে।

**ভালো Ergonomic Chair-এর বৈশিষ্ট্য:**

**১. Adjustable Seat Height:**
চেয়ারের উচ্চতা এমন হওয়া উচিত যাতে পা মেঝেতে সমতলভাবে থাকে এবং হাঁটু প্রায় সমকোণে থাকে।

**২. Proper Back Support:**
Backrest-এর মাধ্যমে Lower Back বা Lumbar Region সঠিকভাবে Support পাওয়া উচিত এবং মেরুদণ্ডের স্বাভাবিক বাঁক বজায় থাকা উচিত।

**৩. Comfortable Seat Depth ও Width:**
Seat-এর আকার এমন হওয়া উচিত যাতে শরীর ভালোভাবে Support পায় এবং হাঁটুর পেছনে অতিরিক্ত চাপ না পড়ে।

**৪. Adjustable Armrests:**
Armrest এমন হওয়া উচিত যাতে কাঁধ Relaxed থাকে এবং কনুই শরীরের কাছাকাছি থাকে।

**৫. Proper Sitting Posture:**
মাথা সোজা ও ভারসাম্যপূর্ণ, কাঁধ Relaxed, পিঠ Supported এবং উরু মেঝের প্রায় সমান্তরাল থাকা উচিত।

**৬. Comfortable ও Stable Base:**
Stable Five-point Base ভালো Balance প্রদান করে এবং অপ্রয়োজনীয় Body Movement কমায়।

**৭. Material ও Cushioning:**
দীর্ঘ সময় বসার জন্য Seat-এ পর্যাপ্ত Cushioning এবং আরামদায়ক ও Breathable Material থাকা উচিত।

**উপসংহার:**

একটি Ergonomic Chair-এর গুণমান  **Adjustability, Lumbar Support, Comfort, Stability, Proper Posture Support**  এবং দীর্ঘ সময় বসার ফলে  **Fatigue ও Physical Strain কমানোর ক্ষমতা**  দ্বারা নির্ণয় করা যায়।



☆

13

Data Structure

Linear Search (Searching Algorithm) which is used to find whether a given number is present in an array and if it is present then at what location is occurs (Using any programming language). Or, Write Linear Search implementation program.

**Linear Search Implementation**

**Linear Search**  is a simple searching algorithm that checks each element of an array sequentially until the required element is found or the end of the array is reached.

**Algorithm:**

```
1. Start
2. Read the array and the number to be searched.
3. Set i = 0.
4. Compare the search number with A[i].
5. If A[i] equals the search number, display its location and stop.
6. Otherwise, increment i and repeat Step 4.
7. If the end of the array is reached, display "Element not found".
8. Stop.
```

**C Program:**

```
#include <stdio.h>

int main() {
int a[100], n, key, i, found = 0;

printf("Enter number of elements: ");
scanf("%d", &n);

printf("Enter the elements:\n");
for (i = 0; i < n; i++) {
scanf("%d", &a[i]);
}

printf("Enter the number to search: ");
scanf("%d", &key);

for (i = 0; i < n; i++) {
if (a[i] == key) {
printf("Element found at location %d\n", i + 1);
found = 1;
break;
}
}

if (!found) {
printf("Element not found\n");
}

return 0;
}
```

**Example:**

If the array is  **10, 25, 30, 45, 60**  and the search value is  **45** , Linear Search checks the elements one by one and finds 45 at  **location 4** .

**Time Complexity:**  Best case:  **O(1)** , Worst case:  **O(n)** .

- ☆

14

Data Structure
BST

Explain operation of Binary Search Tree.

**Operation of Binary Search Tree (BST)**

A  **Binary Search Tree (BST)**  is a binary tree in which, for every node, all values in the left subtree are smaller than the node's value and all values in the right subtree are greater than the node's value.

**1. Insertion:**
To insert a new value, compare it with the root. If the value is smaller, move to the left subtree; if it is greater, move to the right subtree. Continue until an empty position is found, then insert the new node.

**2. Searching:**
Start from the root and compare the required value with the current node. If it is equal, the value is found. If it is smaller, search the left subtree; if it is greater, search the right subtree.

**3. Deletion:**
A node can be deleted in three cases:  **leaf node** ,  **node with one child** , and  **node with two children** . For two children, the node is usually replaced by its inorder successor or predecessor.

**Example:**

```
50
/  \
30    70
/ \    / \
20 40  60 80
```

In this tree, values smaller than  **50**  are on the left and values greater than  **50**  are on the right. Therefore, searching, insertion, and deletion can be performed efficiently.

**Time Complexity:**
Average case:  **O(log n)**
Worst case:  **O(n)** , when the tree becomes skewed.

**Conclusion:**

The main operations of a Binary Search Tree are  **Insertion, Searching,**  and  **Deletion** . Its efficiency depends on the height of the tree.

- ☆

15

Computer Network
Swithcing Technique & Protocol

ARP used in TCP/IP for perform some operation, write the functions of ARP.

**Functions of ARP (Address Resolution Protocol)**

**ARP (Address Resolution Protocol)**  is a protocol used in TCP/IP networks to find the  **MAC address**  corresponding to a known  **IP address**  on a local network.

**Main Functions of ARP:**

**1. IP-to-MAC Address Mapping:**
ARP determines the MAC address of a destination device when its IP address is known.

**2. Sending ARP Request:**
If the MAC address is unknown, the source device broadcasts an  **ARP Request**  asking which device owns the specified IP address.

**3. Receiving ARP Reply:**
The device having that IP address sends an  **ARP Reply**  containing its MAC address.

**4. Maintaining ARP Cache:**
ARP stores recently learned IP-to-MAC address mappings in an  **ARP Cache**  so that repeated requests are not necessary.

**5. Supporting Local Packet Delivery:**
ARP provides the MAC address required to deliver an IP packet over an Ethernet or other local-area network.

**Example:**

- ☆

16

Digital Logic Design
Adder Circuit

Draw a Full Adder circuit using two half adders.
