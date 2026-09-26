# Bangladesh Bank, Assistant Director (ICT), 2025

- **Original URL:** [https://it.jobqns.com/assistant-director-ict-2025/](https://it.jobqns.com/assistant-director-ict-2025/)
- **Date:** 2025-09-07T20:45:41
- **Categories:** Bank IT Job Solution, Bank IT Job Solution 2025, Job Solution 2025

---

Bangladesh Bank • Year 2025

Bangladesh Bank

💼Post Name: Assistant Director (ICT)

📅Exam Date: 07-Feb-2025

- ☆

1

Data Structure
Heap

Convert the array (56,33,48,29,99,12 and 344) into min heap.

#### Initial array as a binary tree:

```
56
/      \
33        48
/  \      /  \
29   99   12  344
```

**Swap 48 and 12:**

```
56
/      \
33        12
/  \      /  \
29   99   48  344
```

**Swap 33 and 29:**

```
56
/      \
29        12
/  \      /  \
33   99   48  344
```

**Swap 56 and 12:**

```
12
/      \
29        56
/  \      /  \
33   99   48  344
```

**Swap 56 and 48:**

```
12
/      \
29        48
/  \      /  \
33   99   56  344
```

#### Final Result

The array now satisfies the  **min heap property** : every parent node is smaller than or equal to its children.

```
12
/      \
29        48
/  \      /  \
33   99   56  344
```

- ☆

2

Programming Concept
Array

Write the pseudocode/ program (in any language) to print the common element between two arrays and the total number of such elements found. [assume each element in an array distinct].

```
#include <iostream>
using namespace std;
int main() {
int size1, size2;
// Taking input size of first array
cout << "Enter size of first array: ";
cin >> size1;
int arr1[size1];
cout << "Enter elements of first array:\n";
for (int i = 0; i < size1; i++) {
cin >> arr1[i];
}
// Taking input size of second array
cout << "Enter size of second array: ";
cin >> size2;
int arr2[size2];
cout << "Enter elements of second array:\n";
for (int i = 0; i < size2; i++) {
cin >> arr2[i];
}
// To store common elements
int commonElements[size1 < size2 ? size1 : size2];
int count = 0;
// Check each element in arr1 against arr2
for (int i = 0; i < size1; i++) {
bool found = false;
for (int j = 0; j < size2; j++) {
if (arr1[i] == arr2[j]) {
found = true;
break;
}
}
if (found) {
// Check for duplicates
bool alreadyExists = false;
for (int k = 0; k < count; k++) {
if (commonElements[k] == arr1[i]) {
alreadyExists = true;
break;
}
}
if (!alreadyExists) {
commonElements[count] = arr1[i];
count++;
}
}
}
// Print common elements
cout << "Common elements: ";
for (int i = 0; i < count; i++) {
cout << commonElements[i] << " ";
}
cout << endl;
// Print total count
cout << "Total number of common elements: " << count << endl;
return 0;
}
```

```
Sample I/O:
Enter size of first array: 5
Enter elements of first array: 0 20 30 40 50
Enter size of second array: 6
Enter elements of second array: 10 2 20 30 60 90
Common elements: 20 30
Total number of common elements: 2

=== Code Execution Successful ===
```

🔗 Run Online: Print Common Elements Between Two Arrays

- ☆

3

Digital Logic Design
Basic Gate

Given a logical function, find out the truth table of AB· (A+B).C

- ☆

4

Operating System
Deadlock

Consider the following snapshot of a system where maximum instance of A, B, C and D are 3, 14, 12 and 12.
Answer the following Question using the Bankers algorithm,  **a) Calculate the need matrix from the above table?b) Is the system in the safe state? Find out the safe sequence if no, justify the reason.**

a) answer: The Need matrix is calculated as: Need = Max - Allocation For each process, we subtract the Allocation from the Max to get the Need Matrix. b) answer: **Step-by-step checking for our system:**

**P0:**  Needs [0, 0, 0, 0] ≤ Available [1, 5, 2, 0] → yes, so finish P0.
Update Available by adding P0's allocation: [1, 5, 2, 0] + [0, 0, 1, 2] = [1, 5, 3, 2]
**P1:**  Needs [0, 7, 5, 0] ≤ Available [1, 5, 3, 2] → no, cannot finish yet.
**P2:**  Needs [1, 0, 0, 2] ≤ Available [1, 5, 3, 2] → yes, finish P2.
Update Available : [1, 5, 3, 2] + [1, 3, 5, 4] = [2, 8, 8, 6]
**P3:**  Needs [0, 0, 2, 0] ≤ Available [2, 8, 8, 6] → yes, finish P3.
Update Available : [2, 8, 8, 6] + [0, 6, 3, 2] = [2, 14, 11, 8]
**P4:**  Needs [0, 6, 4, 2] ≤ Available [2, 14, 11, 8] → yes, finish P4.
Update Available : [2, 14, 11, 8] + [0, 0, 1, 4] = [2, 14, 12, 12]
**P1 (rechecked):**  Needs [0, 7, 5, 0] ≤ Available [2, 14, 12, 12] → yes, finish P1.
Update Available : [2, 14, 12, 12] + [1, 0, 0, 0] = [3, 14, 12, 12]

Since all processes can finish in this order, the system is in a safe state.
**Safe sequence:**  <P0, P2, P3, P4, P1>

**🎥 Video Solution:**
Deadlock Handling (Deadlock Avoidance - Banker's Algorithm)

- ☆

5

Computer Network
OSI/TCP-iP

Synthia wants to send an email to her friend. He sends the email through the application and transport layer. **(a)Mention the protocol of application layer and transport layer(b)Draw a diagram from the above scenario.**

**Protocols used in Application Layer and Transport Layer:**
**Application Layer:**  The protocol commonly used here for sending emails is SMTP (Simple Mail Transfer Protocol).
**Transport Layer:**  This layer is responsible for the reliable transmission of data between applications. The commonly used protocol at this layer is TCP (Transmission Control Protocol), which ensures that the data is delivered accurately and in order.
**ব্যাখ্যা দেখুন:**
Application Layer Protocol :Simple Mail Transfer Protocol(SMTP)
ইমেইল পাঠানোর জন্য Application Layer-এ SMTP ব্যবহৃত হয়। SMTP এর কাজ হলো একটি কম্পিউটার থেকে অন্য কম্পিউটারে ইমেইল মেসেজ পাঠানো। এটি ব্যবহারকারীকে সহজে ইমেইল লিখে পাঠানোর সুযোগ দেয় এবং সার্ভারগুলোর মধ্যে মেসেজ ট্রান্সফার পরিচালনা করে।
**Transport Layer Protocol :TCP (Transmission Control Protocol)**
Transport Layer-এর মূল কাজ হলো ডেটা নির্ভরযোগ্যভাবে (reliably) গন্তব্যে পৌঁছে দেওয়া।
TCP (Transmission Control Protocol) ব্যবহার করা হয় কারণ:

এটি ডেটাকে ছোট ছোট অংশে (segments) ভেঙে পাঠায়।
প্রতিটি অংশ ঠিকভাবে এবং সঠিক ক্রমে (in order) পৌঁছেছে কিনা তা যাচাই করে।
ডেটা হারিয়ে গেলে পুনরায় পাঠানোর ব্যবস্থা করে।

ইমেইল একটি গুরুত্বপূর্ণ যোগাযোগ মাধ্যম। যদি মেসেজের কোনো অংশ হারিয়ে যায় বা এলোমেলোভাবে পৌঁছে যায়, তাহলে ইমেইলটি অপূর্ণ বা ভুল হয়ে যাবে। এজন্য Application Layer-এ SMTP ইমেইল পাঠানোর নিয়ম ঠিক করে দেয়, আর Transport Layer-এ TCP ডেটা সঠিকভাবে, সম্পূর্ণভাবে এবং নির্ভরযোগ্যভাবে পৌঁছানো নিশ্চিত করে।
**(b) Answer:**  The diagram illustrates the process of sending an email from the sender to the receiver
**ব্যাখ্যা দেখুন:**
Sender’s Device → Sender’s Mail Server এর সাথে SMTP protocol ব্যবহার করে যোগাযোগ করে। Sender’s Mail Server → ইন্টারনেটের মাধ্যমে SMTP ব্যবহার করে ইমেইলটি Receiver’s Mail Server-এ পাঠায়। Receiver’s Mail Server → ইমেইলটি Receiver’s Device-এ পৌঁছে দেওয়ার জন্য POP3 অথবা IMAP protocol ব্যবহার করে।

- ☆

6

Database Management System
keys

Find the primary key and foreign key after decomposition of the given schema (Branch_name, Acc_name, Balance, Brnach_city, Assets) and then identify which normalization it is?

Original Schema:
The original schema had attributes like  **Branch_name** ,  **Acc_name** ,  **Balance** ,  **Branch_city** , and  **Assets** .
Initially, everything was in a single table, but it had some issues because  **Branch_name**  was part of the key for identifying branch info, while  **Acc_no**  was the key for account info.
After Decomposition:
1. Account Table:

**Primary Key** :  **Acc_no**  (Each account has a unique identifier).
**Foreign Key** :  **Branch_name**  (This links each account to a branch).
**Non-key attributes**  (Acc_name, Balance) fully depend on  **Acc_no** .

2. Branch Table:

**Primary Key** :  **Branch_name**  (Each branch has a unique name).
**Non-key attributes**  (Branch_city, Assets) fully depend on  **Branch_name** .

Why 2NF?
**2NF**  (Second Normal Form) means:

There are no  **partial dependencies**  (where attributes depend on part of the key).
In each table, all non-key attributes depend entirely on the full primary key.

So, by breaking up the data into two tables, we've removed partial dependencies and made the schema  **2NF** .
Explanation:
**১. প্রথমে একক টেবিলের স্কিমা:**
আমাদের কাছে প্রথমে ছিল একটি টেবিল, এই টেবিলটির মধ্যে অ্যাট্রিবিউটগুলো হলো:

```
(Branch_name, Acc_name, Balance, Branch_city, Assets)
```

এই টেবিলটি ছিল একক টেবিল, কিন্তু এতে কিছু সমস্যা ছিল—বিশেষত  **partial dependency** । এর মানে হলো, কিছু অ্যাট্রিবিউট (যেমন  **Branch_city**  এবং  **Assets** )  **Branch_name**  এর উপর নির্ভরশীল, যেটি এই টেবিলের একটি অংশ। যাতে নরমালাইজেশন ছিলো না।
**২. ডিকম্পোজিশন (Decomposition):**
এখন, এই সমস্যা সমাধান করতে আমরা টেবিলটিকে দুটি আলাদা টেবিলে ভাগ করি:
**Account Table:**

```
(Account_no, Acc_name, Balance, Branch_name)
```

**Primary Key** :  **Acc_no**  **Acc_no**  একটি ইউনিক আইডেন্টিফায়ার, যা প্রতিটি অ্যাকাউন্টকে ইউনিক করে।
**Foreign Key** :  **Branch_name**  **Branch_name**  একটি ফরেন কী হিসেবে কাজ করে, যা
```
Branch
```
টেবিলের শাখার নামের সাথে সম্পর্কিত।

**Branch Table:**

**Primary Key** :  **Branch_name**  **Branch_name**  শাখার ইউনিক আইডেন্টিফায়ার।
**Foreign Key** : এখানে কোনো ফরেন কী নেই।

**৩. ২NF (Second Normal Form):**
**Partial Dependency:**
প্রথম স্কিমাতে  **Branch_name**  ছিল একটি অংশ, যা  **Branch_city**  এবং  **Assets**  এর মতো শাখার তথ্য ধারণ করছিল। তবে, অ্যাকাউন্টের জন্য প্রাথমিক কী  **Acc_no**  পুরোপুরি অ্যাকাউন্টের তথ্য ( **Acc_name** ,  **Balance** ) নির্ধারণ করতে ব্যবহৃত হয়।
ডিকম্পোজিশন করার পর,  **Account**  টেবিলের সমস্ত অ-প্রাথমিক অ্যাট্রিবিউট  **Acc_no**  এর উপর নির্ভরশীল হয়েছে, আর  **Branch**  টেবিলের সমস্ত অ-প্রাথমিক অ্যাট্রিবিউট  **Branch_name**  এর উপর নির্ভরশীল।
এটি  **partial dependency**  দূর করেছে, যেখানে কোনো অ্যাট্রিবিউট প্রাথমিক কীর একটি অংশের উপর নির্ভরশীল ছিল না।
**২NF**  অর্জিত হয়েছে কারণ:

**Account**  টেবিলের সকল Non-key Attribute  **Acc_no**  এর উপর নির্ভরশীল।
**Branch**  টেবিলের সকল Non-key Attribute  **Branch_name**  এর উপর নির্ভরশীল

এই ডিকম্পোজিশনটি নিশ্চিত করেছে যে, আমরা  **partial dependency**  দূর করেছি এবং প্রতিটি টেবিলের Non-key Attribute তাদের পুরো primary keyএর উপর নির্ভরশীল। এর ফলে আমরা  **২NF (Second Normal Form)**  অর্জন করেছি।

- ☆

7

Computer Network
Transmission Mode and Network Performance

Suppose Bangladesh bank is designing a nation of communication network for office located in Dhaka and Rangpur. Their offices are connected via wide area network (WAN). The team needs to ensure that applications with low latency requirements (such as VOIP and video conferencing) can operate efficiently between these offices.         Given:      Distance between Dhaka and Rangpur = 30 km Speed of fiber optic link = 2 × 108 m/s Link capacity = 1 Gbps Average size of data packets = 15,000 bytes Delay at each router/switch along the path = 5 ms RTT between Dhaka and Rangpur = 50 ms       Calculate the total network latency between office at Dhaka and Rangpur, considering the propagation delay and transmission delay.

Distance between Dhaka and Rangpur = 30 km = 30,000 meters
Speed of fiber optic link = 2 × 108 m/s
Link capacity = 1 Gbps = 1 × 109 bps
Average size of data packets = 15,000 bytes = 120,000 bits (15,000 × 8)
Delay at each router/switch = 5 ms
RTT between Dhaka and Rangpur = 50 ms

#### Propagation Delay

Propagation Delay = Distance / Propagation Speed
= 30,000 meters / (2 × 108 m/s) = 0.00015 seconds = 0.15 ms

#### Transmission Delay

Transmission Delay = Packet Size (bits) / Link Capacity (bps)
= 120,000 bits / (1 × 109 bps) = 0.00012 seconds = 0.12 ms

#### Router Delay

There are 1 routers and 1 switch each with 5 ms delay:
Router Delay = 2 × 5 ms = 10 ms

#### Total One-Way Latency

Total Latency = Propagation Delay + Transmission Delay + Router Delay
= 0.15 ms + 0.12 ms + 10 ms =  **10.27 ms (Answer)**

#### Round Trip Time (RTT)

RTT = 2 × One-way latency (since round trip includes going and coming back)
RTT=2×10.27 ms=20.54 ms
The given RTT (50 ms) is higher, which suggests additional delays are present such as queuing delay, processing delay, or other network factors not explicitly included in the simple calculation.
**🎥 Video Solution:**  Network Latency Calculation

**🎥 Video Solution:**  Network Delay Types & Round-Trip Time Explained (in Bangla)

- ☆

8

Data Center & Virtualization
Others

Bangladesh Bank have client server and the communicate with Mail server, DNS server, web server. Bangladesh Bank want to ensure the security using firewall on those server. Draw a diagram with the scenario.

The diagram represents a secure network architecture for Bangladesh Bank, where client-server communication is protected using firewalls:
The diagram illustrates a secure client-server architecture for Bangladesh Bank, where clients communicate with different servers through a firewall to ensure network security. **Clients (Users):**  Users access Bangladesh Bank's online services through the Internet using web browsers or mobile applications.  **Perimeter Firewall:**  The first firewall acts as a security gateway between the Internet and the bank's servers. It filters incoming and outgoing traffic, allowing only authorized requests while blocking unauthorized access and cyber attacks.  **DMZ (Demilitarized Zone):**  Public-facing servers are placed in the DMZ to minimize the risk of exposing the internal network. These include:  Web Server – Handles HTTP/HTTPS requests from clients. Mail Server – Provides email services using SMTP/SMTPS protocols. DNS Server – Resolves domain names to IP addresses for client requests.  **Internal Firewall:**  A second firewall separates the DMZ from the bank's internal network. It allows only necessary communication between the public servers and the internal systems, preventing attackers from directly accessing sensitive resources.  **Application Server:**  This server hosts Bangladesh Bank's core banking applications and business logic. It processes requests received from the Web Server and communicates with the Database Server. **Database Server:**  Stores confidential banking information such as customer records, transaction data, and account details. It is accessible only by the Application Server and is never exposed directly to the Internet.Security Features    Filters unauthorized network traffic.    Allows only required ports and services (HTTP/HTTPS, SMTP, DNS).    Protects internal servers from external attacks.    Isolates public-facing servers using a DMZ.    Restricts access to sensitive banking data through an Internal Firewall.    Enhances confidentiality, integrity, and availability of banking services. **Conclusion:** By deploying perimeter and internal firewalls along with a DMZ architecture, Bangladesh Bank ensures that client requests are securely processed while protecting its critical application and database servers from unauthorized access and cyber threats

- ☆

9

Non Technical Question
Non tech

∫ from 0 to 2 of (2x² + 3x) dx?

In Bangladesh Bank there are 6 Assistant directors and 4 Deputy Directors (DD's). Each AD brings a bag, while only half of the DDs bring a bag. If a bag is selected at random from all the bags, what is the probability that the chosen bag belongs to a Deputy Director (DD)?

**Translations:** ক) শনিবার হতে সে অফিস আসছে নাখ) আপনার ব্যাংঙ্ক একাউন্টের স্থিতি জানার জন্য মোবাইল ব্যাংকিং এপ্লিকেশনে লগিন করুন

Short notes on "AI and machine language mitigate challenge of cyber attack on banking system"

- ☆

10

MCQ
MCQ

Which the universal gate?  **Ans.:**  Nor and NAND gate
What is best way to implement priority queue?  **Ans.:**  Heap
Reverse voltage Zener diode is used as?  **Ans.:**  Voltage Regulator
What kind of encryption is used for email?  **Ans.:**  TLS
Which algorithm used digital signature?  **Ans.:**  RSA
What is HTTP code 500?  **Ans.:**  Internal Server Error
Which one make data access from a database faster?  **Ans.:**  Indexing
Which device that's converts AC to DC?  **Ans.:**  Rectifier
Priority scheduling math no arrival time, find the average TAT?  **Ans.:**  0
Find the current from a circuit, where voltage & resistance already given?  **Ans.:**  0.5A
What factors doesn’t affect inductance?  **Ans:**
What is the major drawback of waterfall model?  **Ans:**  lack of flexibility
What is not a web server type?  **Ans:**
Docker containers within a single application?
A circular queue has size 6, front 2nd index, rear 5th index. What will the position of rear after insert a value in front?
During sending email that message should not alter/modify, which database properties ensure this?
In binary tree what are the root value of the following 56, 58, 12, 78?
Write the 2’s complement of (65)16.
A process needs I/O operations, it switches to …..waiting state.
Which the command of DDL?
Integration testing is the process of testing the interface between two software or modules.
SUEZ canal connects which two seas?  **Ans.:**  Mediterranean sea and the Red sea
First ICC ODI Men's World Cup winner captain?  **Ans.:**  Clive Lloyd
Who won the Nobel peace prize in 2024?  **Ans.:**  Nihon Hidankyo
What the highest peak of Bangladesh?  **Ans.:**  Tazingdong
Strasbourg belongs to which country?  **Ans.:**  France
A pipe can fill a tank in 4 hours, and another pipe can fill it in 6 hours. How much time will they take to fill the tank together? Answer: 2.4 hours
What is the distance from A's starting point to his final position? Answer: 4.24 meters
Mr. X uses 30% of his salary for expenses, 20% for his final position, and 10% for another. His remaining amount is 12,000 Taka. What is his total salary? Ans.: 30,000
The father's age is 36 and the son's age is 16. How many years ago was the father's age three times the son's age?  **Ans.:**  6 years ago
There are 8 balls, and one ball is heavier than the other 7, which are of the same weight. How many weighing are required to guarantee finding the heavier ball?  **Ans:**  2
192.168.16.10, which the subnet address of this ip address?
Find the output.

```
int main() {
int x=3;
int y=2;
if (x==2)
y=3;
else
y=2;
printf("%d %d\n", x, y);
}
```

**Ans.:**  2, 3
