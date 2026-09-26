# Combined Bank, Senior Officer (IT), 2025 (Based Year 2022)

- **Original URL:** [https://it.jobqns.com/combined-bank-senior-officer-it-2025/](https://it.jobqns.com/combined-bank-senior-officer-it-2025/)
- **Date:** 2026-02-13T17:04:13
- **Categories:** Bank IT Job Solution, Bank IT Job Solution 2025, Job Solution 2025

---

Senior Officer (IT) • Year 2025

Combined Bank

💼Post Name: Senior Officer (IT)

📅Exam Date: 17-Oct-2025

- ☆

1

Data Structure
Graphs

Determine whether the following pair of graphs are isomorphic, and justify your answer in one sentence.     (10 Marks)

**Isomorphic Pairs:**

**Graph 1 and Graph 2**  are  **isomorphic**  because they have the same number of vertices, same number of edges, and identical degree sequence with preserved adjacency structure.
**Graph 3 and Graph 4**  are also  **isomorphic**  since their vertex connections follow the same pattern, even though their drawings look different.

**Graph-1:**
Vertices = 6
(u1, u2, u3, u4, u5, u6)
Degree sequence = (3, 3, 3, 3, 3, 3)
**Graph-2:**
Vertices = 6
(v1, v2, v3, v4, v5, v6)
Degree sequence = (3, 3, 3, 3, 3, 3)
**Conclusion for Graph-1 & Graph-2:**
Both graphs have the  **same number of vertices (6)**  and the  **same degree sequence** , so they are  **isomorphic** .
**Graph-3:**
Vertices = 6
(u1, u2, u3, u4, u5, u6)
Degree sequence = (3, 3, 2, 2, 3, 3)
**Graph-4:**
Vertices = 6
(v1, v2, v3, v4, v5, v6)
Degree sequence = (2, 3, 3, 2, 2, 3)
**Conclusion for Graph-3 & Graph-4:**
have not the identical degree sequences, so they are not  **isomorphic** .

**Isomorphic পেয়ার:**

**Graph 1 এবং Graph 2**  পরস্পর  **isomorphic** , কারণ এদের vertex সংখ্যা, edge সংখ্যা এবং  **degree sequence**  একই এবং adjacency ঠিকভাবে সংরক্ষিত।
**Graph 3 এবং Graph 4**  ও  **isomorphic** , কারণ দুটির connection pattern এক হলেও আঁকার ধরন আলাদা।

**Graph-1:**
Vertex সংখ্যা = ৬টি
(u1, u2, u3, u4, u5, u6)
Degree sequence = (3, 3, 3, 3, 3, 3)
**Graph-2:**
Vertex সংখ্যা = ৬টি
(v1, v2, v3, v4, v5, v6)
Degree sequence = (3, 3, 3, 3, 3, 3)
**Graph-1 ও Graph-2 এর সিদ্ধান্ত:**
উভয় graph-এ  **vertex সংখ্যা সমান (৬)**  এবং  **degree sequence একই** , তাই এরা  **isomorphic** ।
**Graph-3:**
Vertex সংখ্যা = ৬টি
(u1, u2, u3, u4, u5, u6)
Degree sequence = (3, 3, 2, 2, 3, 3)
**Graph-4:**
Vertex সংখ্যা = ৬টি
(v1, v2, v3, v4, v5, v6)
Degree sequence =(2, 3, 3, 2, 2, 3)
**Graph-3 ও Graph-4 এর vertex সংখ্যা সমান (৬)**  , **degree sequence একই নয়** , তাই এরা  **isomorphic নয়** ।

- ☆

2

Design Analysis of Algorithm
Sorting Algorithm

Explain the Quick Sort algorithm with a suitable example. Under what conditions does Quick Sort exhibit its worst-case time complexity, and why does this situation occur?(10 Marks)

**Quick Sort Algorithm**  Quick Sort is a divide-and-conquer sorting algorithm. It works by selecting a pivot element, partitioning the array into two parts (elements smaller than pivot and elements greater than pivot), and then recursively sorting the sub-arrays. It is fast and widely used in practice.
**Steps of Quick Sort**  Choose a pivot → Partition the array → Recursively apply Quick Sort on left and right sub-arrays.
**Worst-Case Time Complexity**  The worst-case time complexity of Quick Sort is  **O(n²)** .
**When does Worst Case Occur?**  Worst case occurs when the pivot element is always the smallest or largest element in the array.
Examples: already sorted array, reverse sorted array (when first or last element is chosen as pivot).
**Why does this happen?**  In this case, partitioning creates highly unbalanced sub-arrays (one with n−1 elements and the other with 0). This leads to maximum number of recursive calls, resulting in O(n²) time complexity.

**Quick Sort Algorithm**  Quick Sort হলো একটি divide-and-conquer based sorting algorithm। এখানে একটি pivot element নেওয়া হয়, তারপর array কে pivot এর চেয়ে ছোট এবং বড় দুই ভাগে ভাগ করা হয় এবং এই sub-array গুলোকে recursively sort করা হয়। এটি দ্রুত এবং বাস্তবে খুব বেশি ব্যবহৃত হয়।
**Quick Sort এর ধাপসমূহ**  Pivot নির্বাচন → Array partition → Left ও right sub-array এ recursive sorting。
**Worst-Case Time Complexity**  Quick Sort এর worst-case time complexity হলো  **O(n²)** 。
**Worst Case কখন ঘটে?**  Worst case ঘটে যখন pivot সবসময় array এর সবচেয়ে ছোট বা সবচেয়ে বড় element হয়।
উদাহরণ: already sorted বা reverse sorted array (যখন first বা last element pivot নেওয়া হয়)।
**কেন এমন হয়?**  এই অবস্থায় partition ঠিকভাবে balanced হয় না। একদিকে n−1 element আর অন্যদিকে 0 element থাকে। ফলে recursive call এর সংখ্যা বেড়ে যায় এবং time complexity O(n²) হয়ে যায়।

- ☆

3

Operating System
Paging

Consider a logical address space of 512 pages, each of 2-KB page size, mapped onto a physical memory containing 128 frames. a. How many bits are required in the logical address? b. How many bits are required in the physical address?  (10 Marks)

**Given**
Logical address space = 512 pages
Page size = 2 KB = 2048 bytes
Physical memory = 128 frames
**a) Bits required in the Logical Address**
Number of pages = 512 = 29 → Page number bits =  **9 bits**
Page size = 2048 bytes = 211 → Offset bits =  **11 bits**
So, Logical address bits = Page number bits + Offset bits = 9 + 11 =  **20 bits**
**b) Bits required in the Physical Address**
Number of frames = 128 = 27 → Frame number bits =  **7 bits**
Offset remains same =  **11 bits**
So, Physical address bits = Frame number bits + Offset bits = 7 + 11 =  **18 bits**

**প্রদত্ত তথ্য**
Logical address space = 512 pages
Page size = 2 KB = 2048 bytes
Physical memory = 128 frames
**a) Logical Address এর জন্য কত bit লাগবে**
Page সংখ্যা = 512 = 29 → Page number এর জন্য লাগবে  **9 bit**
Page size = 2048 bytes = 211 → Offset এর জন্য লাগবে  **11 bit**
সুতরাং Logical address bits = 9 + 11 =  **20 bit**
**b) Physical Address এর জন্য কত bit লাগবে**
Frame সংখ্যা = 128 = 27 → Frame number এর জন্য লাগবে  **7 bit**
Offset একই থাকবে =  **11 bit**
সুতরাং Physical address bits = 7 + 11 =  **18 bit**

- ☆

4

Computer Network
Transport Layer Protocol

Why does the Domain Name System (DNS) primarily use UDP as its transport layer protocol instead of TCP? Describe the sequence of events that take place during the DNS name resolution process when a user enters www.companybd.com into a web browser and presses Enter.(10 Marks)

**Why DNS primarily uses UDP instead of TCP**
DNS mainly uses UDP because it is fast and lightweight. UDP does not require connection establishment, which reduces delay and overhead. Most DNS queries and responses are small in size and can easily fit within a single UDP packet. Using UDP allows DNS to provide quick responses, which is important for fast web browsing. TCP is only used in special cases, such as zone transfers or when the response size is too large.
**DNS Name Resolution Process for www.companybd.com**

The user enters  **www.companybd.com**  in the web browser and presses Enter.
The browser first checks its local DNS cache to see if the IP address is already available.
If not found, the request is sent to the local DNS resolver (usually provided by the ISP).
The resolver contacts the Root DNS Server, which directs it to the  **.com**  Top-Level Domain (TLD) server.
The TLD server provides the address of the authoritative DNS server for  **companybd.com** .
The authoritative DNS server returns the IP address of  **www.companybd.com** .
The resolver sends the IP address back to the browser and stores it in cache for future use.
Using the obtained IP address, the browser connects to the web server and loads the website.

**DNS কেন প্রধানত TCP এর পরিবর্তে UDP ব্যবহার করে**
DNS মূলত UDP ব্যবহার করে কারণ এটি দ্রুত এবং কম overhead তৈরি করে। UDP তে connection establish করার দরকার হয় না, ফলে delay কম হয়। বেশিরভাগ DNS query এবং response ছোট আকারের হয়, যা একটি UDP packet এই পাঠানো যায়। দ্রুত response পাওয়ার জন্য UDP ব্যবহার করা হয়। বিশেষ ক্ষেত্রে যেমন zone transfer বা বড় response হলে TCP ব্যবহার করা হয়।
**www.companybd.com এর ক্ষেত্রে DNS Name Resolution Process**

User browser এ  **www.companybd.com**  লিখে Enter চাপ দেয়।
প্রথমে browser নিজের DNS cache এ IP address খোঁজে।
না পেলে request local DNS resolver (সাধারণত ISP) এর কাছে পাঠানো হয়।
Resolver Root DNS Server এর সাথে যোগাযোগ করে, যা তাকে  **.com**  Top-Level Domain (TLD) server এর ঠিকানা দেয়।
TLD server  **companybd.com**  এর authoritative DNS server এর ঠিকানা দেয়।
Authoritative DNS server  **www.companybd.com**  এর IP address পাঠিয়ে দেয়।
Resolver সেই IP address browser এ পাঠায় এবং ভবিষ্যতের জন্য cache এ সংরক্ষণ করে।
প্রাপ্ত IP address ব্যবহার করে browser web server এর সাথে সংযোগ করে এবং website load করে।

- ☆

5

Operating System
Page Fault & Thrashing

Explain the concept of thrashing in an operating system, describing how it occurs in a demand-paged virtual memory system and how it impacts CPU utilization and overall system performance. (10 Marks)

**Thrashing in Operating System**
Thrashing is a condition in an operating system where the system spends most of its time swapping pages in and out of memory instead of executing actual processes. It mainly occurs in a demand-paged virtual memory system when there are not enough frames to support the working sets of active processes.
**How Thrashing Occurs in Demand Paging**
In demand paging, pages are loaded into memory only when they are needed. If too many processes are running and physical memory is insufficient, frequent page faults occur. The OS continuously replaces pages, but the required pages are again needed immediately, causing excessive paging activity. This situation leads to thrashing.
**Impact on CPU Utilization**
During thrashing, CPU utilization becomes very low because the CPU waits for disk I/O operations caused by page faults. Even though many processes are active, the CPU remains mostly idle.
**Impact on System Performance**
Overall system performance degrades severely. Response time increases, throughput decreases, and the system becomes slow and inefficient. To handle thrashing, the OS may reduce the degree of multiprogramming or use working set and page fault frequency control techniques.

**Operating System এ Thrashing**
Thrashing হলো একটি অবস্থা যেখানে operating system অধিকাংশ সময় memory থেকে page আনা-নেওয়ায় ব্যয় করে, process execute করার পরিবর্তে। এটি মূলত demand-paged virtual memory system এ ঘটে, যখন active process গুলোর জন্য যথেষ্ট frame থাকে না।
**Demand Paging এ Thrashing কীভাবে ঘটে**
Demand paging এ page তখনই memory তে আনা হয় যখন সেটি দরকার হয়। যদি একসাথে অনেক process চালানো হয় এবং physical memory কম থাকে, তাহলে বারবার page fault ঘটে। OS এক page remove করে আরেকটা আনে, কিন্তু আগের page আবার দরকার পড়ে। এতে অতিরিক্ত paging শুরু হয়, যা thrashing সৃষ্টি করে।
**CPU Utilization এর উপর প্রভাব**
Thrashing এর সময় CPU utilization খুব কমে যায়, কারণ CPU বারবার disk I/O এর জন্য অপেক্ষা করে। অনেক process থাকা সত্ত্বেও CPU প্রায় idle থাকে।
**System Performance এর উপর প্রভাব**
System performance অনেক খারাপ হয়ে যায়। Response time বেড়ে যায়, throughput কমে যায় এবং system ধীরগতির হয়ে পড়ে। Thrashing কমাতে OS degree of multiprogramming কমাতে পারে অথবা working set ও page fault frequency technique ব্যবহার করতে পারে।

- ☆

6

Programming Concept

Write a structured program (in C or Python) that takes an integer input n and prints the sum of all even numbers from 1 to n.

```
#include <stdio.h>
/* Function to calculate sum of even numbers from 1 to n */
int sumOfEven(int n) {
int sum = 0;
for (int i = 2; i <= n; i += 2) {
sum += i;
}
return sum;
}
int main() {
int n, result;
printf("Enter an integer: ");
scanf("%d", &n);
result = sumOfEven(n);
printf("Sum of even numbers from 1 to %d = %d\n", n, result);
return 0;
}
```

```
Sample I/O:
Enter an integer: 50
Sum of even numbers from 1 to 50 = 650
=== Code Execution Successful ===
```

🔗 Run Online: Sum of even number.


☆

7

Programming Concept

Write a program using any object-oriented language (e.g., C++ / Java / Python) to represent a Bank Account. Your program should include: . A class BankAccount with data members for account holder's name, account number, and balance. . Member functions to deposit() money, withdraw() money (ensuring sufficient balance), and display() account details.  **Demonstrate the concept of encapsulation by keeping data member's private and providing appropriate public methods for accessing and modifying them.**

```
#include <iostream>
using namespace std;

class BankAccount {
private:
string name;
int accountNumber;
double balance;

public:
void setDetails(string n, int accNo, double bal) {
name = n;
accountNumber = accNo;
balance = bal;
}

void deposit(double amount) {
balance += amount;
cout << "Deposited: " << amount << endl;
}

void withdraw(double amount) {
if (amount <= balance) {
balance -= amount;
cout << "Withdrawn: " << amount << endl;
} else {
cout << "Insufficient balance" << endl;
}
}
void display() {
cout << "\nAccount Details\n";
cout << "Account Holder: " << name << endl;
cout << "Account Number: " << accountNumber << endl;
cout << "Balance: " << balance << endl;
}
};
int main() {
BankAccount acc;
string name;
int accNo;
double bal, dep, wit;
cout << "Enter account holder name: ";
getline(cin, name);

cout << "Enter account number: ";
cin >> accNo;
cout << "Enter initial balance: ";
cin >> bal;
acc.setDetails(name, accNo, bal);
cout << "Enter amount to deposit: ";
cin >> dep;
acc.deposit(dep);
cout << "Enter amount to withdraw: ";
cin >> wit;
acc.withdraw(wit);
acc.display();
return 0;
}
```

```
Sample I/O:
Enter account holder name: itjobqns
Enter account number: 02252016
Enter initial balance: 5000
Enter amount to deposit: 300
Deposited: 300
Enter amount to withdraw: 100
Withdrawn: 100
Account Details
Account Holder: itjobqns
Account Number: 2252016
Balance: 5200
=== Code Execution Successful ===
```

🔗 Run Online: Bank Balance & Deposit.


☆

8

Structure Query Language

**Consider the following relation: Sales(sales_id, salesman, region, sale_amount, sale_date)**  ,Write an SQL query to display the region, average sale amount, and total number of sales for each region where: The average sale amount exceeds BDT 50,000 and the total number of sales in that region is at least 5.

**SQL Query**
The following query displays the  **region** ,  **average sale amount** , and  **total number of sales**  for each region where the average sale amount is greater than  **BDT 50,000**  and the total number of sales is at least  **3** .

```
SELECT region,
AVG(sale_amount) AS avg_sale_amount,
COUNT(*) AS total_sales
FROM Sales
GROUP BY region
HAVING AVG(sale_amount) > 50000
AND COUNT(*) >= 3;
```



**SQL Query**
নিচের query টি প্রতিটি  **region**  অনুযায়ী  **average sale amount**  এবং  **total sales সংখ্যা**  দেখায়, যেখানে average sale amount  **BDT 50,000**  এর বেশি এবং ঐ region এ মোট sales কমপক্ষে  **3টি** ।

```
SELECT region,
AVG(sale_amount) AS avg_sale_amount,
COUNT(*) AS total_sales
FROM Sales
GROUP BY region
HAVING AVG(sale_amount) > 50000
AND COUNT(*) >= 3;
```

- ☆

9

Microprocessor & Computer Architecture
Addressing

Explain the difference between direct, immediate, and register addressing modes in the 8086 microprocessor.

**Addressing Modes in 8086 Microprocessor**
**1) Immediate Addressing Mode**
In immediate addressing mode, the  **actual data (operand)**  is specified directly in the instruction itself.
**Example:**

```
MOV AX, 1234H
```

Here,  **1234H**  is the immediate data loaded directly into the AX register.
**2) Register Addressing Mode**
In register addressing mode, the operand is stored in a  **CPU register** , and the instruction specifies the register name.
**Example:**

```
MOV BX, AX
```

Here, data is moved from register AX to register BX.
**3) Direct Addressing Mode**
In direct addressing mode, the  **memory address**  of the operand is directly specified in the instruction.
**Example:**

```
MOV AX, [2000H]
```

Here, the data stored at memory location  **2000H**  is loaded into the AX register.

**8086 Microprocessor এ Addressing Mode গুলোর পার্থক্য**
**1) Immediate Addressing Mode**
Immediate addressing mode এ  **data সরাসরি instruction এর মধ্যেই**  দেওয়া থাকে।
**উদাহরণ:**

```
MOV AX, 1234H
```

এখানে  **1234H**  হলো immediate data যা সরাসরি AX register এ load হয়।
**2) Register Addressing Mode**
Register addressing mode এ operand টি  **CPU register**  এ থাকে এবং instruction এ register এর নাম দেওয়া হয়।
**উদাহরণ:**

```
MOV BX, AX
```

এখানে AX register থেকে data BX register এ transfer করা হয়।
**3) Direct Addressing Mode**
Direct addressing mode এ operand এর  **memory address সরাসরি instruction এ উল্লেখ থাকে** ।
**উদাহরণ:**

```
MOV AX, [2000H]
```

এখানে memory location  **2000H**  এ থাকা data AX register এ load করা হয়।

- ☆

10

Database Management System
ACID

Explain the concept of ACID properties in a database transaction. Describe how each property-Atomicity, Consistency, Isolation, and Durability- ensures the reliability and integrity of a database system.

**ACID Properties in Database Transactions**
ACID properties are a set of rules that ensure  **reliability, consistency, and integrity**  of a database during transactions. Each transaction must satisfy these four properties to maintain a correct database state.
**1) Atomicity**
Atomicity ensures that a transaction is treated as a single unit. Either  **all operations**  of the transaction are completed successfully, or  **none of them**  are applied. If any part fails, the entire transaction is rolled back, preventing partial updates.
**2) Consistency**
Consistency ensures that a transaction moves the database from one  **valid state**  to another valid state. All integrity constraints, rules, and conditions must be satisfied before and after the transaction.
**3) Isolation**
Isolation ensures that multiple transactions executed at the same time do not interfere with each other. Each transaction behaves as if it is executed  **independently** , preventing problems like dirty reads or lost updates.
**4) Durability**
Durability guarantees that once a transaction is  **committed** , its changes are permanently stored in the database. Even if the system crashes, the committed data will not be lost.

**Database Transaction এ ACID Properties**
ACID properties হলো কিছু গুরুত্বপূর্ণ নিয়ম যা database transaction চলাকালীন  **reliability, consistency এবং integrity**  নিশ্চিত করে। প্রতিটি transaction কে এই চারটি property অনুসরণ করতে হয়।
**1) Atomicity**
Atomicity নিশ্চিত করে যে একটি transaction সম্পূর্ণভাবে execute হবে অথবা একেবারেই হবে না। যদি transaction এর কোনো একটি অংশ ব্যর্থ হয়, তাহলে পুরো transaction rollback হয়, ফলে partial update হয় না।
**2) Consistency**
Consistency নিশ্চিত করে যে transaction এর আগে ও পরে database একটি  **valid state**  এ থাকে। সব ধরনের rule, constraint এবং integrity condition মানা হয়।
**3) Isolation**
Isolation নিশ্চিত করে যে একাধিক transaction একসাথে চললেও তারা একে অপরকে প্রভাবিত করবে না। প্রতিটি transaction আলাদাভাবে execute হওয়ার মতো আচরণ করে।
**4) Durability**
Durability নিশ্চিত করে যে transaction একবার commit হয়ে গেলে তার পরিবর্তন স্থায়ীভাবে database এ সংরক্ষিত থাকে, system crash হলেও data হারায় না।

- ☆

11

Web Technology
SOAP

What are SOAP and RESTful APIs in web services? State one main difference between SOAP and REST in terms of how they exchange data.

**SOAP API**
SOAP (Simple Object Access Protocol) is a protocol used in web services to exchange structured information between applications. It relies on  **XML**  for message format and follows strict standards. SOAP is commonly used in enterprise-level applications where security and reliability are critical.
**RESTful API**
REST (Representational State Transfer) is an architectural style for designing web services. RESTful APIs use standard HTTP methods such as  **GET, POST, PUT, DELETE**  and can exchange data in multiple formats like  **JSON, XML, or plain text** . REST is lightweight and widely used in modern web and mobile applications.
**Main Difference (Data Exchange)**
The main difference is that  **SOAP exchanges data only in XML format** , while  **REST can exchange data in multiple formats** , most commonly JSON.

**SOAP API**
SOAP (Simple Object Access Protocol) হলো একটি web service protocol যা application গুলোর মধ্যে structured তথ্য আদান-প্রদান করতে ব্যবহৃত হয়। এটি  **XML**  format ব্যবহার করে এবং কঠোর নিয়ম অনুসরণ করে। সাধারণত enterprise-level application এ SOAP ব্যবহৃত হয় যেখানে security ও reliability খুব গুরুত্বপূর্ণ।
**RESTful API**
REST (Representational State Transfer) হলো web service design করার একটি architectural style। RESTful API গুলো  **GET, POST, PUT, DELETE**  এর মতো HTTP method ব্যবহার করে এবং  **JSON, XML বা text**  format এ data আদান-প্রদান করতে পারে। এটি lightweight এবং আধুনিক web ও mobile application এ ব্যাপকভাবে ব্যবহৃত।
**মূল পার্থক্য (Data Exchange)**
মূল পার্থক্য হলো  **SOAP শুধুমাত্র XML format এ data exchange করে** , আর  **REST একাধিক format এ data exchange করতে পারে** , যেখানে JSON সবচেয়ে বেশি ব্যবহৃত হয়।

- ☆

12

Big Data, ML & AI
Types of ML

Explain the concepts of Reinforcement Learning (RL), Deep Learning (DL), and Federated Learning (FL) in the context of Machine Learning. Briefly describe how each approach differs in its learning mechanism, data usage, and real-world applications.(10 Marks)

**Reinforcement Learning (RL)**
Reinforcement Learning is a type of machine learning where an  **agent learns by interacting with an environment** . The agent takes actions and receives rewards or penalties, and its goal is to maximize cumulative reward over time.
**Learning Mechanism:**  Trial-and-error with reward feedback.
**Data Usage:**  Generated through interaction with the environment.
**Applications:**  Robotics, game playing (AlphaGo), autonomous vehicles, recommendation systems.
**Deep Learning (DL)**
Deep Learning is a subset of machine learning that uses  **multi-layer neural networks**  to automatically learn features from large datasets. It is inspired by the human brain structure.
**Learning Mechanism:**  Supervised/unsupervised learning using deep neural networks.
**Data Usage:**  Requires large, labeled or unlabeled datasets.
**Applications:**  Image recognition, speech recognition, natural language processing, medical diagnosis.
**Federated Learning (FL)**
Federated Learning is a distributed learning approach where the model is trained  **across multiple devices without sharing raw data** . Only model updates are sent to a central server.
**Learning Mechanism:**  Collaborative learning with local model updates.
**Data Usage:**  Data remains on local devices (privacy-preserving).
**Applications:**  Mobile keyboards, healthcare data analysis, IoT systems, privacy-sensitive applications.

**Reinforcement Learning (RL)**
Reinforcement Learning হলো machine learning এর এমন একটি পদ্ধতি যেখানে একটি  **agent environment এর সাথে interaction করে শেখে** । Agent action নেয় এবং reward বা penalty পায়, এবং লক্ষ্য থাকে মোট reward সর্বোচ্চ করা।
**Learning Mechanism:**  Trial-and-error এবং reward ভিত্তিক শেখা।
**Data Usage:**  Environment এর সাথে interaction করে data তৈরি হয়।
**Applications:**  Robotics, game playing (AlphaGo), autonomous vehicle, recommendation system।
**Deep Learning (DL)**
Deep Learning হলো machine learning এর একটি অংশ যেখানে  **multi-layer neural network**  ব্যবহার করে বড় dataset থেকে স্বয়ংক্রিয়ভাবে feature শেখা হয়। এটি মানুষের brain structure থেকে অনুপ্রাণিত।
**Learning Mechanism:**  Deep neural network ব্যবহার করে supervised বা unsupervised learning।
**Data Usage:**  বড় আকারের labeled বা unlabeled data প্রয়োজন।
**Applications:**  Image recognition, speech recognition, NLP, medical diagnosis।
**Federated Learning (FL)**
Federated Learning হলো একটি distributed learning পদ্ধতি যেখানে  **raw data share না করেই**  একাধিক device এ model train করা হয়। শুধু model update central server এ পাঠানো হয়।
**Learning Mechanism:**  Local training এবং global model aggregation।
**Data Usage:**  Data local device এই থাকে (privacy বজায় থাকে)।
**Applications:**  Mobile keyboard prediction, healthcare data analysis, IoT system, privacy-sensitive application।

- ☆

13

Big Data, ML & AI
Generative AI & XAI

Imagine a government agency is developing an AI-based citizen service chatbot that can automatically generate responses, summarize documents, and provide policy information to citizens. Explain how Generative AI can be used to power such a system, and how Explainable AI (XAI) techniques can ensure that its responses are transparent, reliable, and accountable.  (10 Marks)

**Use of Generative AI in a Government Citizen Service Chatbot**
Generative AI can be used to power a government chatbot by enabling it to  **automatically generate human-like responses** ,  **summarize long policy documents** , and  **provide accurate policy-related information**  to citizens. Using large language models, the chatbot can understand citizens’ questions in natural language and generate clear, context-aware answers. It can also analyze official documents, extract key points, and present simplified summaries, making government services more accessible and efficient.
**Role of Explainable AI (XAI)**
Explainable AI (XAI) techniques help ensure that the chatbot’s responses are  **transparent, reliable, and accountable** . XAI allows the system to explain  **why**  a particular response was generated by showing the source policy, rules, or reasoning behind the answer. This helps government officials and citizens trust the system and verify that the information is correct and unbiased.
**Benefits of Using XAI**

**Transparency:**  Citizens can understand how and from where the answer was derived.
**Reliability:**  Officials can audit and validate chatbot decisions.
**Accountability:**  The system can justify responses, reducing the risk of misinformation.
**Public Trust:**  Clear explanations increase confidence in AI-based public services.

**Government Citizen Service Chatbot এ Generative AI এর ব্যবহার**
Generative AI ব্যবহার করে একটি সরকারী chatbot তৈরি করা যায় যা  **স্বয়ংক্রিয়ভাবে মানুষের মতো উত্তর তৈরি**  করতে পারে,  **দীর্ঘ policy document সংক্ষেপ**  করতে পারে এবং নাগরিকদের  **নীতিমালা সংক্রান্ত তথ্য**  সহজভাবে দিতে পারে। Large language model ব্যবহার করে chatbot নাগরিকদের প্রশ্ন বুঝতে পারে এবং প্রাসঙ্গিক ও স্পষ্ট উত্তর প্রদান করতে পারে। এছাড়া সরকারি নথি বিশ্লেষণ করে গুরুত্বপূর্ণ তথ্য সংক্ষেপে তুলে ধরতে পারে, ফলে নাগরিক সেবা আরও সহজ ও দ্রুত হয়।
**Explainable AI (XAI) এর ভূমিকা**
Explainable AI (XAI) chatbot এর উত্তরগুলোকে  **স্বচ্ছ, নির্ভরযোগ্য এবং জবাবদিহিমূলক**  করতে সাহায্য করে। XAI এর মাধ্যমে বোঝানো যায় কেন একটি নির্দিষ্ট উত্তর দেওয়া হয়েছে—যেমন কোন policy, নিয়ম বা তথ্যের ভিত্তিতে উত্তরটি এসেছে। এতে নাগরিক এবং সরকার উভয়ই AI সিস্টেমের উপর আস্থা রাখতে পারে।
**XAI ব্যবহারের সুবিধা**

**স্বচ্ছতা:**  নাগরিকরা বুঝতে পারে উত্তরটি কীভাবে তৈরি হয়েছে।
**নির্ভরযোগ্যতা:**  সরকার সহজে chatbot এর সিদ্ধান্ত যাচাই করতে পারে।
**জবাবদিহিতা:**  ভুল বা বিভ্রান্তিকর তথ্যের ঝুঁকি কমে।
**জনগণের আস্থা:**  ব্যাখ্যাসহ উত্তর দিলে AI-ভিত্তিক সেবার প্রতি বিশ্বাস বাড়ে।

- ☆

14

Computer Security
CIA

Describe how the principles of Confidentiality, Integrity, and Availability work together to protect organizational data, and provide one real-world example of a security breach where one or more of these principles were compromised. (10 Marks)

**Confidentiality, Integrity, and Availability (CIA Triad)**
The CIA Triad represents three fundamental principles used to protect organizational data and information systems. These principles work together to ensure data security and trustworthiness.
**Confidentiality**
Confidentiality ensures that sensitive information is accessible only to  **authorized users** . Techniques such as encryption, authentication, and access control are used to prevent unauthorized data disclosure.
**Integrity**
Integrity ensures that data remains  **accurate, complete, and unaltered**  during storage or transmission. Mechanisms like hashing, checksums, and digital signatures help detect and prevent unauthorized data modification.
**Availability**
Availability ensures that data and systems are  **accessible when needed**  by authorized users. Redundancy, backups, and protection against attacks like DoS help maintain system availability.
**How They Work Together**
All three principles must be maintained simultaneously. For example, data may be confidential and accurate, but if systems are unavailable, the organization cannot operate effectively. Weakness in any one principle can compromise overall security.
**Real-World Security Breach Example**
**Equifax Data Breach (2017):**  In this incident, attackers exploited a vulnerability to access sensitive personal data of millions of users.  **Confidentiality**  was compromised as private data was exposed, and  **Integrity**  was also affected because attackers accessed systems without authorization.

**Confidentiality, Integrity এবং Availability (CIA Triad)**
CIA Triad হলো তথ্য নিরাপত্তার তিনটি মূল নীতি যা কোনো প্রতিষ্ঠানের data ও system সুরক্ষার জন্য একসাথে কাজ করে।
**Confidentiality**
Confidentiality নিশ্চিত করে যে সংবেদনশীল তথ্য শুধুমাত্র  **অনুমোদিত ব্যবহারকারীদের**  জন্যই প্রবেশযোগ্য। Encryption, authentication এবং access control এর মাধ্যমে অননুমোদিত access রোধ করা হয়।
**Integrity**
Integrity নিশ্চিত করে যে data সংরক্ষণ বা আদান-প্রদানের সময়  **সঠিক ও অপরিবর্তিত**  থাকে। Hashing, checksum এবং digital signature ব্যবহার করে data পরিবর্তন শনাক্ত করা যায়।
**Availability**
Availability নিশ্চিত করে যে system এবং data  **প্রয়োজনের সময় উপলব্ধ**  থাকে। Backup, redundancy এবং DoS attack প্রতিরোধ ব্যবস্থা availability বজায় রাখতে সাহায্য করে।
**তিনটি নীতি একসাথে কীভাবে কাজ করে**
এই তিনটি নীতি একসাথে বজায় রাখতে হয়। কোনো একটি দুর্বল হলে পুরো system ঝুঁকিতে পড়ে। যেমন, data সুরক্ষিত হলেও system unavailable হলে কাজ ব্যাহত হয়।
**বাস্তব উদাহরণ (Security Breach)**
**Equifax Data Breach (2017):**  এই ঘটনায় attackers একটি vulnerability ব্যবহার করে কোটি মানুষের ব্যক্তিগত তথ্য চুরি করে। এতে  **Confidentiality**  ভেঙে যায় এবং অননুমোদিত access এর কারণে  **Integrity**  ক্ষতিগ্রস্ত হয়।

- ☆

15

Computer Security
Others

**A banking application requires users to enter a 4-digit PIN for login.**  Explain how you would test this input field to ensure that it accepts only valid 4-digit numbers and rejects invalid inputs. Mention a few test cases you would include and explain why such testing is important for system security and reliability

**Testing a 4-Digit PIN Input Field**
To test a 4-digit PIN input field in a banking application, I would verify that the system accepts  **only numeric values with exactly 4 digits**  and rejects any other input. This involves both functional testing and validation testing at the input level.
**Test Cases**

**Valid Input:**  Enter  **1234**  → Should be accepted (correct 4-digit number).
**Less than 4 digits:**  Enter  **123**  → Should be rejected (too short).
**More than 4 digits:**  Enter  **12345**  → Should be rejected (too long).
**Non-numeric input:**  Enter  **12ab**  → Should be rejected (contains letters).
**Special characters:**  Enter  **12@#**  → Should be rejected.
**Empty input:**  Leave the field blank → Should be rejected.

**Importance of This Testing**
This testing is important for  **security**  because it prevents invalid or malicious inputs that could be used to bypass authentication. It also improves  **reliability**  by ensuring that the system behaves correctly and consistently, reducing login errors and protecting user accounts.

**৪-সংখ্যার PIN Input Field টেস্ট করা**
একটি banking application এ 4-digit PIN input field টেস্ট করার সময় নিশ্চিত করতে হবে যে system টি  **শুধুমাত্র ৪ সংখ্যার numeric value**  গ্রহণ করে এবং অন্য সব input বাতিল করে। এর জন্য input validation এবং functional testing প্রয়োগ করা হয়।
**Test Case সমূহ**

**Valid Input:**   **1234**  ইনপুট → গ্রহণ করা উচিত (সঠিক ৪-digit সংখ্যা)।
**৪ digit এর কম:**   **123**  ইনপুট → বাতিল হওয়া উচিত।
**৪ digit এর বেশি:**   **12345**  ইনপুট → বাতিল হওয়া উচিত।
**Non-numeric input:**   **12ab**  ইনপুট → বাতিল হওয়া উচিত।
**Special character:**   **12@#**  ইনপুট → বাতিল হওয়া উচিত।
**খালি input:**  কিছু না লিখে submit → বাতিল হওয়া উচিত।

**এই Testing কেন গুরুত্বপূর্ণ**
এই ধরনের testing  **security**  নিশ্চিত করে, কারণ ভুল বা ক্ষতিকর input দিয়ে authentication bypass করার ঝুঁকি কমে। পাশাপাশি এটি system এর  **reliability**  বাড়ায় এবং ব্যবহারকারীদের জন্য একটি স্থিতিশীল ও নিরাপদ login ব্যবস্থা নিশ্চিত করে।

- ☆

16

Non Technical Question
Non tech

16. Focus Writing in Bangla (10 Marks) বাংলাদেশের ব্যাংকিং খাতে কৃত্রিম বুদ্ধিমত্তার প্রয়োগ কীভাবে কার্যক্রমের দক্ষতা ও নিরাপত্তা বৃদ্ধি করতে পারে? একই সঙ্গে, এর সম্ভাব্য ঝুঁকি ও নৈতিক চ্যালেঞ্জসমূহ বিশেষণ করুন।
17. Focus Writing in English (10 Marks)
Why are data privacy and regulatory compliance (such as AML, KYC, and international data- protection standards) vital for the stability and credibility of the banking sector in Bangladesh? Discuss with examples and practical recommendations.
18. Translation : Bangla to English (10 Marks)
বাংলাদেশের তরুণ জনগোষ্ঠীর একটি বড় অংশ বর্তমানে শিক্ষা, কর্মসংস্থান বা প্রশিক্ষণ-এই তিনটির কোনো ক্ষেত্রেই সক্রিয় নয়। এই শ্রেণির তরুণ-তরুণীরা না পড়াশোনায় যুক্ত, না কোনো আযমূলক কাজে নিয়োজিত, আবার কোনো প্রশিক্ষণমূলক কর্মসূচিতেও অংশ নিচ্ছে না। ফলে দেশের বিপুল জনশক্তির একটি অংশ অকেজো থেকে যাচ্ছে, যা অর্থনৈতিক ও সামাজিক উভয় ক্ষেত্রেই উদ্বেগজনক । এই সমস্যার প্রধান কারণ হলো শিক্ষার সঙ্গে কর্মক্ষেত্রের প্রয়োজনের সামঞ্জস্যহীনতা, দক্ষতার ঘাটতি, কর্মসংস্থানের অভাব, সামাজিক বাধা এবং মানসিক অনুপ্রেরণার অভাব। বিশেষ করে নারী ও গ্রামীণ এলাকার তরুণদের মধ্যে এই সমস্যা বেশি লক্ষ করা যায়।
19. Translation : English to Bangla (10 Marks)
The ongoing war in Gaza has created a serious humanitarian crisis. Continuous bombing and fighting have destroyed thousands of houses, hospitals, and schools. Many innocent people have lost their homes and are living without enough food, clean water, or medicine. Children and women are suffering the most because they have no protection and very little help. Aid workers say that the situation in Gaza is getting worse every day and people may soon face starvation and disease. The Gaza war has become a tragedy that affects the whole world. It shows how war destroys not only buildings but also hope and humanity.
20. Writing on General Knowledge(10 Marks)
Evaluate the challenges and prospects of managing the Rohingya refugee crisis in Bangladesh. How important is international cooperation, and what reforms or support mechanisms should be prioritized?
