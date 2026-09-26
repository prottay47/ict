# Sonali & Janata Bank, Assistant Database Administrator, 2022

- **Original URL:** [https://it.jobqns.com/sonali-janata-bank-assistant-database-administrator-2022/](https://it.jobqns.com/sonali-janata-bank-assistant-database-administrator-2022/)
- **Date:** 2026-02-05T22:34:24
- **Categories:** Bank IT Job Solution, Bank IT Job Solution 2022, Job Solution 2022

---

ADA • Year 2022

Sonali and Janata Bank

💼Post Name: Assistant Database Administrator

🏛Exam Taker: CTI

📅Exam Date: 01-Mar-2022

ℹ️ (IT : 15*10 + Non IT : 4*10 + GK: 2*5) = 200

- ☆

1

Database Management System
ER Diagram

Draw an ER diagram for BPL.

- ☆

2

Database Management System
Database Types

What is distributed database?Write the role of a DB administrator.


**Distributed Database**
A  **distributed database**  is a database in which data is stored across multiple physical locations (different computers or servers) that are connected through a network. Although the data is distributed, it appears to users as a single unified database.
Each site in a distributed database system can process local queries independently and also participate in global queries.
**Example:**  A bank database where customer data is stored in different branch servers located in different cities.
**Role of a Database Administrator (DBA)**
A  **Database Administrator (DBA)**  is responsible for managing, maintaining, and securing the database system to ensure data availability, integrity, and performance.

**Database Installation & Configuration:**  Installs, configures, and upgrades database software.
**Data Security:**  Controls user access, permissions, and ensures data protection.
**Backup & Recovery:**  Performs regular backups and restores data during failures.
**Performance Monitoring:**  Optimizes database performance and handles tuning.
**Data Integrity:**  Ensures accuracy and consistency of stored data.



**Distributed Database**
**Distributed database**  হলো এমন একটি database যেখানে data একাধিক physical location-এ (ভিন্ন computer বা server-এ) সংরক্ষিত থাকে এবং network-এর মাধ্যমে সংযুক্ত থাকে। তবে user-এর কাছে এটি একটি single unified database হিসেবেই দেখা যায়।
এই system-এ প্রতিটি site নিজস্ব local query process করতে পারে এবং একই সাথে global query-তেও অংশ নিতে পারে।
**উদাহরণ:**  একটি bank system যেখানে বিভিন্ন শহরের branch server-এ customer data সংরক্ষিত থাকে।
**Database Administrator (DBA)-এর ভূমিকা**
**Database Administrator (DBA)**  হলো সেই ব্যক্তি যিনি database system পরিচালনা, রক্ষণাবেক্ষণ এবং নিরাপত্তা নিশ্চিত করেন যাতে data সবসময় available, secure এবং consistent থাকে।

**Database Installation & Configuration:**  Database software install, configure এবং update করে।
**Data Security:**  User access control ও permission manage করে data সুরক্ষিত রাখে।
**Backup & Recovery:**  নিয়মিত backup নিয়ে data loss হলে restore করে।
**Performance Monitoring:**  Database-এর performance পর্যবেক্ষণ ও tuning করে।
**Data Integrity:**  Data-এর accuracy ও consistency নিশ্চিত করে।

- ☆

3

Data Center & Virtualization
RAID

RAID Related question

**RAID (Redundant Array of Independent Disks)**  is a technology that combines multiple physical disks into a single logical unit to improve  **performance** ,  **reliability** , and  **data availability** .

**Techniques:**  Uses striping, mirroring, and parity.
**Goal:**  Faster data access and protection against disk failure

**Relevance in Database**
RAID is highly important in database systems because databases require  **high speed**  and  **data reliability** .

Ensures continuous database availability.
Prevents data loss due to disk failure.
Improves read/write performance.

**Uses in Database**

**RAID 1:**  Used for critical data (mirroring for safety).
**RAID 5:**  Used for balance of performance and storage efficiency.
**RAID 10:**  Used for high-performance databases.
**Backup Systems:**  Ensures data redundancy.

**Is it Possible?**
Yes, RAID is  **widely used**  in database systems.

Implemented using hardware RAID controllers or software RAID.
Common in servers, data centers, and enterprise systems.
Essential for systems like banking, e-commerce, and cloud databases.

**RAID (Redundant Array of Independent Disks)**  হলো একটি প্রযুক্তি যেখানে একাধিক physical disk একসাথে ব্যবহার করে একটি logical unit তৈরি করা হয় যাতে  **performance** ,  **reliability**  এবং  **data availability**  বাড়ানো যায়。

**Technique:**  Striping, mirroring এবং parity ব্যবহার করা হয়।
**Goal:**  দ্রুত data access এবং disk failure থেকে সুরক্ষা।

**Database-এ RAID-এর গুরুত্ব**
Database system-এ RAID খুব গুরুত্বপূর্ণ কারণ এখানে  **speed**  এবং  **data নিরাপত্তা**  অত্যন্ত জরুরি।

Database সবসময় চালু রাখতে সাহায্য করে।
Disk নষ্ট হলেও data loss কমায়।
Read/write performance উন্নত করে।

**Database-এ RAID-এর ব্যবহার**

**RAID 1:**  গুরুত্বপূর্ণ data-এর জন্য (mirroring)।
**RAID 5:**  performance এবং storage-এর balance।
**RAID 10:**  high-performance database-এর জন্য।
**Backup System:**  data redundancy নিশ্চিত করে।

**এটি কি সম্ভব?**
হ্যাঁ, RAID database system-এ  **ব্যাপকভাবে ব্যবহৃত হয়** ।

Hardware বা software RAID ব্যবহার করে implement করা যায়।
Server, data center এবং enterprise system-এ ব্যবহৃত হয়।
Banking, e-commerce এবং cloud system-এ অত্যন্ত গুরুত্বপূর্ণ।

- ☆

4

Design Analysis of Algorithm
Greedy Algorithm

Is bellman ford a greedy algorithm ? Can all pair shortest paths (with negative cycles) be done in O(V3)?

**No.**  The  **Bellman-Ford Algorithm**  is  **not**  a  **Greedy Algorithm** . It is a  **Dynamic Programming** -based algorithm because it repeatedly relaxes all edges to find the shortest path from the source vertex to every other vertex.

**Why?**

• It performs  **Edge Relaxation**  for all edges exactly  **V − 1**  times.
• A shorter path found in a later iteration can update a previously calculated distance.
• It works correctly even when the graph contains  **Negative Edge Weights** .
• It can also detect  **Negative Weight Cycles** .

**Can All-Pairs Shortest Paths (with Negative Edge Weights) be computed in O(V3)?**
**Yes.**  The  **Floyd-Warshall Algorithm**  computes the  **All-Pairs Shortest Paths (APSP)**  in  **O(V3)**  time, provided that the graph does  **not**  contain a  **Negative Weight Cycle** .

**Key Points:**

• Supports  **Negative Edge Weights** .
• Time Complexity is  **O(V3)** .
• If a  **Negative Weight Cycle**  exists, the shortest path is undefined because the path cost can decrease indefinitely.
• The algorithm can detect a  **Negative Weight Cycle** , but it cannot produce valid shortest paths in that case.

- ☆

5

Database Management System
Trigger

What is trigger? When it is used? Write down some advantages of trigger.

A  **Trigger**  is a special type of  **Stored Procedure**  in a  **Database Management System (DBMS)**  that automatically executes (fires) when a specified event occurs on a table or view. These events are typically  **INSERT** ,  **UPDATE** , or  **DELETE**  operations.
**When is a Trigger Used?**

Triggers are used when certain actions need to be performed automatically after or before changes are made to database data.

Common uses of Triggers include:
• Automatically maintaining  **Audit Logs** .
• Enforcing  **Business Rules**  and data integrity.
• Validating data before insertion or update.
• Automatically updating related tables.
• Preventing unauthorized or invalid data modifications.

**Advantages of Trigger**

• Executes automatically without user intervention.
• Maintains data consistency and integrity.
• Reduces repetitive application code.
• Helps implement complex business rules.
• Keeps an audit trail of database changes.
• Improves database security by controlling data modifications.

**Example**

A Trigger can automatically store the old employee salary in an  **Audit Table**  whenever the salary is updated.

- ☆

6

Database Management System
ACID

Write short note on ACID Propertise of database

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

7

Linux Command

Unix command (directory listing with hidden files).

**Answer:**
```
$ ls -al
```



☆

8

Programming Concept

String reverse program but without using new storage.

```
#include <bits/stdc++.h>
using namespace std;

int main() {
string s;
cout << "Enter String: ";
cin >> s;
int n = s.length();
int start = 0, end = n - 1;

while (start < end) {
// XOR-based swapping without using extra storage
s[start] ^= s[end];
s[end] ^= s[start];
s[start] ^= s[end];
start++;
end--;
}

cout << "Reverse String = " << s << endl;
return 0;
}
```

```
Sample I/O:
Enter String: itjobqns
Reverse String = snqbojti
=== Code Execution Successful ===
```

🔗 Run Online: Reverse String



☆

9

Database Management System

Suppose a relational schema R(w,x,y,z)R(w,x,y,z) and the set of functional dependencies FF is given as: F={wx→yz,y→w,z→x} Find the candidate keys in the above relation.

**Given:**  R(w,x,y,z)
**Functional Dependencies:**  F = { wx→yz, y→w, z→x }
**Goal:**  Find all  **candidate keys**  (minimal superkeys).
**Key idea:**  Find attribute sets whose  **closure**  gives {w,x,y,z} and are  **minimal** .
**Closures:**

**(wx)+**  = wx → yz ⇒ {w,x,y,z} ⇒  **wx**  is a candidate key.
**(yz)+** : y→w ⇒ add w, z→x ⇒ add x ⇒ {w,x,y,z} ⇒  **yz**  is a candidate key.
**(wz)+** : z→x ⇒ get x, now wx→yz ⇒ get y,z ⇒ {w,x,y,z} ⇒  **wz**  is a candidate key.
**(xy)+** : y→w ⇒ get w, now wx→yz ⇒ get y,z ⇒ {w,x,y,z} ⇒  **xy**  is a candidate key.

**Answer (Candidate Keys):**  { **wx** }, { **xy** }, { **wz** }, { **yz** }


**প্রদত্ত:**  R(w,x,y,z)
**Functional Dependencies:**  F = { wx→yz, y→w, z→x }
**উদ্দেশ্য:**  সবগুলো  **candidate key**  (minimal superkey) বের করা।
**Key idea:**  যে attribute set-এর  **closure**  থেকে {w,x,y,z} পাওয়া যায় এবং সেটি  **minimal** , সেটিই candidate key।
**Closures:**

**(wx)+**  = wx → yz ⇒ {w,x,y,z} ⇒  **wx**  candidate key।
**(yz)+** : y→w ⇒ w যোগ, z→x ⇒ x যোগ ⇒ {w,x,y,z} ⇒  **yz**  candidate key।
**(wz)+** : z→x ⇒ x পাওয়া যায়, এরপর wx→yz ⇒ y,z পাওয়া যায় ⇒ {w,x,y,z} ⇒  **wz**  candidate key।
**(xy)+** : y→w ⇒ w পাওয়া যায়, এরপর wx→yz ⇒ z পাওয়া যায় ⇒ {w,x,y,z} ⇒  **xy**  candidate key।

**উত্তর (Candidate Keys):**  { **wx** }, { **xy** }, { **wz** }, { **yz** }


☆

10

Database Management System

Weak Entry vs strong entity difference with relation.





☆

11

Structure Query Language

Four queries(table client, salesman, sale, order etc) (unable to collect this question)

- ☆

12

Database Management System
Keys

Relation to find primary, candidate, super key

**Primary Key, Candidate Key, and Super Key (with Example)**
In a relational database, keys are used to uniquely identify each record (tuple) in a relation.
**Example Relation: STUDENT**
STUDENT( **StudentID** , Name, Email, Phone)

**Super Key:**  A  **super key**  is a set of one or more attributes that can uniquely identify a record in a table.

**Super Key Examples:**
{StudentID}, {Email}, {StudentID, Name}, {StudentID, Phone}

**Candidate Key:**  A  **candidate key**  is a minimal super key. It uniquely identifies a record and has no unnecessary attributes.

**Candidate Key Examples:**
{StudentID}, {Email}

**Primary Key:**  A  **primary key**  is one candidate key chosen to uniquely identify records in the relation.

**Primary Key Example:**
StudentID


**Primary Key, Candidate Key এবং Super Key (উদাহরণসহ)**
Relational database-এ key ব্যবহার করা হয় relation-এর প্রতিটি record (tuple) uniquely identify করার জন্য।
**উদাহরণ Relation: STUDENT**
STUDENT( **StudentID** , Name, Email, Phone)

**Super Key:**   **Super key**  হলো এক বা একাধিক attribute-এর সমন্বয় যা একটি record uniquely identify করতে পারে।

**Super Key-এর উদাহরণ:**
{StudentID}, {Email}, {StudentID, Name}, {StudentID, Phone}

**Candidate Key:**   **Candidate key**  হলো minimal super key, অর্থাৎ কোনো অতিরিক্ত attribute থাকে না।

**Candidate Key-এর উদাহরণ:**
{StudentID}, {Email}

**Primary Key:**   **Primary key**  হলো candidate key থেকে নির্বাচিত একটি key যা table-এর প্রতিটি record uniquely identify করে।

**Primary Key-এর উদাহরণ:**
StudentID

- ☆

13

Data Structure
Hashning

Separate chaining hash function math.(How hashing is done for a particular set of numbers with the hashing function f(x)=x mod 7, show ythe process in diagrams and the resulting hashing table

we have some elements :- {15, 47, 23, 34, 85, 97, 65, 89, 70}. And hash function is h(x) = x mod 7.
The hash values will be

x
h(x) = x mod 7

15
1

47
5

23
2

34
6

85
1

97
6

56
2

89
5

70
0

The Hashing with chaining will be like −

- ☆

14

Non Technical Question
Non Tech

বাংলা ফোকাস: -প্রযুক্তির অপব্যবহার এবং নৈতিক অবক্ষয়English Focus: Drug Abuse and its remedy.B2E: Covid-19 and the situation E2B- Intl Mother Language Day GK
