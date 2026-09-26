# BAPEX, AGM (ICT), 2023

- **Original URL:** [https://it.jobqns.com/bapex-agm-ict-2023/](https://it.jobqns.com/bapex-agm-ict-2023/)
- **Date:** 2026-02-11T22:54:43
- **Categories:** Gas Field IT Job Solution, Gas Field IT Job Solution 2023, Job Solution 2023

---

#### Bangladesh Petroleum Exploration and Production Company Limited
Post: Assistant General Manager (ICT)Exam Date: 20-01-2023 , Exam Taker: BUET



**1. Consider the following routing table at an IP router:**


**For each IP address in Group I, identify the correct outgoing interface         from Group II using the routing table above.**
**Answer using Longest Prefix Match (LPM)**
**Longest Prefix Match (LPM) ব্যবহার করে উত্তর**

**Routing নিয়ম:** Router  **Longest Prefix Match (LPM)**  algorithm ব্যবহার করে। যে route টি সবচেয়ে বেশি specific prefix match করে, সেটিই নির্বাচিত হয়। কোনো route match না করলে  **default route (0.0.0.0)**  ব্যবহার করা হয়।

**1) IP Address: 172.168.165.121** এই IP টি  **172.168.164.0/23**  network এর মধ্যে পড়ে, যার range হলো 172.168.164.0 থেকে 172.168.165.255। **Outgoing Interface: Interface 0**

**2) IP Address: 172.168.167.151** এই IP টি  **172.168.166.0/23**  network এর অন্তর্ভুক্ত, যার range 172.168.166.0 থেকে 172.168.167.255। **Outgoing Interface: Interface 1**

**3) IP Address: 172.168.163.151** এই IP টি routing table এ দেওয়া কোনো /23 network এর মধ্যে পড়ে না। তাই কোনো specific route match হয় না। **Outgoing Interface: Interface 4 (Default Route)**  **4) IP Address: 172.168.171.92** এই IP টি  **172.168.170.0/23**  network এর মধ্যে পড়ে, যার range 172.168.170.0 থেকে 172.168.171.255। **Outgoing Interface: Interface 3**  **5) IP Address: 0.0.0.0** এটি সরাসরি default route এর সাথে match করে। **Outgoing Interface: Interface 4 (Default Route)**

2. Write the function for which the output is 1 for that input.



**3. Consider the Schema employee(id, name,salary), equipment(id, name, price),**  **hire(employee_id, equipment_id)**



3(i) Draw the ERD digram for the relation.

Entity-Relationship Diagram (ERD) for Employee, Equipment, and Hire

Explanation:

**Employee Entity** : Contains information about employees such as  **id**  (Primary Key),  **name** , and  **salary** .

**Equipment Entity** : Holds details about equipment, including  **id**  (Primary Key),  **name** , and  **price** .

**Hire Relationship** : The  **Hire**  relationship connects employees to the equipment they have hired. This is a  **many-to-many**  relationship between Employee and Equipment. It includes:

**employee_id** : A foreign key from the Employee entity.

**equipment_id** : A foreign key from the Equipment entity.

**Many-to-Many Relationship** : An employee can hire multiple pieces of equipment, and each piece of equipment can be hired by multiple employees over time.

3(ii) Write the SQL query to show the name of employee who borrow the maximum equipment?
```
SELECT e.name
FROM employee e
JOIN hire h ON e.id = h.employee_id
JOIN (
SELECT equipment_id, COUNT(*) AS num_borrowed
FROM hire
GROUP BY equipment_id
ORDER BY num_borrowed DESC
LIMIT 1)
AS max_equip ON h.equipment_id = max_equip.equipment_id;
```



4. Identify the type of algorithm? (i) MD5 (ii) AES (iii) RSA (iv) Diffie-Hellman

**(i) MD5 – Hashing Algorithm**

MD5 (Message Digest 5) is a cryptographic hash function that generates a fixed-length hash value from variable-length input data. It is mainly used for data integrity checking to verify that data has not been modified.

**(ii) AES – Symmetric Encryption Algorithm**

AES (Advanced Encryption Standard) is a symmetric encryption algorithm that uses the same secret key for both encryption and decryption. It is widely used to ensure data confidentiality.

**(iii) RSA – Asymmetric Encryption Algorithm**

RSA (Rivest–Shamir–Adleman) is an asymmetric encryption algorithm that uses a pair of keys (public key and private key) for encryption and decryption. It is commonly used for secure communication and digital signatures.

**(iv) Diffie-Hellman – Key Exchange Algorithm**

Diffie-Hellman is a key exchange algorithm that allows two parties to securely establish a shared secret key over an insecure communication channel. The shared key is then used for symmetric encryption.

**(i) MD5 – Hashing Algorithm**

MD5 (Message Digest 5) হলো একটি cryptographic hash function যা যেকোনো দৈর্ঘ্যের input থেকে নির্দিষ্ট দৈর্ঘ্যের hash value তৈরি করে। এটি মূলত data integrity যাচাই করার জন্য ব্যবহৃত হয়।

**(ii) AES – Symmetric Encryption Algorithm**

AES (Advanced Encryption Standard) হলো একটি symmetric encryption algorithm যেখানে একই secret key ব্যবহার করে encryption ও decryption করা হয়। এটি data confidentiality নিশ্চিত করে।

**(iii) RSA – Asymmetric Encryption Algorithm**

RSA (Rivest–Shamir–Adleman) হলো একটি asymmetric encryption algorithm যা public key ও private key ব্যবহার করে data encrypt ও decrypt করে। এটি secure communication ও digital signature-এর জন্য ব্যবহৃত হয়।

**(iv) Diffie-Hellman – Key Exchange Algorithm**

Diffie-Hellman হলো একটি key exchange algorithm যা দুই পক্ষকে অনিরাপদ যোগাযোগ চ্যানেলের মাধ্যমে একটি shared secret key স্থাপন করতে সাহায্য করে। পরে এই key symmetric encryption-এ ব্যবহার করা হয়।

5. What are BFS and DFS for Binary Tree?


**Breadth First Traversal: 1 2 3 4 5 or 1 2 3 5 4 or 1 3 2 4 5 or 1 3 2 5 4**

**Depth First Traversals:**  **1 2 4 5 3**



6. Push(200), Push(500), Push(100), S= Pop(). What is the value of S after the Operation?

**Given the operations:**

Push(200), Push(500), Push(100), S = Pop();

The sequence of operations is as follows:

- **Push(200)** : Adds 200 to the stack.
- **Push(500)** : Adds 500 to the stack.
- **Push(100)** : Adds 100 to the stack.
- **Pop()** : Removes the topmost element (100) from the stack and assigns it to  **S** .

The value of S after the operation is: 100

7. Explain following program while part in step for the input 1221 and 3456 and also write the output of the program. (সম্পূর্ণ প্রশ্ন সংগ্রহ করা সম্ভব হয়নি)

1
