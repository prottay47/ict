# M2: Computer Network (Previous Job Questions)

- **Original URL:** [https://it.jobqns.com/m2-computer-network-previous-job-questions/](https://it.jobqns.com/m2-computer-network-previous-job-questions/)
- **Date:** 2026-08-30T10:52:14
- **Categories:** Uncategorized, IT Preparation Module

---

**Computer Network**  Previous Job Question and Solution

Topic Wise Question Bank

Computer Network

- ☆

1

Computer Network
Subnetting

An organization has been assigned the IPv4 network address 192.168.1.0/24. As part of the network deployment, the network administrator is required to divide the address space into four equal-sized subnets to support different departments. Determine the Network Address, Subnet Mask (both CIDR and dotted-decimal notation)

CB, O(IT-24), 26
| Officer (IT)

**Subnetting of 192.168.1.0/24 into Four Equal-Sized Subnets**

To divide the network  **192.168.1.0/24**  into  **4 equal-sized subnets** :

• Original Prefix =  **/24**
• Number of Required Subnets =  **4 = 2²**
• Borrowed Bits =  **2**
• New Prefix =  **/26**
• Subnet Mask =  **255.255.255.192**

**Subnet Details**

Subnet
Network Address
CIDR
Subnet Mask
Broadcast Address
Usable Host Range

Subnet 1
192.168.1.0
/26
255.255.255.192
192.168.1.63
192.168.1.1 – 192.168.1.62

Subnet 2
192.168.1.64
/26
255.255.255.192
192.168.1.127
192.168.1.65 – 192.168.1.126

Subnet 3
192.168.1.128
/26
255.255.255.192
192.168.1.191
192.168.1.129 – 192.168.1.190

Subnet 4
192.168.1.192
/26
255.255.255.192
192.168.1.255
192.168.1.193 – 192.168.1.254

**Final Answer**

Network Addresses:  **192.168.1.0** ,  **192.168.1.64** ,  **192.168.1.128** ,  **192.168.1.192**
Subnet Mask (CIDR):  **/26**
Subnet Mask (Dotted Decimal):  **255.255.255.192**



☆

2

Computer Network
Subnetting

Using this IP 172.16.16.137/22 find the answer of the following question.  i. Subnet Mask  ii. Block Size.  iii. Network Address  iv. Broadcast Address  v. Total valid Host.

CB, SO(IT), 22
| Senior Officer (IT)

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


☆

3

Computer Network
Subnetting

A company named ICB has been allotted the IP address 192.198.10.0/22. Using subnetting, allocate subnets for Finance, Admin, IT, Loan, and HR requiring 250, 125, 120, 250, and 60 hosts respectively. Find the subnet mask, valid host addresses, and network address for each subnet.

ICB, AP, 26
| Assistant Programmer

The given network is 192.198.10.0/22, which provides 1024 IP addresses (from 192.198.8.0 to 192.198.11.255). VLSM is used to allocate different subnet sizes based on host requirements. **Step 1: Sort requirements (descending)** 250, 250, 125, 120, 60 hosts **Step 2: Required subnet sizes** 250 hosts → /24 (256 addresses)250 hosts → /24125 hosts → /25 (128 addresses)120 hosts → /2560 hosts → /26 (64 addresses) **Step 3: Subnet allocation**  **Finance:**  192.198.8.0/24Mask: 255.255.255.0Valid hosts: 192.198.8.1 – 192.198.8.254 **Loan:**  192.198.9.0/24Mask: 255.255.255.0Valid hosts: 192.198.9.1 – 192.198.9.254 **Admin:**  192.198.10.0/25Mask: 255.255.255.128Valid hosts: 192.198.10.1 – 192.198.10.126 **IT:**  192.198.10.128/25Mask: 255.255.255.128Valid hosts: 192.198.10.129 – 192.198.10.254 **HR:**  192.198.11.0/26Mask: 255.255.255.192Valid hosts: 192.198.11.1 – 192.198.11.62 **Conclusion:**  VLSM minimizes wastage by allocating IPs according to requirement.

☆

4

Computer Network
Subnetting

An organization is granted the IPv4 network block 14.24.74.0/24 and needs to
segment it into two subnets: Subnet A (requires 120 addresses) and Subnet B (requires 60 addresses). Allocating sequentially from the requirement first to maximize remaining address space, state only the Network Address (with its CIDR mask) and the Broadcast Address for both subnets.

Combined Bank, SO(IT-24), 26
| Senior Officer (IT)

**Given:**

Network Block =  **14.24.74.0/24**
Subnet A requires =  **120 addresses**
Subnet B requires =  **60 addresses**

Allocate the largest subnet first.

**Subnet A**

Required Addresses = 120
Allocated Block Size = 128 addresses
CIDR Mask =  **/25**

Item
Value

Network Address
14.24.74.0/25

Broadcast Address
14.24.74.127

**Subnet B**

Required Addresses = 60
Allocated Block Size = 64 addresses
CIDR Mask =  **/26**

Item
Value

Network Address
14.24.74.128/26

Broadcast Address
14.24.74.191

**Final Answer**

Subnet
Network Address
Broadcast Address

Subnet A
14.24.74.0/25
14.24.74.127

Subnet B
14.24.74.128/26
14.24.74.191



☆

5

Computer Network
Subnetting

Differentiate between IPv4 and IPv6. Given the IP address 192.168.10.0/24, calculate. Number of subnets if borrowed bits = 3 and hosts per subnet.

Combined Bank, AE(IT)/AME, 26
| AME/ANE/AE

**Subnet Calculation:**  Given IP: 192.168.10.0/24
Borrowed bits = 3

**Number of Subnets = 2³ = 8**
**New subnet mask = /24 + 3 = /27**
**Host bits = 32 - 27 = 5**
**Hosts per subnet = 2⁵ - 2 = 32 - 2 = 30**

**Final Answer:**

Subnets =  **8**
Hosts per subnet =  **30**
**Total Time in a Month**

30 days = 30 × 24 =  **720 hours**
Downtime =  **4 hours**

**Availability Calculation**

Availability = [(Total Time − Downtime) / Total Time] × 100
= [(720 − 4) / 720] × 100
= (716 / 720) × 100 ≈  **99.44%**

**Revenue Loss**

Transactions per hour = 500
Fee per transaction = 0.50 Tk
Loss per hour = 500 × 0.50 =  **250 Tk**
Total loss = 250 × 4 =  **1000 Tk**


**Subnet Calculation:**  Given IP: 192.168.10.0/24
Borrowed bits = 3

**Number of Subnets = 2³ = 8**
**New subnet mask = /24 + 3 = /27**
**Host bits = 32 - 27 = 5**
**Hosts per subnet = 2⁵ - 2 = 32 - 2 = 30**

**Final Answer:**

Subnets =  **8**
Hosts per subnet =  **30**


☆

6

Computer Network
Subnetting

A Classless IP Address is: 105.38.89.230/20. Find out the answer of the following question.(i) What is Net id and Host id?(ii) What is network address and broadcast address?(ii) What is network size?(iv) If this classless IP address is used to classfull IP address what will be the class?

CB, AE(IT)/AHME/SO, 21
| AME/ANE/AE

**(i) Net ID and Host ID:**
The CIDR notation /20 means the first 20 bits are for the Net ID and the remaining 12 bits are for the Host ID.
**Net ID (first 20 bits):**  105.38.80.0/20
**Host ID**  (remaining 12 bits) represents the specific host in the network.
**(ii) Network Address and Broadcast Address:**
**Network Address:**  Set all host bits to 0.
=>105.38.80.0 (first 20 bits).
**Broadcast Address:**  Set all host bits to 1.
=>105.38.95.255 (last 12 bits as 1).
**(iii) Network Size:**
12 host bits: 2^12 = 4096 total addresses.
Usable addresses: 4096 - 2 = 4094 (since network and broadcast are reserved).
**(iv) Classful IP Address:**
The first octet 105 in binary is 01101001, which starts with 0.
This indicates the address is Class A (1.0.0.0 to 127.255.255.255).


☆

7

Computer Network
Subnetting

What is the primary motivation for transitioning from classful IP addressing to classless IP addressing?

Sonali Bank, ADA, 24
| ADA

The primary motivation for moving from  **classful IP addressing**  to  **classless IP addressing (CIDR)**  was to use IP addresses more efficiently

**Address Wastage:**  Classful addressing allocated fixed-size blocks, leading to large wastage of IP addresses.
**Flexibility:**  CIDR allows flexible allocation of IP addresses based on actual need.
**Routing Efficiency:**  CIDR reduces the size of routing tables by using route aggregation.
**Scalability:**  Helps support the rapid growth of the internet.
**Better Utilization:**  Ensures optimal use of available IP address space.

**Classful IP addressing**  থেকে  **CIDR (classless)** -এ যাওয়ার মূল উদ্দেশ্য ছিল IP address-এর সঠিক ও efficient ব্যবহার নিশ্চিত করা

**Address Wastage:**  Classful পদ্ধতিতে fixed block দেওয়ায় অনেক IP address অপচয় হতো।
**Flexibility:**  CIDR প্রয়োজন অনুযায়ী IP address বরাদ্দ করতে দেয়।
**Routing Efficiency:**  Route aggregation-এর মাধ্যমে routing table ছোট হয়।
**Scalability:**  Internet দ্রুত বড় হওয়ার সাথে মানিয়ে নিতে সাহায্য করে।
**Better Utilization:**  IP address-এর সর্বোত্তম ব্যবহার নিশ্চিত করে।

☆

8

Computer Network
Subnetting

A bank has the network block 192.168.10.0/24. The IT manager wants to divide this into 4 equal subnets.(a) How many bits do you need to borrow to make 4 subnets?(b) What is the new Subnet Mask in dotted-decimal format?(c) Write down the Network Address, the First Usable IP, and the Broadcast Address for the second subnet created. Show your calculation.

Combined Bank, SO(IT-23), 26
| Senior Officer (IT)

**(a) Number of bits to borrow**
To create 4 subnets, we use the formula: 2n = 4
So, n = 2 bits must be borrowed from the host part.
**(b) New Subnet Mask**
Original network: /24
Borrowed bits: 2
New prefix: /26
Subnet mask = 255.255.255.192
**(c) Second Subnet Details**
Block size = 256 - 192 = 64
Subnets are:
1st: 192.168.10.0 - 192.168.10.63
2nd: 192.168.10.64 - 192.168.10.127
So for the second subnet:
Network Address: 192.168.10.64
First Usable IP: 192.168.10.65
Broadcast Address: 192.168.10.127

☆

9

Computer Network
Subnetting

Consider the IP address 10.20.30.0/25 now answer the below question: a. What is the subnet mask of the above IP address? b. How many host per subnet have? c. What is the Broadcast address of this 10.20.30.0/3 IP address?

Janata, ASA, 21
| AME/ANE/AE

**Given:**
IP Address = 10.20.30.0/25
**a) Subnet Mask**
A  **/25**  prefix means 25 bits are used for the network.
Subnet Mask =  **255.255.255.128**
Binary form:
11111111.11111111.11111111.10000000
**b) Number of hosts per subnet**
Host bits = 32 − 25 =  **7 bits**
Total IP addresses per subnet = 27 =  **128**
Usable hosts = 128 − 2 =  **126 hosts**
(2 addresses are reserved for network and broadcast)
**c) Broadcast address**
With /25, each subnet block size =  **128** .
Subnet range:
10.20.30.0 → 10.20.30.127
Network address =  **10.20.30.0**
Broadcast address =  **10.20.30.127**
Usable host range:
10.20.30.1 – 10.20.30.126
**Final Answers:**

Question
Answer

Subnet Mask
255.255.255.128

Hosts per subnet
126 usable hosts

Broadcast Address
10.20.30.127

☆

10

Computer Network
Subnetting

What is Subnet mask and Localhost IP address?

SPCBL, SAME, 22
| AME/ANE/AE

**Subnet Mask**
A  **subnet mask**  is a 32-bit number used to divide an IP address into network and host portions. It helps determine which part of the IP address identifies the network and which part identifies the device within that network.
**Example:**  255.255.255.0
**Localhost IP Address**
The  **localhost IP address**  refers to the local machine itself. It is used to test network applications on the same device.
**Localhost IPv4:**  127.0.0.1

**Subnet Mask**
**Subnet mask**  হলো একটি 32-bit number যা একটি IP address-কে network অংশ এবং host অংশে ভাগ করতে ব্যবহৃত হয়। এটি নির্ধারণ করে কোন অংশ network নির্দেশ করে এবং কোন অংশ device নির্দেশ করে।
**উদাহরণ:**  255.255.255.0
**Localhost IP Address**
**Localhost IP address**  হলো নিজের computer বা device-কে নির্দেশ করার জন্য ব্যবহৃত একটি special IP address। এটি মূলত testing-এর কাজে ব্যবহৃত হয়।
**Localhost IPv4:**  127.0.0.1


☆

11

Computer Network
Subnetting

VLSM Subnetting . Given an  IP address 172.16.0.0/20 For creating 4 subnets department of A,B,C,D with 4000,2000,6000 and 8000 hosts, find out every department first and last IP address. Also write the subnet mask of q.x.y.z/notation.

Rupali, ANE, 21
|

First, calculate the number of required bits for each subnet:

For 4000 hosts: Needs at least 12 bits for host portion (212 = 4096).
For 2000 hosts: Needs at least 11 bits for host portion (211 = 2048).
For 6000 hosts: Needs at least 13 bits for host portion (213 = 8192).
For 8000 hosts: Needs at least 13 bits for host portion (213 = 8192).

**Subnet Calculations:**
Department C (6000 hosts)
Subnet Mask:  **172.16.0.0/19**  (because 32 - 13 = 19 bits for network portion).
Subnet Range: 172.16.0.0 - 172.16.31.255
First IP: 172.16.0.1
Last IP: 172.16.31.254
Department D (8000 hosts)
Subnet Mask:  **172.16.32.0/19**  (same as above).
Subnet Range: 172.16.32.0 - 172.16.63.255
First IP: 172.16.32.1
Last IP: 172.16.63.254
Department A (4000 hosts)
Subnet Mask:  **172.16.64.0/20**  (because 32 - 12 = 20 bits for network portion).
Subnet Range: 172.16.64.0 - 172.16.79.255
First IP: 172.16.64.1
Last IP: 172.16.79.254
Department B (2000 hosts)
Subnet Mask:  **172.16.80.0/21**  (because 32 - 11 = 21 bits for network portion).
Subnet Range: 172.16.80.0 - 172.16.95.255
First IP: 172.16.80.1
Last IP: 172.16.95.254

☆

12

Computer Network
Subnetting

Subnetting logic requires precise binary calculation. A network engineer is tasked with dividing the internal network 192.168.10.0/24 into exactly 4 equal subnets for four different bank branches.Show the mathematical calculation to determine how many bits must be borrowed to create 4 subnets, and state the New Subnet Mask in Both CIDR notation and decimal format

Combined Bank, O(IT-23), 26
| Officer (IT)

**Given:**
Network Address = 192.168.10.0/24
Required Subnets = 4
**Step 1: Determine Borrowed Bits**
To create subnets, host bits are borrowed from the host portion.
Formula:
Number of subnets = 2n
Here, required subnets = 4
So,
2n = 4
22 = 4
Therefore,  **2 bits**  must be borrowed.
**Step 2: Find New CIDR Prefix**
Original prefix = /24
Borrowed bits = 2
So,
New prefix = 24 + 2 =  **/26**
**Step 3: Find New Subnet Mask**
A /26 subnet mask means first 26 bits are network bits.
Binary subnet mask:
11111111.11111111.11111111.11000000
Convert to decimal:
11111111 = 255
11111111 = 255
11111111 = 255
11000000 = 192
**Final Answer:**
Borrowed Bits = 2
New CIDR Notation = 192.168.10.0/26
New Subnet Mask = 255.255.255.192

**প্রশ্ন: 192.168.10.0/24 Network-কে 4টি Equal Subnet-এ ভাগ করে New Subnet Mask নির্ণয় কর**
**প্রদত্ত:**
Network Address = 192.168.10.0/24
Required Subnets = 4
**ধাপ ১: Borrowed Bit নির্ণয়**
Subnet তৈরি করার জন্য host portion থেকে bit borrow করা হয়।
Formula:
Number of subnets = 2n
এখানে required subnets = 4
সুতরাং,
2n = 4
22 = 4
তাই  **2 bits**  borrow করতে হবে।
**ধাপ ২: New CIDR Prefix নির্ণয়**
Original prefix = /24
Borrowed bits = 2
সুতরাং,
New prefix = 24 + 2 =  **/26**
**ধাপ ৩: New Subnet Mask নির্ণয়**
/26 subnet mask মানে প্রথম 26 bit network bit।
Binary subnet mask:
11111111.11111111.11111111.11000000
Decimal-এ রূপান্তর:
11111111 = 255
11111111 = 255
11111111 = 255
11000000 = 192
**Final Answer:**
Borrowed Bits = 2
New CIDR Notation = 192.168.10.0/26
New Subnet Mask = 255.255.255.192

☆

13

Computer Network
Subnetting

Given IP address 192.168.1.0 and divided four subnets in equal size: A) find the new subnet mask (CIDR) B) find out first usable host address of subnetting

Sonali Bank, ADA, 26
| ADA

**Given:**

IP Address = 192.168.1.0
Default mask = /24
Required subnets = 4

**A) New Subnet Mask (CIDR)**

Required subnets = 4 = 2²
So, borrowed bits = 2
New CIDR = /24 + 2 =  **/26**
Subnet Mask =  **255.255.255.192**

**B) First Usable Host Address of Each Subnet**

Subnet 1: 192.168.1.0/26 → First usable host =  **192.168.1.1**
Subnet 2: 192.168.1.64/26 → First usable host =  **192.168.1.65**
Subnet 3: 192.168.1.128/26 → First usable host =  **192.168.1.129**
Subnet 4: 192.168.1.192/26 → First usable host =  **192.168.1.193**


☆

14

Computer Network
Subnetting

An ISP has been assigned the networks 192.168.0.0/24, 192.168.1.0/24, 192.168.2.0/24, and 192.168.3.0/24. To reduce routing table entries, the network engineer decides to use CIDR-based route aggregation. Determine the supernet address and explain how supernetting improves routing efficiency.[assume]

Combined Bank, ADA-23, 26
| ADA

**Given Networks:**

192.168.0.0/24
192.168.1.0/24
192.168.2.0/24
192.168.3.0/24

**Step 1: Convert to Binary**

Network
Binary (last octet)

192.168.0.0
0000 0000

192.168.1.0
0000 0001

192.168.2.0
0000 0010

192.168.3.0
0000 0011

**Step 2: Find Common Prefix**

Looking at the last octet in binary:

0 =  **00** 00 0000
1 =  **00** 00 0001
2 =  **00** 00 0010
3 =  **00** 00 0011

The first  **22 bits**  are identical across all four networks. The last 2 bits vary (00, 01, 10, 11).

**Step 3: Determine Supernet Address**

Supernet address =  **192.168.0.0/22**
Mask: 255.255.252.0
Range: 192.168.0.0 to 192.168.3.255
Total hosts: 1024 (4 × 256)

**How Supernetting Improves Routing Efficiency**

**Reduced table size:**  Instead of 4 separate /24 entries, the router stores 1 /22 entry.

**Faster lookups:**  Smaller routing tables mean faster longest-prefix-match searches.

**Less update traffic:**  Changes in one subnet do not require re-advertising all routes.

**Hierarchical routing:**  ISPs can advertise a single aggregated route instead of multiple subnets.

**Given Networks:**

192.168.0.0/24
192.168.1.0/24
192.168.2.0/24
192.168.3.0/24

**Step 1: Binary-তে Convert করা**

Network
Binary (last octet)

192.168.0.0
0000 0000

192.168.1.0
0000 0001

192.168.2.0
0000 0010

192.168.3.0
0000 0011

**Step 2: Common Prefix খোঁজা**

Last octet binary-তে দেখলে:

0 =  **00** 00 0000
1 =  **00** 00 0001
2 =  **00** 00 0010
3 =  **00** 00 0011

চারটা network-এর প্রথম  **22 bits**  identical। শেষ 2 bits vary করে (00, 01, 10, 11)।

**Step 3: Supernet Address নির্ধারণ**

Supernet address =  **192.168.0.0/22**
Mask: 255.255.252.0
Range: 192.168.0.0 থেকে 192.168.3.255
Total hosts: 1024 (4 × 256)

**Supernetting Routing Efficiency কীভাবে Improve করে**

**Reduced table size:**  4টা আলাদা /24 entry-এর পরিবর্তে router 1টা /22 entry store করে।

**Faster lookups:**  ছোট routing tables মানে দ্রুত longest-prefix-match search।

**Less update traffic:**  এক subnet change হলেও full advertisement লাগে না।

**Hierarchical routing:**  ISP একটাই aggregated route advertise করতে পারে।

☆

15

Computer Network
Subnetting

What do you mean by Subnet and Subnet Mask? The network address 172.16.0.0/19 provides how many subnets and hosts? What is the function of OSPF?

Rupali, ANE, 23
| AME/ANE/AE

**1. Subnet and Subnet Mask**
**Subnet:**  A subnet is a smaller logical division of a large IP network created to improve network management, performance, and security.
**Subnet Mask:**  A subnet mask is a 32-bit number used to identify the network portion and the host portion of an IP address.
**2. Subnet Calculation for Network 172.16.0.0/19**
The IP address 172.16.0.0 belongs to Class B, whose default subnet mask is /16.
Given subnet mask is /19, so additional bits used for subnetting = 19 − 16 = 3 bits.
**Number of Subnets:**
Number of subnets = 2³ =  **8 subnets** .
**Number of Hosts per Subnet:**
Host bits = 32 − 19 = 13 bits.
Number of hosts per subnet = 2¹³ − 2 =  **8190 hosts** .
**3. Function of OSPF**
OSPF (Open Shortest Path First) is a link-state routing protocol used to find the shortest path for data transmission within an IP network.

Uses cost-based shortest path algorithm (Dijkstra)
Supports fast convergence
Scales well for large networks
Uses area-based routing for efficiency



☆

16

Computer Network
Subnetting

Convert the decimal IP address 192.168.101.5 into binary IP address. Fill-up the following in tabular form:

Rupali, ANE, 23
| AME/ANE/AE

Conversion of IP Address (192.168.101.5) into Binary:
Decimal IP: 192.168.101.5
Binary IP: 11000000.10101000.01100101.00000101


☆

17

Computer Network
Subnetting

Given the network 245.248.128.0/20, divide the address space among three departments as follows: (a) Manager: half of the address space (b) HR: one-quarter of the address space (c) Admin: the remaining one-quarter

Dwasa,AME,25
| Other

**Subnetting: 245.248.128.0/20**
**Given Network:**

Network Address: 245.248.128.0/20
Subnet Mask: 255.255.240.0
Total Addresses: 232-20 = 212 = 4096

The address space needs to be divided among three departments:

**Manager:**  Half of the address space = 50% = 2048 addresses
**HR:**  One-quarter of the address space = 25% = 1024 addresses
**Admin:**  Remaining one-quarter = 25% = 1024 addresses

**Step 1: Manager — Half of the Address Space**
Manager needs 2048 addresses.
2048 = 211
Therefore, the new prefix is:
32 − 11 =  **/21**

**Network:**  245.248.128.0/21
**Subnet Mask:**  255.255.248.0
**Address Range:**  245.248.128.0 – 245.248.135.255
**Usable Host Range:**  245.248.128.1 – 245.248.135.254
**Broadcast:**  245.248.135.255

**Step 2: HR — One-Quarter of the Address Space**
HR needs 1024 addresses.
1024 = 210
Therefore, the new prefix is:
32 − 10 =  **/22**

**Network:**  245.248.136.0/22
**Subnet Mask:**  255.255.252.0
**Address Range:**  245.248.136.0 – 245.248.139.255
**Usable Host Range:**  245.248.136.1 – 245.248.139.254
**Broadcast:**  245.248.139.255

**Step 3: Admin — Remaining One-Quarter**
Admin also needs 1024 addresses.
1024 = 210
Therefore, the new prefix is  **/22** .

**Network:**  245.248.140.0/22
**Subnet Mask:**  255.255.252.0
**Address Range:**  245.248.140.0 – 245.248.143.255
**Usable Host Range:**  245.248.140.1 – 245.248.143.254
**Broadcast:**  245.248.143.255

**Final Subnet Allocation:**

Department
Required Size
Network
Prefix
Address Range
Broadcast

Manager
2048
245.248.128.0
/21
245.248.128.0 – 245.248.135.255
245.248.135.255

HR
1024
245.248.136.0
/22
245.248.136.0 – 245.248.139.255
245.248.139.255

Admin
1024
245.248.140.0
/22
245.248.140.0 – 245.248.143.255
245.248.143.255

**Final Answer:**
Manager gets  **245.248.128.0/21** , HR gets  **245.248.136.0/22** , and Admin gets  **245.248.140.0/22** .

- ☆

18

Computer Network
Network Topology & Devices

Describe the functions of a Switch and a Router and explain two key differences between these networking devices.

CB, O(IT-24), 26
| Officer (IT)

**Switch and Router**
**Functions of a Switch**

A  **Switch**  is a networking device that connects multiple devices within the same  **Local Area Network (LAN)** . It forwards data frames to the correct destination using  **MAC Addresses** , improving network efficiency and reducing unnecessary traffic.

**Functions of a Router**

A  **Router**  is a networking device that connects two or more different networks, such as a  **LAN**  and the  **Internet** . It forwards data packets between networks using  **IP Addresses**  and determines the best path for packet delivery.

**Key Differences Between Switch and Router**

Switch
Router

Operates mainly at the  **Data Link Layer (Layer 2)**  of the OSI model.
Operates at the  **Network Layer (Layer 3)**  of the OSI model.

Uses  **MAC Addresses**  to forward data within the same network.
Uses  **IP Addresses**  to route packets between different networks.



**Switch এবং Router**
**Switch-এর কাজ**

**Switch**  হলো একটি Networking Device, যা একই  **Local Area Network (LAN)** -এর একাধিক Device-কে সংযুক্ত করে। এটি  **MAC Address**  ব্যবহার করে Data Frame সঠিক Device-এ পাঠায়, ফলে Network Traffic কমে এবং Communication আরও কার্যকর হয়।

**Router-এর কাজ**

**Router**  হলো একটি Networking Device, যা দুই বা ততোধিক ভিন্ন Network (যেমন  **LAN**  এবং  **Internet** ) সংযুক্ত করে। এটি  **IP Address**  ব্যবহার করে Data Packet-এর সর্বোত্তম পথ নির্ধারণ করে এবং এক Network থেকে অন্য Network-এ পাঠায়।

**Switch এবং Router-এর দুটি প্রধান পার্থক্য**

Switch
Router

**OSI Model** -এর  **Data Link Layer (Layer 2)** -এ কাজ করে।
**OSI Model** -এর  **Network Layer (Layer 3)** -এ কাজ করে।

একই Network-এর মধ্যে Data পাঠাতে  **MAC Address**  ব্যবহার করে।
ভিন্ন Network-এর মধ্যে Packet পাঠাতে  **IP Address**  ব্যবহার করে।



☆

19

Computer Network
Network Topology & Devices

Briefly describe the following network devices: Repeater, Hub, Bridge, Switch and Router.

Combined Bank, SO(IT), 24
| Senior Officer (IT)

**Repeater:**
A  **Repeater**  is a network device that works as a signal booster. When data signals travel over long distances through cables or wireless media, the signal becomes weak. A repeater receives the weak signal, regenerates it, and forwards it to extend the network range.
**Hub:**
A  **Hub**  is a networking device used to connect multiple devices in a LAN. When a hub receives data from one device, it broadcasts the data to all connected devices. It cannot filter data and works in half-duplex mode, which reduces network performance.
**Bridge:**
A  **Bridge**  connects two or more LAN segments and forwards data between them. It uses MAC addresses to decide whether to forward or block data, reducing unnecessary network traffic.
**Switch:**
A  **Switch**  connects multiple devices in a LAN and forwards data based on MAC addresses. It sends data only to the intended device, improving network speed and security compared to a hub.
**Router:**
A  **Router**  connects different networks and routes data packets using a routing table. It selects the best path for data transmission between networks.

**Repeater:**
**Repeater**  হলো একটি network device যা signal booster হিসেবে কাজ করে। দীর্ঘ দূরত্বে data transmit করার সময় signal দুর্বল হয়ে যায়। Repeater সেই দুর্বল signal গ্রহণ করে regenerate করে আবার পাঠায়, ফলে network range বৃদ্ধি পায়।
**Hub:**
**Hub**  একটি network device যা LAN-এ একাধিক device সংযুক্ত করে। Hub কোনো data পেলে তা সব connected device-এ broadcast করে। এটি data filter করতে পারে না এবং half-duplex mode-এ কাজ করে, ফলে network slow হয়।
**Bridge:**
**Bridge**  দুই বা ততোধিক LAN segment সংযুক্ত করে। এটি MAC address ব্যবহার করে data forward বা block করে, ফলে অপ্রয়োজনীয় traffic কমে।
**Switch:**
**Switch**  LAN-এ একাধিক device সংযুক্ত করে এবং MAC address অনুযায়ী নির্দিষ্ট device-এ data পাঠায়। Hub-এর তুলনায় এটি দ্রুত এবং বেশি secure।
**Router:**
**Router**  একাধিক network সংযুক্ত করে এবং routing table ব্যবহার করে data packet-এর জন্য সবচেয়ে efficient path নির্বাচন করে।

☆

20

Computer Network
Network Topology & Devices

Write connection type? i. Router to Router ii. Router to switch iii. Computer to computer iv. Hub to Switch

SPCBL, SAME, 22
| AME/ANE/AE

**Connection Types in Networking**
**i. Router to Router:**
Uses a  **Crossover Cable**  because both devices transmit and receive on the same pins.
**ii. Router to Switch:**
Uses a  **Straight-Through Cable**  because router and switch use different transmit/receive pins.
**iii. Computer to Computer:**
Uses a  **Crossover Cable**  for direct communication without an intermediate device.
**iv. Hub to Switch:**
Uses a  **Crossover Cable**  since both are similar networking devices.

**Networking-এ Connection Type**
**i. Router to Router:**
এক্ষেত্রে  **Crossover Cable**  ব্যবহার করা হয় কারণ দুইটি device একই pin দিয়ে data পাঠায় ও গ্রহণ করে।
**ii. Router to Switch:**
এক্ষেত্রে  **Straight-Through Cable**  ব্যবহার করা হয় কারণ router ও switch-এর transmit/receive pin আলাদা।
**iii. Computer to Computer:**
Directভাবে সংযোগের জন্য  **Crossover Cable**  ব্যবহার করা হয়।
**iv. Hub to Switch:**
Hub এবং Switch একই ধরনের device হওয়ায়  **Crossover Cable**  ব্যবহার করা হয়।


☆

21

Computer Network
Network Topology & Devices

Difference among Switch, Bridge and Router.

CB, O(IT), 23
| Officer (IT)

**Switch**

**Layer of Operation:**  Works at Layer 2 (Data Link Layer) of the OSI model.
**Function:**  Connects devices within a local network and forwards data based on MAC addresses.
**Addressing:**  Uses MAC address to send data to the correct device.
**Broadcast Handling:**  Reduces network congestion by sending data only to the destination device.
**Example:**  Ethernet switch used in office or home LAN.

**Bridge**

**Layer of Operation:**  Operates at Layer 2 (Data Link Layer).
**Function:**  Connects two or more network segments and filters traffic using MAC addresses.
**Segment Isolation:**  Reduces collision by separating network segments.
**Example:**  Connecting two Ethernet LAN segments.

**Router**

**Layer of Operation:**  Operates at Layer 3 (Network Layer).
**Function:**  Connects different networks and routes data using IP addresses.
**NAT:**  Allows multiple devices to share a single public IP address.
**Segmentation:**  Controls traffic between different networks.
**Example:**  Internet router used by ISP or enterprise networks.

**Switch**

**Layer of Operation:**  OSI model-এর Layer 2 (Data Link Layer)-এ কাজ করে।
**Function:**  Local network-এর ডিভাইস সংযুক্ত করে এবং MAC address অনুযায়ী data পাঠায়।
**Addressing:**  MAC address ব্যবহার করে destination নির্ধারণ করে।
**Broadcast Handling:**  নির্দিষ্ট device-এ data পাঠিয়ে network congestion কমায়।
**উদাহরণ:**  Office বা home LAN-এ ব্যবহৃত Ethernet switch।

**Bridge**

**Layer of Operation:**  OSI model-এর Layer 2-এ কাজ করে।
**Function:**  একাধিক network segment যুক্ত করে এবং MAC address অনুযায়ী traffic filter করে।
**Segment Isolation:**  Network segment আলাদা করে collision কমায়।
**উদাহরণ:**  দুইটি Ethernet LAN segment সংযোগ করা।

**Router**

**Layer of Operation:**  OSI model-এর Layer 3 (Network Layer)-এ কাজ করে।
**Function:**  ভিন্ন ভিন্ন network সংযুক্ত করে এবং IP address ব্যবহার করে data route করে।
**NAT:**  একাধিক device-কে একটি public IP ব্যবহার করতে দেয়।
**Segmentation:**  Network গুলোকে logicalভাবে আলাদা করে traffic নিয়ন্ত্রণ করে।
**উদাহরণ:**  ISP বা বড় network-এ ব্যবহৃত Internet router।

☆

22

Computer Network
Network Topology & Devices

What is Topology in data communication? What are differences between Bus, Ring, Tree and Star topology? Purpose of IEEE 802.11 committee. 10

CB, SO(IT), 23
| Senior Officer (IT)

**Network Topology**
Network topology refers to the physical or logical arrangement of computers, devices, and communication links in a network that determines how data is transmitted.
**Example:**  Computers connected through a central switch in an office network follow Star topology.
**1. Bus Topology**
**Working:**  In bus topology, all devices are connected to a single backbone cable. When a device sends data, it travels along the cable and reaches all devices, but only the intended receiver accepts it.

**Advantage:**  Low installation cost and simple structure.
**2. Ring Topology**
**Working:**  In ring topology, devices are connected in a circular manner. Data moves in one direction from one device to the next until it reaches the destination.

**Advantage:**  No data collision occurs.
**3. Star Topology**
**Working:**  In star topology, all devices are connected to a central hub or switch. Data sent by a device first goes to the hub, which then forwards it to the destination device.

**Advantage:**  Easy to manage and troubleshoot.
**4. Tree Topology**
**Working:**  Tree topology uses a hierarchical structure where multiple star networks are connected to a main backbone cable, and data flows from parent nodes to child nodes.

**Advantage:**  Suitable for large and expandable networks.
**3. Purpose of IEEE 802.11 Committee**
The IEEE 802.11 committee is responsible for developing standards for  **Wireless Local Area Networks (WLAN)** .

Defines Wi-Fi communication standards
Ensures interoperability between wireless devices
Improves wireless speed, security, and reliability

**Network Topology**
Network Topology বলতে একটি network-এ computer, device এবং communication link-এর physical বা logical বিন্যাসকে বোঝায়, যা data চলাচলের পদ্ধতি নির্ধারণ করে।
**উদাহরণ:**  একটি office network-এ central switch ব্যবহার করে computer সংযোগ করা Star topology-এর উদাহরণ।
**১. Bus Topology**
**কাজ:**  Bus topology-তে সব ডিভাইস একটি backbone cable-এর সাথে যুক্ত থাকে। কোনো ডিভাইস data পাঠালে তা cable দিয়ে সব ডিভাইসে পৌঁছায়, কিন্তু নির্দিষ্ট receiver-ই data গ্রহণ করে।

**সুবিধা:**  গঠন সহজ এবং খরচ কম।
**২. Ring Topology**
**কাজ:**  Ring topology-তে ডিভাইসগুলো বৃত্তাকারে সংযুক্ত থাকে। Data একদিকে ঘুরে এক ডিভাইস থেকে অন্য ডিভাইসে যায় যতক্ষণ না গন্তব্যে পৌঁছায়।

**সুবিধা:**  Data collision হয় না।
**৩. Star Topology**
**কাজ:**  Star topology-তে সব ডিভাইস একটি central hub বা switch-এর সাথে যুক্ত থাকে। Data প্রথমে hub-এ যায়, তারপর destination ডিভাইসে পাঠানো হয়।

**সুবিধা:**  Management ও troubleshooting সহজ।
**৪. Tree Topology**
**কাজ:**  Tree topology-তে hierarchical কাঠামো ব্যবহার করা হয়, যেখানে একাধিক star network একটি main backbone-এর সাথে যুক্ত থাকে এবং data parent node থেকে child node-এ প্রবাহিত হয়।

**সুবিধা:**  বড় ও expandable network-এর জন্য উপযোগী。
**৩. IEEE 802.11 Committee-এর উদ্দেশ্য**
IEEE 802.11 Committee-এর প্রধান উদ্দেশ্য হলো  **Wireless Local Area Network (WLAN)** -এর জন্য standard তৈরি ও উন্নয়ন করা।

Wi-Fi standard নির্ধারণ করা
Wireless device-এর compatibility নিশ্চিত করা
Wireless network-এর speed ও security বৃদ্ধি করা

☆

23

Computer Network
Network Topology & Devices

A network administrator is replacing a hub-based LAN with a switch-based LAN. Explain the differences between half-duplex and full-duplex communication and discuss how the change affects network performance.[assume]

Combined Bank, ADA-23, 26
| ADA

**Half-Duplex:**
In half-duplex communication, data can flow in both directions, but not at the same time. Devices must take turns sending and receiving data.
**Full-Duplex:**
In full-duplex communication, data can flow in both directions simultaneously. Devices can send and receive data at the same time.
**Key Differences:**

**Data Flow:**  Half-duplex = one direction at a time, Full-duplex = both directions simultaneously
**Efficiency:**  Full-duplex is more efficient
**Collisions:**  Half-duplex has collisions, full-duplex eliminates collisions
**Performance:**  Full-duplex provides higher throughput

**Impact of Replacing Hub with Switch**
**Hub-based LAN:**
- Operates in half-duplex mode
- All devices share bandwidth
- High collisions and congestion
**Switch-based LAN:**
- Supports full-duplex communication
- Dedicated bandwidth per port
- No collisions (due to separate collision domains)
**Performance Improvement:**

Higher network speed and throughput
Reduced collisions and retransmissions
Better bandwidth utilization
Improved overall LAN efficiency

**Conclusion:**
Switching from hub to switch enables full-duplex communication, eliminates collisions, and significantly improves network performance and scalability.

**Half-Duplex vs Full-Duplex Communication**
**Half-Duplex:**
Half-duplex communication-এ data দুই দিকেই যেতে পারে, কিন্তু একসাথে নয়। ডিভাইসগুলোকে একে অপরের সাথে পালাক্রমে send এবং receive করতে হয়।
**Full-Duplex:**
Full-duplex communication-এ data একই সময়ে দুই দিকেই যেতে পারে। একই সাথে send এবং receive করা যায়।
**মূল পার্থক্য:**

**Data Flow:**  Half-duplex = এক সময়ে এক দিক, Full-duplex = একসাথে দুই দিক
**Efficiency:**  Full-duplex বেশি efficient
**Collision:**  Half-duplex-এ collision হয়, Full-duplex-এ হয় না
**Performance:**  Full-duplex বেশি speed দেয়

**Hub থেকে Switch-এ পরিবর্তনের প্রভাব:**
**Hub-based LAN:**
- Half-duplex mode-এ কাজ করে
- সব device একই bandwidth share করে
- বেশি collision এবং congestion হয়
**Switch-based LAN:**
- Full-duplex support করে
- প্রতিটি port আলাদা bandwidth পায়
- collision হয় না (separate collision domain)
**Performance improvement:**

Network speed এবং throughput বাড়ে
Collision এবং retransmission কমে
Bandwidth utilization ভালো হয়
Overall network efficiency বাড়ে

**উপসংহার:**
Hub থেকে switch-এ পরিবর্তন করলে full-duplex communication সম্ভব হয়, collision দূর হয় এবং network performance অনেক উন্নত হয়।

☆

24

Computer Network
Network Topology & Devices

What is Network Topology? Distinguish between Bus, Ring, Tree and Star topology. Discuss how the Bus topology works.

Rupali, ANE, 23
| AME/ANE/AE

**Network Topology**
Network topology refers to the physical or logical arrangement of computers, devices, and communication links in a network that determines how data is transmitted.
**Example:**  Computers connected through a central switch in an office network follow Star topology.
**1. Bus Topology**
**Working:**  In bus topology, all devices are connected to a single backbone cable. When a device sends data, it travels along the cable and reaches all devices, but only the intended receiver accepts it.

**Advantage:**  Low installation cost and simple structure.
**2. Ring Topology**
**Working:**  In ring topology, devices are connected in a circular manner. Data moves in one direction from one device to the next until it reaches the destination.

**Advantage:**  No data collision occurs.
**3. Star Topology**
**Working:**  In star topology, all devices are connected to a central hub or switch. Data sent by a device first goes to the hub, which then forwards it to the destination device.

**Advantage:**  Easy to manage and troubleshoot.
**4. Tree Topology**
**Working:**  Tree topology uses a hierarchical structure where multiple star networks are connected to a main backbone cable, and data flows from parent nodes to child nodes.

**Advantage:**  Suitable for large and expandable networks.


**Network Topology**
Network Topology বলতে একটি network-এ computer, device এবং communication link-এর physical বা logical বিন্যাসকে বোঝায়, যা data চলাচলের পদ্ধতি নির্ধারণ করে।
**উদাহরণ:**  একটি office network-এ central switch ব্যবহার করে computer সংযোগ করা Star topology-এর উদাহরণ।
**১. Bus Topology**
**কাজ:**  Bus topology-তে সব ডিভাইস একটি backbone cable-এর সাথে যুক্ত থাকে। কোনো ডিভাইস data পাঠালে তা cable দিয়ে সব ডিভাইসে পৌঁছায়, কিন্তু নির্দিষ্ট receiver-ই data গ্রহণ করে।
**সুবিধা:**  গঠন সহজ এবং খরচ কম।
**২. Ring Topology**
**কাজ:**  Ring topology-তে ডিভাইসগুলো বৃত্তাকারে সংযুক্ত থাকে। Data একদিকে ঘুরে এক ডিভাইস থেকে অন্য ডিভাইসে যায় যতক্ষণ না গন্তব্যে পৌঁছায়।

**সুবিধা:**  Data collision হয় না।
**৩. Star Topology**
**কাজ:**  Star topology-তে সব ডিভাইস একটি central hub বা switch-এর সাথে যুক্ত থাকে। Data প্রথমে hub-এ যায়, তারপর destination ডিভাইসে পাঠানো হয়।

**সুবিধা:**  Management ও troubleshooting সহজ।
**৪. Tree Topology**
**কাজ:**  Tree topology-তে hierarchical কাঠামো ব্যবহার করা হয়, যেখানে একাধিক star network একটি main backbone-এর সাথে যুক্ত থাকে এবং data parent node থেকে child node-এ প্রবাহিত হয়।

**সুবিধা:**  বড় ও expandable network-এর জন্য উপযোগী।

- ☆

25

Computer Network

How stop and wait ARQ is used for reliable data transfer?

CB, SO(IT), 22
| Senior Officer (IT)

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

26

Computer Network

Make a list of LTE Network elements.


CB, O(IT), 20
| Officer (IT)

**LTE (Long Term Evolution)**  is a 4G wireless communication technology. An LTE network consists of several network elements that work together to provide high-speed voice and data communication.
**List of LTE Network Elements**

Network Element
Function

**UE (User Equipment)**
The user's mobile device (smartphone, tablet, modem) used to access the LTE network.

**eNodeB (Evolved Node B)**
The LTE base station that provides radio communication between the UE and the core network.

**MME (Mobility Management Entity)**
Handles user authentication, mobility management, and session management.

**S-GW (Serving Gateway)**
Routes user data packets between the eNodeB and the core network.

**P-GW (Packet Data Network Gateway)**
Connects the LTE network to external IP networks such as the Internet.

**HSS (Home Subscriber Server)**
Stores subscriber information, authentication data, and user profiles.

**PCRF (Policy and Charging Rules Function)**
Manages Quality of Service (QoS) and charging policies.

The main LTE network elements are  **UE** ,  **eNodeB** ,  **MME** ,  **S-GW** ,  **P-GW** ,  **HSS** , and  **PCRF** . Together, they provide reliable, secure, and high-speed mobile communication.

**LTE (Long Term Evolution)**  হলো একটি  **4G Wireless Communication Technology** । একটি  **LTE Network**  একাধিক  **Network Element**  নিয়ে গঠিত, যা একসাথে কাজ করে উচ্চগতির (High-Speed) Voice এবং Data Communication নিশ্চিত করে।
**LTE Network-এর প্রধান Network Element**

Network Element
কাজ

**UE (User Equipment)**
ব্যবহারকারীর  **Mobile Device**  (Smartphone, Tablet, Modem), যা LTE Network ব্যবহার করে।

**eNodeB (Evolved Node B)**
LTE-এর  **Base Station** , যা  **UE**  এবং  **Core Network** -এর মধ্যে Radio Communication প্রদান করে।

**MME (Mobility Management Entity)**
User Authentication, Mobility Management এবং Session Management পরিচালনা করে।

**S-GW (Serving Gateway)**
**eNodeB**  এবং  **Core Network** -এর মধ্যে User Data Packet Forward করে।

**P-GW (Packet Data Network Gateway)**
LTE Network-কে Internet-এর মতো External  **IP Network** -এর সাথে সংযুক্ত করে।

**HSS (Home Subscriber Server)**
Subscriber Information, Authentication Data এবং User Profile সংরক্ষণ করে।

**PCRF (Policy and Charging Rules Function)**
**Quality of Service (QoS)**  এবং Charging Policy নিয়ন্ত্রণ করে।

LTE Network-এর প্রধান  **Network Element**  হলো  **UE** ,  **eNodeB** ,  **MME** ,  **S-GW** ,  **P-GW** ,  **HSS**  এবং  **PCRF** । এরা সম্মিলিতভাবে দ্রুত, নিরাপদ এবং নির্ভরযোগ্য Mobile Communication নিশ্চিত করে।

☆

27

Computer Network

A network administrator is connecting hosts A and B directly through their Ethernet interfaces, as shown in the illustration. Ping attempts between the hosts are unsuccessful. What can be done to provide connectivity between the hosts? Write some reason how the problem will identify?

SPCBL, SAME, 22
| AME/ANE/AE

**Why ping fails (from the diagram)**

**Wrong IP subnet:**  Mask 255.255.255.240 = /28 (block size 16). Host A = 192.168.1.20 belongs to network  **192.168.1.16/28**  (range 16–31). Host B = 192.168.1.201 belongs to network  **192.168.1.192/28**  (range 192–207). They are in  **different subnets** , so direct communication fails without a router.
**Cable type issue (possible):**  Two PCs directly connected usually need a  **crossover cable**  (unless NIC supports  **Auto MDI/MDIX** ). Using straight-through may cause no physical link on some devices.

**What can be done to provide connectivity**

**Option 1 (Best for direct link): Put both hosts in the same subnet**
Example (keep /28): Set Host B to  **192.168.1.21**  with mask  **255.255.255.240**  (or any IP within 192.168.1.17–192.168.1.30). Then both are in  **192.168.1.16/28** .
**Option 2: Use a router (if different subnets must remain)**
Connect both to a router (or L3 switch), configure routing, and set correct  **default gateway**  on both hosts.
**Option 3 (Physical fix): Use correct Layer-1 connection**
Use a  **crossover cable**  OR connect both hosts to a  **switch**  using straight-through cables (or ensure Auto MDI/MDIX is enabled).

**How to identify the problem (troubleshooting reasons)**

**Check physical link:**  Link LEDs should be ON; if OFF, suspect wrong cable/port/speed-duplex.
**Verify IP settings:**  Check IP & mask on both hosts (ipconfig/ifconfig). Compute network IDs to see if they match.
**Ping tests:**  Ping  **127.0.0.1**  (TCP/IP stack), then ping own IP, then ping the other host.
**Check ARP:**  If same subnet, ARP table should show the other host’s MAC; if not appearing, subnet/cable issue likely.
**ICMP blocking:**  Check host firewall settings that may block ping (ICMP).



**Ping কেন হচ্ছে না (diagram থেকে)**

**Subnet mismatch:**  Mask 255.255.255.240 = /28 (block size 16)। Host A = 192.168.1.20 পড়ে  **192.168.1.16/28**  network-এ (range 16–31)। Host B = 192.168.1.201 পড়ে  **192.168.1.192/28**  network-এ (range 192–207)। দুইটা  **ভিন্ন subnet** , তাই router ছাড়া direct ping হবে না।
**Cable issue (সম্ভাব্য):**  দুইটা PC direct connect করলে সাধারণত  **crossover cable**  লাগে (যদি NIC-এ  **Auto MDI/MDIX**  না থাকে)। Straight-through হলে অনেক ক্ষেত্রে link উঠবে না।

**Connectivity আনার সমাধান**

**Option 1 (Direct link-এর জন্য best): একই subnet-এ আনা**
/28 রাখলে: Host B-কে  **192.168.1.21**  এবং mask  **255.255.255.240**  দাও (অথবা 192.168.1.17–192.168.1.30 এর মধ্যে যেকোনো valid IP)। তখন দুজনই  **192.168.1.16/28**  subnet-এ থাকবে।
**Option 2: Router ব্যবহার (যদি দুই subnet আলাদা রাখতেই হয়)**
Router/L3 switch দিয়ে connect করে routing configure করতে হবে এবং দুই host-এ সঠিক  **default gateway**  দিতে হবে।
**Option 3 (Physical fix): সঠিক Layer-1 connection**
**Crossover cable**  ব্যবহার করো অথবা দুটো host-কে  **switch** -এ দাও (straight-through দিয়ে) / অথবা Auto MDI/MDIX নিশ্চিত করো।

**Problem কীভাবে identify করবে (troubleshooting reasons)**

**Physical link check:**  Link LED ON কিনা দেখো; OFF হলে cable/port/speed-duplex issue হতে পারে।
**IP configuration verify:**  ipconfig/ifconfig দিয়ে IP ও mask দেখে network ID calculate করে মিলাও।
**Ping test:**  আগে  **127.0.0.1** , তারপর নিজের IP, তারপর অন্য host ping করো।
**ARP check:**  Same subnet হলে ARP table-এ অন্য host-এর MAC দেখা উচিত; না দেখালে subnet/cable issue সম্ভাবনা বেশি।
**ICMP blocking:**  Host firewall ping (ICMP) block করছে কি না দেখো।



☆

28

Computer Network

What is Blacklist and Whitelist? Write down the Difference between Black list and white list.

SPCBL, SAP, 22
| Assistant Programmer

**Blacklist**
A  **Blacklist**  is a list of users, IP addresses, websites, or applications that are  **explicitly blocked**  from accessing a system or network.
**Whitelist**
A  **Whitelist**  is a list of users, IP addresses, websites, or applications that are  **explicitly allowed**  to access a system or network. Everything else is blocked by default.
**Difference between Blacklist and Whitelist**

**Access Rule:**  Blacklist blocks specific entities; Whitelist allows only specific entities.
**Default Behavior:**  Blacklist allows all except blocked ones; Whitelist blocks all except allowed ones.
**Security Level:**  Blacklist is less secure; Whitelist is more secure.
**Use Case:**  Blacklist is used to block known threats; Whitelist is used in high-security environments.



**Blacklist**
**Blacklist**  হলো এমন একটি তালিকা যেখানে নির্দিষ্ট user, IP address, website বা application-কে  **block**  করে রাখা হয় যাতে তারা system বা network access না পায়।
**Whitelist**
**Whitelist**  হলো এমন একটি তালিকা যেখানে শুধুমাত্র নির্দিষ্ট user, IP address, website বা application-কে  **allow**  করা হয়। তালিকার বাইরে থাকা সবকিছু block থাকে।
**Blacklist এবং Whitelist-এর পার্থক্য**

**Access Rule:**  Blacklist নির্দিষ্ট entity block করে; Whitelist নির্দিষ্ট entity allow করে।
**Default Behavior:**  Blacklist-এ সব allow থাকে শুধু blocked ছাড়া; Whitelist-এ সব block থাকে শুধু allowed ছাড়া।
**Security Level:**  Blacklist তুলনামূলক কম secure; Whitelist বেশি secure।
**Use Case:**  Blacklist পরিচিত threat block করতে ব্যবহৃত হয়; Whitelist উচ্চ security পরিবেশে ব্যবহৃত হয়।



☆

29

Computer Network

What is the difference between packet sniffing (Snooping) and Packet spoofing?

CB, SO(IT), 20
| Senior Officer (IT)

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

30

Computer Network

Difference between spoofing and sniffing

CB, AP, 20
| Assistant Programmer

- ☆

31

Computer Network
Swithcing Technique & Protocol

Explain packet switching. A packet passes through 4 routers with each router introducing 2 ms processing delay. Transmission delay per link is 5 ms. Calculate total end-to-end delay (ignore propagation).

Combined Bank, AE(IT)/AME, 26
| AME/ANE/AE

**Packet Switching**

Packet Switching is a method of data transmission where data is broken into  **small packets** .
Each packet travels  **independently**  through the network and may take different paths.
At the destination, packets are  **reassembled**  to form the original message.

**End-to-End Delay Calculation:**

Number of routers = 4
**Processing delay per router**  = 2 ms → Total = 4 × 2 =  **8 ms**
Number of links = routers + 1 = 5
**Transmission delay per link**  = 5 ms → Total = 5 × 5 =  **25 ms**
**Total Delay = Processing + Transmission**
= 8 ms + 25 ms =  **33 ms**

**Packet Switching**

Packet Switching হলো একটি data transmission পদ্ধতি যেখানে data-কে  **ছোট ছোট packet** -এ ভাগ করা হয়।
প্রতিটি packet আলাদা পথে  **independently**  network দিয়ে যায়।
শেষে destination-এ packet গুলো  **reassemble**  করে মূল data তৈরি করা হয়।

**End-to-End Delay Calculation:**

Number of routers = 4
**Processing delay per router**  = 2 ms → Total = 4 × 2 =  **8 ms**
Number of links = routers + 1 = 5
**Transmission delay per link**  = 5 ms → Total = 5 × 5 =  **25 ms**
**Total Delay = Processing + Transmission**
= 8 ms + 25 ms =  **33 ms**

☆

32

Computer Network
Swithcing Technique & Protocol

What is DHCP? How does it work? What is DHCP function?

Pubali, JHE, 23
|

DHCP (Dynamic Host Configuration Protocol) is a network protocol that automatically assigns IP addresses and other network configuration details to devices connected to a network.
**Step-by-Step Working of DHCP**
**Step 1: DHCP Discover**
When a device connects to a network, it broadcasts a DHCP Discover message to find available DHCP servers.
**Step 2: DHCP Offer**
The DHCP server responds with a DHCP Offer message that contains an available IP address and configuration details.
**Step 3: DHCP Request**
The client selects one offer and sends a DHCP Request message to request the offered IP address.
**Step 4: DHCP Acknowledgement (ACK)**
The DHCP server sends a DHCP ACK message confirming the IP address assignment along with subnet mask, gateway, and DNS details.
**Result**
The client can now communicate on the network using the assigned IP address.
**Example**
When you connect your laptop to a Wi-Fi network, the router (DHCP server) automatically assigns an IP address to your laptop.



DHCP (Dynamic Host Configuration Protocol) হলো একটি network protocol যা স্বয়ংক্রিয়ভাবে device-কে IP address এবং অন্যান্য network configuration প্রদান করে।
**DHCP কাজ করার ধাপসমূহ**
**Step 1: DHCP Discover**
Network-এ যুক্ত হওয়ার সময় client একটি DHCP Discover message broadcast করে DHCP server খোঁজে।
**Step 2: DHCP Offer**
DHCP server একটি DHCP Offer পাঠায় যেখানে একটি available IP address ও configuration থাকে।
**Step 3: DHCP Request**
Client পছন্দের offer নির্বাচন করে DHCP Request message পাঠায়।
**Step 4: DHCP Acknowledgement (ACK)**
DHCP server DHCP ACK পাঠিয়ে IP address, subnet mask, gateway ও DNS নিশ্চিত করে।
**ফলাফল**
Client নির্ধারিত IP address ব্যবহার করে network-এ যোগাযোগ করতে পারে।
**উদাহরণ**
আপনি যখন Wi-Fi-তে laptop সংযোগ করেন, তখন router (DHCP server) স্বয়ংক্রিয়ভাবে IP address assign করে।



☆

33

Computer Network
Swithcing Technique & Protocol

Explain how do DHCP work?

Pubali, HE, 23
| Bank

**How DHCP Works**
DHCP (Dynamic Host Configuration Protocol) is a network protocol that automatically assigns IP addresses and other network configuration details to devices connected to a network.
**Step-by-Step Working of DHCP**
**Step 1: DHCP Discover**
When a device connects to a network, it broadcasts a DHCP Discover message to find available DHCP servers.
**Step 2: DHCP Offer**
The DHCP server responds with a DHCP Offer message that contains an available IP address and configuration details.
**Step 3: DHCP Request**
The client selects one offer and sends a DHCP Request message to request the offered IP address.
**Step 4: DHCP Acknowledgement (ACK)**
The DHCP server sends a DHCP ACK message confirming the IP address assignment along with subnet mask, gateway, and DNS details.
**Result**
The client can now communicate on the network using the assigned IP address.
**Example**
When you connect your laptop to a Wi-Fi network, the router (DHCP server) automatically assigns an IP address to your laptop.



**DHCP কীভাবে কাজ করে**
DHCP (Dynamic Host Configuration Protocol) হলো একটি network protocol যা স্বয়ংক্রিয়ভাবে device-কে IP address এবং অন্যান্য network configuration প্রদান করে।
**DHCP কাজ করার ধাপসমূহ**
**Step 1: DHCP Discover**
Network-এ যুক্ত হওয়ার সময় client একটি DHCP Discover message broadcast করে DHCP server খোঁজে।
**Step 2: DHCP Offer**
DHCP server একটি DHCP Offer পাঠায় যেখানে একটি available IP address ও configuration থাকে।
**Step 3: DHCP Request**
Client পছন্দের offer নির্বাচন করে DHCP Request message পাঠায়।
**Step 4: DHCP Acknowledgement (ACK)**
DHCP server DHCP ACK পাঠিয়ে IP address, subnet mask, gateway ও DNS নিশ্চিত করে।
**ফলাফল**
Client নির্ধারিত IP address ব্যবহার করে network-এ যোগাযোগ করতে পারে।
**উদাহরণ**
আপনি যখন Wi-Fi-তে laptop সংযোগ করেন, তখন router (DHCP server) স্বয়ংক্রিয়ভাবে IP address assign করে।



☆

34

Computer Network
Swithcing Technique & Protocol

What is DNS? How DNS work?

Sonali Bank, ADA, 26
| ADA

**DNS (Domain Name System)**
DNS is a system that translates  **domain names**  (like google.com) into  **IP addresses**  (like 142.250.190.78). It works like the  **phonebook of the internet** .
**How DNS Works:**

**1. User Request:**  User enters a domain name (e.g., www.google.com) in the browser.
**2. DNS Resolver:**  The request goes to a  **DNS resolver**  (usually ISP or local cache).
**3. Root Server:**  If not cached, resolver queries the  **Root DNS server** .
**4. TLD Server:**  Root server directs to  **TLD server**  (.com, .org).
**5. Authoritative Server:**  TLD server provides the  **authoritative DNS server**  for the domain.
**6. IP Address Returned:**  Authoritative server returns the  **IP address** .
**7. Connection:**  Browser uses the IP to connect to the website.

**Example:**

User types  **www.facebook.com**
DNS converts it to an IP (e.g., 157.240.x.x)
Browser connects to that IP and loads the website

**DNS (Domain Name System)**
DNS এমন একটি system যা  **domain name**  (যেমন google.com) কে  **IP address** -এ রূপান্তর করে।এটি internet-এর  **phonebook**  হিসেবে কাজ করে।
**DNS কীভাবে কাজ করে:**

**১. User Request:**  user browser-এ domain name লিখে (যেমন www.google.com)।
**২. DNS Resolver:**  request প্রথমে  **DNS resolver** -এ যায়।
**৩. Root Server:**  cache না থাকলে root DNS server-এ query যায়।
**৪. TLD Server:**  root server .com/.org TLD server-এ পাঠায়।
**৫. Authoritative Server:**  TLD server domain-এর authoritative server দেয়।
**৬. IP Address:**  authoritative server থেকে IP পাওয়া যায়।
**৭. Connection:**  browser সেই IP দিয়ে website-এ connect করে।

**উদাহরণ:**

user লিখলো  **www.facebook.com**
DNS এটাকে IP-এ convert করে
browser সেই IP দিয়ে website load করে

☆

35

Computer Network
Swithcing Technique & Protocol

Differentiate between Collision Domain and Broadcast Domain in computer network. What is the function of DNS and DHCP?

Rupali, ANE, 23
| AME/ANE/AE

**1. Difference between Collision Domain and Broadcast Domain**

Aspect
Collision Domain
Broadcast Domain

Definition
A network area where data packets can collide
A network area where broadcast packets are forwarded

Device Control
Broken by switches and bridges
Broken by routers

Data Issue
Data collision may occur
No collision, only broadcast traffic

Example
Devices connected to a hub
Devices in the same LAN

**Explanation:**  Collision domain is related to data collision, while broadcast domain is related to broadcast message distribution.
**2. Function of DNS**
DNS (Domain Name System) converts human-readable domain names into IP addresses so that computers can locate and communicate with each other on a network.
**Example:**  DNS converts www.google.com into an IP address like 142.250.190.14.
**3. Function of DHCP**
DHCP (Dynamic Host Configuration Protocol) automatically assigns IP address and network configuration parameters to devices in a network.
**Example:**  When a computer connects to Wi-Fi, DHCP assigns it an IP address automatically.


**১. Collision Domain ও Broadcast Domain-এর পার্থক্য**

বিষয়
Collision Domain
Broadcast Domain

সংজ্ঞা
যে network অংশে data collision হতে পারে
যে network অংশে broadcast packet ছড়িয়ে পড়ে

নিয়ন্ত্রণকারী ডিভাইস
Switch ও bridge দ্বারা ভাঙা যায়
Router দ্বারা ভাঙা যায়

Data সমস্যা
Collision হতে পারে
Collision হয় না, শুধু broadcast হয়

উদাহরণ
Hub-এর সাথে সংযুক্ত ডিভাইস
একই LAN-এর ডিভাইস

**ব্যাখ্যা:**  Collision domain মূলত data collision-এর সাথে সম্পর্কিত, আর broadcast domain broadcast message ছড়ানোর সাথে সম্পর্কিত।
**২. DNS-এর কাজ**
DNS (Domain Name System) মানুষের বোঝার উপযোগী domain name-কে IP address-এ রূপান্তর করে, যাতে computer network-এ একে অপরকে খুঁজে পায়।
**উদাহরণ:**  DNS www.google.com-কে একটি IP address-এ রূপান্তর করে।
**৩. DHCP-এর কাজ**
DHCP (Dynamic Host Configuration Protocol) network-এ যুক্ত ডিভাইসকে স্বয়ংক্রিয়ভাবে IP address ও অন্যান্য network configuration প্রদান করে।
**উদাহরণ:**  Wi-Fi-তে সংযুক্ত হলে DHCP নিজে থেকেই IP address দেয়।


☆

36

Computer Network
Swithcing Technique & Protocol

Do you prefer packet switching compared to circuit switching in communication network? If Yes, why? How does packet switching work step by step? What applications use packet switching?

Rupali, ANE, 23
| AME/ANE/AE

**1. Do we prefer Packet Switching over Circuit Switching?**
Yes, in most modern communication networks packet switching is preferred over circuit switching because it uses network resources more efficiently and supports many users at the same time.
**Why Packet Switching is Preferred (Reasons)**

**Efficient Bandwidth Use:**  No dedicated path is reserved, so bandwidth is shared and not wasted when a user is idle.
**Better for Burst Traffic:**  Internet data is usually bursty (not continuous), and packet switching handles this well.
**Scalability:**  Works efficiently for large networks like the Internet.
**Reliability:**  If one route fails, packets can take alternative routes.
**Cost Effective:**  Shared infrastructure reduces overall cost.

**2. How Packet Switching Works (Step by Step)**

**Step 1:**  The sender’s message is divided into small units called  **packets** .
**Step 2:**  Each packet gets a header containing  **source address, destination address, sequence number, and error-check info** .
**Step 3:**  Packets are sent into the network and travel through routers and switches.
**Step 4:**  Each router reads the destination address and forwards the packet to the next best route (routing decision).
**Step 5:**  Packets may take different paths and may arrive out of order due to congestion or routing changes.
**Step 6:**  At the receiver side, packets are checked for errors, arranged by sequence number, and reassembled into the original message.
**Step 7:**  If any packet is missing or corrupted, it is retransmitted (common in reliable protocols like TCP).

**3. Applications that Use Packet Switching**

**Internet browsing:**  HTTP/HTTPS (websites)
**Email services:**  SMTP, IMAP, POP3
**File transfer:**  FTP, SFTP, cloud file sharing
**Video streaming:**  YouTube, Netflix, IPTV
**VoIP and video calls:**  WhatsApp call, Zoom, Google Meet (packet-based voice/video)
**Online gaming:**  Multiplayer games over the Internet
**Messaging apps:**  WhatsApp, Messenger, Telegram



**১. Packet Switching কি Circuit Switching-এর চেয়ে বেশি prefer করা হয়?**
হ্যাঁ, আধুনিক communication network-এ সাধারণত circuit switching-এর তুলনায় packet switching বেশি prefer করা হয়, কারণ এতে network resource দক্ষভাবে ব্যবহার হয় এবং একসাথে অনেক user service নিতে পারে।
**Packet Switching prefer করার কারণ**

**Efficient Bandwidth Use:**  Dedicated path reserve করা লাগে না, তাই idle থাকলেও bandwidth waste হয় না।
**Burst Traffic Handle:**  Internet-এর data traffic বেশিরভাগ সময় bursty, packet switching এতে ভালো কাজ করে।
**Scalability:**  Internet-এর মতো বড় network-এ খুব ভালোভাবে কাজ করে।
**Reliability:**  একটি route সমস্যা হলে packet অন্য route দিয়ে যেতে পারে।
**Cost Effective:**  Shared infrastructure হওয়ায় খরচ কম।

**২. Packet Switching কীভাবে কাজ করে (Step by Step)**

**Step 1:**  Sender-এর message ছোট ছোট অংশে ভাগ করা হয়, এগুলোকে  **packet**  বলা হয়।
**Step 2:**  প্রতিটি packet-এর সাথে header যুক্ত থাকে, যেমন  **source address, destination address, sequence number, error-check** ।
**Step 3:**  Packet গুলো network-এ পাঠানো হয় এবং router/switch দিয়ে অতিক্রম করে।
**Step 4:**  Router destination address দেখে packet-এর জন্য পরবর্তী best route নির্বাচন করে forward করে।
**Step 5:**  Congestion বা routing পরিবর্তনের কারণে packet ভিন্ন ভিন্ন path দিয়ে যেতে পারে এবং order এলোমেলো হতে পারে।
**Step 6:**  Receiver side-এ packet error-check করা হয়, sequence number অনুযায়ী সাজানো হয় এবং original message তৈরি করা হয়।
**Step 7:**  কোনো packet missing বা corrupted হলে retransmission হয় (বিশেষ করে TCP-তে)।

**৩. কোন কোন Application Packet Switching ব্যবহার করে**

**Internet browsing:**  HTTP/HTTPS (website)
**Email:**  SMTP, IMAP, POP3
**File transfer:**  FTP, SFTP, cloud sharing
**Video streaming:**  YouTube, Netflix, IPTV
**VoIP/Video call:**  WhatsApp, Zoom, Google Meet
**Online gaming:**  Multiplayer online games
**Messaging:**  WhatsApp, Messenger, Telegram



☆

37

Computer Network
Swithcing Technique & Protocol

ARP used in TCP/IP for perform some operation, write the functions of ARP.

CB, SO(IT), 20
| Senior Officer (IT)

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

38

Computer Network
OSI/TCP-IP

Draw a tabular representation of the TCP/IP Model. Explain the function of each layer, protocols related to each layer, and associated devices and software. Describe different types of Network Firewalls. Explain the advantages of Next-Generation Firewall (NGFW) over a Traditional Firewall.

CB, AE(IT)/AME, 24
| AME/ANE/AE

**TCP/IP Model (Tabular Representation)**

**Types of Network Firewall**

**Packet Filtering Firewall:**  Filters packets based on IP, port, protocol.
**Stateful Inspection Firewall:**  Tracks connection state and allows valid traffic.
**Proxy Firewall:**  Acts as intermediary between user and internet.
**Application Firewall:**  Filters traffic at application layer.
**Next-Generation Firewall (NGFW):**  Advanced firewall with deep inspection and security features.

**Advantages of NGFW over Traditional Firewall**

**Deep Packet Inspection:**  Analyzes full packet content, not just headers.
**Application Awareness:**  Identifies and controls specific applications.
**Intrusion Prevention (IPS):**  Detects and blocks attacks in real-time.
**Better Security:**  Protects against modern threats like malware and phishing.
**User-Based Control:**  Policies based on user identity, not just IP.

**Network Firewall-এর ধরন**

**Packet Filtering Firewall:**  IP, port অনুযায়ী packet filter করে।
**Stateful Firewall:**  connection state track করে।
**Proxy Firewall:**  user ও internet-এর মাঝে intermediary হিসেবে কাজ করে।
**Application Firewall:**  application layer-এ traffic control করে।
**NGFW:**  advanced security feature সহ modern firewall।

**NGFW এর সুবিধা (Traditional Firewall-এর উপর)**

**Deep Packet Inspection:**  পুরো packet analyze করতে পারে।
**Application Control:**  specific application control করা যায়।
**IPS Support:**  real-time attack detect ও block করে।
**উন্নত Security:**  malware, phishing থেকে সুরক্ষা দেয়।
**User-Based Policy:**  user অনুযায়ী control করা যায়।

☆

39

Computer Network
OSI/TCP-IP

What is OSI model? Explain the functions of each layer with examples.

Combined Bank, SO(IT-23), 26
| Senior Officer (IT)

The OSI (Open Systems Interconnection) Model is a reference framework that explains how data travels from one device to another over a network. It divides the entire communication process into seven layers. Each layer has its own specific job and passes data to the next layer. It helps developers and network engineers understand and troubleshoot network problems easily.
**The Seven Layers of the OSI Model**
**1. Physical Layer**
This is the lowest layer. It deals with the actual physical connection between devices. It transmits raw bits (0s and 1s) through cables, switches, and hubs.
**Function:**  Bit transmission, voltage levels, cable types, and signal timing.
**Devices:**  Cables, hubs, repeaters, and network interface cards (NIC).<
**Example:**  An Ethernet cable carrying electrical signals between a computer and a router.
**2. Data Link Layer**
This layer handles data transfer between two directly connected devices on the same network. It makes sure data is delivered without errors.
**Function:**  Framing, MAC addressing, error detection, and flow control.
**Devices:**  Switches and bridges.
**Example:**  A switch uses MAC addresses to send data to the correct computer in a local network.
**3. Network Layer**
This layer is responsible for moving data from one network to another. It finds the best path (routing) for the data to reach its destination.
**Function:**  Logical addressing (IP), routing, and path selection.
**Devices:**  Routers.
**Example:**  A router uses IP addresses to send a packet from your home network to a website server on the internet.
**4. Transport Layer**
This layer ensures data is delivered completely and correctly. It breaks large data into smaller segments and reassembles them at the other end.
**Function:**  Segmentation, error recovery, and flow control.
**Protocols:**  TCP and UDP.
**Example:**  TCP breaks an email into small parts, sends them, and puts them back together in the right order at the receiver.
**5. Session Layer**
This layer creates, manages, and ends communication sessions between two devices. It keeps the conversation active and organized.
**Function:**  Session establishment, maintenance, and termination.
**Example:**  When you log into a video call, the session layer sets up and keeps the call active until you hang up.
**6. Presentation Layer**
This layer acts like a translator. It formats, encrypts, and compresses data so the application layer can understand it.
**Function:**  Data translation, encryption, decryption, and compression.
**Example:**  SSL/TLS encryption on a website that keeps your password safe during login.
**7. Application Layer**
This is the top layer where users directly interact with the network. It provides services like email, file transfer, and web browsing.
**Function:**  User interface and network services for applications.
**Protocols:**  HTTP, FTP, SMTP, DNS.
**Example:**  A web browser using HTTP to load a webpage when you type www.google.com.
**Summary Table:**

Layer
Name
Main Function
Example

**7**
Application
User services like web and email
Browser loading a website

**6**
Presentation
Encryption and data formatting
SSL encrypting login password

**5**
Session
Manage connection sessions
Keeping a video call active

**4**
Transport
Reliable data delivery
TCP sending email in parts

**3**
Network
Routing and IP addressing
Router sending packet to server

**2**
Data Link
Error-free local delivery
Switch using MAC address

**1**
Physical
Raw bit transmission
Ethernet cable carrying signal

OSI (Open Systems Interconnection) Model হলো একটি reference framework যা ব্যাখ্যা করে কীভাবে data একটি device থেকে অন্য device-এ network-এর মাধ্যমে travel করে। এটি পুরো communication process-কে seven layers-এ ভাগ করে। প্রতিটি layer-এর নিজস্ব specific job আছে এবং data পরবর্তী layer-এ pass করে। এটি developers এবং network engineers-কে network problems বুঝতে এবং troubleshoot করতে সহজ করে।
**OSI Model-এর Seven Layers**
**1. Physical Layer**
এটি সবচেয়ে নিচের layer। এটি devices-এর মধ্যে actual physical connection নিয়ে কাজ করে। এটি raw bits (0s এবং 1s) cables, switches এবং hubs-এর মাধ্যমে transmit করে।
**Function:**  Bit transmission, voltage levels, cable types এবং signal timing।
**Devices:**  Cables, hubs, repeaters এবং network interface cards (NIC)।
**Example:**  একটি Ethernet cable computer এবং router-এর মধ্যে electrical signals carry করে।
**2. Data Link Layer**
এই layer একই network-এ সরাসরি connected দুটি device-এর মধ্যে data transfer handle করে। এটি নিশ্চিত করে যে data errors ছাড়াই deliver হয়।
**Function:**  Framing, MAC addressing, error detection এবং flow control।
**Devices:**  Switches এবং bridges।
**Example:**  একটি switch MAC addresses ব্যবহার করে local network-এ সঠিক computer-এ data পাঠায়।
**3. Network Layer**
এই layer একটি network থেকে অন্য network-এ data move করার দায়িত্বে। এটি data-এর destination-এ পৌঁছানোর জন্য best path (routing) খুঁজে বের করে।
**Function:**  Logical addressing (IP), routing এবং path selection।
**Devices:**  Routers।
**Example:**  একটি router IP addresses ব্যবহার করে home network থেকে internet-এর website server-এ packet পাঠায়।
**4. Transport Layer**
এই layer নিশ্চিত করে যে data সম্পূর্ণ এবং সঠিকভাবে deliver হয়। এটি বড় data-কে ছোট segments-এ ভাগ করে এবং অন্য প্রান্তে সেগুলো reassemble করে।
**Function:**  Segmentation, error recovery এবং flow control।
**Protocols:**  TCP এবং UDP।
**Example:**  TCP একটি email-কে ছোট ছোট parts-এ ভাগ করে পাঠায় এবং receiver-এ সঠিক order-এ জোড়া লাগায়।
**5. Session Layer**
এই layer দুটি device-এর মধ্যে communication sessions তৈরি, manage এবং end করে। এটি conversation active এবং organized রাখে।
**Function:**  Session establishment, maintenance এবং termination।
**Example:**  একটি video call-এ log in করার সময় session layer call set up করে এবং hang up না হওয়া পর্যন্ত active রাখে।
**6. Presentation Layer**
এই layer অনেকটা translator-এর মতো কাজ করে। এটি data format, encrypt এবং compress করে যাতে application layer এটি বুঝতে পারে।
**Function:**  Data translation, encryption, decryption এবং compression।
**Example:**  একটি website-এ SSL/TLS encryption যা login-এর সময় password safe রাখে।
**7. Application Layer**
এটি top layer যেখানে users সরাসরি network-এর সাথে interact করে। এটি email, file transfer এবং web browsing এর মতো services provide করে।
**Function:**  User interface এবং applications-এর জন্য network services।
**Protocols:**  HTTP, FTP, SMTP, DNS।
**Example:**  একটি web browser HTTP ব্যবহার করে www.google.com type করলে webpage load করে।
**Summary Table:**

Layer
Name
Main Function
Example

**7**
Application
User services যেমন web এবং email
Browser website load করা

**6**
Presentation
Encryption এবং data formatting
SSL login password encrypt করা

**5**
Session
Connection sessions manage করা
Video call active রাখা

**4**
Transport
Reliable data delivery
TCP email parts-এ পাঠানো

**3**
Network
Routing এবং IP addressing
Router server-এ packet পাঠানো

**2**
Data Link
Error-free local delivery
Switch MAC address ব্যবহার করা

**1**
Physical
Raw bit transmission
Ethernet cable signal carry করা

☆

40

Computer Network
OSI/TCP-IP

What is OSI model? Describe briefly about OSI model layer? Difference between OSI and TCP IP layer?

SPCBL, SAME, 22
| AME/ANE/AE

The  **OSI (Open Systems Interconnection) Model**  is a conceptual framework that standardizes the functions of a network communication system by dividing it into seven distinct layers. These layers ensure seamless communication between different systems and networks by defining protocols and packet transfer processes.

**Difference Between OSI and TCP/IP Model:**

**OSI (Open Systems Interconnection) Model**  হলো একটি conceptual framework যা network communication system-এর কাজগুলোকে সাতটি পৃথক layer-এ ভাগ করে standardize করে। এই layer-গুলো protocol ও packet transfer process নির্ধারণের মাধ্যমে বিভিন্ন system ও network-এর মধ্যে seamless communication নিশ্চিত করে।

**Difference Between OSI and TCP/IP Model:**



☆

41

Computer Network
OSI/TCP-IP

Difference between OSI model and TCP/IP model. Relation between Data, Segment, Packet and Bit in OSI model.  10

CB, SO(IT), 23
| Senior Officer (IT)

**Difference between OSI Model and TCP/IP Model**

**Relation between Data, Segment, Packet and Bit in OSI Model**
As data moves down through the OSI layers, it changes its form. This process is called  **encapsulation** .

**Data:**  At the  **Application, Presentation, and Session layers** , information is called Data.
**Segment:**  At the  **Transport layer** , data is divided into Segments (TCP) or Datagrams (UDP).
**Packet:**  At the  **Network layer** , segments are encapsulated into Packets.
**Frame:**  At the  **Data Link layer** , packets are converted into Frames.
**Bit:**  At the  **Physical layer** , frames are transmitted as Bits (0s and 1s).

**Flow:**  Data → Segment → Packet → Frame → Bit

**OSI Model এবং TCP/IP Model-এর পার্থক্য**

**OSI Model-এ Data, Segment, Packet ও Bit-এর সম্পর্ক**
OSI Model-এর বিভিন্ন layer দিয়ে data যাওয়ার সময় তার রূপ পরিবর্তন হয়, একে  **Encapsulation**  বলা হয়।

**Data:**  Application, Presentation ও Session layer-এ তথ্যকে Data বলা হয়।
**Segment:**  Transport layer-এ data ভাগ হয়ে Segment হয়।
**Packet:**  Network layer-এ Segment থেকে Packet তৈরি হয়।
**Frame:**  Data Link layer-এ Packet থেকে Frame হয়।
**Bit:**  Physical layer-এ Frame bit (0 ও 1) আকারে পাঠানো হয়।

**ধাপ:**  Data → Segment → Packet → Frame → Bit

☆

42

Computer Network
OSI/TCP-IP

At which layer of the OSI model does a standard Router primarily operate, and what is the specific name of the Protocol Data Unit (PDU) at this layer? A router has four contiguous /24 routing table entries: 10.1.0.0/24, 10.1.1.0/24, 10.1.2.0/24, and 10.1.3.0/24. If you summarize these into a single route, what will be the new CIDR notation?

CB, AME/AE(IT-23), 26
| AME/ANE/AE

A standard router primarily operates at the  **Network Layer** , which is  **Layer 3**  of the OSI model.
The Protocol Data Unit (PDU) at the Network Layer is called a  **Packet** .
**Given Routing Entries:**
10.1.0.0/24
10.1.1.0/24
10.1.2.0/24
10.1.3.0/24
These four networks are continuous or contiguous because their network addresses increase sequentially.
**First Network:**  10.1.0.0/24
Range: 10.1.0.0 to 10.1.0.255
**Second Network:**  10.1.1.0/24
Range: 10.1.1.0 to 10.1.1.255
**Third Network:**  10.1.2.0/24
Range: 10.1.2.0 to 10.1.2.255
**Fourth Network:**  10.1.3.0/24
Range: 10.1.3.0 to 10.1.3.255
Together, these four networks cover addresses from:
10.1.0.0 to 10.1.3.255
Each /24 network contains 256 addresses.
So total addresses become:
256 + 256 + 256 + 256 = 1024 addresses
To represent 1024 addresses, 10 host bits are required.
Since IPv4 address contains 32 bits:
32 − 10 = 22
Therefore, the summarized CIDR notation becomes:
**10.1.0.0/22**
**Final Answer:**
Router Layer = Network Layer / Layer 3
PDU Name = Packet
Supernet = 10.1.0.0/22

Standard router মূলত  **Network Layer** -এ কাজ করে, যা OSI model-এর  **Layer 3** ।
Network Layer-এর Protocol Data Unit (PDU)-কে  **Packet**  বলা হয়।
**প্রদত্ত Routing Entries:**
10.1.0.0/24
10.1.1.0/24
10.1.2.0/24
10.1.3.0/24
এই চারটি network continuous বা contiguous কারণ network address ধারাবাহিকভাবে বৃদ্ধি পাচ্ছে।
**প্রথম Network:**  10.1.0.0/24
Range: 10.1.0.0 থেকে 10.1.0.255
**দ্বিতীয় Network:**  10.1.1.0/24
Range: 10.1.1.0 থেকে 10.1.1.255
**তৃতীয় Network:**  10.1.2.0/24
Range: 10.1.2.0 থেকে 10.1.2.255
**চতুর্থ Network:**  10.1.3.0/24
Range: 10.1.3.0 থেকে 10.1.3.255
এই চারটি network একসাথে নিচের address range cover করে:
10.1.0.0 থেকে 10.1.3.255
প্রতিটি /24 network-এ 256টি address থাকে।
তাই মোট address সংখ্যা:
256 + 256 + 256 + 256 = 1024 addresses
1024টি address প্রকাশ করার জন্য 10টি host bit দরকার হয়।
যেহেতু IPv4 address মোট 32 bit-এর হয়:
32 − 10 = 22
তাই summarized CIDR notation হবে:
**10.1.0.0/22**
**Final Answer:**
Router Layer = Network Layer / Layer 3
PDU Name = Packet
Supernet = 10.1.0.0/22

☆

43

Computer Network
OSI/TCP-IP

Differentiate between OSI Model and TCP/IP Model. Draw the diagram of 4 Layers of TCP/IP Model including the main function of each layer and related protocols. List some basic functions performed at MAC layer.

Rupali, ANE, 23
| AME/ANE/AE

**OSI vs TCP/IP Model**

**TCP/IP Layer with protocol**
a
**Basic Functions Performed at MAC Layer**

**Frame Encapsulation:**  Converts data into frames for transmission.
**MAC Addressing:**  Uses physical (MAC) addresses to identify devices.
**Error Detection:**  Detects transmission errors using CRC.
**Medium Access Control:**  Controls access to the shared transmission medium.
**Collision Handling:**  Manages data collision in shared networks.
**Frame Synchronization:**  Identifies start and end of data frames.



**OSI vs TCP/IP Model**

**TCP/IP Layer with protocol**

**MAC Layer-এ সম্পাদিত মৌলিক কাজসমূহ**

**Frame Encapsulation:**  Data-কে frame-এ রূপান্তর করে পাঠানো।
**MAC Addressing:**  Physical (MAC) address ব্যবহার করে device শনাক্ত করা।
**Error Detection:**  CRC ব্যবহার করে transmission error শনাক্ত করা।
**Medium Access Control:**  Shared transmission media-তে access নিয়ন্ত্রণ করা।
**Collision Handling:**  Shared network-এ data collision নিয়ন্ত্রণ করা।
**Frame Synchronization:**  Data frame-এর শুরু ও শেষ নির্ধারণ করা।



☆

44

Computer Network
OSI/TCP-IP

Mention the layer of OSI Model and Function of each layer.

Combined Bank, O(IT-22), 26
| Officer (IT)

**OSI Model Layers and Their Functions**
**1. Physical Layer:**  Responsible for the transmission of raw bits over a physical medium. It defines cables, connectors, voltage levels, and data rates.
**2. Data Link Layer:**  Ensures error-free data transfer between two directly connected nodes. It handles framing, error detection, and MAC addressing.
**3. Network Layer:**  Manages logical addressing and routing of data packets across different networks.
**Example:**  IP addressing.
**4. Transport Layer:**  Provides reliable data transfer between end systems. It handles segmentation, flow control, and error recovery.
**Example:**  TCP, UDP.
**5. Session Layer:**  Manages sessions between applications. It establishes, maintains, and terminates communication sessions.
**6. Presentation Layer:**  Translates data formats, handles encryption/decryption, and data compression.
**7. Application Layer:**  Provides network services directly to end users and applications.
**Example:**  HTTP, FTP, SMTP.

**OSI Model-এর Layers এবং তাদের Function**
**1. Physical Layer:**  Physical Layer raw bit গুলোকে physical medium-এর মাধ্যমে transmit করে। এটি cable, connector, voltage level এবং data rate নির্ধারণ করে।
**2. Data Link Layer:**  Data Link Layer দুইটি directly connected device-এর মধ্যে error-free data transfer নিশ্চিত করে। এটি framing, error detection এবং MAC addressing handle করে।
**3. Network Layer:**  Network Layer logical addressing এবং packet routing পরিচালনা করে যাতে data এক network থেকে অন্য network-এ পৌঁছাতে পারে।
**Example:**  IP addressing।
**4. Transport Layer:**  Transport Layer end-to-end reliable data transfer নিশ্চিত করে। এটি segmentation, flow control এবং error recovery পরিচালনা করে।
**Example:**  TCP, UDP।
**5. Session Layer:**  Session Layer application-এর মধ্যে session establish, maintain এবং terminate করে।
**6. Presentation Layer:**  Presentation Layer data format translation, encryption/decryption এবং data compression পরিচালনা করে।
**7. Application Layer:**  Application Layer end user এবং application-এর জন্য সরাসরি network service প্রদান করে।
**Example:**  HTTP, FTP, SMTP।

☆

45

Computer Network
OSI/TCP-IP

In order to prevent that the company decided to add end to end encryption techniques which layer of the OSI model is suitable to work in considering parameters like development time, software maintainability and development cost, Give reasons for your concepts.

BB, AP, 23
| Assistant Programmer

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

☆

46

Computer Network
OSI/TCP-IP

Write down the functionality of OSI model.

CB, AP, 20
| Assistant Programmer

- ☆

47

Computer Network
NAT Concept

What is NAT? Why we used it and how NAT translate?

CB, AE(IT)/AHME/SO, 21
| AME/ANE/AE

**NAT (Network Address Translation)**  is a networking technique used in routers to translate  **private IP addresses**  into a  **public IP address**  before sending data to the Internet.
It allows multiple devices in a private network to access the Internet using a single public IP address.
**Why NAT is Used**

**IP Address Conservation:**  NAT helps save public IPv4 addresses by allowing many devices to share one public IP.
**Security:**  Internal private IP addresses are hidden from external networks, which increases network security.
**Internet Access:**  It allows devices in a private network to communicate with external networks like the Internet.

**How NAT Translation Works**

A device in a private network sends a request to the Internet using its  **private IP address** .
The router replaces the private IP address with its own  **public IP address** .
The request is sent to the destination server on the Internet.
When the response comes back, the router converts the public IP address back to the original  **private IP address**  and sends the data to the correct device.

**NAT (Network Address Translation)**  হলো একটি networking প্রযুক্তি যা router ব্যবহার করে  **private IP address**  কে  **public IP address** -এ রূপান্তর করে Internet-এ data পাঠানোর আগে।
এটি একটি private network-এর একাধিক device-কে একটি public IP ব্যবহার করে Internet ব্যবহার করার সুযোগ দেয়।
**NAT কেন ব্যবহার করা হয়**

**IP Address সংরক্ষণ:**  অনেক device একটি public IPv4 address ব্যবহার করতে পারে, ফলে public IP address সংরক্ষণ করা যায়।
**Security:**  Internal private IP address বাইরে থেকে দেখা যায় না, ফলে network-এর নিরাপত্তা বৃদ্ধি পায়।
**Internet Access:**  Private network-এর device গুলো Internet-এর সাথে যোগাযোগ করতে পারে।

**NAT Translation কীভাবে কাজ করে**

Private network-এর একটি device তার  **private IP address**  ব্যবহার করে Internet-এ request পাঠায়।
Router সেই private IP address-কে নিজের  **public IP address**  দিয়ে প্রতিস্থাপন করে।
Request Internet-এর destination server-এ পাঠানো হয়।
Server থেকে response এলে router আবার public IP-কে মূল  **private IP address** -এ পরিবর্তন করে এবং সঠিক device-এ পাঠিয়ে দেয়।



☆

48

Computer Network
NAT Concept

Network Address Translation (NAT) maps internal networks to the public internet. (a) Explain the historical IP addressing limitation that made NAT a necessity globally. (b) Explain the step-by-step logical translation process that occurs at a branch router when an internal employee (IP 192.168.1.5) sends a web request to an external server, and how the router correctly handles the returning response packet.

Combined Bank, O(IT-23), 26
| Officer (IT)

**Historical Limitation Behind NAT**
NAT became necessary because of the limited number of available IPv4 addresses.
IPv4 uses a 32-bit addressing system, which can provide approximately 4.3 billion unique IP addresses. During the early development of the Internet, this number seemed sufficient. However, as the number of computers, smartphones, servers, IoT devices, and internet users increased rapidly worldwide, IPv4 addresses started running out.
Public IP addresses must be globally unique, but there were not enough addresses for every device connected to the Internet.
To solve this problem, private IP addressing and NAT were introduced.
Using NAT:

Many internal devices can share a single public IP address.
Private IP addresses can be reused in different organizations.
IPv4 address exhaustion is reduced significantly.

Thus, NAT became an important solution for conserving public IPv4 addresses and enabling large-scale Internet growth.
**(b) Step-by-Step NAT Translation Process**
**Scenario:**

Internal Employee IP = 192.168.1.5
Branch Router Public IP = 203.0.113.10
External Web Server IP = 8.8.8.8

**Step 1: Employee Sends Request**
The employee's computer creates a web request packet.
Source IP = 192.168.1.5
Destination IP = 8.8.8.8
Since 192.168.1.5 is a private IP address, it cannot travel directly over the Internet.
**Step 2: Packet Reaches the Branch Router**
The router receives the packet and checks its NAT table.
The router replaces the private source IP address with its own public IP address.
For example:
Before NAT:
Source = 192.168.1.5
Destination = 8.8.8.8
After NAT:
Source = 203.0.113.10
Destination = 8.8.8.8
The router stores this mapping in its NAT translation table.
Example NAT Table Entry:

Private IP
Public IP

192.168.1.5
203.0.113.10

**Step 3: Packet Travels Across the Internet**
The modified packet is sent through the Internet to the external web server.
The web server sees the request coming from the router’s public IP address instead of the private internal address.
**Step 4: External Server Sends Response**
The web server replies to:
Destination IP = 203.0.113.10
The response packet travels back to the branch router.
**Step 5: Router Performs Reverse Translation**
The router checks the NAT table and finds the matching internal device.
It replaces the destination public IP address with the original private IP address.
Before Reverse NAT:
Destination = 203.0.113.10
After Reverse NAT:
Destination = 192.168.1.5
**Step 6: Response Delivered to Employee**
The router forwards the packet to the employee’s computer.
The employee receives the web response correctly even though the internal private IP address was hidden from the Internet.
NAT allows multiple internal devices using private IP addresses to communicate with external networks using a smaller number of public IP addresses. It conserves IPv4 addresses and provides an additional layer of network privacy.



**কোন ঐতিহাসিক IP addressing limitation-এর কারণে NAT বিশ্বব্যাপী প্রয়োজনীয় হয়ে ওঠে তা ব্যাখ্যা কর।**
**NAT-এর প্রয়োজনীয়তার ঐতিহাসিক কারণ**
IPv4 address-এর সীমাবদ্ধতার কারণে NAT প্রয়োজনীয় হয়ে ওঠে。
IPv4 একটি 32-bit addressing system ব্যবহার করে, যা প্রায় 4.3 billion unique IP address প্রদান করতে পারে। Internet-এর শুরুতে এই সংখ্যা যথেষ্ট মনে হলেও পরবর্তীতে computer, smartphone, server, IoT device এবং internet user দ্রুত বৃদ্ধি পাওয়ায় IPv4 address ফুরিয়ে যেতে শুরু করে।
Public IP address অবশ্যই globally unique হতে হয়, কিন্তু Internet-এ যুক্ত প্রতিটি device-এর জন্য পর্যাপ্ত public IP address ছিল না।
এই সমস্যার সমাধানের জন্য private IP addressing এবং NAT চালু করা হয়।
NAT ব্যবহারের ফলে:

একটি public IP address বহু internal device share করতে পারে।
Private IP address বিভিন্ন organization-এ পুনরায় ব্যবহার করা যায়।
IPv4 address exhaustion অনেক কমে যায়।

অতএব, NAT public IPv4 address সংরক্ষণ এবং বৃহৎ Internet expansion সম্ভব করার জন্য অত্যন্ত গুরুত্বপূর্ণ হয়ে ওঠে।
**(b) NAT Translation Process ধাপে ধাপে ব্যাখ্যা**
**Scenario:**

Internal Employee IP = 192.168.1.5
Branch Router Public IP = 203.0.113.10
External Web Server IP = 8.8.8.8

**ধাপ ১: Employee Request পাঠায়**
Employee-এর computer একটি web request packet তৈরি করে。
Source IP = 192.168.1.5
Destination IP = 8.8.8.8
যেহেতু 192.168.1.5 একটি private IP address, তাই এটি সরাসরি Internet-এ যেতে পারে না।
**ধাপ ২: Packet Branch Router-এ পৌঁছে**
Router packet গ্রহণ করে এবং NAT table পরীক্ষা করে।
Router private source IP address-এর পরিবর্তে নিজের public IP address ব্যবহার করে。
উদাহরণ:
NAT-এর আগে:
Source = 192.168.1.5
Destination = 8.8.8.8
NAT-এর পরে:
Source = 203.0.113.10
Destination = 8.8.8.8
Router এই mapping NAT translation table-এ সংরক্ষণ করে।
উদাহরণ NAT Table Entry:

Private IP
Public IP

192.168.1.5
203.0.113.10

**ধাপ ৩: Packet Internet-এর মাধ্যমে যায়**
Modified packet Internet-এর মাধ্যমে external web server-এর কাছে যায়।
Web server request-টিকে router-এর public IP address থেকে এসেছে বলে দেখে।
**ধাপ ৪: External Server Response পাঠায়**
Web server response পাঠায়:
Destination IP = 203.0.113.10
এই response packet branch router-এ ফিরে আসে।
**ধাপ ৫: Router Reverse Translation করে**
Router NAT table পরীক্ষা করে matching internal device খুঁজে বের করে।
এরপর router destination public IP address-এর পরিবর্তে original private IP address বসায়。
Reverse NAT-এর আগে:
Destination = 203.0.113.10
Reverse NAT-এর পরে:
Destination = 192.168.1.5
**ধাপ ৬: Employee-এর কাছে Response পৌঁছে যায়**
Router packet employee-এর computer-এ forward করে。
এভাবে internal private IP Internet থেকে লুকানো থাকলেও employee সঠিক web response পেয়ে যায়।
NAT private IP ব্যবহারকারী বহু internal device-কে সীমিত সংখ্যক public IP ব্যবহার করে Internet-এর সাথে যোগাযোগ করতে সাহায্য করে। এটি IPv4 address সংরক্ষণ করে এবং অতিরিক্ত network privacy প্রদান করে।

- ☆

49

Computer Network
Basic

Ensure secure communication between a client application and the database server.

Sonali Bank, ADA, 24
| ADA

To ensure secure communication between a client application and a database server, the following measures should be taken:

**Encryption (SSL/TLS):**  Use SSL/TLS protocols to encrypt data during transmission.
**Authentication:**  Verify user identity using strong authentication methods (username/password, MFA).
**Authorization:**  Ensure proper access control so users can only access permitted data.
**Use Secure Connections:**  Avoid plain-text connections; always use secure database connections (e.g., HTTPS, secure ports).
**Firewall Protection:**  Restrict database access only to trusted IP addresses.
**Regular Updates:**  Keep database software and security patches up to date.
**VPN:**  Use Virtual Private Network for secure remote access.

Client application এবং database server-এর মধ্যে নিরাপদ যোগাযোগ নিশ্চিত করতে নিচের বিষয়গুলো অনুসরণ করা উচিত:

**Encryption (SSL/TLS):**  Data transmission-এর সময় SSL/TLS ব্যবহার করে data encrypt করা।
**Authentication:**  শক্তিশালী user verification (username/password, MFA) ব্যবহার করা।
**Authorization:**  User যেন শুধুমাত্র অনুমোদিত data access করতে পারে তা নিশ্চিত করা।
**Secure Connection:**  Plain-text connection ব্যবহার না করে secure connection ব্যবহার করা।
**Firewall Protection:**  শুধুমাত্র trusted IP থেকে database access দেওয়া।
**Regular Update:**  Database software এবং security patch update রাখা।
**VPN ব্যবহার:**  Remote access-এর জন্য secure VPN ব্যবহার করা।

☆

50

Computer Network
Basic

Define Computer Network. Describe different types of Computer Networks.

Combined Bank, SO(IT-23), 26
| Senior Officer (IT)

A Computer Network is a group of two or more computers or devices that are connected together to share resources, exchange data, and communicate with each other. The connection can be made using cables, wireless signals, or optical fibers. Networks allow users to share files, printers, internet connections, and applications easily and efficiently.
**Key Features:**

**Resource sharing:**  Multiple users can share hardware and software resources.
**Communication:**  Devices can send messages, emails, and data to each other.
**Cost saving:**  Reduces the need for separate devices for each user.
**Reliability:**  Data can be stored in multiple locations for backup.

**Different Types of Computer Networks**
**1. PAN (Personal Area Network)**
A PAN is a very small network that connects devices around a single person. It covers a short range, usually within a few meters.
**Range:**  Up to 10 meters.
**Example:**  A smartphone connected to wireless earbuds via Bluetooth, or a laptop connected to a wireless mouse.
**2. LAN (Local Area Network)**
A LAN connects computers and devices within a limited area such as a home, school, or office building. It is privately owned and offers high-speed data transfer.
**Range:**  Up to 1 kilometer.
**Example:**  Computers in a university lab connected to the same printer and internet connection.
**3. MAN (Metropolitan Area Network)**
A MAN covers a larger area than a LAN, such as a city or a large campus. It connects multiple LANs together using high-speed connections.
**Range:**  Up to 50 kilometers.
**Example:**  A cable TV network that serves an entire city, or a university connecting all its branches across town.
**4. WAN (Wide Area Network)**
A WAN spans a very large geographical area, such as a country, continent, or even the entire world. It connects multiple LANs and MANs together.
**Range:**  Unlimited, across countries and continents.
**Example:**  The Internet is the largest WAN. A bank connecting all its branches across different countries.
**5. WLAN (Wireless Local Area Network)**
A WLAN is a type of LAN that uses wireless technology (Wi-Fi) instead of cables to connect devices within a local area.
**Range:**  Similar to LAN, but without wires.
**Example:**  Laptops and phones connected to Wi-Fi in a coffee shop or home.
**6. SAN (Storage Area Network)**
A SAN is a specialized network that provides access to consolidated block-level storage. It is mainly used in data centers and enterprises.
**Example:**  A company storing all its data on a central server that multiple departments can access securely.
**Summary Table:**

Type
Full Form
Range
Example

**PAN**
Personal Area Network
Up to 10 meters
Bluetooth earphones with phone

**LAN**
Local Area Network
Up to 1 km
Office computers sharing printer

**MAN**
Metropolitan Area Network
Up to 50 km
City-wide cable TV network

**WAN**
Wide Area Network
Unlimited
The Internet

**WLAN**
Wireless Local Area Network
Up to 1 km (wireless)
Home Wi-Fi network

**SAN**
Storage Area Network
Data center level
Central enterprise data storage

Computer Network হলো দুটি বা ততোধিক computers বা devices-এর একটি group যা resources share, data exchange এবং একে অপরের সাথে communicate করার জন্য connected থাকে। Connection cables, wireless signals বা optical fibers-এর মাধ্যমে করা যেতে পারে। Networks users-কে files, printers, internet connections এবং applications সহজে এবং efficiently share করতে দেয়।
**Key Features:**

**Resource sharing:**  একাধিক users hardware এবং software resources share করতে পারেন।
**Communication:**  Devices একে অপরের কাছে messages, emails এবং data পাঠাতে পারে।
**Cost saving:**  প্রতিটি user-এর জন্য আলাদা devices কেনার প্রয়োজন কমে।
**Reliability:**  Backup-এর জন্য data multiple locations-এ store করা যায়।

**Different Types of Computer Networks**
**1. PAN (Personal Area Network)**
PAN হলো একটি খুব ছোট network যা একটি person-এর চারপাশের devices connect করে। এটি অল্প range cover করে, সাধারণত কয়েক মিটারের মধ্যে।
**Range:**  10 meters পর্যন্ত।
**Example:**  Bluetooth-এর মাধ্যমে smartphone wireless earbuds-এর সাথে connected, বা laptop wireless mouse-এর সাথে connected।
**2. LAN (Local Area Network)**
LAN একটি limited area যেমন home, school বা office building-এর মধ্যে computers এবং devices connect করে। এটি privately owned এবং high-speed data transfer offer করে।
**Range:**  1 kilometer পর্যন্ত।
**Example:**  একটি university lab-এর computers একই printer এবং internet connection share করে।
**3. MAN (Metropolitan Area Network)**
MAN একটি LAN-এর চেয়ে বড় area যেমন city বা large campus cover করে। এটি multiple LANs-কে high-speed connections-এর মাধ্যমে একসাথে connect করে।
**Range:**  50 kilometers পর্যন্ত।
**Example:**  একটি city-তে cable TV network, বা university তার সব branches-কে town জুড়ে connect করে।<
**4. WAN (Wide Area Network)**
WAN একটি very large geographical area যেমন country, continent বা পুরো world জুড়ে বিস্তৃত থাকতে পারে। এটি multiple LANs এবং MANs-কে একসাথে connect করে।
**Range:**  Unlimited, countries এবং continents জুড়ে。<
**Example:**  Internet হলো সবচেয়ে বড় WAN। বিভিন্ন countries-এ branches থাকা একটি bank তাদের সব অফিস connect করে।
**5. WLAN (Wireless Local Area Network)**
WLAN হলো LAN-এর একটি type যা cables ছাড়াই wireless technology (Wi-Fi) ব্যবহার করে local area-তে devices connect করে।
**Range:**  LAN-এর মতোই, কিন্তু wires ছাড়া।
**Example:**  Coffee shop বা home-এ Wi-Fi-এর মাধ্যমে laptops এবং phones connected।<
**6. SAN (Storage Area Network)**
SAN হলো একটি specialized network যা consolidated block-level storage access provide করে। এটি মূলত data centers এবং enterprises-এ ব্যবহৃত হয়।
**Example:**  একটি company তার সব data একটি central server-এ store করে যা multiple departments securely access করতে পারে।
**Summary Table:**

Type
Full Form
Range
Example

**PAN**
Personal Area Network
10 meters পর্যন্ত
Bluetooth earphones phone-এর সাথে

**LAN**
Local Area Network
1 km পর্যন্ত
Office computers printer share করা

**MAN**
Metropolitan Area Network
50 km পর্যন্ত
City-wide cable TV network

**WAN**
Wide Area Network
Unlimited
Internet

**WLAN**
Wireless Local Area Network
1 km পর্যন্ত (wireless)
Home Wi-Fi network

**SAN**
Storage Area Network
Data center level
Central enterprise data storage

- ☆

51

Computer Network
Transport Layer Protocol

Compare TCP and UDP in terms of connection, reliability, and speed. Give one real-life use case of UDP.

Combined Bank, AP-23, 26
| Assistant Programmer

**TCP vs UDP**

TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) are both transport layer protocols, but they serve different purposes based on application requirements.

**1. Connection**

**TCP:**  Connection-oriented. It establishes a connection using a 3-way handshake (SYN, SYN-ACK, ACK) before data transfer begins. The connection is closed gracefully after communication ends.
**UDP:**  Connectionless. It sends data directly without any handshake or setup phase. No formal connection is established or terminated.

**2. Reliability**

**TCP:**  Highly reliable. It guarantees delivery through acknowledgments, retransmissions, and sequence numbers. Lost packets are resent and data arrives in correct order.
**UDP:**  Unreliable. No guarantee of delivery, order, or duplicate protection. Packets may be lost or arrive out of order.

**3. Speed**

**TCP:**  Slower due to handshake, acknowledgments, congestion control, and flow control overhead.
**UDP:**  Faster due to minimal overhead and no retransmission mechanism.

**Comparison Table:**

Feature
TCP
UDP

**Connection**
Connection-oriented (3-way handshake)
Connectionless

**Reliability**
Guaranteed delivery with ACK
No delivery guarantee

**Speed**
Slower
Faster

**Ordering**
In-order delivery
No ordering guarantee

**Error Handling**
Recovery supported
No recovery

**Use Case**
Web, email, file transfer
Streaming, gaming, DNS

**UDP Real-Life Use Case**
**Video Streaming (YouTube Live, Netflix, Twitch)**

UDP is used because low latency is more important than perfect reliability. Dropped frames are skipped instead of retransmitted to maintain smooth playback.

**Online Gaming:**  Real-time updates must be instant; delayed packets are useless.
**DNS Queries:**  Simple request-response with minimal overhead.
**VoIP:**  Voice calls prioritize continuity over perfect delivery.

**TCP vs UDP**

TCP (Transmission Control Protocol) এবং UDP (User Datagram Protocol) উভয়ই transport layer protocol, কিন্তু application অনুযায়ী তাদের ব্যবহার ভিন্ন।

**1. Connection**

**TCP:**  Connection-oriented। 3-way handshake (SYN, SYN-ACK, ACK) দিয়ে connection establish করে। শেষে connection close করা হয়।
**UDP:**  Connectionless। কোনো handshake ছাড়া সরাসরি data পাঠায়।

**2. Reliability**

**TCP:**  Reliable। ACK, retransmission এবং sequence number ব্যবহার করে delivery নিশ্চিত করে।
**UDP:**  Unreliable। Delivery বা order guarantee নেই।

**3. Speed**

**TCP:**  Slower কারণ overhead বেশি।
**UDP:**  Faster কারণ minimal overhead।

**Comparison Table:**

Feature
TCP
UDP

**Connection**
Connection-oriented
Connectionless

**Reliability**
Guaranteed delivery
No guarantee

**Speed**
Slower
Faster

**Ordering**
In-order
No order guarantee

**Error Handling**
Recovery supported
No recovery

**Use Case**
Web, email, file transfer
Streaming, gaming, DNS

**UDP Real-Life Use Case**
**Video Streaming (YouTube Live, Netflix, Twitch)**

UDP ব্যবহার করা হয় কারণ low latency গুরুত্বপূর্ণ। কিছু frame হারিয়ে গেলে retransmit না করে stream continue রাখা হয়।

**Online Gaming:**  Real-time update দরকার, delay useless।
**DNS:**  ছোট request, overhead কম।
**VoIP:**  Smooth conversation জরুরি।

☆

52

Computer Network
Transport Layer Protocol

The primary function of the Transmission control Protocol (TCP) is to turn an unreliable network into a reliable network that is free from lost and duplicate packets. What are the functions performed by TCP to make a network more reliable?


CB, O(IT), 20
| Officer (IT)

**Transmission Control Protocol (TCP)**  is a  **connection-oriented**  Transport Layer protocol that provides reliable, ordered, and error-free data transmission between devices over an unreliable network such as the Internet.
**Functions of TCP**
**1. Connection Establishment**  TCP establishes a reliable connection between the sender and receiver using the  **Three-Way Handshake**  before transmitting data.
**2. Reliable Data Delivery**  TCP uses  **Sequence Numbers**  and  **Acknowledgments (ACK)**  to ensure that all packets are delivered correctly.
**3. Error Detection and Recovery**  TCP uses a  **Checksum**  to detect transmission errors. If an error or packet loss occurs, the lost packet is retransmitted.
**4. Flow Control**  TCP uses the  **Sliding Window**  mechanism to control the amount of data sent, preventing the receiver from being overwhelmed.
**5. Congestion Control**  TCP controls network congestion using techniques such as  **Slow Start** ,  **Congestion Avoidance** , and  **Fast Recovery** .
**6. Ordered Data Delivery**  TCP ensures that data is delivered to the application in the same order in which it was sent.
**7. Duplicate Packet Elimination**  TCP identifies and discards duplicate packets using  **Sequence Numbers** .
**8. Connection Termination**  After communication is complete, TCP gracefully closes the connection using the  **FIN/ACK**  process

☆

53

Computer Network
Transport Layer Protocol

Why does the Domain Name System (DNS) primarily use UDP as its transport layer protocol instead of TCP? Describe the sequence of events that take place during the DNS name resolution process when a user enters www.companybd.com into a web browser and presses Enter.(10 Marks)

Combined Bank, SO-IT, 25
| Senior Officer (IT)

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

☆

54

Computer Network
Transport Layer Protocol

Difference between TCP and UDP, HTTP and HTTPs.

SPCBL, SAME, 22
| AME/ANE/AE

**Difference between HTTP and HTTPS**

**Meaning:**  HTTP = HyperText Transfer Protocol, HTTPS = HyperText Transfer Protocol Secure.
**Security:**  HTTP is not encrypted, HTTPS is encrypted using SSL/TLS.
**Data Protection:**  HTTP data can be intercepted, HTTPS protects against eavesdropping and tampering.
**Port:**  HTTP uses port 80, HTTPS uses port 443.
**Certificate:**  HTTP does not require a certificate, HTTPS requires a digital certificate.

**HTTP এবং HTTPS-এর পার্থক্য**

**Meaning:**  HTTP = HyperText Transfer Protocol, HTTPS = HyperText Transfer Protocol Secure.
**Security:**  HTTP encrypted নয়, HTTPS SSL/TLS ব্যবহার করে encrypted।
**Data Protection:**  HTTP data intercept হতে পারে, HTTPS data কে eavesdropping ও tampering থেকে সুরক্ষা দেয়।
**Port:**  HTTP port 80 ব্যবহার করে, HTTPS port 443 ব্যবহার করে।
**Certificate:**  HTTP certificate চায় না, HTTPS-এর জন্য digital certificate লাগে।



☆

55

Computer Network
Transport Layer Protocol

Difference between TCP and UDP. Distinguish between Cat5 and Cat6. Difference among exFAT, FAT32 and NTFS

CB, O(IT), 23
| Officer (IT)





☆

56

Computer Network
Transport Layer Protocol

Explain Three-Way Handshaking in TCP Protocol.

Sonali, O(it), 21
| Officer (IT)

The  **Three-Way Handshake**  in  **TCP (Transmission Control Protocol)**  is a process used to establish a reliable connection between a client and a server before data transmission begins.
**Steps of the Three-Way Handshake**

**SYN (Synchronize):**
The client (Host P) generates a random sequence number (X) and sends a connection request to the server (Host Q) with the  **SYN flag** , indicating that it wants to establish a connection.
**SYN-ACK (Synchronize-Acknowledgment):**
The server (Host Q) receives the request and responds by selecting its own random sequence number (Y). It sends back a packet containing the  **SYN flag**  and an  **ACK flag**  to acknowledge the client’s sequence number (X + 1).
**ACK (Acknowledgment):**
The client receives the server’s response and sends an acknowledgment packet with the  **ACK flag**  set, confirming the server’s sequence number (Y + 1). After this step, the connection is successfully established

**Three-Way Handshake**  হলো  **TCP (Transmission Control Protocol)** -এ ব্যবহৃত একটি process যার মাধ্যমে client এবং server-এর মধ্যে data transmission শুরু করার আগে একটি reliable connection স্থাপন করা হয়।
**Three-Way Handshake-এর ধাপসমূহ**

**SYN (Synchronize):**
Client (Host P) একটি random  **sequence number (X)**  তৈরি করে এবং  **SYN flag**  সহ server (Host Q)-এর কাছে connection request পাঠায়, যা connection শুরু করার ইঙ্গিত দেয়।
**SYN-ACK (Synchronize-Acknowledgment):**
Server (Host Q) request পাওয়ার পর তার নিজের একটি  **sequence number (Y)**  নির্বাচন করে। এরপর এটি  **SYN flag**  এবং  **ACK flag**  সহ একটি packet পাঠায়, যা client-এর sequence number (X + 1) acknowledge করে।
**ACK (Acknowledgment):**
Client server-এর response পাওয়ার পর  **ACK flag**  সহ একটি acknowledgment packet পাঠায় এবং server-এর sequence number (Y + 1) confirm করে। এরপর connection সম্পূর্ণভাবে establish হয়।



☆

57

Computer Network
Transport Layer Protocol

Compare TCP and UDP protocol with examples.

Combined Bank, O(IT-22), 26
| Officer (IT)

**Examples of TCP:**
Web browsing (HTTP/HTTPS), Email (SMTP), File transfer (FTP).

**Examples of UDP:**
Video streaming, Online gaming, Voice calls (VoIP).

- ☆

58

Computer Network
IP Address

What is IP? Why does need IP in every network?

Pubali, JHE, 23
|

An  **IP (Internet Protocol)**  is a unique logical address assigned to every device connected to a network. It is used to identify devices and enable communication between them over a network or the Internet.

**Why Do We Need an IP Address in Every Network?**

An  **IP Address**  is essential because it allows devices to communicate and exchange data correctly within a network.

• Uniquely identifies every device on the network.
• Enables data packets to reach the correct destination.
• Helps routers determine the best path for data transmission.
• Supports communication between devices on local networks and the Internet.
• Prevents data from being sent to the wrong device.

**Example**

When a computer sends a request to a web server, the  **IP Address**  identifies both the sender and the receiver, ensuring that the data reaches the correct destination.



**IP (Internet Protocol)**  হলো একটি  **Unique Logical Address** , যা Network-এ সংযুক্ত প্রতিটি Device-কে প্রদান করা হয়। এটি Device-কে শনাক্ত (Identify) করে এবং Network বা Internet-এর মাধ্যমে এক Device থেকে অন্য Device-এ Data আদান-প্রদান নিশ্চিত করে।

**প্রতিটি Network-এ IP Address কেন প্রয়োজন?**

**IP Address**  ছাড়া Network-এর Device-গুলো একে অপরকে শনাক্ত করতে এবং সঠিকভাবে যোগাযোগ করতে পারে না।

• প্রতিটি Device-কে  **Unique Identification**  প্রদান করে।
• Data Packet সঠিক Destination-এ পৌঁছাতে সাহায্য করে।
•  **Router** -কে Data-এর সর্বোত্তম Path নির্ধারণ করতে সহায়তা করে।
• Local Network এবং Internet-এ Device-এর মধ্যে Communication নিশ্চিত করে।
• ভুল Device-এ Data পৌঁছানো প্রতিরোধ করে।

**উদাহরণ**

যখন একটি Computer কোনো Web Server-এ Request পাঠায়, তখন  **IP Address**  Sender এবং Receiver উভয়কে শনাক্ত করে, ফলে Data সঠিক Destination-এ পৌঁছে যায়।



☆

59

Computer Network
IP Address

২. (ক) IP address এবং MAC address-এর মাঝে তুলনা করুন।

BPSC_MoHA_AP, 26
| Assistant Programmer (BPSC)

An  **IP Address**  and a  **MAC Address**  are both used to identify devices in a computer network, but they work at different layers and have different purposes.   **IP Address:**  An IP Address is a logical address assigned to a device for identifying the device and determining its location within a network. It is mainly used for routing packets from one network to another.  **MAC Address:**  A MAC Address (Media Access Control Address) is a physical or hardware address associated with a network interface. It is mainly used for communication between devices within the same local network.   **Comparison Table:**

Feature
IP Address
MAC Address

**Full Form**
Internet Protocol Address
Media Access Control Address

**Type**
Logical Address
Physical/Hardware Address

**OSI Layer**
Network Layer (Layer 3)
Data Link Layer (Layer 2)

**Purpose**
Used for logical addressing and routing.
Used for identifying a network interface within a local network.

**Format**
IPv4: 32-bit; IPv6: 128-bit
Usually 48-bit (6 bytes)

**Example**
192.168.1.10
00:1A:2B:3C:4D:5E

**Changeability**
Can change depending on the network or configuration.
Usually assigned to the network interface and is intended to be unique.

**Communication Scope**
Can be used for communication across different networks.
Primarily used for communication within the local network.



**IP Address**  এবং  **MAC Address**  উভয়ই computer network-এ device শনাক্ত করতে ব্যবহৃত হয়। তবে এদের কাজ, address-এর ধরন এবং OSI layer ভিন্ন।   **IP Address:**  IP Address হলো একটি logical address, যা network-এর মধ্যে একটি device-কে শনাক্ত করতে এবং network-এ deviceটির অবস্থান নির্ধারণ করতে ব্যবহৃত হয়। এটি মূলত এক network থেকে অন্য network-এ packet routing-এর জন্য ব্যবহৃত হয়।  **MAC Address:**  MAC Address (Media Access Control Address) হলো একটি physical বা hardware address, যা একটি network interface-এর সাথে যুক্ত থাকে। এটি মূলত একই local network-এর মধ্যে device-to-device communication-এর জন্য ব্যবহৃত হয়।   **তুলনামূলক পার্থক্য:**

বিষয়
IP Address
MAC Address

**পূর্ণরূপ**
Internet Protocol Address
Media Access Control Address

**ধরন**
Logical Address
Physical/Hardware Address

**OSI Layer**
Network Layer (Layer 3)
Data Link Layer (Layer 2)

**উদ্দেশ্য**
Logical addressing এবং routing-এর জন্য ব্যবহৃত হয়।
Local network-এর মধ্যে network interface শনাক্ত করার জন্য ব্যবহৃত হয়।

**Format**
IPv4: 32-bit; IPv6: 128-bit
সাধারণত 48-bit (6 bytes)

**উদাহরণ**
192.168.1.10
00:1A:2B:3C:4D:5E

**পরিবর্তন**
Network বা configuration অনুযায়ী পরিবর্তিত হতে পারে।
সাধারণত network interface-এর সাথে নির্ধারিত থাকে এবং unique হওয়ার জন্য তৈরি করা হয়।

**Communication Scope**
বিভিন্ন network-এর মধ্যে communication-এর জন্য ব্যবহার করা যায়।
মূলত একই local network-এর মধ্যে communication-এর জন্য ব্যবহৃত হয়।

☆

60

Computer Network
IP Address

২(খ) Classful এবং Classless IP Address কী? এদের প্রধান পার্থক্যগুলো কী কী? নিচের IP-গুলোর Class নির্ণয় করুন।
i) 00000001 00001011 00001011 11101111
ii) 211.10.15.4

BPSC_MoHA_AP, 26
| Assistant Programmer (BPSC)

**Classful IP Address:**  Classful IP Addressing হলো এমন একটি IP addressing পদ্ধতি যেখানে IPv4 address-কে পূর্বনির্ধারিত পাঁচটি class-এ ভাগ করা হয়: Class A, Class B, Class C, Class D এবং Class E। IP address-এর class অনুযায়ী network এবং host অংশ নির্ধারিত হয়।  **Classless IP Address:**  Classless IP Addressing, যা CIDR (Classless Inter-Domain Routing) নামেও পরিচিত, হলো এমন একটি IP addressing পদ্ধতি যেখানে network এবং host অংশের boundary নির্দিষ্ট class-এর উপর নির্ভর করে না। বরং subnet mask বা prefix length ব্যবহার করে network অংশ নির্ধারণ করা হয়।  **Classful ও Classless IP Address-এর প্রধান পার্থক্য:**

**Address Division:**  Classful addressing-এ IP address পূর্বনির্ধারিত class অনুযায়ী ভাগ করা হয়, কিন্তু Classless addressing-এ prefix length অনুযায়ী ভাগ করা হয়।
**Subnet Mask:**  Classful addressing-এ default subnet mask ব্যবহার করা হয়, কিন্তু Classless addressing-এ বিভিন্ন subnet mask বা prefix length ব্যবহার করা যায়।
**Address Utilization:**  Classful addressing-এ অনেক IP address অপচয় হতে পারে, কিন্তু Classless addressing-এ IP address আরও দক্ষতার সাথে ব্যবহার করা যায়।
**Flexibility:**  Classful addressing কম flexible, কিন্তু Classless addressing বেশি flexible।
**CIDR Support:**  Classless addressing CIDR support করে, যা efficient IP allocation এবং route aggregation-এর জন্য ব্যবহৃত হয়।

**IP Class Determination:**   **i) 00000001 00001011 00001011 11101111**  First Octet =  **00000001**  The first bit of the first octet is  **0** . A Class A IP address always starts with the binary bit  **0** . Therefore, the given IP address belongs to  **Class A** .  **Answer: Class A**    **বাংলা:**  প্রথম Octet =  **00000001**  প্রথম Octet-এর প্রথম bit হলো  **0** । Class A IP address-এর প্রথম bit সবসময়  **0**  হয়। অতএব, প্রদত্ত IP address-টি  **Class A** ।  **উত্তর: Class A**    **ii) 211.10.15.4**  First Octet =  **211**  The first octet range of Class C is  **192–223** . Since  **211**  falls within this range, the given IP address belongs to  **Class C** .  **Answer: Class C**    **বাংলা:**  প্রথম Octet =  **211**  Class C-এর প্রথম Octet-এর range হলো  **192–223** । যেহেতু  **211**  এই range-এর মধ্যে রয়েছে, তাই প্রদত্ত IP address-টি  **Class C** ।  **উত্তর: Class C**    **Final Answer:**  i) 00000001 00001011 00001011 11101111 →  **Class A**  ii) 211.10.15.4 →  **Class C**

☆

61

Computer Network
IP Address

What is IP address? Explain the necessity of IP address in network?

Pubali, HE, 23
| Bank

**IP Address**
An IP address (Internet Protocol address) is a unique numerical identifier assigned to each device connected to a network. It is used to identify devices and enable communication between them over a network or the Internet.
**Necessity of IP Address in a Network**
An IP address uniquely identifies each device in a network, ensuring that data reaches the correct destination.
It helps in identifying the source and destination of data packets during communication.
Routers use IP addresses to determine the best path for forwarding data across different networks.
IP addresses enable devices to access network resources such as servers, printers, and the Internet.
Without IP addresses, communication between devices in a network would not be possible.
**Example**
When a computer requests a webpage, its IP address is used by the web server to send the requested data back to the correct computer.


**IP Address**
IP address (Internet Protocol address) হলো একটি unique numerical identifier যা network-এ সংযুক্ত প্রতিটি device-কে প্রদান করা হয়, যাতে device-গুলোকে শনাক্ত করা যায় এবং তাদের মধ্যে data আদান-প্রদান সম্ভব হয়।
**Network-এ IP Address-এর প্রয়োজনীয়তা**
IP address প্রতিটি device-কে আলাদাভাবে চিহ্নিত করে, যাতে data সঠিক destination-এ পৌঁছায়।
Data communication-এর সময় source ও destination নির্ধারণ করতে IP address ব্যবহৃত হয়।
Router IP address ব্যবহার করে বিভিন্ন network-এর মধ্যে data পাঠানোর সঠিক পথ নির্বাচন করে।
IP address device-কে server, printer ও Internet-এর মতো resource access করতে সাহায্য করে।
IP address না থাকলে network-এ device-এর মধ্যে যোগাযোগ সম্ভব নয়।
**উদাহরণ**
আপনি যখন কোনো website খুলেন, তখন web server আপনার device-এর IP address ব্যবহার করে সঠিকভাবে data পাঠায়।


☆

62

Computer Network
IP Address

What is IPv6? Why IPv6 needed?

SPCBL, SAME, 22
| AME/ANE/AE

**IPv6 (Internet Protocol version 6)**  is the latest version of the Internet Protocol used to identify devices on a network. It uses a 128-bit address format, allowing a very large number of unique IP addresses.
**Why IPv6 is Needed**

IPv4 address space is almost exhausted.
IPv6 provides a much larger address space.
Improves security with built-in IPsec support.
Supports better routing and network efficiency.

**IPv6**
**IPv6 (Internet Protocol version 6)**  হলো Internet Protocol-এর সর্বশেষ সংস্করণ, যা network-এ device শনাক্ত করতে ব্যবহৃত হয়। এটি 128-bit address ব্যবহার করে, ফলে বিপুল সংখ্যক unique IP address প্রদান করে।
**কেন IPv6 প্রয়োজন**

IPv4 address প্রায় শেষ হয়ে গেছে।
IPv6 অনেক বড় address space প্রদান করে।
Built-in IPsec-এর মাধ্যমে security উন্নত হয়।
Routing এবং network efficiency ভালো হয়।



☆

63

Computer Network
IP Address

Why does IPv6 header architecture faster processing than IPv4 architecture.

RAKUB, ANSE, 26
| AME/ANE/AE

IPv6 header architecture enables faster processing than IPv4 due to several design simplifications that reduce router workload at each hop.

**Fixed header size:**  IPv6 uses a fixed 40-byte header. IPv4 has a variable header length (20 to 60 bytes) because of optional fields, forcing routers to parse and calculate the actual header size every time.
**No header checksum:**  IPv6 removes the header checksum entirely. IPv4 routers must recalculate and verify the checksum at every hop, adding CPU overhead. IPv6 delegates error detection to upper-layer protocols like TCP and UDP.
**No router fragmentation:**  IPv4 allows routers to fragment packets when they are too large, which requires complex reassembly logic. IPv6 only permits fragmentation by the source host, so routers never perform this task.
**Simplified header fields:**  IPv6 has fewer header fields (8 vs 14 in IPv4), making parsing faster. Fields like Header Length, Identification, Flags, Fragment Offset, and Options are removed or relocated to extension headers.
**Extension headers:**  Optional features in IPv6 are placed in separate extension headers that routers can skip unless specifically needed, unlike IPv4 where options are embedded in the main header.

**Comparison Table:**

Feature
IPv4
IPv6

Header size
Variable (20–60 bytes)
Fixed 40 bytes

Header checksum
Yes, recalculated at every hop
Removed

Fragmentation
Routers can fragment
Only source fragments

Header fields
14 fields
8 fields

Options handling
Embedded in main header
Extension headers



**IPv6 Header Architecture and Why It Enables Faster Processing**

IPv6 header design is optimized to reduce router workload at every hop, making packet forwarding faster compared to IPv4. This improvement comes from several structural simplifications in the header format.

**Fixed header size:**  IPv6 uses a fixed 40-byte header. In contrast, IPv4 has a variable header size (20–60 bytes) due to optional fields. This forces routers to calculate and parse header length every time in IPv4, while IPv6 eliminates that overhead.
**No header checksum:**  IPv6 removes the header checksum field completely. In IPv4, routers must recalculate and verify checksum at every hop, increasing CPU usage. IPv6 shifts error detection responsibility to upper-layer protocols like TCP and UDP.
**No router fragmentation:**  In IPv4, routers can fragment packets when they are too large, requiring complex processing and reassembly logic. IPv6 removes this responsibility from routers and allows only the source device to perform fragmentation, simplifying router operations.
**Simplified header fields:**  IPv6 contains fewer header fields (8 fields compared to IPv4’s 14 fields). Fields like Header Length, Identification, Flags, Fragment Offset, and Options are removed or moved to extension headers, reducing parsing complexity.
**Extension headers:**  Optional features in IPv6 are placed in separate extension headers. Routers can skip these unless needed, instead of processing everything in the main header as in IPv4, which improves forwarding efficiency.

**Comparison Table:**

Feature
IPv4
IPv6

Header size
Variable (20–60 bytes)
Fixed 40 bytes

Header checksum
Required, recalculated at each hop
Removed

Fragmentation
Routers can fragment packets
Only source performs fragmentation

Header fields
14 fields
8 fields

Options handling
Embedded in main header
Placed in extension headers

- ☆

64

Computer Network
Definition

৭. (ক) সংজ্ঞা লিখুন: (i) Propagation delay. (ii) Transmission delay.

BPSC_MoHA_AP, 26
| Assistant Programmer (BPSC)

- ☆

65

Computer Network
Difference https & http

৮(গ) HTTP ও HTTPS প্রোটোকলের মধ্যে সুরক্ষার দিক থেকে কোনটি কার্যকর?

BPSC_MoHA_AP, 26
| Assistant Programmer (BPSC)

- ☆

66

Computer Network
Active Directory

Assume that an office has three departments and each department has 50 to 70 employees who are using computers with Windows operating systems. The office space is designed in such a way that an employee can use any computer within a department. Once an employee logs in from a computer, he/she will get access to his files from the server. Let you are planning for network and server setup for this company. **a) What is Active Directory? Do you need an Active Directory for such an office? If yes, briefly explain its use under this circumstance.b) What is subnet? What benefits will you get using subnets for this office?**

Combined Bank, SO(IT), 24
| Senior Officer (IT)

**What is Active Directory?**
Active Directory (AD **)**  is a directory service developed by Microsoft for managing users, computers, and network resources in Windows-based environments. It provides authentication, authorization, and centralized control over network resources.
**Do You Need Active Directory for This Office?**
**Yes** , implementing Active Directory is beneficial for an office with multiple departments and a large number of employees. Since employees can use any computer within their department and still need access to their personal files stored on the server, Active Directory can centrally manage user accounts, authentication, and permissions.

When an employee logs in from any computer, AD verifies their identity and grants access to their files and resources based on their user account.
This eliminates the need to create separate accounts on each computer.
AD also simplifies managing user permissions, ensuring employees access only the resources allowed for their department.
It provides centralized control over security, password policies, and resource sharing, making IT management easier and more secure.

**🎥 Video Solution:**  What is Active Directory? It uses, benefits & structure.
**Subnet**
A subnet (subnetwork) is a smaller part of a larger network. It is created by dividing a large IP network into multiple smaller networks to improve management, performance, and efficient use of network resources.
**Benefits of Using Subnets in an Office**
**Improved Network Performance:**
Subnets reduce network congestion by limiting broadcast traffic, especially when multiple employees access shared resources like file servers.
**Enhanced Security & Access Control:**
Each department can be isolated into its own subnet, preventing unauthorized access between departments and improving overall security.
**Simplified Management & Troubleshooting:**
Network administrators can easily monitor, manage, and troubleshoot issues within a specific department or subnet.
**Efficient IP Address Allocation:**
Subnets allow efficient use of IP addresses by allocating only the required number of IPs to each department and supporting future expansion.
**Flexible Roaming Within Departments:**
Employees can log in from any computer within their department, and subnet-based authentication ensures smooth access to department-specific resources.

- ☆

67

Computer Network
Transmission Mode and Network Performance

How many types of modes are used in data transferring through networks? Briefly explain those modes. Differentiate between TCP vs UDP.

Combined Bank, SO(IT), 24
| Senior Officer (IT)

Data transmission mode is a process by which data is sent from a source to one or more destinations. Simply put, it defines how data flows from one device to another. It is also known as  **Communication Mode** .
**Types of Data Transmission Modes**
**1. Simplex Mode**
- Communication is  **one-way only** .
- Data flows in a single direction, meaning one device can only send data while the other can only receive it.
- No two-way communication.
**Example:**  Keyboard to Computer, Radio, Television.

```
[Source] ----> [Destination]
```

**2. Half-Duplex Mode**
- Data can flow in  **both directions** , but  **only one direction at a time** .
- The entire communication channel is used for sending data in one direction at a time.
- Error detection is possible.
**Example:**  Walkie-Talkie Communication.

```
[Source] ----> [Destination]
[Source] <---- [Destination]
```

**3. Full-Duplex Mode**
- Data  **flows in both directions simultaneously** .
- Both devices can send and receive data at the same time.
- Uses two simplex channels, where one channel sends data in one direction, and the other channel sends data in the opposite direction.
**Example:**  Mobile Phones, Telephones.

```
[Source] <----> [Destination]
```



☆

68

Computer Network
Transmission Mode and Network Performance

Suppose Bangladesh bank is designing a nation of communication network for office located in Dhaka and Rangpur. Their offices are connected via wide area network (WAN). The team needs to ensure that applications with low latency requirements (such as VOIP and video conferencing) can operate efficiently between these offices.         Given:      Distance between Dhaka and Rangpur = 30 km Speed of fiber optic link = 2 × 108 m/s Link capacity = 1 Gbps Average size of data packets = 15,000 bytes Delay at each router/switch along the path = 5 ms RTT between Dhaka and Rangpur = 50 ms       Calculate the total network latency between office at Dhaka and Rangpur, considering the propagation delay and transmission delay.

BB, AD(ICT), 25
| Bangladesh Bank

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

69

Computer Network
Routing Protocol

Apply the concept of IP addressing and routing to explain how packets are delivered across networks using Open Shortest Path First (OSPF) at the network layer.

Combined Bank, AP-22, 26
| Assistant Programmer

**IP Addressing and Routing with OSPF**
IP addressing provides a  **unique logical address**  to every device in a network, which allows packets to be identified and routed to the correct destination. Routing is the process of selecting the best path for these packets to travel across interconnected networks.
**Role of OSPF at the Network Layer**
Open Shortest Path First (OSPF) is a  **link-state routing protocol**  used at the network layer. Each router running OSPF maintains a complete map of the network topology using IP addresses and link information.
**How Packet Delivery Works Using OSPF**

Routers exchange link-state advertisements (LSAs) containing information about their networks and IP subnets.
Each router builds a  **link-state database**  representing the entire network.
OSPF uses the  **Dijkstra shortest path algorithm**  to calculate the best path to every destination IP network based on cost (bandwidth).
The routing table is updated with the shortest paths.
When a packet arrives, the router checks the destination IP address and forwards the packet to the  **next-hop router**  based on the routing table.

**Result**
Using IP addressing for identification and OSPF for intelligent routing, packets are delivered efficiently, reliably, and dynamically across large networks, even when network changes occur.

**OSPF ব্যবহার করে IP Addressing ও Routing**
IP addressing প্রতিটি device কে একটি  **unique logical address**  দেয়, যার মাধ্যমে packet গুলো সঠিক destination এ পৌঁছাতে পারে। Routing হলো এই packet গুলোর জন্য সর্বোত্তম পথ নির্বাচন করার প্রক্রিয়া।
**Network Layer এ OSPF এর ভূমিকা**
Open Shortest Path First (OSPF) হলো একটি  **link-state routing protocol**  যা network layer এ কাজ করে। OSPF চালু থাকা প্রতিটি router IP address ও link information ব্যবহার করে পুরো network এর একটি topology map তৈরি করে।
**OSPF দিয়ে Packet কীভাবে পৌঁছায়**

Router গুলো link-state advertisement (LSA) আদান-প্রদান করে, যেখানে network ও IP subnet এর তথ্য থাকে।
প্রতিটি router একটি  **link-state database**  তৈরি করে, যা পুরো network এর চিত্র দেখায়।
OSPF  **Dijkstra shortest path algorithm**  ব্যবহার করে প্রতিটি destination network এর জন্য সবচেয়ে কম খরচের পথ নির্ধারণ করে।
Routing table আপডেট হয় সর্বোত্তম path দিয়ে।
Packet আসলে router destination IP address দেখে routing table অনুযায়ী পরবর্তী router এ পাঠায়।

**ফলাফল**
IP addressing এবং OSPF routing একসাথে ব্যবহার করে packet দ্রুত, নির্ভরযোগ্য এবং স্বয়ংক্রিয়ভাবে বিভিন্ন network অতিক্রম করে destination এ পৌঁছে যায়, এমনকি network পরিবর্তন হলেও।

☆

70

Computer Network
Routing Protocol

What is Routing? Explain different types of Routing? Why using benefit of an Adhoce routing? Which routing algorithm is used in shortest path algorithm?

CB, O(IT), 23
| Officer (IT)

**1. What is Routing?**
Routing is the process of selecting the best path for data packets to travel from a source device to a destination device across a network using routing algorithms.
**2. Types of Routing**
**(a) Static Routing**
In static routing, routes are manually configured by a network administrator and do not change automatically.
**(b) Dynamic Routing**
In dynamic routing, routers automatically update routing tables using routing protocols such as RIP, OSPF, and BGP.
**(c) Default Routing**
Default routing is used when no specific route is available, and all packets are forwarded to a default gateway.
**(d) Ad Hoc Routing**
Ad hoc routing is used in wireless ad hoc networks where nodes dynamically form routes without fixed infrastructure.
**3. Benefits of Using Ad Hoc Routing**

**No Fixed Infrastructure:**  Works without routers or access points.
**Dynamic Topology:**  Automatically adapts to node movement.
**Fast Deployment:**  Easy to set up in emergency situations.
**Cost Effective:**  No need for expensive networking equipment.

**4. Routing Algorithm Used in Shortest Path**
The  **Dijkstra’s Algorithm**  is used to calculate the shortest path between nodes in a network.
It is widely used by routing protocols such as OSPF to find the most efficient route based on cost.

**১. Routing কী?**
Routing হলো একটি network-এ source device থেকে destination device পর্যন্ত data packet পাঠানোর জন্য সবচেয়ে ভালো path নির্বাচন করার প্রক্রিয়া, যা routing algorithm ব্যবহার করে সম্পন্ন হয়।
**২. Routing-এর ধরন**
**(a) Static Routing**
Static routing-এ network administrator নিজে হাতে route নির্ধারণ করে দেয় এবং এটি স্বয়ংক্রিয়ভাবে পরিবর্তিত হয় না।
**(b) Dynamic Routing**
Dynamic routing-এ router স্বয়ংক্রিয়ভাবে routing table update করে এবং RIP, OSPF, BGP-এর মতো routing protocol ব্যবহার করে।
**(c) Default Routing**
Default routing তখন ব্যবহৃত হয় যখন নির্দিষ্ট কোনো route পাওয়া যায় না এবং সব packet default gateway-এ পাঠানো হয়।
**(d) Ad Hoc Routing**
Ad hoc routing wireless ad hoc network-এ ব্যবহৃত হয়, যেখানে কোনো fixed infrastructure ছাড়াই node গুলো নিজেরাই route তৈরি করে।
**৩. Ad Hoc Routing ব্যবহারের সুবিধা**

**Fixed Infrastructure প্রয়োজন নেই:**  Router বা access point ছাড়াই কাজ করে।
**Dynamic Topology:**  Node চলাচলের সাথে সাথে route পরিবর্তন হয়।
**দ্রুত স্থাপন:**  Emergency বা disaster পরিস্থিতিতে দ্রুত network তৈরি করা যায়।
**খরচ কম:**  আলাদা networking equipment প্রয়োজন হয় না।

**৪. Shortest Path-এ ব্যবহৃত Routing Algorithm**
**Dijkstra’s Algorithm**  network-এর মধ্যে shortest path নির্ণয়ের জন্য ব্যবহৃত হয়.
OSPF-এর মতো routing protocol এই algorithm ব্যবহার করে সবচেয়ে কম cost-এর route নির্বাচন করে।

- ☆

71

Computer Network
Error Detection

Explain the logic of a "Checksum". How is it used to verify data integrity during file transfer?

Combined Bank, AP-22, 26
| Assistant Programmer

**Logic of a Checksum**
A checksum is a small, fixed-size value calculated from a block of data using a mathematical algorithm. It represents a summary of the data and is used to detect errors that may occur during data transmission or storage.
**How a Checksum Works**

1) The sender divides the data into fixed-size blocks (such as bytes or words).
2) These blocks are added together (or processed using a checksum algorithm).
3) The final result is the checksum value, which is sent along with the data.

**Verification During File Transfer**

• The receiver recalculates the checksum from the received data using the same algorithm.
• The newly calculated checksum is compared with the checksum sent by the sender.
• If both values match, the data is assumed to be intact.
• If they do not match, it indicates that the data was corrupted during transmission.

**Purpose**
Checksums provide a simple and fast way to ensure  **data integrity** , helping detect transmission errors in file transfers.

**Checksum এর Logic**
Checksum হলো একটি ছোট, নির্দিষ্ট আকারের value যা একটি data block থেকে গাণিতিকভাবে হিসাব করা হয়। এটি data এর একটি summary হিসেবে কাজ করে এবং data transmission বা storage এর সময় কোনো error হয়েছে কিনা তা শনাক্ত করতে ব্যবহৃত হয়।
**Checksum কীভাবে কাজ করে**

1) Sender data কে ছোট ছোট block এ ভাগ করে।
2) প্রতিটি block যোগ করে (বা checksum algorithm ব্যবহার করে) একটি মান বের করা হয়।
3) এই মানটিই checksum, যা data এর সাথে পাঠানো হয়।

**File Transfer এ Verification**

• Receiver প্রাপ্ত data থেকে একই algorithm ব্যবহার করে checksum পুনরায় গণনা করে।
• Sender পাঠানো checksum এর সাথে receiver এর checksum তুলনা করা হয়।
• দুইটি মান মিললে data ঠিক আছে ধরা হয়।
• মিল না হলে বোঝা যায় data transmission এর সময় corrupted হয়েছে।

**উদ্দেশ্য**
Checksum দ্রুত এবং সহজভাবে  **data integrity**  নিশ্চিত করতে সাহায্য করে এবং file transfer এর সময় error শনাক্ত করে।

- ☆

72

Computer Network
OSI/TCP-iP

Synthia wants to send an email to her friend. He sends the email through the application and transport layer. **(a)Mention the protocol of application layer and transport layer(b)Draw a diagram from the above scenario.**

BB, AD(ICT), 25
| Bangladesh Bank

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

73

Computer Network
Flow Control Protocol

A satellite link has a one way propagation delay of 250 ms and a transmission rate 1 Mbps. Frame size 1000 bytes , calculate utilization efficiency if stop-and-wait protocol is used what is minimum window size required to achieve 100% efficiency.

RAKUB, ANSE, 26
| AME/ANE/AE

Given:    One-way propagation delay (Tp) = 250 ms = 0.25 s    Transmission rate (Bandwidth) = 1 Mbps = 106 bits/s    Frame size = 1000 bytes = 1000 × 8 = 8000 bits    Protocol: Stop-and-WaitStep 1: Calculate Transmission Time (Tt)
Tt = Frame size ÷ Bandwidth Tt = 8000 bits ÷ 106 bits/s = 0.008 s = 8 ms
Step 2: Calculate Round Trip Time (RTT)
RTT = 2 × Tp = 2 × 250 ms = 500 ms
Step 3: Calculate Efficiency (Utilization) for Stop-and-Wait
Efficiency = Tt ÷ (Tt + RTT)
Efficiency = 8 ÷ (8 + 500) = 8 ÷ 508
= 0.0157 Efficiency = 1.57%
Step 4: Calculate Minimum Window Size for 100% Efficiency For 100% efficiency, the sender must keep the channel fully utilized. This means the window size must be large enough so that the total transmission time of all frames in the window equals or exceeds the RTT.
Window size (N) = RTT ÷ Tt N = 500 ÷ 8 = 62.5 N = 63 frames (rounded up to the nearest whole number)
Alternatively, using the formula: Efficiency = (N × Tt) ÷ (Tt + RTT)
For 100% efficiency: N × Tt ≥ Tt + RTT N ≥ (Tt + RTT) ÷ Tt = (8 + 500) ÷ 8 = 63.5 N = 63 or 64 framesReference:

☆

74

Computer Network
Flow Control Protocol

Using an explanation of the difference between flow-control and congestion  control, Discuss the impact of a stable end-to-end latency.

Combined Bank, O(IT), 24
| Officer (IT)

**Flow-Control vs Congestion Control**

**Flow-Control:**  Flow-control manages the rate of data transmission between a sender and receiver to prevent the receiver's buffer from overflowing. It ensures the sender does not overwhelm the receiver.
**Congestion Control:**  Congestion control manages the overall traffic in the network to prevent network congestion. It reduces the sending rate when the network is overloaded to avoid packet loss and high delays.

**Impact of Stable End-to-End Latency**
Stable latency ensures that the time taken for data to travel from source to destination remains consistent, even under varying network loads.

**Improved QoS:**  Real-time applications like VoIP and video conferencing rely on consistent latency for smooth performance.
**Reduced Jitter:**  Low variation in latency leads to smoother audio and video playback.
**Efficient Flow-Control:**  Predictable latency helps flow-control algorithms maintain optimal data rates without overwhelming the receiver.
**Effective Congestion Control:**  With stable latency, network devices can detect congestion accurately and react appropriately, preventing unnecessary packet drops or retransmissions.
**Reliable Real-Time Systems:**  Industrial automation and control systems benefit from predictable delays, ensuring timely and safe operations.

**Flow-Control বনাম Congestion Control**

**Flow-Control:**  Flow-control sender এবং receiver-এর মধ্যে data transmission rate নিয়ন্ত্রণ করে, যাতে receiver-এর buffer overflow না হয়। এটি নিশ্চিত করে যে sender receiver-কে overwhelm করবে না।
**Congestion Control:**  Congestion control পুরো network-এ traffic নিয়ন্ত্রণ করে, যাতে network congested না হয়। Network overload হলে এটি sending rate কমায়, packet loss এবং high delays এড়াতে।

**Stable End-to-End Latency-এর প্রভাব**
Stable latency নিশ্চিত করে যে source থেকে destination পর্যন্ত data travel time ধ্রুবক থাকে, এমনকি network load পরিবর্তিত হলেও।

**Improved QoS:**  VoIP এবং video conferencing-এর মতো real-time applications smooth performance পায় consistent latency-র মাধ্যমে।
**Reduced Jitter:**  Latency variation কমলে smoother audio এবং video playback হয়।
**Efficient Flow-Control:**  Predictable latency flow-control algorithm-কে সাহায্য করে optimal data rate maintain করতে এবং receiver overwhelm হওয়া রোধ করতে।
**Effective Congestion Control:**  Stable latency থাকলে network devices congestion সঠিকভাবে detect করে এবং উপযুক্তভাবে react করে, unnecessary packet drop বা retransmission এড়াতে।
**Reliable Real-Time Systems:**  Industrial automation এবং control systems predictable delay-এর সুবিধা পায়, timely এবং safe operation নিশ্চিত হয়।

- ☆

75

Computer Network
Subnettingx

A core router receives a packet with destination IP address  **192.168.20.45** . The router's forwarding table contains the following overlapping routes:      192.168.0.0/16 192.168.16.0/20 192.168.20.0/22 192.168.20.32/25       Identify the exact routing interface the router will use to forward this packet

RAKUB, ANSE, 26

| AME/ANE/AE

**Given:**
Destination IP: 192.168.20.45
**Routing Table Entries:**
192.168.0.0/16
192.168.16.0/20
192.168.20.0/22
192.168.20.32/25

**Step 1: Check Each Route for Match**
A packet matches a route when the destination IP is ANDed with the subnet mask and the result equals the network address.

Route
Match?

192.168.0.0/16
Yes

192.168.16.0/20
Yes

192.168.20.0/22
Yes

192.168.20.32/25
Yes

**Step 2: Apply Longest Prefix Match Rule**
When multiple routes match, the router selects the route with the longest subnet prefix (the most specific network).

Route
Prefix Length

192.168.0.0/16
16

192.168.16.0/20
20

192.168.20.0/22
22

192.168.20.32/25
25 ← Longest

**Final Answer:**
The router will forward the packet using the route  **192.168.20.32/25**  because it has the longest prefix match (25 bits), making it the most specific route available.
**Why This Rule Exists:**
Longest Prefix Match ensures that traffic follows the most precise route. A /25 network covers a smaller and more specific range of addresses than a /16 network. Therefore, when both routes match, the router chooses the more specific route to deliver the packet accurately.

- ☆

76

Computer Network
Protocol

A corporate network pool experience IP exhaustion due to a high volume of transient guest devices. What lease duration parameter adjustment resolves this?

RAKUB, ANSE, 26
| AME/ANE/AE

**Problem:**  A corporate network pool experiences IP exhaustion due to a high volume of transient guest devices.
**Root Cause:**  Guest devices connect briefly (minutes or hours), but the DHCP server assigns IP addresses with long lease durations (days or weeks). These IPs remain reserved even after devices disconnect, which quickly exhausts the available address pool.
**Solution:**   **Reduce the DHCP lease duration**  for guest networks to a shorter period — typically  **2 to 4 hours** .
**How It Works:**

**Shorter lease:**  When a guest disconnects, the IP address returns to the available pool within hours instead of remaining locked for days.
**Faster recycling:**  Freed IPs can be reassigned quickly to new guest devices, improving utilization of the address pool.
**Balanced timing:**  If the lease is too short (e.g., under 30 minutes), it increases DHCP renewal traffic. If too long, IP exhaustion remains unresolved.

**Additional Measures:**

**Separate VLANs:**  Isolate guest traffic into a dedicated network segment to protect corporate resources and simplify management.
**Smaller subnets for guests:**  Use appropriately sized subnets (e.g., /23 or /22) to ensure sufficient address capacity for high-density environments.
**MAC address filtering:**  Limit the number of IPs a single device or user can consume to prevent abuse.


**Problem:**
Corporate network pool IP exhaustion experience করছে transient guest devices-এর high volume-এর কারণে।

**Root Cause:**
Guest devices briefly connect করে (minutes বা hours), কিন্তু DHCP server তাদের long lease durations (days বা weeks)-এর জন্য IP addresses assign করে। Guests চলে গেলেও এসব IP addresses reserved থাকে, ফলে reuse করা যায় না এবং pool দ্রুত exhausted হয়ে যায়।

**Solution:**
**DHCP lease duration কমিয়ে**  guest networks-এর জন্য shorter time period রাখা — সাধারণত  **2 থেকে 4 hours** ।

**কীভাবে কাজ করে:**

**Shorter lease:**  Guest disconnect করলে IP address days-এর পরিবর্তে hours-এর মধ্যে আবার available pool-এ ফিরে আসে।
**Faster recycling:**  DHCP server freed IPs দ্রুত নতুন guest devices-কে assign করতে পারে।
**Balanced timing:**  খুব কম (30 minutes-এর নিচে) lease দিলে excessive DHCP renewal traffic তৈরি হয়, আর খুব বেশি হলে IP exhaustion সমাধান হয় না।

**Additional Measures:**

**Separate VLANs:**  Guest traffic dedicated subnet-এ isolate করে corporate network resources protect করা হয়।
**Smaller subnets for guests:**  /23 বা /22 subnet ব্যবহার করে IP capacity বাড়ানো যায় main corporate pool affect না করে।
**MAC address filtering:**  একটি device কতগুলো IP consume করতে পারবে তা limit করে misuse prevent করা যায়।

- ☆

77

Computer Network
Difference

Write down the basic differences of the following: (i) Public vs Private IP address  (ii) TLS 1.2 vs. 1.3

Rupali, ANE, 23
| AME/ANE/AE

**(i) Difference between Public IP Address and Private IP Address**

Aspect
Public IP Address
Private IP Address

Definition
An IP address that is accessible over the internet
An IP address used within a private network

Uniqueness
Globally unique
Not globally unique

Internet Access
Directly accessible from the internet
Not directly accessible from the internet

Assignment
Assigned by ISP
Assigned by local network administrator

Example
8.8.8.8
192.168.1.1

**(ii) Difference between TLS 1.2 and TLS 1.3**

Aspect
TLS 1.2
TLS 1.3

Release Year
2008
2018

Handshake Process
Multiple round trips
Fewer round trips

Security
Secure but uses older algorithms
More secure with modern cryptography

Performance
Slower
Faster

Cipher Suites
Supports many legacy ciphers
Removes insecure cipher suites



**(i) Public IP Address ও Private IP Address-এর পার্থক্য**

বিষয়
Public IP Address
Private IP Address

সংজ্ঞা
Internet-এ ব্যবহৃত IP address
Private network-এর ভেতরে ব্যবহৃত IP address

Uniqueness
বিশ্বব্যাপী unique
বিশ্বব্যাপী unique নয়

Internet Access
Internet থেকে সরাসরি access করা যায়
Internet থেকে সরাসরি access করা যায় না

Assignment
ISP দ্বারা দেওয়া হয়
Local network administrator দ্বারা দেওয়া হয়

উদাহরণ
8.8.8.8
192.168.1.1

**(ii) TLS 1.2 ও TLS 1.3-এর পার্থক্য**

বিষয়
TLS 1.2
TLS 1.3

প্রকাশের সাল
2008
2018

Handshake Process
একাধিক round trip লাগে
কম round trip লাগে

Security
নিরাপদ কিন্তু পুরোনো algorithm ব্যবহার করে
আধুনিক cryptography ব্যবহারে বেশি নিরাপদ

Performance
ধীর
দ্রুত

Cipher Suite
Legacy cipher সমর্থন করে
Insecure cipher বাদ দেওয়া হয়েছে

- ☆

78

Computer Network
Packetization delay

One of the drawbacks of a small packet size is that a large fraction of link bandwidth is consumed by overhead bytes. To this end, suppose that the packet consists of P bytes and 5 bytes of header. Consider sending a digitally encoded voice source directly. Suppose the source is encoded at a constant rate of 128 kbps. Assume each packet is entirely filled before the source sends the packet into the network. The time required to fill a packet is the packetization delay. Determine the packetization delay for length L = 1500 bytes (roughly corresponding to maximum-sized Ethernet packet).

BB, AME, 23
| AME/ANE/AE

**Determine the Payload Size**
The payload size is the part of a packet that excludes the header.
**Payload Size = Total Packet Size − Header Size**
Given:
Total Packet Size = 1500 bytes
Header Size = 5 bytes
**Payload Size = 1500 − 5 = 1495 bytes**
**Convert Payload Size to Bits**
Since data rate is given in bits per second, payload size must be converted to bits.
**Payload Size (bits) = 1495 × 8 = 11,960 bits**
**Calculate Packetization Delay**
Packetization delay is the time needed to fill a packet with data.
**Packetization Delay = Packet Length (bits) / Source Data Rate**
Packet Length = 12,000 bits
Source Data Rate = 128,000 bps
**Packetization Delay = 12,000 / 128,000 = 0.09375 s = 93.75 ms**
**Calculate Transmission Time**
Transmission time is the time required to send the payload over the network.
**Transmission Time = Payload Size (bits) / Data Rate**
**Transmission Time = 11,960 / 128,000 = 0.0934375 s = 93.4375 ms**

**Payload Size:**  11,960 bits
**Packetization Delay:**  93.75 milliseconds
**Transmission Time:**  93.4375 milliseconds

**Payload Size নির্ধারণ**
Payload size হলো packet-এর সেই অংশ যেখানে header বাদ দেওয়া হয়।
**Payload Size = Total Packet Size − Header Size**
প্রদত্ত:
Total Packet Size = 1500 bytes
Header Size = 5 bytes
**Payload Size = 1500 − 5 = 1495 bytes**
**Payload Size কে Bits-এ রূপান্তর**
Data rate bits per second-এ দেওয়া থাকায় payload size bits-এ রূপান্তর করতে হবে।
**Payload Size (bits) = 1495 × 8 = 11,960 bits**
**Packetization Delay নির্ণয়**
Packetization delay হলো packet পূর্ণ হতে যে সময় লাগে।
**Packetization Delay = Packet Length (bits) / Source Data Rate**
Packet Length = 12,000 bits
Source Data Rate = 128,000 bps
**Packetization Delay = 12,000 / 128,000 = 0.09375 s = 93.75 ms**
**Transmission Time নির্ণয়**
Transmission time হলো payload network দিয়ে পাঠাতে যে সময় লাগে।
**Transmission Time = Payload Size (bits) / Data Rate**
**Transmission Time = 11,960 / 128,000 = 0.0934375 s = 93.4375 ms**

**Payload Size:**  11,960 bits
**Packetization Delay:**  93.75 milliseconds
**Transmission Time:**  93.4375 milliseconds

- ☆

79

Computer Network
Others

Draw A class diagram. A token-ring based local area network (LAN) is a network consisting of nodes in which network packets are sent around. Every node has a unique name within the network, and refers to its next node. Different kinds of nodes exist: Workstations are originators of messages; servers and printers are network nodes that can receive messages. Packets contain an originator a destination and content, and are sent around on a network. A LAN is a circular configuration of nodes.

BB, AP, 23
| Assistant Programmer

[source:visual-paradigm.com]
