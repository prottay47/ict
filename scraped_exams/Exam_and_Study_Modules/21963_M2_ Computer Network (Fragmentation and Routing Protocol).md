# M2: Computer Network (Fragmentation and Routing Protocol)

- **Original URL:** [https://it.jobqns.com/m2-computer-network-fragmentation-and-routing-protocol/](https://it.jobqns.com/m2-computer-network-fragmentation-and-routing-protocol/)
- **Date:** 2026-08-29T16:54:34
- **Categories:** Uncategorized, IT Preparation Module

---

**Computer Network**  Fragmentation and Routing Protocol (ET: 1.5 Hours)



**Video Tutorial:**  Fragmentation and Routing Protocol



- **Watch Video:**  Fragmentation in Computer Networks: Concepts and Mechanisms

- **Watch Video:**   Fragmentation and IPV4 Frame Examples

- **Watch Video:**   Static Routing vs Dynamic Routing

- **Watch Video:**   Distance Vector VS Link State Routing

Fragmentation and Routing Protocol

- 1

Fragmentation in Network Layer


**Fragmentation**  is the process of dividing a large IP datagram into smaller fragments so that it can be transmitted through a network whose  **Maximum Transmission Unit (MTU)**  is smaller than the size of the original packet.
IPv4 can have a maximum packet size of  **216 − 1 = 65,535 bytes** , because the Total Length field is 16 bits. However, the Data Link Layer may support a smaller MTU. For example,  **Ethernet MTU = 1500 bytes** . Therefore, a large IP packet may need to be fragmented before forwarding.
**Why is Fragmentation Required?**
Fragmentation is required when the size of an IPv4 packet is greater than the  **MTU**  of the outgoing network. The router divides the original datagram into smaller fragments that can fit within the available MTU.
**Important IPv4 Fragmentation Fields:**
**Identification (ID):**  A unique value used to identify fragments belonging to the same original IP datagram. All fragments of one original packet have the  **same Identification value** .
**DF (Don't Fragment) Flag:**  If  **DF = 1** , fragmentation is not allowed. If the packet is larger than the outgoing MTU, the router cannot forward it and must drop it.
**MF (More Fragments) Flag:**  If  **MF = 1** , more fragments are still to follow. The  **last fragment has MF = 0** .
**Fragment Offset:**  It indicates the position of a fragment's data within the original datagram. The Fragment Offset field is  **13 bits** . The offset is represented in units of  **8 bytes** , so fragment payload sizes (except the last fragment) must be multiples of 8 bytes.
**Key Formula for Fragment Offset:**
**Fragment Offset = Starting Byte of Fragment ÷ 8**
**Example:**  If the first fragment contains  **3976 bytes** , then the next fragment starts at byte  **3976** .
Therefore:
**3976 ÷ 8 = 497**
So, the Fragment Offset of the second fragment is  **497** .
**Important Numerical Example:**
Suppose the original IP packet contains  **10,000 bytes of payload** . It can be fragmented into:
**3976 + 3976 + 2048 = 10,000 bytes**
The three fragments will have:
**Fragment 1:**  Payload = 3976 bytes, Offset = 0, MF = 1
**Fragment 2:**  Payload = 3976 bytes, Offset = 497, MF = 1
**Fragment 3:**  Payload = 2048 bytes, Offset = 994, MF = 0
All three fragments have the  **same Identification (ID)** .
**Why 3976 Bytes?**
The minimum IPv4 header size is  **20 bytes** . If the MTU is 4000 bytes, the maximum payload would initially appear to be:
**4000 − 20 = 3980 bytes**
But  **3980 is not divisible by 8** . Since the Fragment Offset uses 8-byte units, the payload must be reduced to  **3976 bytes** .
**3976 ÷ 8 = 497**
Therefore, 3976 bytes is used instead of 3980 bytes for the fragment payload.

2

Consider an IP packet with a length of 4500 bytes that includes a 20-Byte IPV4 header and a 40-byte TCP header. The packet is forwarded to an IPV4 router that supports a maximum transmission unit (MTU) of 600 bytes. Assume that the length of the IP header in all the outgoing fragments of this packet is 20 bytes. Assume that the fragmentation offset value stored in the first fragment is 0. The fragmentation offset value stored in the third fragment is


**Given:**
Total IP Packet Length =  **4500 bytes**
IPv4 Header =  **20 bytes**
TCP Header =  **40 bytes**
MTU =  **600 bytes**
First Fragment Offset =  **0**
**Step 1: Calculate IP Payload**
IP Payload = Total IP Packet Length − IP Header
IP Payload = 4500 − 20
**IP Payload = 4480 bytes**
**Note:**  The 40-byte TCP header is already included inside the IP payload, so it is not subtracted separately.
**Step 2: Calculate Maximum Data per Fragment**
Maximum Data = MTU − IP Header
Maximum Data = 600 − 20
=  **580 bytes**
Since the Fragment Offset is measured in units of  **8 bytes** , the data size of each fragment (except the last) must be divisible by 8.
580 is not divisible by 8, so:
**Maximum Fragment Data = 576 bytes**
**Step 3: Calculate Fragment Offsets**
**1st Fragment:**
Starting Byte = 0
Fragment Offset = 0 ÷ 8 =  **0**
**2nd Fragment:**
Starting Byte = 0 + 576 =  **576**
Fragment Offset = 576 ÷ 8 =  **72**
**3rd Fragment:**
Starting Byte = 576 + 576 =  **1152**
Fragment Offset = 1152 ÷ 8 =  **144**
**Therefore:**
**Fragmentation Offset Value in the Third Fragment = 144**
**Final Answer: 144**

3

The maximum number of IPV4 router address addresses that can be listed in the record route (RR) option field of an IPV4 header is


The IPv4 header option field can have a maximum length of  **40 bytes** . In the Record Route option,  **3 bytes**  are used for the option type, length, and pointer fields. Each IPv4 address requires  **4 bytes** .

Therefore:
**(40 − 3) / 4 = 37 / 4 = 9**

Hence, the maximum number of IPv4 router addresses that can be recorded is  **9** .

4

An IP datagram of size 1000 bytes arrives at a router. The router has to forward this packet on a link whose MTU (Maximum Transmission Unit) is 100 bytes. Assume that the size of the IP header is 20 bytes. The number of fragments that the IP datagram will be divided into for transmission is


**Given:**

IP Datagram Size =  **1000 bytes**
MTU =  **100 bytes**
IP Header Size =  **20 bytes**

**Step 1: Calculate the data size**
Data Size = Total Datagram Size − Header Size
Data Size = 1000 − 20 =  **980 bytes**
**Step 2: Calculate the maximum data size per fragment**
Each fragment must fit within the MTU of 100 bytes.
Maximum data per fragment = MTU − Header Size
= 100 − 20 =  **80 bytes**
**Step 3: Calculate the number of fragments**
Number of fragments = 980 / 80
= 12.25
Since the last fragment can contain the remaining data, we need  **13 fragments** .

5

Distance Vector Routing


**Distance Vector Routing**  is a routing algorithm in which a router determines the best path based mainly on information received from its  **neighboring routers** .
The term  **Distance Vector**  has two parts:
**Distance**  means the cost or distance required to reach a destination. The distance may be measured using metrics such as  **hop count** .
**Vector**  means the direction or  **next-hop router**  through which the destination can be reached.
In Distance Vector Routing, each router maintains a routing table containing information about the destination, distance/cost, and next hop.
**Example:**  If Router R1 sends a packet through Router R4 to reach Router R5, then R4 can be considered the  **next-hop router**  and the associated cost represents the  **distance** .
**Algorithm Used:**  Bellman-Ford Algorithm
**Common Protocols:**  RIP (Routing Information Protocol) and IGRP (Interior Gateway Routing Protocol).
**Working of Distance Vector Routing:**

1. Each router creates and maintains its routing table.
2. The router identifies its directly connected or neighboring routers.
3. The router determines the distance or cost to its neighboring routers.
4. Routers exchange routing information with their neighboring routers.
5. Each router updates its routing table based on the information received from its neighbors.
6. The process is repeated until the routers find the best available paths.
7. The shortest or lowest-cost path is selected for packet forwarding.

**Characteristics of Distance Vector Routing:**

• Uses information mainly about neighboring routers.
• Uses the  **Bellman-Ford algorithm** .
• Routing information is exchanged periodically with neighbors.
• Convergence is relatively slow.
• It may suffer from the  **Count-to-Infinity problem** .
• It generally requires less network information than Link State Routing.

**Distance Vector Routing**  হলো এমন একটি Routing Algorithm যেখানে Router মূলত তার  **প্রতিবেশী Router বা Neighbor Router**  থেকে পাওয়া তথ্য ব্যবহার করে Destination-এর জন্য সর্বোত্তম পথ নির্ধারণ করে।
**Distance**  বলতে Destination-এ পৌঁছানোর জন্য প্রয়োজনীয় Cost বা দূরত্ব বোঝায়। এটি সাধারণত  **Hop Count**  দ্বারা পরিমাপ করা যেতে পারে।
**Vector**  বলতে Destination-এ যাওয়ার Direction বা  **Next-Hop Router**  বোঝায়।
Distance Vector Routing-এ প্রতিটি Router একটি Routing Table সংরক্ষণ করে। এই Table-এ সাধারণত Destination, Distance/Cost এবং Next Hop-এর তথ্য থাকে।
**Algorithm:**  Bellman-Ford Algorithm
**প্রধান Protocol:**  RIP (Routing Information Protocol) এবং IGRP (Interior Gateway Routing Protocol)।
**Distance Vector Routing-এর কার্যপ্রণালী:**

১. প্রতিটি Router তার Routing Table তৈরি ও সংরক্ষণ করে।
২. Router তার সরাসরি সংযুক্ত Neighbor Router শনাক্ত করে।
৩. Neighbor Router-এর কাছে পৌঁছানোর Distance বা Cost নির্ধারণ করে।
৪. Router তার Neighbor-এর সাথে Routing Information আদান-প্রদান করে।
৫. Neighbor থেকে পাওয়া তথ্য অনুযায়ী Routing Table Update করে।
৬. এই প্রক্রিয়া বারবার চলতে থাকে যতক্ষণ না সর্বোত্তম Path নির্ধারিত হয়।
৭. সর্বনিম্ন Cost বা Shortest Path Packet Forward করার জন্য নির্বাচন করা হয়।

**Distance Vector Routing-এর বৈশিষ্ট্য:**

• প্রধানত Neighbor Router-এর তথ্য ব্যবহার করে।
• Bellman-Ford Algorithm ব্যবহার করে।
• Neighbor Router-এর সাথে Routing Information Exchange করে।
• Convergence তুলনামূলকভাবে ধীর।
• Count-to-Infinity Problem হতে পারে।
• Link State Routing-এর তুলনায় সাধারণত কম Network Information প্রয়োজন হয়।

6

Consider a network consisting of  **5 routers: A, B, C, D, and E**  connected with the following direct edge costs:

**1.**  Construct the initial routing table for  **Router A**  containing Destination, Distance, and Next Hop.
**2.**  Assume Router E shares its distance vector table with Router A. Construct  **Router E's routing table** .
**3.** Calculate and construct the updated routing table for  **Router A**  after receiving updates from Router E using the Bellman-Ford equation.

**Step 1: Initial Routing Table of Router A**
Router A has a direct connection only with Router E, and the cost of  **A → E = 5** . Therefore, the other routers are initially considered unreachable from A.

Destination
Distance
Next Hop

A
0
—

B
∞
—

C
∞
—

D
∞
—

E
5
E

**Explanation:**
A → A = 0 because the source and destination are the same router.
A → E = 5 because A has a direct link to E.
A → B, A → C, and A → D are initially  **∞**  because there are no direct links from A to these routers.

**Router E's Routing Table**
Router E is directly connected to A, B, and D. Therefore:

E → A = 5
E → B = 4
E → D = 7
E → C = ∞ initially because there is no direct E-C link.

Destination
Distance
Next Hop

A
5
A

B
4
B

C
∞
—

D
7
D

E
0
—

**Step 2: Router A Receives Router E's Distance Vector**
The cost from A to E is:
**c(A,E) = 5**
Router A now uses the Bellman-Ford equation:
**DA(Y) = min { DA(Y), c(A,E) + DE(Y) }**
We calculate the distance to each destination using Router E as the intermediate/next-hop router.
**1. Destination A**
DA(A) = min { 0, 5 + 5 } =  **0**
**2. Destination B**
DA(B) = min { ∞, 5 + 4 }
DA(B) = min { ∞, 9 } =  **9**
Therefore, the path is:  **A → E → B**
**3. Destination C**
DA(C) = min { ∞, 5 + ∞ } =  **∞**
Router E currently has no direct known route to C in the given distance vector.
**4. Destination D**
DA(D) = min { ∞, 5 + 7 }
DA(D) = min { ∞, 12 } =  **12**
Therefore, the path is:  **A → E → D**
**5. Destination E**
DA(E) = min { 5, 5 + 0 } =  **5**
Therefore, A reaches E directly with a cost of 5.

**Updated Routing Table of Router A**

Destination
Old Distance
Via E
New Distance
Next Hop

A
0
5 + 5 = 10
**0**
—

B
∞
5 + 4 = 9
**9**
E

C
∞
5 + ∞ = ∞
**∞**
—

D
∞
5 + 7 = 12
**12**
E

E
5
5 + 0 = 5
**5**
E

**Final Result:**
After receiving Router E's distance vector, Router A learns routes to  **B**  and  **D**  through E.
**A → E → B = 5 + 4 = 9**
**A → E → D = 5 + 7 = 12**
Router A still has no route to C at this stage because Router E's current distance vector shows  **C = ∞** .
**Therefore, the updated routing table of A is:**

Destination
Distance
Next Hop

A
0
—

B
9
E

C
∞
—

D
12
E

E
5
E

7

Link State Routing


**Link State Routing**  is a routing algorithm in which each router builds a  **complete view or topology map of the network**  and uses that information to calculate the shortest path.
Unlike Distance Vector Routing, a router does not depend only on information about its immediate neighbors. Each router eventually obtains information about the  **entire network topology** .
**Algorithm Used:**  Dijkstra's Shortest Path First (SPF) Algorithm
**Common Protocols:**  OSPF (Open Shortest Path First) and IS-IS (Intermediate System to Intermediate System).
**Working of Link State Routing:**

1. Each router discovers its neighboring routers.
2. The router measures the cost or distance of its links to neighboring routers.
3. The router creates a  **Link State Packet (LSP)**  containing information about its links and neighbors.
4. The LSP is distributed to other routers through a process called  **flooding** .
5. Every router receives sufficient link-state information to build a complete network topology map.
6. Each router runs the  **Dijkstra algorithm**  to calculate the shortest path to each destination.
7. Each router creates its routing table based on the calculated shortest paths.

**Characteristics of Link State Routing:**

• Provides a view of the entire network topology.
• Uses the  **Dijkstra (Shortest Path First) algorithm** .
• Uses Link State Packets (LSPs).
• Uses flooding to distribute link-state information.
• Converges faster than Distance Vector Routing.
• Does not have the traditional Count-to-Infinity problem of Distance Vector Routing.
• Requires more processing power and memory because each router maintains topology information.

**Link State Routing**  হলো এমন একটি Routing Algorithm যেখানে প্রতিটি Router পুরো Network-এর একটি  **Complete Topology Map**  তৈরি করে এবং সেই তথ্য ব্যবহার করে Shortest Path নির্ধারণ করে।
Distance Vector Routing-এর মতো শুধু Neighbor-এর তথ্যের উপর নির্ভর না করে Link State Routing-এ প্রতিটি Router শেষ পর্যন্ত  **সম্পূর্ণ Network Topology**  সম্পর্কে তথ্য পায়।
**Algorithm:**  Dijkstra's Shortest Path First (SPF) Algorithm
**প্রধান Protocol:**  OSPF (Open Shortest Path First) এবং IS-IS (Intermediate System to Intermediate System)।
**Link State Routing-এর কার্যপ্রণালী:**

১. প্রতিটি Router তার Neighbor Router শনাক্ত করে।
২. Neighbor-এর সাথে সংযুক্ত Link-এর Cost বা Distance পরিমাপ করে।
৩. Router একটি  **Link State Packet (LSP)**  তৈরি করে।
৪. LSP Network-এর অন্যান্য Router-এর কাছে পাঠানো হয়। এই প্রক্রিয়াকে  **Flooding**  বলা হয়।
৫. প্রতিটি Router পর্যাপ্ত Link-State Information পাওয়ার পর পুরো Network-এর একটি Topology Map তৈরি করে।
৬. প্রতিটি Router  **Dijkstra Algorithm**  ব্যবহার করে প্রতিটি Destination-এর Shortest Path নির্ধারণ করে।
৭. নির্ধারিত Shortest Path-এর ভিত্তিতে Routing Table তৈরি করা হয়।

**Link State Routing-এর বৈশিষ্ট্য:**

• পুরো Network Topology সম্পর্কে ধারণা রাখে।
• Dijkstra Algorithm ব্যবহার করে।
• Link State Packet (LSP) ব্যবহার করে।
• Flooding-এর মাধ্যমে Link-State Information ছড়িয়ে দেয়।
• Distance Vector Routing-এর তুলনায় দ্রুত Converge করে।
• Distance Vector-এর প্রচলিত Count-to-Infinity Problem নেই।
• Topology Information সংরক্ষণের জন্য বেশি Memory ও Processing Power প্রয়োজন হয়।

8

Given a network graph with vertices (nodes) A, B, C, D, E, and F and the following weighted bidirectional edge links:

1. Using Dijkstra's Shortest Path First algorithm (Link State Routing), compute the shortest distance and predecessor node from source vertex A to all other routers in the network.
2. Fill out the step-by-step Link State Routing table showing set N' (visited nodes) and updated distance vector tuples D(v), P(v) for each unvisited node.
3. Determine the shortest path and total path cost from A to F.

Step
N'
D(B), P(B)
D(C), P(C)
D(D), P(D)
D(E), P(E)
D(F), P(F)

**0**
{A}
(2, A)
(5, A)
(1, A)
(∞, —)
(∞, —)

**1**
{A,D}
(2, A)
(4, D)
(1, A)
(2, D)
(∞, —)

**2**
{A,D,B}
(2, A)
(4, D)
(1, A)
(2, D)
(∞, —)

**3**
{A,D,B,E}
(2, A)
(3, E)
(1, A)
(2, D)
(4, E)

**4**
{A,D,B,E,C}
(2, A)
(3, E)
(1, A)
(2, D)
(4, E)

**5**
{A,D,B,E,C,F}
(2, A)
(3, E)
(1, A)
(2, D)
(4, E)

**A → B:**  Distance = 2, Predecessor = A
**A → D:**  Distance = 1, Predecessor = A
**A → E:**  Distance = 2, Predecessor = D
**A → C:**  Distance = 3, Predecessor = E
**A → F:**  Distance = 4, Predecessor = E

Therefore, the shortest path from  **A to F**  is:

**A → D → E → F**

**Total Path Cost = 1 + 1 + 2 = 4**

**Final Answer:**  The shortest path from A to F is
**A → D → E → F** , and the minimum total cost is
**4** .

9

Distance Vector Routing vs Link State Routing


**1. Knowledge:**
Distance Vector Routing uses mainly  **local/neighbor information** , whereas Link State Routing maintains knowledge of the  **entire network topology** .
**2. Algorithm:**
Distance Vector Routing uses the  **Bellman-Ford algorithm** , whereas Link State Routing uses the  **Dijkstra algorithm** .
**3. Information Exchange:**
Distance Vector routers exchange routing information mainly with their  **neighbors** , whereas Link State routers distribute Link State Packets throughout the network using  **flooding** .
**4. Convergence:**
Distance Vector Routing generally has  **slower convergence** , whereas Link State Routing generally has  **faster convergence** .
**5. Count-to-Infinity Problem:**
Distance Vector Routing can suffer from the  **Count-to-Infinity problem** , whereas Link State Routing does not have this traditional problem.
**6. Network View:**
Distance Vector Routing has a limited view of the network, whereas Link State Routing has a  **complete topology view** .
**7. Resource Requirement:**
Distance Vector Routing generally requires less memory and processing, whereas Link State Routing requires more memory and processing to maintain the topology database and calculate shortest paths.
**8. Examples:**
Distance Vector:  **RIP, IGRP**
Link State:  **OSPF, IS-IS**

**Comparison Table:**

Feature
Distance Vector Routing
Link State Routing

**Network Knowledge**
Neighbor/local information
Complete network topology

**Algorithm**
Bellman-Ford
Dijkstra

**Information Exchange**
With neighboring routers
Link State Packets are flooded

**Convergence**
Slower
Faster

**Count-to-Infinity**
Possible
Not a traditional issue

**Complexity**
Relatively simple
More complex

**Resource Requirement**
Lower
Higher

**Examples**
RIP, IGRP
OSPF, IS-IS

**১. Network Knowledge:**  Distance Vector Routing মূলত Neighbor-এর তথ্য ব্যবহার করে, কিন্তু Link State Routing পুরো Network-এর Topology সম্পর্কে তথ্য রাখে।
**২. Algorithm:**  Distance Vector Routing-এ Bellman-Ford Algorithm এবং Link State Routing-এ Dijkstra Algorithm ব্যবহার করা হয়।
**৩. Information Exchange:**  Distance Vector Routing-এ মূলত Neighbor Router-এর সাথে তথ্য আদান-প্রদান হয়। Link State Routing-এ LSP Flooding-এর মাধ্যমে Network-এর অন্যান্য Router-এ তথ্য ছড়িয়ে দেওয়া হয়।
**৪. Convergence:**  Distance Vector Routing-এর Convergence ধীর, কিন্তু Link State Routing-এর Convergence দ্রুত।
**৫. Count-to-Infinity:**  Distance Vector Routing-এ Count-to-Infinity Problem হতে পারে, কিন্তু Link State Routing-এ এই প্রচলিত Problem নেই।
**৬. Network View:**  Distance Vector-এর Network View সীমিত, কিন্তু Link State-এর Complete Network View থাকে।
**৭. Resource:**  Distance Vector Routing তুলনামূলকভাবে কম Memory ও Processing ব্যবহার করে। Link State Routing বেশি Memory ও Processing ব্যবহার করে।
**৮. Protocol:**  Distance Vector-এর উদাহরণ RIP ও IGRP। Link State-এর উদাহরণ OSPF ও IS-IS।

10

Routing Protocols


**Routing Protocol**  is a set of rules used by routers to exchange routing information and determine the best path for forwarding packets from a source network to a destination network.
Routing protocols are mainly used in  **dynamic routing** , where routers automatically learn, update, and maintain routing information.
Three important routing protocols are:
**1. RIP — Routing Information Protocol**
**2. OSPF — Open Shortest Path First**
**3. BGP — Border Gateway Protocol**

**Routing Protocol**  হলো কিছু নিয়ম বা Rules-এর সমষ্টি, যার মাধ্যমে Router-গুলো নিজেদের মধ্যে Routing Information আদান-প্রদান করে এবং Source Network থেকে Destination Network-এ Packet পাঠানোর জন্য সবচেয়ে উপযুক্ত পথ নির্ধারণ করে।
Routing Protocol মূলত  **Dynamic Routing** -এ ব্যবহৃত হয়। Dynamic Routing-এর ক্ষেত্রে Router স্বয়ংক্রিয়ভাবে বিভিন্ন Network-এর Route শিখতে, Update করতে এবং Routing Table maintain করতে পারে।
গুরুত্বপূর্ণ তিনটি Routing Protocol হলো:

**১. RIP — Routing Information Protocol**
**২. OSPF — Open Shortest Path First**
**৩. BGP — Border Gateway Protocol**

11

RIP (Routing Information Protocol)


**RIP**  is a  **Distance Vector routing protocol** . It determines the best route mainly using  **hop count**  as its routing metric.
In RIP, a router exchanges routing information with its neighboring routers and learns the distance to different destination networks.
**Important Features of RIP:**

•  **Type:**  Distance Vector
•  **Metric:**  Hop Count
•  **Algorithm:**  Bellman-Ford based
•  **Maximum usable hop count:**  15
•  **16 hops:**  Considered unreachable
•  **Transport:**  UDP
•  **Port:**  UDP 520
• Mainly suitable for  **small networks** .

**Example:**
If one route requires 3 hops and another route requires 5 hops, RIP normally selects the 3-hop route, regardless of whether the 5-hop route has higher bandwidth.
**Advantages of RIP:**

• Simple to configure.
• Easy to understand.
• Requires relatively low resources.
• Suitable for small and simple networks.

**Disadvantages of RIP:**

• Limited to 15 usable hops.
• Slow convergence compared with OSPF.
• Does not consider bandwidth when selecting the route.
• Not suitable for large and complex networks.

**RIP**  হলো একটি  **Distance Vector Routing Protocol** । এটি মূলত  **Hop Count**  ব্যবহার করে Destination-এর জন্য Best Route নির্বাচন করে।
RIP-এ একটি Router তার Neighbor Router-গুলোর সাথে Routing Information exchange করে এবং বিভিন্ন Destination Network-এ পৌঁছানোর Distance জানতে পারে।
**RIP-এর গুরুত্বপূর্ণ বৈশিষ্ট্য:**

•  **Type:**  Distance Vector
•  **Metric:**  Hop Count
•  **Algorithm:**  Bellman-Ford ভিত্তিক
•  **Maximum usable hop count:**  15
•  **16 hops:**  Unreachable হিসেবে বিবেচিত হয়
•  **Transport:**  UDP
•  **Port:**  UDP 520
• প্রধানত  **ছোট Network** -এর জন্য উপযোগী।

**উদাহরণ:**
যদি একটি Destination-এ যাওয়ার জন্য একটি Route-এ 3টি Hop এবং অন্য Route-এ 5টি Hop প্রয়োজন হয়, তাহলে RIP সাধারণত 3-Hop Route-টি নির্বাচন করবে।
**RIP-এর সুবিধা:**

• Configure করা সহজ।
• বোঝা সহজ।
• তুলনামূলকভাবে কম Resource প্রয়োজন হয়।
• ছোট ও Simple Network-এর জন্য উপযোগী।

**RIP-এর অসুবিধা:**

• সর্বোচ্চ 15টি usable hop-এর সীমাবদ্ধতা রয়েছে।
• OSPF-এর তুলনায় Convergence ধীর।
• Route নির্বাচন করার সময় Link Bandwidth বিবেচনা করে না।
• বড় ও Complex Network-এর জন্য উপযোগী নয়।

12

OSPF (Open Shortest Path First)


**OSPF**  is a  **Link State routing protocol** . It builds a topology database of the network and uses  **Dijkstra's Shortest Path First (SPF) algorithm**  to calculate the shortest path.
Unlike RIP, OSPF does not simply count the number of routers. It uses a  **cost**  metric, which is commonly related to link bandwidth.
**Important Features of OSPF:**

•  **Type:**  Link State
•  **Algorithm:**  Dijkstra / SPF
•  **Metric:**  Cost
•  **Protocol Number:**  IP Protocol 89
• Used mainly as an  **Interior Gateway Protocol (IGP)** .
• Suitable for  **medium and large networks** .
• Supports hierarchical network design using  **Areas** .
•  **Area 0**  is known as the backbone area.

**How OSPF Works:**

1. Routers discover their neighboring routers.
2. Routers exchange  **Link-State Advertisements (LSAs)** .
3. Each router builds a  **Link-State Database (LSDB)** .
4. The router creates a complete view of the network topology.
5. Dijkstra's SPF algorithm is used to calculate the shortest paths.
6. The router creates its routing table.

**Advantages of OSPF:**

• Fast convergence.
• Highly scalable.
• Suitable for large enterprise networks.
• Supports hierarchical routing using areas.
• Supports VLSM and CIDR.
• Provides efficient path selection using cost.

**Disadvantages of OSPF:**

• More complex than RIP.
• Requires more CPU and memory resources.
• Configuration and network design can be more complicated.

**OSPF**  হলো একটি  **Link State Routing Protocol** । এটি Network-এর একটি Topology Database তৈরি করে এবং  **Dijkstra's Shortest Path First (SPF) Algorithm**  ব্যবহার করে Shortest Path নির্ধারণ করে।
RIP-এর মতো শুধু Hop Count গণনা না করে OSPF একটি  **Cost**  Metric ব্যবহার করে। এই Cost সাধারণত Link Bandwidth-এর সাথে সম্পর্কিত।
**OSPF-এর গুরুত্বপূর্ণ বৈশিষ্ট্য:**

•  **Type:**  Link State
•  **Algorithm:**  Dijkstra / SPF
•  **Metric:**  Cost
•  **Protocol Number:**  IP Protocol 89
• এটি একটি  **Interior Gateway Protocol (IGP)** ।
• Medium এবং Large Network-এর জন্য উপযোগী।
• Network-কে বিভিন্ন  **Area** -তে ভাগ করে Hierarchical Design তৈরি করা যায়।
•  **Area 0**  হলো OSPF-এর Backbone Area।

**OSPF কীভাবে কাজ করে:**

১. Router তার Neighbor Router-গুলোকে Discover করে।
২. Router-গুলো  **Link-State Advertisement (LSA)**  আদান-প্রদান করে।
৩. প্রতিটি Router একটি  **Link-State Database (LSDB)**  তৈরি করে।
৪. Router পুরো Network Topology সম্পর্কে ধারণা লাভ করে।
৫. Dijkstra's SPF Algorithm ব্যবহার করে Shortest Path নির্ধারণ করা হয়।
৬. এরপর Routing Table তৈরি করা হয়।

**OSPF-এর সুবিধা:**

• দ্রুত Convergence হয়।
• অত্যন্ত Scalable।
• বড় Enterprise Network-এর জন্য উপযোগী।
• Area ব্যবহার করে Hierarchical Routing করা যায়।
• VLSM এবং CIDR Support করে।
• Cost ব্যবহার করে কার্যকরভাবে Best Path নির্বাচন করতে পারে।

**OSPF-এর অসুবিধা:**

• RIP-এর তুলনায় Configure করা বেশি জটিল।
• বেশি CPU এবং Memory প্রয়োজন হতে পারে।
• Network Design ও Management তুলনামূলকভাবে Complex।

13

BGP (Border Gateway Protocol)


**BGP**  is a  **Path Vector routing protocol** . It is mainly used to exchange routing information between different  **Autonomous Systems (AS)** .
BGP is the primary routing protocol used for  **inter-domain routing on the Internet** .
**Important Features of BGP:**

•  **Type:**  Path Vector
•  **Routing Scope:**  Inter-domain / Between Autonomous Systems
•  **Transport Protocol:**  TCP
•  **Port:**  TCP 179
• Uses multiple  **path attributes and routing policies** .
• Highly scalable and suitable for Internet-scale routing.

**Important BGP Path Attributes:**

•  **AS-PATH**
•  **NEXT-HOP**
•  **LOCAL-PREFERENCE**
•  **MED (Multi-Exit Discriminator)**

**Types of BGP:**
**eBGP (External BGP):**  Used for exchanging routing information between different Autonomous Systems.
**iBGP (Internal BGP):**  Used for exchanging BGP routing information within the same Autonomous System.
**Advantages of BGP:**

• Extremely scalable.
• Suitable for Internet-scale routing.
• Provides powerful routing policy control.
• Supports route filtering and route aggregation.
• Can connect different Autonomous Systems.

**Disadvantages of BGP:**

• Complex to configure and manage.
• Requires significant routing knowledge.
• Convergence is generally slower than OSPF.
• Requires more powerful network equipment in large deployments.

**BGP**  হলো একটি  **Path Vector Routing Protocol** । এটি প্রধানত বিভিন্ন  **Autonomous System (AS)** -এর মধ্যে Routing Information আদান-প্রদান করতে ব্যবহৃত হয়।
BGP হলো Internet-এর  **Inter-Domain Routing** -এর প্রধান Routing Protocol।
**BGP-এর গুরুত্বপূর্ণ বৈশিষ্ট্য:**

•  **Type:**  Path Vector
•  **Routing Scope:**  Inter-domain / Autonomous Systems-এর মধ্যে
•  **Transport Protocol:**  TCP
•  **Port:**  TCP 179
• বিভিন্ন  **Path Attribute এবং Routing Policy**  ব্যবহার করে।
• Internet-scale Network-এর জন্য অত্যন্ত Scalable।

**গুরুত্বপূর্ণ BGP Path Attributes:**

•  **AS-PATH**
•  **NEXT-HOP**
•  **LOCAL-PREFERENCE**
•  **MED (Multi-Exit Discriminator)**

**BGP-এর ধরন:**
**eBGP (External BGP):**  বিভিন্ন Autonomous System-এর মধ্যে Routing Information আদান-প্রদানের জন্য ব্যবহৃত হয়।
**iBGP (Internal BGP):**  একই Autonomous System-এর অভ্যন্তরে BGP Routing Information আদান-প্রদানের জন্য ব্যবহৃত হয়।
**BGP-এর সুবিধা:**

• অত্যন্ত Scalable।
• Internet-scale Routing-এর জন্য উপযোগী।
• Powerful Routing Policy Control প্রদান করে।
• Route Filtering এবং Route Aggregation Support করে।
• বিভিন্ন Autonomous System-কে Connect করতে পারে।

**BGP-এর অসুবিধা:**

• Configure ও Manage করা জটিল।
• Routing সম্পর্কে ভালো Knowledge প্রয়োজন।
• OSPF-এর তুলনায় Convergence সাধারণত ধীর।
• বড় Network-এ শক্তিশালী Router প্রয়োজন হতে পারে।

14

RIP vs OSPF vs BGP


Feature
RIP
OSPF
BGP

**Full Form**
Routing Information Protocol
Open Shortest Path First
Border Gateway Protocol

**Type**
Distance Vector
Link State
Path Vector

**Algorithm**
Bellman-Ford based
Dijkstra / SPF
Path Vector / Policy-based

**Metric**
Hop Count
Cost
Path Attributes / Policies

**Routing Scope**
Intra-domain
Intra-domain
Inter-domain

**Suitable For**
Small Networks
Medium/Large Networks
Internet / ISP Networks

**Scalability**
Low
High
Very High

**Convergence**
Slow
Fast
Generally slower, stability/policy focused

**Transport**
UDP 520
IP Protocol 89
TCP 179



**Previous Job Question:**  Fragmentation and Routing Protocol



Topic Wise Question Bank

All Topics

- ☆

1

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

2

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

**Assigment:**   Fragmentation and Routing Protocol

- Explain fragmentation in the Network Layer. Why is IP fragmentation required? Discuss the role of MTU, Fragment Offset, Identification, and the More Fragments (MF) flag in IPv4 fragmentation.

- Consider an IP packet with a total length of 4500 bytes, including a 20-byte IPv4 header and a 40-byte TCP header. The packet is forwarded to an IPv4 router that supports a maximum transmission unit (MTU) of 600 bytes. Assume that the length of the IP header in all outgoing fragments is 20 bytes and the fragmentation offset value stored in the first fragment is 0. Determine the fragmentation offset value stored in the third fragment.

- What is the Record Route (RR) option in IPv4? Explain its purpose and determine the maximum number of IPv4 router addresses that can be listed in the Record Route option field of an IPv4 header.

- An IP datagram of size 1000 bytes arrives at a router. The router has to forward this packet through a link whose MTU is 100 bytes. Assume that the size of the IP header is 20 bytes. Determine the number of fragments into which the IP datagram will be divided for transmission. Also determine the data size carried by each fragment.

- Explain the Distance Vector Routing algorithm. Discuss how routers exchange distance vectors and explain the Bellman-Ford equation used to calculate the shortest path.

- What is Link State Routing? Explain the major steps involved in Link State Routing. Discuss Link State Advertisement (LSA), flooding, and the role of Dijkstra’s Shortest Path First algorithm.

- Compare Distance Vector Routing and Link State Routing.

- Compare RIP, OSPF, and BGP based on routing algorithm, routing metric, network scope, convergence, scalability, and practical applications.


📘 Fragmentation and Routing Protocol

#### 1. What is IP fragmentation?

#### 2. Which field in an IPv4 header identifies fragments belonging to the same original datagram?

#### 3. What does MTU stand for?

#### 4. Which IPv4 header field specifies the position of a fragment in the original datagram?

#### 5. In IPv4 fragmentation, what is the unit of the Fragment Offset field?

#### 6. Consider an IPv4 packet of total length 4500 bytes with a 20-byte header. If the outgoing MTU is 600 bytes, what is the maximum data size of each full-sized fragment?

#### 7. For the 4500-byte IPv4 packet with a 600-byte MTU, what is the Fragment Offset of the third fragment?

#### 8. What is the purpose of the More Fragments (MF) flag in IPv4?

#### 9. What is the Fragment Offset value of the first fragment?

#### 10. An IPv4 datagram has a total size of 1000 bytes and a 20-byte header. If the outgoing MTU is 100 bytes, what is the maximum data carried by each full-sized fragment?

#### 11. For the 1000-byte datagram with a 100-byte MTU and a 20-byte header, how many fragments are required?

#### 12. What is the maximum number of IPv4 router addresses that can be recorded in the Record Route (RR) option?

#### 13. What is the main purpose of the IPv4 Record Route option?

#### 14. What is Distance Vector Routing?

#### 15. Which algorithm is commonly associated with Distance Vector Routing?

#### 16. In Distance Vector Routing, what information does a router primarily exchange with its neighbors?

#### 17. What does the Bellman-Ford equation help a router determine?

#### 18. In Distance Vector Routing, what is a next hop?

#### 19. What is a major disadvantage of Distance Vector Routing?

#### 20. What is Link State Routing?

#### 21. Which algorithm is commonly used in Link State Routing?

#### 22. What does Dijkstra's algorithm calculate?

#### 23. What does N' represent in the Dijkstra shortest path algorithm?

#### 24. In a Dijkstra table, what does D(v) represent?

#### 25. In a Dijkstra table, what does P(v) represent?

#### 26. What is a major advantage of Link State Routing over Distance Vector Routing?

#### 27. Which routing method provides routers with a more complete view of the network topology?

#### 28. Which routing method generally exchanges routing information primarily with neighboring routers?

#### 29. Which protocol is an example of Distance Vector Routing?

#### 30. Which protocol is an example of Link State Routing?

#### 31. What does RIP stand for?

#### 32. What metric does RIP primarily use to select routes?

#### 33. What is the maximum hop count supported by RIP for a reachable destination?

#### 34. Which statement about RIP is correct?

#### 35. What does OSPF stand for?

#### 36. Which algorithm is used by OSPF to calculate shortest paths?

#### 37. What type of routing protocol is OSPF?

#### 38. What does BGP stand for?

#### 39. What type of routing protocol is BGP?

#### 40. What is the primary purpose of BGP?

#### 41. What is an Autonomous System (AS) in the context of BGP?

#### 42. Which of the following correctly compares RIP, OSPF, and BGP?
