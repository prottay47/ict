# Combined Bank, Senior Officer (IT), 2022

- **Original URL:** [https://it.jobqns.com/combined-bank-senior-officer-it-2022-2/](https://it.jobqns.com/combined-bank-senior-officer-it-2022-2/)
- **Date:** 2026-02-05T23:04:57
- **Categories:** Bank IT Job Solution, Bank IT Job Solution 2022, Job Solution 2022

---

Senior Officer (IT) • Year 2022

Combined Bank

💼Post Name: Senior Officer (IT)

📅Exam Date: 31-Jan-2022

- ☆

1

Structure Query Language

What happened after executing the following SQL Statement: CREATE TABLE t (Val INT); INSERT INTO t(val) VALUES (1,2,2,3, "null", "null",4,5); SELECT COUNT (val) FROM t; SELECT COUNT DISTICT (val) FROM t;

**CREATE TABLE** : A table
```
t
```
is created with one column
```
val
```
of type
```
INTEGER
```
.
**INSERT INTO** : The values
```
1, 2, 2, 3, NULL, NULL, 4, 5
```
are inserted into the column
```
val
```
.
**SELECT COUNT(val)** : This query counts all non-NULL values in the
```
val
```
column.
Total non-NULL values:
```
1, 2, 2, 3, 4, 5
```

**Result: 6**
**SELECT COUNT(DISTINCT val)** : This query counts only the unique non-NULL values in the
```
val
```
column.
Unique values:
```
1, 2, 3, 4, 5
```

**Result: 5**


☆

2

Programming Concept

Write a recursive function that returns a boolean after taking a string as parameter to check if its a palindrome or not.

```
#include<stdio.h>
using namespace std;

// Recursive function to check if a string is a palindrome
bool isPalindrome(string str, int start, int end) {
// Base case: If the start index is greater than or equal to the end index
if (start >= end) {
return true;
}
// Check if the first and last characters are the same
if (str[start] != str[end]) {
return false;
}
// Recursive case: Check the substring excluding the first and last characters
return isPalindrome(str, start + 1, end - 1);
}

int main() {
string input;
cout << "Enter a string: "; cin >> input;

if (isPalindrome(input, 0, input.length() - 1)) {
cout << input << " is a palindrome." << endl;
} else {
cout << input << " is not a palindrome." << endl;
}

return 0;
}
```

```
Sample I/O:Enter a string: noonnoon is a palindrome.=== Code Execution Successful ===
```

🔗 Run Online: Check Palindrome


☆

3

Microprocessor & Computer Architecture

Consider a disk with a sector size of 512 bytes, 2000 tracks pér surface, 50 sectors per track, five double-sided platters, and average seek time of 10 msec. What is the capacity of a track in bytes? What is the capacity of each surface? What is the capacity of the disk?

**Capacity of a Track**
Bytes per Track = Bytes per Sector × Sectors per Track
Bytes per Track = 512 × 50 = 25,600 bytes
**Capacity of a Surface**
Bytes per Surface = Bytes per Track × Tracks per Surface
Bytes per Surface = 25,600 × 2000 = 51,200,000 bytes (50,000 KB)
**Capacity of the Disk**
Bytes per Disk = Bytes per Surface × Number of Surfaces
Number of Surfaces = 5 Platters × 2 Surfaces per Platter = 10 Surfaces
Bytes per Disk = 51,200,000 × 10 = 512,000,000 bytes (500,000 KB)


☆

4

Data Communication

A telephone line normally has a bandwidth of 3000 Hz (300 to 3300 Hz) assigned for data communications. The signal-to-noise ratio is usually 3162. calculate the capacity For this channel ?

C = B log2(1 + SNR)
= 3000 log2(1 + 3162)
= 3000 log2(3163)
= 3000 × 11.62
= 34,860 bps


☆

5

Theory of Computation

Construct a DFA of the following language. (W⊂ (a, b)* | every a in W is followed by at least two b's}




☆

6

Web Technology

Web-caching, is it available for every user request? Why or why not?

**Web Caching**
**Web caching**  is a technique where frequently accessed web content (such as web pages, images, or files) is stored temporarily in a cache to reduce server load and improve response time.
**Is web caching available for every user request?**
**No, web caching is not available for every user request.**
**Reasons:**

**First-time Requests:**  If a user requests a resource for the first time, it is not available in the cache and must be fetched from the original server.
**Dynamic Content:**  Pages that change frequently (such as personalized dashboards or live data) are usually not cached.
**Cache Expiration:**  Cached content may expire after a certain time (TTL), requiring a fresh copy from the server.
**Cache-Control Rules:**  Some servers specify that certain content should not be cached for security or accuracy reasons.

**Conclusion:**  Web caching improves performance, but it is applied only when cached content is valid and available.


**Web Caching**
**Web caching**  হলো এমন একটি technique যেখানে প্রায়ই ব্যবহৃত web content (যেমন web page, image, file) সাময়িকভাবে cache-এ সংরক্ষণ করা হয় যাতে response time কমে এবং server load হ্রাস পায়।
**সব user request-এর জন্য কি web caching পাওয়া যায়?**
**না, সব user request-এর জন্য web caching পাওয়া যায় না।**
**কারণসমূহ:**

**First-time Request:**  কোনো resource প্রথমবার request করা হলে তা cache-এ থাকে না এবং original server থেকে আনতে হয়।
**Dynamic Content:**  যেসব page বারবার পরিবর্তিত হয় বা user-specific data দেখায় সেগুলো সাধারণত cache করা হয় না।
**Cache Expiration:**  Cache করা data নির্দিষ্ট সময় পরে expire হয়ে যায়, ফলে নতুন করে server থেকে আনতে হয়।
**Cache-Control Rules:**  Security বা accuracy-এর কারণে কিছু content cache করার অনুমতি দেওয়া হয় না।

**উপসংহার:**  Web caching performance বাড়ায়, কিন্তু এটি শুধুমাত্র তখনই কাজ করে যখন valid cached content পাওয়া যায়।


☆

7

Computer Network

How stop and wait ARQ is used for reliable data transfer?

**ARQ (Automatic Repeat reQuest)**
**ARQ**  is an error control technique used in data communication to ensure reliable data transmission. It detects errors in transmitted frames and automatically requests retransmission of incorrect or lost data.
**Working Principle:**

The sender transmits a data frame to the receiver.
The receiver checks the frame for errors using error-detection techniques.
If the frame is correct, the receiver sends an  **ACK (Acknowledgement)** .
If the frame is incorrect or lost, the receiver sends a  **NACK**  or no response.
The sender retransmits the frame when required.

**Types of ARQ:**

**Stop-and-Wait ARQ**
**Go-Back-N ARQ**
**Selective Repeat ARQ**



**ARQ (Automatic Repeat reQuest)**
**ARQ**  হলো একটি error control technique যা data communication-এ reliable transmission নিশ্চিত করতে ব্যবহৃত হয়। এটি transmission-এর সময় error সনাক্ত করে এবং ভুল বা হারানো data পুনরায় পাঠানোর অনুরোধ করে।
**Working Principle:**

Sender receiver-এর কাছে data frame পাঠায়।
Receiver error-detection technique ব্যবহার করে frame যাচাই করে।
Frame সঠিক হলে  **ACK**  পাঠানো হয়।
Frame ভুল হলে বা না পেলে  **NACK**  বা কোনো response পাঠানো হয় না।
Sender প্রয়োজন অনুযায়ী frame পুনরায় পাঠায়।

**ARQ-এর প্রকারভেদ:**

**Stop-and-Wait ARQ**
**Go-Back-N ARQ**
**Selective Repeat ARQ**



☆

8

Data Structure

Pre-order and Post-order are given bellow, draw the graph. Pre-order: a, b, e, j, k, n, o, p ,f, c, d, g ,l, m ,h,i;  Post-order: j, n, o, p, k, é, f, b, c, l, m, g, h, i, d, a;

- ☆

9

Database Management System
ER Diagram

ER diagram from the given infos.

- ☆

10

Computer Network
Subnetting

Using this IP 172.16.16.137/22 find the answer of the following question.  i. Subnet Mask  ii. Block Size.  iii. Network Address  iv. Broadcast Address  v. Total valid Host.

**Subnet Mask** :
```
/22
```
corresponds to the subnet mask
```
255.255.252.0
```
.
**Block Size** : 2^(32−22)=2^10=1024.
**Network Address** :
```
172.16.16.0/22
```
.
**Broadcast Address** :
```
172.16.19.255/22
```
.
**Total Valid Hosts** : 2^(32−22)−2=1024−2=1022

Explanation:
**Given IP Address:**  172.16.16.137/22
**Step 1: /22 বোঝা**
/22 মানে Network bits = 22
Host bits = 32 − 22 =  **10 bits**
**Step 2: Subnet Mask লেখা**
/22 এর Binary Subnet Mask:
11111111.11111111.11111100.00000000
Decimal Subnet Mask =  **255.255.252.0**
**Step 3: IP Address কে Binary তে রূপান্তর**
172 = 10101100
16 = 00010000
16 = 00010000
137 = 10001001
IP (Binary):
10101100.00010000.00010000.10001001
**Step 4: AND Operation (Network Address)**
IP Address AND Subnet Mask করা হয়।
যেখানে Subnet Mask = 0 → Host bits 0 হয়ে যায়。

```
IP:     10101100.00010000.00010000.10001001Mask:   11111111.11111111.11111100.00000000------------------------------------------------Result: 10101100.00010000.00010000.00000000
```

Binary Result কে Decimal এ রূপান্তর করলে:
**Network Address = 172.16.16.0**
**Step 5: Broadcast Address বের করা**
Broadcast address পেতে সব Host bits = 1 করা হয়。

```
Network (Binary):10101100.00010000.00010000.00000000Host bits (10 bits) = 1111111111Broadcast (Binary):10101100.00010000.00010011.11111111
```

Binary থেকে Decimal করলে:
**Broadcast Address = 172.16.19.255**
**Step 6: Valid Host Range**
First Host = Network + 1 →  **172.16.16.1**
Last Host = Broadcast − 1 →  **172.16.19.254**
**Step 7: Total Valid Hosts**
Host bits = 10
Total = 210 = 1024
Valid Hosts = 1024 − 2 =  **1022**

- ☆

11

Computer Security
Different Attack

Explain the problems with possible solutions- Session hijacking and SQL injection.

**1. Session Hijacking**
**Problem:**  Session hijacking is an attack where an attacker steals a valid user session ID to gain unauthorized access to a web application. This can occur through packet sniffing, XSS attacks, or insecure cookies.
**Possible Solutions:**

Use HTTPS to encrypt data transmission.
Implement secure and HttpOnly cookies.
Regenerate session IDs after login.
Set proper session timeout.

**2. SQL Injection**
**Problem:**  SQL injection occurs when an attacker inserts malicious SQL queries through input fields, allowing unauthorized access to the database or manipulation of data.
**Possible Solutions:**

Use prepared statements and parameterized queries.
Validate and sanitize user inputs.
Apply least privilege principle for database users.
Use Web Application Firewalls (WAF).



**1. Session Hijacking**
**Problem:**  Session hijacking হলো এমন একটি attack যেখানে attacker বৈধ user-এর session ID চুরি করে unauthorized access লাভ করে। এটি packet sniffing, XSS attack বা insecure cookie-এর মাধ্যমে ঘটতে পারে।
**Possible Solutions:**

HTTPS ব্যবহার করে data encrypt করা।
Secure এবং HttpOnly cookie ব্যবহার করা।
Login-এর পর session ID regenerate করা।
Proper session timeout সেট করা।

**2. SQL Injection**
**Problem:**  SQL injection তখন ঘটে যখন attacker input field-এর মাধ্যমে malicious SQL query প্রবেশ করিয়ে database থেকে unauthorized data access বা manipulation করে।
**Possible Solutions:**

Prepared statement এবং parameterized query ব্যবহার করা।
User input validate ও sanitize করা।
Database user-এর জন্য least privilege প্রয়োগ করা।
Web Application Firewall (WAF) ব্যবহার করা।

- ☆

12

Digital Logic Design
Kmap

Solve the following function using K-map. F (w, x, y, z)=  ∑(0,4,5,6,12,14,15)

- ☆

13

Web Technology
HTTP

How HTTP works? How many HTTP requests would be needed for a given situation?

**How HTTP Works**
**HTTP (HyperText Transfer Protocol)**  is a request–response protocol used for communication between a web client (browser) and a web server.

The client sends an  **HTTP request**  (e.g., GET, POST) to the server.
The server processes the request.
The server sends back an  **HTTP response**  containing status code and data.
The browser renders the received content.

**How many HTTP requests are needed?**
The number of HTTP requests depends on the number of resources a webpage contains.

1 request for the main HTML page.
Each embedded resource (image, CSS, JS, video) needs a separate request.

**Example:**
If a webpage contains:

1 HTML file
2 images
1 CSS file
1 JavaScript file

**Total HTTP requests = 5**


**HTTP কীভাবে কাজ করে**
**HTTP (HyperText Transfer Protocol)**  হলো একটি request–response protocol যা web client (browser) এবং web server-এর মধ্যে communication নিশ্চিত করে।

Client server-এর কাছে একটি  **HTTP request**  পাঠায়।
Server request process করে।
Server একটি  **HTTP response**  পাঠায়।
Browser সেই data প্রদর্শন করে।

**কতটি HTTP request প্রয়োজন?**
HTTP request-এর সংখ্যা নির্ভর করে webpage-এ থাকা resource-এর উপর।

Main HTML page-এর জন্য ১টি request।
প্রতিটি image, CSS, JavaScript file-এর জন্য আলাদা request।

**উদাহরণ:**
একটি webpage-এ যদি থাকে:

1টি HTML file
2টি image
1টি CSS file
1টি JavaScript file

**মোট HTTP request = 5**

- ☆

14

Design Analysis of Algorithm
Complexity

Determine the time complexity of a given function (nested loop). Slow_solution(n){ result = 0; for i in to (n){ for j in to (i+ 1){ result +=1;) return result;}

**Given Function:**

```
Slow_solution(n){
result = 0;
for i = 1 to n{
for j = 1 to (i + 1){
result += 1;
}
}
return result;
}
```

**Step-by-step Time Complexity Analysis:**

The outer loop runs from  **i = 1**  to  **n** , so it executes  **n**  times.
The inner loop runs from  **j = 1**  to  **(i + 1)** .
For each value of  **i** , the inner loop runs approximately  **i**  times.

**Total number of operations:**
1 + 2 + 3 + ... + n = n(n + 1)/2
This is a quadratic expression.
**Final Time Complexity:**
**O(n²)**


**প্রদত্ত Function:**

```
Slow_solution(n){
result = 0;
for i = 1 to n{
for j = 1 to (i + 1){
result += 1;
}
}
return result;
}
```

**Step-by-step Time Complexity বিশ্লেষণ:**

Outer loop  **i = 1**  থেকে  **n**  পর্যন্ত চলে, অর্থাৎ মোট  **n**  বার execute হয়।
Inner loop  **j = 1**  থেকে  **(i + 1)**  পর্যন্ত চলে।
প্রতিটি  **i**  মানের জন্য inner loop প্রায়  **i**  বার চলে।

**মোট operation সংখ্যা:**
1 + 2 + 3 + ... + n = n(n + 1)/2
এটি একটি quadratic expression।
**Final Time Complexity:**
**O(n²)**

- ☆

15

Non Technical Question
Non Tech

**সামগ্রিক প্রবৃদ্ধিতে বহুমুখি অর্থনীতির ভুমিকা।**
**Bangladesh and UN Peace-keeping**
**B2E Translation**
**E2B Translation**
**GK**

When Bangabandhu satellite was launch?
Location of Niagara Falls
Golden crescent countries.
One city two towns in BD.
Ibn Battuta was from which country.
