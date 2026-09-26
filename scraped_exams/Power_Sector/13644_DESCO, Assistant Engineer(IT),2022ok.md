# DESCO, Assistant Engineer(IT),2022ok

- **Original URL:** [https://it.jobqns.com/desco-assistant-engineerit2022/](https://it.jobqns.com/desco-assistant-engineerit2022/)
- **Date:** 2026-03-07T16:59:43
- **Categories:** Job Solution 2022, Power Sector IT Job Solution, Power Sector IT Job Solution 2022

---

#### Dhaka Electric Supply Company Limited (DESCO)
Post: Assistant Engineer(IT)  Exam Date: 10.09.2022, Exam Taker: MIST



1. What is the output of this program?
int main() {
int a=10, b=25;
a=b++ + ++a;
b=++b + ++a;
printf("%d, %d\n",a,b);
return 0;
}

**Step 1:**
```
a = b++ + ++a
```

- ```
b++
```
→ The value of
```
b
```
(25) is used, and then
```
b
```
is incremented to 26.
- ```
++a
```
→
```
a
```
is incremented to 11 before being used.
- So,
```
a = b++ + ++a
```
becomes:
```
a = 25 + 11 = 36
```
- Now:
```
a = 36
```
,
```
b = 26
```

**Step 2:**
```
b = ++b + ++a
```

- ```
++b
```
→
```
b
```
is incremented to 27 before being used.
- ```
++a
```
→
```
a
```
is incremented to 37 before being used.
- So,
```
b = ++b + ++a
```
becomes:
```
b = 27 + 37 = 64
```
- Now:
```
a = 37
```
,
```
b = 64
```

2.	What is the range of IP addresses of class A, B, and C?

**Class A:**

- **Range:**  0.0.0.0 to 127.255.255.255
- **Default Subnet Mask:**  255.0.0.0

**Class B:**

- **Range:**  128.0.0.0 to 191.255.255.255
- **Default Subnet Mask:**  255.255.0.0

**Class C:**

- **Range:**  192.0.0.0 to 223.255.255.255
- **Default Subnet Mask:**  255.255.255.0

3.	What is cyberspace? Find out some threats of cyberspace.

**Definition of cyberspace:**  Cyberspace is defined as a virtual and dynamic environment comprised of electronic and communication devices over various networks to store and utilize electronic data. It functions similarly to the structure of the human brain, consisting of numerous networks and connections to share information globally.

**Threats of cyberspace:**

- Ransomware
- Phishing
- Data leakage
- Hacking
- Insider threats

4. What is the OSI model? Write the different layers of the OSI model. What is the difference between the DoD and OSI models?

The  **OSI (Open Systems Interconnection) model**  is a conceptual framework developed by  **ISO**  to standardize communication between different computer systems.

**Layers of OSI Model**

- **Physical Layer:**  Deals with physical connection like cables and hardware.
- **Data Link Layer:**  Ensures error-free data transfer between devices.
- **Network Layer:**  Handles routing and IP addressing.
- **Transport Layer:**  Provides reliable data transfer (e.g., TCP/UDP).
- **Session Layer:**  Manages communication sessions between devices.
- **Presentation Layer:**  Handles data formatting and encryption.
- **Application Layer:**  Provides services to end users (e.g., HTTP, FTP).

**Difference between OSI Model and DoD Model**

- **Number of Layers:**  OSI has 7 layers; DoD (TCP/IP) has 4 layers.
- **Concept vs Implementation:**  OSI is a conceptual model; DoD is a practical implementation.
- **Complexity:**  OSI is more complex; DoD is simpler.
- **Usage:**  DoD is widely used in real-world networks; OSI is mainly used as a reference model.

**OSI (Open Systems Interconnection) model**  হলো একটি conceptual framework যা  **ISO**  তৈরি করেছে বিভিন্ন computer system-এর মধ্যে communication standardize করার জন্য।

**OSI Model-এর Layerসমূহ**

- **Physical Layer:**  Physical connection যেমন cable এবং hardware নিয়ে কাজ করে।
- **Data Link Layer:**  Device-এর মধ্যে error-free data transfer নিশ্চিত করে।
- **Network Layer:**  Routing এবং IP addressing পরিচালনা করে।
- **Transport Layer:**  Reliable data transfer নিশ্চিত করে (যেমন TCP/UDP)।
- **Session Layer:**  Device-এর মধ্যে communication session পরিচালনা করে।
- **Presentation Layer:**  Data formatting এবং encryption পরিচালনা করে।
- **Application Layer:**  User এবং application-এর জন্য service প্রদান করে (যেমন HTTP, FTP)।

**OSI Model এবং DoD Model-এর পার্থক্য**

- **Number of Layers:**  OSI-তে 7টি layer আছে; DoD (TCP/IP)-তে 4টি layer আছে।
- **Concept vs Implementation:**  OSI একটি conceptual model; DoD একটি practical implementation।
- **Complexity:**  OSI বেশি complex; DoD তুলনামূলক সহজ।
- **Usage:**  DoD বাস্তব network-এ বেশি ব্যবহৃত হয়; OSI মূলত reference model হিসেবে ব্যবহৃত হয়।

5.	Write down the output of this program.
int main() {
int a = 2, b = 5, c;
c = a++ + b;
printf("%d, %d, %d", a, b, c);
return 0;
}
- ```
a++
```
: The value of
```
a
```
(2) is used first, then incremented to 3.
- ```
c = a++ + b
```
:
```
c = 2 + 5 = 7
```
.
- Final values:
```
a = 3
```
(incremented after the operation)
```
b = 5
```
(unchanged)
```
c = 7
```
.

**Output:**
```
3, 5, 7
```

6. What is the difference between hashing and encryption?

7.  What is a spanning tree? Find the minimum spanning tree from the given graph.
A  **spanning tree**  is a subgraph of a graph that connects all the vertices together without forming any cycles and with the minimum possible total edge weight.

**Properties of Spanning Tree**

- **No Cycles:**  A spanning tree does not contain any cycles.
- **Number of Edges:**  A spanning tree has  **N − 1 edges** , where N is the number of vertices.
- **Minimum Weight:**  The total weight of all edges is minimized in a spanning tree.

**Spanning tree**  হলো একটি graph-এর subgraph যা সবগুলো vertex-কে সংযুক্ত করে, কোনো cycle তৈরি করে না এবং মোট edge weight সর্বনিম্ন হয়।

**Spanning Tree-এর বৈশিষ্ট্য**

- **No Cycles:**  Spanning tree-এ কোনো cycle থাকে না।
- **Number of Edges:**  একটি spanning tree-এ  **N − 1টি edge**  থাকে, যেখানে N হলো vertex-এর সংখ্যা।
- **Minimum Weight:**  সব edge-এর মোট weight সর্বনিম্ন হয়।

```

```

**Total weight of the minimum spanning tree:**
```
410 + 612 + 310 + 200 = 1532
```

8. What is a subnet mask? For address 192.168.0.0/29, what is the first IP and last IP address of the 10th and 22nd subnet networks?

A  **subnet mask**  is a  **32-bit address**  used in networking to separate the  **network portion**  and the  **host portion**  of an IP address.

- **Function:**  It identifies which part of an IP address belongs to the network and which part belongs to the host.
- **Structure:**  It consists of 32 bits, just like an IP address.
- **Usage:**  It is used to divide networks into smaller sub-networks (subnets).

**Subnet mask**  হলো একটি  **32-bit address**  যা networking-এ IP address-এর  **network অংশ**  এবং  **host অংশ**  আলাদা করতে ব্যবহৃত হয়।

- **Function:**  এটি নির্ধারণ করে IP address-এর কোন অংশ network এবং কোন অংশ host নির্দেশ করে।
- **Structure:**  এটি 32-bit নিয়ে গঠিত, ঠিক IP address-এর মতো।
- **Usage:**  এটি network-কে ছোট ছোট subnet-এ ভাগ করতে ব্যবহৃত হয়।

**Given IP Address:**
```
192.168.0.0/29
```

- Subnet Mask:
```
255.255.255.248
```
- Block Size:
```
256 - 248 = 8
```
- Total Valid Hosts:
```
2^3 - 2 = 6
```

**Details of Subnets:**

- **1st Subnet/Network:** Subnet/Network =
```
192.168.0.0
```
First Valid IP =
```
192.168.0.1
```
Last Valid IP =
```
192.168.0.6
```
Broadcast IP =
```
192.168.0.7
```
- **10th Subnet/Network:** Subnet/Network =
```
192.168.0.72
```
First Valid IP =
```
192.168.0.73
```
Last Valid IP =
```
192.168.0.78
```
Broadcast IP =
```
192.168.0.79
```
- **22nd Subnet/Network:** Subnet/Network =
```
192.168.0.168
```
First Valid IP =
```
192.168.0.169
```
Last Valid IP =
```
192.168.0.174
```
Broadcast IP =
```
192.168.0.175
```

9.  Convert decimal (1741) to hexadecimal.

**Division Steps:**

- ```
1741 ÷ 16 = 108
```
remainder
```
13
```
→ Digit =
```
D
```
- ```
108 ÷ 16 = 6
```
remainder
```
12
```
→ Digit =
```
C
```
- ```
6 ÷ 16 = 0
```
remainder
```
6
```
→ Digit =
```
6
```

**Combine Digits in Reverse Order:**

- Hexadecimal Value =
```
6CD
```


Non Department – 60 Marks

- **Bangla:**  সমার্থক শব্দ, এক কথায় প্রকাশ, শব্দের অর্থ, সারাংশ।
- **English:**  Translation, Paragraph.
- **General Knowledge (20)**
- **Analytical Ability(20)**
- **Desco/ power sector related(10)**
