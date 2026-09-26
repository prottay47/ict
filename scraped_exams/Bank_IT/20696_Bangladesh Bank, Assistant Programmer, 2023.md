# Bangladesh Bank, Assistant Programmer, 2023

- **Original URL:** [https://it.jobqns.com/bangladesh-bank-assistantprogrammer-2023/](https://it.jobqns.com/bangladesh-bank-assistantprogrammer-2023/)
- **Date:** 2026-07-15T23:48:09
- **Categories:** Bank IT Job Solution 2023, Job Solution 2023

---

Assistant Programmer • Year 2023

Bangladesh Bank

💼Post Name: Assistant Programmer

📅Exam Date: 03-Feb-2024

- ☆

1

Data Structure
Hashing

Consider strong entries with integer keys. Suppose the hash function is h (k) = k mod 13. Insert in the given order entries with keys 10, 3, 6, 16, 17, 19 in to the hash table using linear probing to resolve collisions. Show all the work.

The hash function is given as h(k)=k mod 13.
The table size is 13, meaning we have indices from 0 to 12.
**Step-by-Step Insertion Process**
**Key: 10**
Hash value: h(10) = 10 mod 13 = 10. Insert 10 at index 10.
**Key: 3**
Hash value: h(3) = 3 mod 13 = 3. Insert 3 at index 3.
**Key: 6**
Hash value: h(6) = 6 mod 13 = 6. Insert 6 at index 6.
**Key: 16**
Hash value: h(16) = 16 mod 13 = 3. Index 3 is occupied. Use linear probing and insert 16 at index 4.
**Key: 17**
Hash value: h(17) = 17 mod 13 = 4. Index 4 is occupied. Use linear probing and insert 17 at index 5.
**Key: 19**
Hash value: h(19) = 19 mod 13 = 6. Index 6 is occupied. Use linear probing and insert 19 at index 7.
**Final Hash Table**

Index
Value

0
-

1
-

2
-

3
3

4
16

5
17

6
6

7
19

8
-

9
-

10
10

11
-

12
-

Summary
The final hash table after inserting all keys using linear probing is as follows:

```
[ - , - , - , 3 , 16 , 17 , 6 , 19 , - , - , 10 , - , - ]
```

- ☆

2

Computer Security
Threats

Describe a man-in the middle attack on the Diffie-Hellman key exchange protocol in which the adversary generates two public key pairs for the attack.

**Man-in-the-Middle (MITM) Attack on Diffie–Hellman Key Exchange**
In a  **MITM attack**  on  **Diffie–Hellman (DH)** , an attacker (Mallory) sits between  **Alice**  and  **Bob** , intercepts their public keys, and replaces them with her own. Since basic DH provides  **no authentication** , Alice and Bob cannot verify the real sender of the public key.
**Normal DH (No Attack)**

Public parameters: prime  **p** , generator  **g**
Alice selects private key  **a** , sends public key  **A = ga mod p**
Bob selects private key  **b** , sends public key  **B = gb mod p**
Shared key:  **K = gab mod p**

**MITM Attack (Attacker Generates Two Key Pairs)**
**Step 1: Interception**
Mallory intercepts Alice’s public key  **A**  and Bob’s public key  **B** .
**Step 2: Mallory Creates Two Private Keys**
Mallory chooses two private keys:  **m1**  (for Bob) and  **m2**  (for Alice).
**Step 3: Mallory Generates Two Public Keys**
Mallory computes:
**M1 = gm1 mod p**
**M2 = gm2 mod p**
**Step 4: Key Replacement (Fake Public Keys)**
Mallory sends  **M1**  to Bob pretending it is from Alice.
Mallory sends  **M2**  to Alice pretending it is from Bob.
**Step 5: Two Different Shared Keys are Formed**

Alice computes:  **K1 = (M2)a mod p**  (Alice–Mallory key)
Bob computes:  **K2 = (M1)b mod p**  (Bob–Mallory key)
Mallory can compute both keys:
**K1 = (A)m2 mod p**  and  **K2 = (B)m1 mod p**

**Result**

Alice and Bob do  **not**  share the same secret key.
Mallory shares one key with Alice and another key with Bob.
Mallory can  **read, modify, and re-encrypt**  messages between them.

**Why It Works**
Because basic Diffie–Hellman does  **not provide authentication** , public keys can be replaced without detection.
**Prevention**

Use  **Authenticated Diffie–Hellman**
Use  **Digital Signatures**  /  **Certificates (PKI)**
Use  **TLS (DHE/ECDHE + certificates)**

**Diffie–Hellman Key Exchange-এ Man-in-the-Middle (MITM) Attack**
**MITM attack** -এ attacker (Mallory)  **Alice**  এবং  **Bob** -এর মাঝখানে বসে public key গুলো intercept করে এবং নিজের public key বসিয়ে দেয়। Basic Diffie–Hellman-এ  **authentication নেই** , তাই Alice/Bob বুঝতে পারে না public key আসলেই কার কাছ থেকে এসেছে。
**Normal DH (Attack নেই)**

Public parameter: prime  **p** , generator  **g**
Alice private key  **a**  নেয়, public key পাঠায়  **A = ga mod p**
Bob private key  **b**  নেয়, public key পাঠায়  **B = gb mod p**
Shared key:  **K = gab mod p**

**MITM Attack (Attacker দুইটি Key Pair তৈরি করে)**
**Step 1: Interception**
Mallory Alice-এর public key  **A**  এবং Bob-এর public key  **B**  intercept করে।
**Step 2: Mallory দুইটি Private Key নেয়**
Mallory দুইটি private key বেছে নেয়:  **m1**  (Bob-এর জন্য) এবং  **m2**  (Alice-এর জন্য)।
**Step 3: Mallory দুইটি Public Key তৈরি করে**
Mallory হিসাব করে:
**M1 = gm1 mod p**
**M2 = gm2 mod p**
**Step 4: Public Key Replace করে**
Mallory Bob-কে  **M1**  পাঠায় (যেন Alice পাঠিয়েছে)।
Mallory Alice-কে  **M2**  পাঠায় (যেন Bob পাঠিয়েছে)।
**Step 5: দুইটা আলাদা Shared Key তৈরি হয়**

Alice হিসাব করে:  **K1 = (M2)a mod p**  (Alice–Mallory key)
Bob হিসাব করে:  **K2 = (M1)b mod p**  (Bob–Mallory key)
Mallory দুইটাই বের করতে পারে:
**K1 = (A)m2 mod p**  এবং  **K2 = (B)m1 mod p**

**Result**

Alice এবং Bob-এর মধ্যে একই secret key তৈরি হয় না।
Mallory Alice-এর সাথে একটি key এবং Bob-এর সাথে আরেকটি key share করে।
Mallory মাঝখান থেকে message  **পড়তে, পরিবর্তন করতে, এবং পুনরায় encrypt করে পাঠাতে**  পারে।

**কেন Attack কাজ করে**
Basic Diffie–Hellman-এ  **authentication নেই** , তাই public key সহজে replace করা যায়।
**Prevention**

**Authenticated Diffie–Hellman**  ব্যবহার
**Digital Signature**  /  **Certificate (PKI)**  ব্যবহার
**TLS (DHE/ECDHE + certificate)**  ব্যবহার

- ☆

3

Computer Security
CIA

Preserving confidentiality integrity and availability of data is a restatement of the concern over falsification, interception, masquerade and denial of service. Explain how the first three concepts relate to the last four.

The concepts of confidentiality, integrity, and availability (CIA triad) directly address the security concerns of falsification, interception, masquerade, and denial of service.
**Confidentiality**  ensures that sensitive information is accessible only to authorized users, protecting against interception, where data could be accessed or stolen by unauthorized parties.
**Integrity**  guarantees that data remains accurate and unaltered, defending against falsification, which involves malicious modification of data, and masquerade, where attackers assume false identities to tamper with information.
**Availability**  ensures that information and resources are accessible when needed, countering denial of service (DoS) attacks that aim to make systems or data unavailable to legitimate users.
By maintaining confidentiality, integrity, and availability, organizations can effectively mitigate these four major security threats and enhance overall data protection.

Confidentiality, Integrity, Availability (CIA triad)-এর ধারণাগুলো মূলত চারটি security threat-এর সাথে সম্পর্কিত: falsification, interception, masquerade, এবং denial of service।
**Confidentiality (গোপনীয়তা):**  সংবেদনশীল তথ্যকে শুধুমাত্র authorized users-এর জন্য accessible রাখে। এটি interception থেকে রক্ষা করে, অর্থাৎ unauthorized ব্যক্তি তথ্য access বা steal করতে পারবে না.
**Integrity (অখণ্ডতা):**  নিশ্চিত করে যে তথ্য correct এবং unaltered আছে। এটি falsification থেকে রক্ষা করে, যেখানে data maliciously modify করা হয়, এবং masquerade থেকে, যেখানে attacker false identity ব্যবহার করে information manipulate করতে পারে.
**Availability (উপলব্ধতা):**  তথ্য এবং resources ব্যবহারকারীদের প্রয়োজন অনুযায়ী accessible রাখে। এটি denial of service (DoS) attack থেকে রক্ষা করে, যা legitimate users-এর জন্য system বা data কে unavailable করতে চায়.
সারসংক্ষেপে, maintaining the CIA triad এই চারটি security threat mitigate করতে সাহায্য করে এবং overall data protection ensure করে।

- ☆

4

Programming Concept

Given two integers A and B as input write a program to compute the least common multiple of A and B.

```
#include <stdio.h>
int main () {
int n1, n2, max;
printf ("Enter two positive integers: ");
scanf ("%d %d", &n1, &n2);
// maximum number between n1 and n2 is stored in max

max = (n1> n2) ? n1: n2;
while (1) {
// Check if max is divisible by both n1 and n2
if ((max% n1 == 0)&& (max % n2 ==0)) {
// If true, max is the LCM of n1 and n2
printf("The LCM of %d and %d is %d.", n1,n2,max);
break;
}
++max;
}
return 0;
}
```

```
Sample I/O:
Enter two positive integers: 14 8
The LCM of 14 and 8 is 56.
=== Code Execution Successful ===
```

🔗 Run Online: LCM of two integer


☆

5

Programming Concept

Consider the following code: Public class Class A {Public void m1 () {}Public void m2 (int i) {}Public void m3 (int i) {}Public static void m4 (int i) {} Public class class B extends class A {Public static void ml (int i) {} Public void m2 (int i) {} Public void m3 (string s) {} Public static void m4 (int i) {}Mention which of the methods overload, override and hied supper class methods. What about the remaining method?

- ☆

6

Data Structure
Heap

Given the adjacency list representation of a complete binary tree with 7 vertices, write the equivalent adjacency matrix representation. Assume that the vertices are numbered from 1 to 7 as in a binary heap.

**Complete Binary Tree**    **Adjacency List Representation**

Vertex
Connected Vertices

1
2, 3

2
4, 5

3
6, 7

4


5


6


7


**Adjacency Matrix Representation**


1
2
3
4
5
6
7

1
0
1
1
0
0
0
0

2
0
0
0
1
1
0
0

3
0
0
0
0
0
1
1

4
0
1
0
0
0
0
0

5
0
1
0
0
0
0
0

6
0
0
1
0
0
0
0

7
0
0
1
0
0
0
0

- ☆

7

Database Management System
Keys

Suppose that we have a relational database with the following table. Underlined one represent primary key Movies (mid, title, year) People (pid, name) Genres (gid, genre) HasRole (pid, mid, role) Has Genre (gid, mid) Write a SQL query to return the number of movies that are romantic comedies.

SELECT COUNT(*)
FROM Movies, Genres, HasGenre
WHERE Movies.mid = HasGenre.mid
AND HasGenre.gid = Genres.gid
AND Genres.genre = "romantic comedy";

- ☆

8

Computer Network
OSI/TCP-IP

In order to prevent that the company decided to add end to end encryption techniques which layer of the OSI model is suitable to work in considering parameters like development time, software maintainability and development cost, Give reasons for your concepts.

**Suitable OSI Layer for End-to-End Encryption** To implement  **end-to-end encryption (E2EE)**  while considering  **development time, software maintainability, and development cost** , the most suitable layer of the OSI model is the  **Application Layer (Layer 7)** .
**Reasons for Choosing the Application Layer**

**Faster Development Time:**  Encryption at the application layer can be implemented directly within the application logic. Developers do not need to modify lower-level networking protocols, which significantly reduces development time.
**Better Software Maintainability:**  Application-layer encryption is easier to update, debug, and maintain. Changes can be made without affecting the underlying network infrastructure or operating system.
**Lower Development Cost:**  No changes are required in routers, switches, or transport-layer implementations. This avoids hardware upgrades and reduces overall implementation cost.
**True End-to-End Security:**  Data is encrypted at the sender’s application and decrypted only at the receiver’s application. Intermediate systems (routers, proxies, servers) cannot read the data.
**Platform Independence:**  Application-layer encryption works across different networks, protocols, and platforms without compatibility issues.

**Why Not Lower Layers?**

**Transport Layer (e.g., TLS):**  Requires certificate management and protocol-level integration, increasing complexity and cost.
**Network/Data Link Layers:**  Require hardware or OS-level changes, leading to high cost and poor maintainability.

Considering development time, cost efficiency, and long-term maintainability, implementing end-to-end encryption at the  **Application Layer**  is the best and most practical choice.

**End-to-End Encryption-এর জন্য উপযুক্ত OSI Layer**
**End-to-end encryption (E2EE)**  বাস্তবায়নের ক্ষেত্রে যদি  **development time, software maintainability এবং development cost**  বিবেচনা করা হয়, তাহলে OSI model-এর মধ্যে সবচেয়ে উপযুক্ত হলো  **Application Layer (Layer 7)** ।
**Application Layer নির্বাচন করার কারণ**

**কম Development Time:**  Application layer-এ encryption সরাসরি application logic-এর ভেতরে implement করা যায়। নিচের network protocol পরিবর্তনের প্রয়োজন হয় না, ফলে সময় কম লাগে।
**সহজ Software Maintainability:**  Application-level encryption সহজে update, debug এবং maintain করা যায়। Network বা OS পরিবর্তন ছাড়াই security update সম্ভব।
**কম Development Cost:**  Router, switch বা hardware পরিবর্তনের দরকার হয় না। এতে implementation cost অনেক কমে যায়।
**প্রকৃত End-to-End Security:**  Sender-এর application-এ data encrypt হয় এবং receiver-এর application-এই decrypt হয়। মাঝখানের কোনো system data পড়তে পারে না।
**Platform Independent:**  Application layer encryption বিভিন্ন network ও platform-এ একইভাবে কাজ করে।

**নিচের Layer গুলো কেন উপযুক্ত নয়?**

**Transport Layer (যেমন TLS):**  Certificate management ও protocol complexity বেশি, ফলে খরচ ও রক্ষণাবেক্ষণ কঠিন।
**Network/Data Link Layer:**  Hardware বা OS পরিবর্তন দরকার হয়, যা ব্যয়বহুল ও জটিল।

Development time, খরচ এবং ভবিষ্যৎ maintainability বিবেচনা করলে  **Application Layer** -এ end-to-end encryption বাস্তবায়নই সবচেয়ে কার্যকর সমাধান।

- ☆

9

Computer Network
Others

Draw A class diagram. A token-ring based local area network (LAN) is a network consisting of nodes in which network packets are sent around. Every node has a unique name within the network, and refers to its next node. Different kinds of nodes exist: Workstations are originators of messages; servers and printers are network nodes that can receive messages. Packets contain an originator a destination and content, and are sent around on a network. A LAN is a circular configuration of nodes.

[source:visual-paradigm.com]

- ☆

10

Object Oriented Programming
Basic

Determine overloading method, overridden method and hide super class method?

**Method Overloading, Method Overriding, and Method Hiding**
**1. Method Overloading**
Method overloading occurs when multiple methods in the  **same class**  have the  **same method name**  but  **different parameter lists**  (different number, type, or order of parameters).

Resolved at  **compile time**
Improves code readability and flexibility

**Example:**

```
int add(int a, int b)
int add(int a, int b, int c)
```

**2. Method Overriding**
Method overriding happens when a  **subclass provides a new implementation**  of a method that is already defined in its  **superclass**  with the  **same method signature** .

Occurs in  **inheritance**
Resolved at  **runtime**  (runtime polymorphism)
Method must be  **non-static**

**Example:**

```
class Parent {
void show() { }
}
class Child extends Parent {
void show() { }
}
```

**3. Method Hiding (Hiding Superclass Method)**
Method hiding occurs when a  **static method**  in a subclass has the  **same name and signature**  as a static method in the superclass.

Applies only to  **static methods**
Resolved at  **compile time**
Not true overriding

**Example:**

```
class Parent {
static void display() { }
}
class Child extends Parent {
static void display() { }
}
```

**Summary Comparison**

**Overloading:**  Same class, same method name, different parameters
**Overriding:**  Subclass redefines superclass method (non-static)
**Hiding:**  Static method in subclass hides static method of superclass

**Method Overloading, Method Overriding এবং Method Hiding**
**১. Method Overloading**
একই class-এর ভেতরে একই নামের method থাকলে কিন্তু তাদের  **parameter আলাদা**  হলে তাকে method overloading বলে।

**Compile time** -এ সিদ্ধান্ত হয়
Code সহজ ও flexible হয়

**উদাহরণ:**

```
int add(int a, int b)
int add(int a, int b, int c)
```

**২. Method Overriding**
Subclass যখন superclass-এর একটি  **non-static method**  একই signature দিয়ে নতুনভাবে implement করে, তখন তাকে method overriding বলে।

**Inheritance** -এর ক্ষেত্রে হয়
**Runtime** -এ সিদ্ধান্ত হয়

**উদাহরণ:**

```
class Parent {
void show() { }
}
class Child extends Parent {
void show() { }
}
```

**৩. Method Hiding (Superclass Method Hide করা)**
Subclass যদি superclass-এর  **static method**  একই নাম ও signature দিয়ে define করে, তাহলে তাকে method hiding বলে।

শুধু  **static method** -এর ক্ষেত্রে হয়
**Compile time** -এ resolve হয়
এটা real overriding নয়

**উদাহরণ:**

```
class Parent {
static void display() { }
}
class Child extends Parent {
static void display() { }
}
```

**সংক্ষেপে পার্থক্য**

**Overloading:**  একই class, আলাদা parameter
**Overriding:**  Subclass superclass-এর method পরিবর্তন করে
**Hiding:**  Static method subclass দ্বারা hide হয়

- ☆

11

Non Technical Question
Non tech

10. Growing use to technology in the Financial Service Industry.11. Translation English to Bangla.12. Translation Bangla to English.13. If x is an Integer and x + 1/x= 17/4, then value of x – 1/x =?14. A basketball team has won 15 games and lost 9. If these games represent 16% of the games to be played, then how many more games must the team win to average 75% for the season?15. Students of a class are made to stand in rows. If 4 students are extra in each row, then there would be 2 rows less. If four students are less in each row, then there would be 4 more rows. What is the number of students in the class? 16. In the given figure, PQT is a right triangle then what is the area of square QRST.
