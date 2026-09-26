# M1: Computer Network (Network Topology and Networking Devices)

- **Original URL:** [https://it.jobqns.com/m1-computer-network-network-topology-and-networking-devices/](https://it.jobqns.com/m1-computer-network-network-topology-and-networking-devices/)
- **Date:** 2026-08-26T15:39:04
- **Categories:** Uncategorized, IT Preparation Module

---

**Computer Network**  (Network Topology and Networking Devices ) (ET: 1.5 Hours)



**Video Tutorial:**  Network Topology and Networking Devices



- **Watch Video:**  Network Topology

- **Watch Video:**  Network Devices

- **Watch Video:**   Access Point Vs Router

- **Watch Video:**   Network Security Devices (Firewall and it Types)

Network Topology & Networking Devices

- 1

What is Network Topology and its types.


Network topology refers to the geometric arrangement or structure of how computers or devices are connected within a network.
It explains both types of network layout —  **Physical Topology**  and  **Logical Topology** . It helps us understand how data flows from one device to another.
**Physical Topology**  describes how devices are physically connected, while  **Logical Topology**  explains how data flows inside the network. Sometimes both may be the same, but depending on design, they can also be different.

**Types of Network Topology:**

Bus Topology
Ring Topology
Star Topology
Tree Topology
Mesh Topology
Hybrid Topology

**Network Topology**  হলো একটি Network-এ Computer বা Device গুলো কীভাবে সংযুক্ত আছে তার Geometric Arrangement বা Structure।
এটি Network Layout-এর দুই ধরনের ব্যাখ্যা করে —  **Physical Topology**  এবং  **Logical Topology** । এটি বুঝতে সাহায্য করে Data কীভাবে এক Device থেকে অন্য Device-এ প্রবাহিত হয়।
**Physical Topology**  বোঝায় Device গুলো কীভাবে শারীরিকভাবে সংযুক্ত, আর  **Logical Topology**  বোঝায় Network-এর ভিতরে Data কীভাবে প্রবাহিত হয়। কখনো Physical ও Logical Topology একই হতে পারে, আবার Network Design অনুযায়ী ভিন্নও হতে পারে।

**Network Topology-এর প্রকারভেদ:**

Bus Topology
Ring Topology
Star Topology
Tree Topology
Mesh Topology
Hybrid Topology

2

Bus Topology


In  **Bus Topology** , all devices are connected to a single central cable called the  **Backbone** .
Each node is connected to the backbone using a  **Drop Cable** .
When a device sends data, it travels along the backbone and is broadcast to all devices. Only the intended recipient accepts the data; others ignore it.

**Advantages of Bus Topology:**

Simple to install and requires less hardware.
Failure of one device does not affect other devices.
Easy to troubleshoot due to simple structure.

**Disadvantages of Bus Topology:**

If the backbone cable fails, the entire network stops working.
Data collision occurs when multiple devices send data at the same time, reducing speed.
As more devices are added, network performance decreases due to shared backbone traffic.

In conclusion, Bus Topology is simple and cost-effective but less reliable for large networks.

**Bus Topology** -তে সকল Device একটি কেন্দ্রীয় Cable-এর সাথে সংযুক্ত থাকে, যাকে  **Backbone**  বলা হয়।
প্রতিটি Node একটি  **Drop Cable**  ব্যবহার করে Backbone-এর সাথে যুক্ত থাকে।
কোনো Device Data পাঠালে তা Backbone বরাবর সব Device-এ Broadcast হয়। তবে শুধুমাত্র নির্দিষ্ট Recipient Data গ্রহণ করে, অন্যরা তা উপেক্ষা করে।

**Bus Topology-এর সুবিধাসমূহ:**

Install করা সহজ এবং কম Hardware প্রয়োজন।
একটি Device নষ্ট হলেও অন্য Device-এ প্রভাব পড়ে না।
সহজ Structure হওয়ায় Troubleshoot করা সহজ।

**Bus Topology-এর অসুবিধাসমূহ:**

Backbone Cable নষ্ট হলে পুরো Network অকার্যকর হয়ে যায়।
একাধিক Device একসাথে Data পাঠালে  **Data Collision**  হয়, ফলে Speed কমে যায়।
বেশি Device যুক্ত হলে Shared Backbone-এর কারণে Network Performance কমে যায়।

সারসংক্ষেপে,  **Bus Topology**  সহজ ও কম খরচের হলেও বড় Network-এর জন্য কম নির্ভরযোগ্য।

3

Ring Topology


In  **Ring Topology** , each device is connected to exactly two other devices, forming a circular structure. This creates a closed loop for data transmission.
Data moves in one direction from one device to another until it reaches the destination.

**Working Principle of Ring Topology:**

Data transmission occurs using a special signal called a  **Token** , which is why it is also called  **Token Ring** .
A  **Token**  is a special data packet that circulates through the network and controls permission to send data.
Only the device holding the token can transmit data.
The token moves sequentially from one device to another.
When a device wants to send data, it captures the token, attaches the data, and transmits it.
After successful transmission, the token is released and passed to the next device. Since only one device sends data at a time, collisions do not occur.

**Advantages of Ring Topology:**

No data collision due to token-based transmission.
Each device gets equal opportunity to send data.

**Disadvantages of Ring Topology:**

Data travels in only one direction, even if the destination is nearby in the opposite direction.
Failure of one node or link can disrupt the entire network.
Performance decreases as network traffic increases.
Data passes through multiple nodes, increasing security risks.

**Ring Topology** -তে প্রতিটি Device ঠিক দুইটি অন্য Device-এর সাথে সংযুক্ত থাকে, ফলে একটি Circular Structure তৈরি হয়। এটি Data Transmission-এর জন্য একটি Closed Loop তৈরি করে।
Data একদিকে (One Direction) এক Device থেকে অন্য Device-এ প্রবাহিত হয় এবং নির্দিষ্ট Destination-এ পৌঁছায়।

**Ring Topology-এর কার্যপ্রণালী:**

এই Topology-তে Data একটি বিশেষ Signal  **Token** -এর মাধ্যমে প্রেরণ করা হয়, তাই একে  **Token Ring** ও বলা হয়।
**Token**  হলো একটি বিশেষ Data Packet যা Network-এ ঘুরে বেড়ায় এবং Data পাঠানোর অনুমতি নিয়ন্ত্রণ করে।
যে Device Token ধারণ করে, কেবল সেই Device Data পাঠাতে পারে।
Token ধারাবাহিকভাবে এক Device থেকে অন্য Device-এ যায়।
Device Data পাঠাতে চাইলে Token গ্রহণ করে, Data যুক্ত করে Network-এ পাঠায়।
Transmission শেষ হলে Token আবার Release করা হয় এবং পরবর্তী Device-এ পাঠানো হয়। ফলে Data Collision ঘটে না।

**Ring Topology-এর সুবিধাসমূহ:**

Token ব্যবহারের কারণে Data Collision হয় না।
প্রতিটি Device সমানভাবে Data পাঠানোর সুযোগ পায়।

**Ring Topology-এর অসুবিধাসমূহ:**

Data শুধুমাত্র একদিকে প্রবাহিত হয়, তাই বিপরীত দিকে কাছাকাছি Destination হলেও পুরো Ring ঘুরে যেতে হয়।
একটি Node বা Link নষ্ট হলে পুরো Network অকার্যকর হতে পারে।
Network Traffic বাড়লে Performance কমে যায়।
Data একাধিক Node-এর মধ্য দিয়ে যাওয়ায় Security ঝুঁকি থাকে।

4

Star Topology


In  **Star Topology** , all devices are connected to a central  **Hub**  or  **Switch** , which acts as a mediator for data transmission. All network traffic passes through this central device.
This topology is widely used in modern networks because it is easy to set up and scalable.

**Advantages of Star Topology:**

Easy to design and implement.
Centralized administration is possible since all devices connect to a hub or switch.
Adding new devices is simple.
Failure of one device does not affect other devices.

**Disadvantages of Star Topology:**

If the hub or switch fails, the entire network stops working.
Overload on the hub or switch can reduce network performance.
Requires more hardware (hub/switch), increasing cost.

**Star Topology** -তে সকল Device একটি কেন্দ্রীয়  **Hub**  বা  **Switch** -এর সাথে সংযুক্ত থাকে, যা Data Transmission-এর মধ্যস্থতাকারী হিসেবে কাজ করে। সব Network Traffic এই Central Device-এর মাধ্যমে যায়।
সহজ Setup ও Scalability-এর কারণে এটি আধুনিক Network-এ ব্যাপকভাবে ব্যবহৃত হয়।

**Star Topology-এর সুবিধাসমূহ:**

Design ও Implement করা সহজ।
সব Device কেন্দ্রীয় Hub বা Switch-এর সাথে যুক্ত থাকায় Centralized Administration সম্ভব।
নতুন Device যুক্ত করা সহজ।
একটি Device নষ্ট হলেও অন্য Device-এ প্রভাব পড়ে না।

**Star Topology-এর অসুবিধাসমূহ:**

Hub বা Switch নষ্ট হলে পুরো Network বন্ধ হয়ে যায়।
Hub বা Switch Overload হলে Network Performance কমে যায়।
অতিরিক্ত Hardware (Hub/Switch) প্রয়োজন হওয়ায় খরচ বেশি।

5

Tree Topology


In  **Tree Topology** , characteristics of both  **Bus**  and  **Star**  topologies are combined. Devices are organized in a hierarchical structure with multiple branches connected to a central root node.
It is commonly used in large networks such as  **WAN (Wide Area Network)** .

**Advantages of Tree Topology:**

The network can easily expand by adding new nodes or branches.
Easy to detect and troubleshoot problems.
Large networks can be divided into smaller segments for better management.

**Disadvantages of Tree Topology:**

If the main cable (root node) fails, the entire network is affected.
Requires more cables and hardware, increasing installation cost.

**Tree Topology** -তে  **Bus**  ও  **Star**  Topology-এর বৈশিষ্ট্য একত্রিত করা হয়। Device গুলো Hierarchical Structure-এ সাজানো থাকে এবং একাধিক Branch একটি Central Root Node-এর সাথে সংযুক্ত থাকে।
এটি বড় Network যেমন  **WAN (Wide Area Network)** -এ ব্যবহৃত হয়।

**Tree Topology-এর সুবিধাসমূহ:**

নতুন Node বা Branch যুক্ত করে Network সহজে সম্প্রসারণ করা যায়।
সমস্যা শনাক্ত ও Troubleshoot করা সহজ।
বড় Network-কে ছোট Segment-এ ভাগ করে সহজে পরিচালনা করা যায়।

**Tree Topology-এর অসুবিধাসমূহ:**

Main Cable (Root Node) নষ্ট হলে পুরো Network প্রভাবিত হয়।
Installation-এর জন্য বেশি Cable ও Hardware প্রয়োজন হয়।

6

Mesh Topology


In  **Mesh Topology** , devices are interconnected through multiple paths. Each device is either directly connected to every other device ( **Full Mesh** ) or connected to only some devices ( **Partial Mesh** ).
Mesh topology is suitable for large-scale networks where reliability and redundancy are important.

**Advantages of Mesh Topology:**

**Fault Tolerance:**  Multiple paths allow continuous communication even if one link fails.
**High Security:**  Direct point-to-point connections provide better security.
**Fast Communication:**  Data can travel through the shortest path, increasing speed.

**Disadvantages of Mesh Topology:**

Requires a large amount of wiring and hardware, making it expensive.
Difficult to configure and manage.
Not practical for very large networks due to complexity and cost.

**Mesh Topology** -তে Device গুলো একাধিক Path-এর মাধ্যমে সংযুক্ত থাকে। প্রতিটি Device হয় সব Device-এর সাথে সরাসরি সংযুক্ত থাকে ( **Full Mesh** ) অথবা কিছু নির্দিষ্ট Device-এর সাথে সংযুক্ত থাকে ( **Partial Mesh** )।
যেখানে Reliability ও Redundancy গুরুত্বপূর্ণ, সেখানে বড় Network-এ এই Topology ব্যবহৃত হয়।

**Mesh Topology-এর সুবিধাসমূহ:**

**Fault Tolerance:**  একাধিক Path থাকার কারণে একটি Link নষ্ট হলেও যোগাযোগ বজায় থাকে।
**High Security:**  Direct Point-to-Point Connection থাকার ফলে নিরাপত্তা বেশি।
**Fast Communication:**  Data সবচেয়ে ছোট Path দিয়ে যেতে পারে, ফলে Speed বৃদ্ধি পায়।

**Mesh Topology-এর অসুবিধাসমূহ:**

বেশি Cable ও Hardware প্রয়োজন হওয়ায় খরচ বেশি।
Configure ও Manage করা জটিল।
অত্যন্ত বড় Network-এর জন্য Practical নয়।

7

Hybrid Topology


**Hybrid Topology**  is a combination of two or more different topologies designed to meet specific organizational needs. For example, a network may combine  **Star**  and  **Bus**  topologies.
Hybrid networks are highly customizable and scalable.

**Advantages of Hybrid Topology:**
**1. Flexibility:**  Can be customized according to organizational requirements.
**2. Fault Tolerance:**  If one part of the network fails, the remaining parts may continue to function.
**3. Scalability:**  New devices can be added without affecting the existing network structure.
**Disadvantages of Hybrid Topology:**
**1. Complex Design:**  Designing and managing a hybrid network is complex.
**2. Expensive:**  Requires more hardware, cabling, and installation cost.

**Hybrid Topology**  হলো দুই বা ততোধিক ভিন্ন Topology-এর সমন্বয়ে গঠিত একটি Network Structure, যা নির্দিষ্ট প্রয়োজন অনুযায়ী তৈরি করা হয়। উদাহরণস্বরূপ, একটি Network-এ  **Star**  ও  **Bus**  Topology একত্রে থাকতে পারে।
Hybrid Network অত্যন্ত Customizable ও Scalable।

**Hybrid Topology-এর সুবিধাসমূহ:**
**১. Flexibility:**  প্রতিষ্ঠানের প্রয়োজন অনুযায়ী Design করা যায়।
**২. Fault Tolerance:**  Network-এর একটি অংশ নষ্ট হলেও বাকি অংশ সচল থাকতে পারে।
**৩. Scalability:**  বিদ্যমান Structure পরিবর্তন না করে নতুন Device যুক্ত করা যায়।
**Hybrid Topology-এর অসুবিধাসমূহ:**
**১. Complex Design:**  Design ও Manage করা জটিল।
**২. Expensive:**  বেশি Hardware, Cable ও Installation খরচ প্রয়োজন হয়।

8

Networking Device

Networking Devices(Hub, Bridge, Switch, Router, Modem, Repeater, and Gateway) (One Shot)


Networking devices are hardware devices used to connect computers, network devices, and different networks. They help transmit data packets between devices and networks efficiently, accurately, and securely. Common networking devices include  **Hub, Bridge, Switch, Router, Modem, Repeater, and Gateway** .
**1. Hub**  A  **Hub**  is a basic networking device used mainly within a Local Area Network (LAN). When a device sends data to the hub, the hub broadcasts that data to  **all devices**  connected to it. Therefore, every connected device receives the transmitted signal, although only the intended device needs the data.  Hub generally supports small networks and works in  **half-duplex mode** , meaning it can either send or receive data at a time, but cannot perform both simultaneously. It is a relatively inexpensive device and operates at  **Layer 1 (Physical Layer)**  of the OSI model.   **Key Point:**  Hub broadcasts data to all connected devices.
**2. Bridge**  A  **Bridge**  connects two or more LAN segments and facilitates communication between them. It uses the  **MAC address**  of devices to determine where data should be forwarded. Each device has a physical address known as a MAC address.  When a bridge receives data, it checks the destination MAC address against its  **lookup table**  and forwards the data toward the appropriate destination instead of broadcasting it to every device. A bridge operates at  **Layer 2 (Data Link Layer)**  of the OSI model.   **Key Point:**  Bridge uses MAC addresses to forward data between LAN segments.
**3. Switch**  A  **Switch**  is a more advanced networking device compared with a hub and bridge. It uses  **MAC addresses**  to identify the destination device and forward data to the appropriate port. In this way, a switch performs a function similar to a bridge but provides more ports and advanced functionality.  According to the reference, the switch also performs  **error checking**  and forwards information only when the information is considered error-free. Switches support  **full-duplex communication** , allowing sending and receiving to occur simultaneously. A switch operates at  **Layer 2 (Data Link Layer)**  of the OSI model.   **Key Point:**  Switch forwards data using MAC addresses and supports full-duplex communication.
**4. Router**  A  **Router**  is a networking device used to connect  **multiple networks** . It can connect devices through wired Ethernet connections as well as wireless connections.  Unlike a switch or bridge, which primarily uses MAC addresses, a router checks the  **IP address**  of the destination. It analyzes the destination IP address and selects an appropriate path for forwarding the data.  The reference also describes routers as providing a firewall-like function by blocking unauthorized access to a network. A router operates at  **Layer 3 (Network Layer)**  of the OSI model.   **Key Point:**  Router connects different networks and forwards packets based on IP addresses.
**5. Modem**  The word  **Modem**  comes from  **Modulator-Demodulator** . A modem converts digital signals into analog signals and converts analog signals back into digital signals.  When a computer sends digital data through a communication system that uses analog signaling, the modem performs  **modulation** , converting digital signals into analog signals. When information comes back from the network, the modem performs  **demodulation** , converting analog signals into digital signals that the computer can understand.  A modem provides the connection between the user's network and the Internet Service Provider (ISP), allowing Internet access for homes and businesses.   **Key Point:**  Modem performs digital-to-analog and analog-to-digital conversion.
**6. Repeater**  A  **Repeater**  is a signal-strengthening device used when signals become weak over long distances. It receives a weak signal, amplifies or regenerates it, and retransmits a stronger signal toward the destination.  Repeaters help reduce problems caused by weak signals and data loss over long distances. A repeater operates at  **Layer 1 (Physical Layer)**  of the OSI model.   **Key Point:**  Repeater strengthens and retransmits weak signals.
**7. Gateway**  A  **Gateway**  connects two or more  **dissimilar networks** . It can connect networks such as LAN, MAN, and WAN that may use different architectures, protocols, or data formats.  A gateway monitors and controls incoming and outgoing traffic between different networks. One of its important functions is to act as a  **translator** , allowing communication between networks that use different protocols, architectures, or data formats.  According to the reference, a gateway operates across  **all seven layers of the OSI model** .   **Key Point:**  Gateway connects dissimilar networks and can translate between different protocols.
**Important Comparison**   **Hub:**  Uses broadcasting; Layer 1; Half-duplex.  **Bridge:**  Uses MAC address; connects LAN segments; Layer 2.  **Switch:**  Uses MAC address; more advanced than hub and bridge; Layer 2; Full-duplex.  **Router:**  Uses IP address; connects multiple networks; Layer 3.  **Modem:**  Performs modulation and demodulation for communication with the ISP.  **Repeater:**  Amplifies/regenerates weak signals; Layer 1.  **Gateway:**  Connects dissimilar networks and translates between different protocols; all seven OSI layers.
**OSI Layer-wise Classification**   **Physical Layer (Layer 1):**  Hub, Repeater.  **Data Link Layer (Layer 2):**  Bridge, Switch.  **Network Layer (Layer 3):**  Router.  **All Seven Layers:**  Gateway.  **Signal Conversion:**  Modem.
**Exam Focus**  Remember the main differences:  **Hub broadcasts to all devices** ,  **Bridge and Switch use MAC addresses** ,  **Router uses IP addresses** ,  **Repeater strengthens weak signals** ,  **Modem converts digital and analog signals** , and  **Gateway connects dissimilar networks and performs translation** . The reference specifically notes that questions may ask students to explain devices such as router and switch, so the functions and OSI layers of all devices should be prepared.

Networking device হলো এমন hardware device যা কম্পিউটার, অন্যান্য network device এবং বিভিন্ন network-এর মধ্যে সংযোগ স্থাপন করে। এগুলো data packet সঠিকভাবে ও দক্ষতার সাথে এক স্থান থেকে অন্য স্থানে পাঠাতে সাহায্য করে। প্রধান networking device হলো  **Hub, Bridge, Switch, Router, Modem, Repeater এবং Gateway** ।
**১. Hub**   **Hub**  একটি মৌলিক networking device, যা সাধারণত LAN-এর মধ্যে ব্যবহৃত হয়। কোনো device hub-এর মাধ্যমে data পাঠালে hub সেই data-কে সংযুক্ত  **সব device-এর কাছে broadcast**  করে। ফলে সব device signal পায়, যদিও নির্দিষ্ট destination device-ই মূল data গ্রহণ করে।  Hub সাধারণত ছোট network-এ ব্যবহৃত হয় এবং  **half-duplex mode** -এ কাজ করে। অর্থাৎ একই সময়ে send এবং receive উভয় কাজ করতে পারে না। এটি তুলনামূলকভাবে কম ব্যয়বহুল এবং OSI model-এর  **Layer 1 বা Physical Layer** -এ কাজ করে।   **মূল কথা:**  Hub data সব connected device-এর কাছে broadcast করে।
**২. Bridge**   **Bridge**  দুই বা ততোধিক LAN segment-এর মধ্যে সংযোগ স্থাপন করে। এটি device-এর  **MAC address**  ব্যবহার করে data কোন destination-এ পাঠাতে হবে তা নির্ধারণ করে।  Bridge-এর একটি  **lookup table**  থাকে যেখানে device-এর MAC address সংরক্ষিত থাকে। Destination MAC address পরীক্ষা করে bridge নির্দিষ্ট destination-এর দিকে data forward করে। এটি OSI model-এর  **Layer 2 বা Data Link Layer** -এ কাজ করে।   **মূল কথা:**  Bridge MAC address ব্যবহার করে LAN segment-এর মধ্যে data forward করে।
**৩. Switch**   **Switch**  Hub ও Bridge-এর তুলনায় একটি উন্নত networking device। এটি  **MAC address**  ব্যবহার করে নির্দিষ্ট destination device-এর port-এ data পাঠায়।  Reference অনুযায়ী switch error checking করে এবং data error-free হলে destination-এ forward করে। Switch  **full-duplex mode** -এ কাজ করতে পারে, অর্থাৎ একই সময়ে data send এবং receive করা সম্ভব। এটি OSI model-এর  **Layer 2 বা Data Link Layer** -এ কাজ করে।   **মূল কথা:**  Switch MAC address ব্যবহার করে data নির্দিষ্ট device-এ পাঠায় এবং full-duplex communication সমর্থন করে।
**৪. Router**   **Router**  একাধিক network-এর মধ্যে সংযোগ স্থাপন করে। এটি wired Ethernet এবং wireless উভয় ধরনের connection সমর্থন করতে পারে।  Switch বা bridge-এর মতো MAC address-এর পরিবর্তে router মূলত  **IP address**  পরীক্ষা করে। Destination IP address বিশ্লেষণ করে router data packet-এর জন্য উপযুক্ত path নির্বাচন করে।  Reference অনুযায়ী router unauthorized access block করার মাধ্যমে firewall-এর মতো কাজও করতে পারে। Router OSI model-এর  **Layer 3 বা Network Layer** -এ কাজ করে।   **মূল কথা:**  Router বিভিন্ন network সংযুক্ত করে এবং IP address-এর ভিত্তিতে packet forward করে।
**৫. Modem**   **Modem**  শব্দটি  **Modulator-Demodulator**  থেকে এসেছে। এটি digital signal-কে analog signal এবং analog signal-কে digital signal-এ রূপান্তর করে।  Computer থেকে digital data পাঠানোর সময় modem  **modulation**  করে digital signal-কে analog signal-এ রূপান্তর করে। আবার network থেকে analog signal এলে modem  **demodulation**  করে সেটিকে computer-এর উপযোগী digital signal-এ রূপান্তর করে।  Modem Internet Service Provider (ISP)-এর সাথে connection স্থাপন করে home ও business network-এ Internet access প্রদান করতে সাহায্য করে।   **মূল কথা:**  Modem digital ও analog signal-এর মধ্যে conversion করে।
**৬. Repeater**   **Repeater**  হলো signal-strengthening device। দীর্ঘ দূরত্বে signal দুর্বল হয়ে গেলে repeater সেই weak signal গ্রহণ করে সেটিকে amplify বা regenerate করে আবার শক্তিশালী signal হিসেবে পাঠায়।  এটি দীর্ঘ দূরত্বে weak signal-এর কারণে data loss ও communication সমস্যার সম্ভাবনা কমাতে সাহায্য করে। Repeater OSI model-এর  **Layer 1 বা Physical Layer** -এ কাজ করে।   **মূল কথা:**  Repeater দুর্বল signal-কে শক্তিশালী করে পুনরায় transmit করে।
**৭. Gateway**   **Gateway**  দুই বা ততোধিক  **dissimilar network** -এর মধ্যে সংযোগ স্থাপন করে। যেমন LAN, MAN এবং WAN-এর মধ্যে যোগাযোগ স্থাপনে এটি ব্যবহৃত হতে পারে। ভিন্ন network-এর architecture, protocol এবং data format থাকলেও gateway তাদের মধ্যে communication করতে সাহায্য করে।  Gateway incoming ও outgoing network traffic monitor ও control করতে পারে। এর গুরুত্বপূর্ণ কাজ হলো  **translator**  হিসেবে কাজ করা, অর্থাৎ ভিন্ন protocol, architecture বা data format-এর network-এর মধ্যে data translation করা।  Reference অনুযায়ী gateway OSI model-এর  **সকল ৭টি layer** -এ কাজ করে।   **মূল কথা:**  Gateway ভিন্ন ধরনের network সংযুক্ত করে এবং protocol translation করতে পারে।
**গুরুত্বপূর্ণ তুলনা**   **Hub:**  সব device-এর কাছে data broadcast করে; Layer 1; Half-duplex।  **Bridge:**  MAC address ব্যবহার করে; LAN segment সংযুক্ত করে; Layer 2।  **Switch:**  MAC address ব্যবহার করে; Hub ও Bridge-এর চেয়ে উন্নত; Layer 2; Full-duplex।  **Router:**  IP address ব্যবহার করে; বিভিন্ন network সংযুক্ত করে; Layer 3।  **Modem:**  Modulation ও demodulation করে।  **Repeater:**  Weak signal শক্তিশালী করে; Layer 1।  **Gateway:**  Dissimilar network সংযুক্ত করে এবং protocol translation করে; OSI-এর সব ৭টি layer-এ কাজ করে।
**OSI Layer অনুযায়ী মনে রাখুন**   **Layer 1 – Physical:**  Hub, Repeater।  **Layer 2 – Data Link:**  Bridge, Switch।  **Layer 3 – Network:**  Router।  **All 7 Layers:**  Gateway।  **Signal Conversion:**  Modem।
**Exam Focus**  মনে রাখুন:  **Hub → Broadcast** ,  **Bridge/Switch → MAC Address** ,  **Router → IP Address** ,  **Repeater → Signal Strengthening** ,  **Modem → Digital ↔ Analog Conversion** , এবং  **Gateway → Dissimilar Network + Protocol Translation** । Reference-এ Router ও Switch নিয়ে প্রশ্ন আসার কথা উল্লেখ করা হয়েছে, তাই সব networking device-এর function এবং OSI layer ভালোভাবে প্রস্তুত করা গুরুত্বপূর্ণ।

9

Networking Device

Network Interface Card (NIC)


A  **Network Interface Card (NIC)**  is a hardware device that enables a computer or other network device to connect and communicate with a network.
NIC can be  **built-in**  or installed as an  **expansion card** . Modern computers commonly have an integrated NIC, while external USB network adapters can also be used.
A NIC mainly operates at the  **Physical Layer**  and  **Data Link Layer**  of the  **OSI Model** . It converts data into signals suitable for transmission over the network medium and handles Data Link Layer functions such as frame processing.
Every network interface normally has a unique  **MAC Address** , which is used to identify the network interface on the local network.
NICs can provide connectivity through different technologies, such as  **Ethernet**  using network cables and  **Wi-Fi**  using wireless signals.
**Functions of NIC:**  Connecting a device to a network, sending and receiving data, converting data into appropriate signals, processing network frames, and providing a MAC address for network identification.
**Types of NIC:**  The two common types are  **Wired NIC**  and  **Wireless NIC** . A wired NIC generally uses Ethernet cables, while a wireless NIC uses Wi-Fi radio signals.
**Example:**  The Ethernet port of a desktop computer and the built-in Wi-Fi adapter of a laptop are examples of network interfaces.

**Network Interface Card (NIC)**  হলো একটি Hardware Device, যা Computer বা অন্য কোনো Network Device-কে Network-এর সাথে সংযুক্ত ও Communication করতে সাহায্য করে।
NIC  **Built-in**  হতে পারে অথবা  **Expansion Card**  হিসেবে Computer-এ যুক্ত করা যেতে পারে। বর্তমানে অধিকাংশ Computer-এ Integrated NIC থাকে এবং USB Network Adapter-ও ব্যবহার করা যায়।
NIC প্রধানত  **OSI Model** -এর  **Physical Layer**  এবং  **Data Link Layer** -এ কাজ করে। এটি Data-কে Network Medium-এর মাধ্যমে পাঠানোর উপযোগী Signal-এ রূপান্তর করে এবং Data Link Layer-এর Frame Processing-এর মতো কাজ সম্পন্ন করে।
প্রতিটি Network Interface-এর সাধারণত একটি Unique  **MAC Address**  থাকে, যা Local Network-এ Network Interface-কে সনাক্ত করতে ব্যবহৃত হয়।
NIC বিভিন্ন Technology-এর মাধ্যমে Network Connectivity প্রদান করতে পারে, যেমন Cable ব্যবহার করে  **Ethernet**  এবং Wireless Signal ব্যবহার করে  **Wi-Fi** ।
**NIC-এর প্রধান কাজ:**  Device-কে Network-এর সাথে সংযুক্ত করা, Data Send ও Receive করা, Data-কে উপযুক্ত Signal-এ রূপান্তর করা, Network Frame Process করা এবং Network Identification-এর জন্য MAC Address প্রদান করা।
**NIC-এর ধরন:**  সাধারণত  **Wired NIC**  এবং  **Wireless NIC** —এই দুই ধরনের NIC বেশি ব্যবহৃত হয়। Wired NIC সাধারণত Ethernet Cable ব্যবহার করে, আর Wireless NIC Wi-Fi Radio Signal ব্যবহার করে।
**উদাহরণ:**  Desktop Computer-এর Ethernet Port এবং Laptop-এর Built-in Wi-Fi Adapter হলো Network Interface-এর উদাহরণ।

10

Networking Device

Reapeter


A  **Repeater**  is a network device that receives a weak network signal, regenerates it, and retransmits it to extend the communication distance.
When a network signal travels through transmission media such as  **Ethernet Cable**  or wireless media, its strength gradually decreases as the distance increases. This phenomenon is known as  **Signal Attenuation** .
A repeater receives the weakened signal and  **regenerates**  it before forwarding it to the next segment or device. Therefore, it helps maintain the quality of the signal over a longer distance.
A traditional repeater operates at the  **Physical Layer (Layer 1)**  of the  **OSI Model** . It does not examine the destination address or make routing decisions.
**Advantages:**  It extends network coverage, helps overcome signal attenuation, and allows devices to communicate over greater distances.
**Example:**  A Wi-Fi repeater can receive a weak Wi-Fi signal and retransmit it to provide network coverage in an area that is farther from the main router.

**Repeater**  হলো একটি Network Device, যা দুর্বল Network Signal গ্রহণ করে তা Regenerate করে পুনরায় প্রেরণ করে এবং Communication-এর দূরত্ব বৃদ্ধি করতে সাহায্য করে।
Network Signal যখন  **Ethernet Cable**  বা Wireless Media-এর মতো Transmission Media-এর মধ্য দিয়ে দীর্ঘ দূরত্ব অতিক্রম করে, তখন দূরত্ব বৃদ্ধির সাথে সাথে Signal-এর শক্তি ধীরে ধীরে কমে যায়। এই ঘটনাকে  **Signal Attenuation**  বলা হয়।
Repeater দুর্বল Signal গ্রহণ করে তা  **Regenerate**  করার পর পরবর্তী Network Segment বা Device-এর দিকে পাঠায়। ফলে দীর্ঘ দূরত্বেও Signal-এর মান বজায় রাখতে সাহায্য করে।
একটি সাধারণ Repeater  **OSI Model** -এর  **Physical Layer (Layer 1)** -এ কাজ করে। এটি Destination Address পরীক্ষা করে না এবং Routing Decision গ্রহণ করে না।
**সুবিধা:**  এটি Network Coverage বৃদ্ধি করে, Signal Attenuation-এর সমস্যা কমাতে সাহায্য করে এবং অধিক দূরত্বে Device-এর মধ্যে Communication করতে সহায়তা করে।
**উদাহরণ:**  একটি Wi-Fi Repeater দুর্বল Wi-Fi Signal গ্রহণ করে তা পুনরায় Transmit করতে পারে, ফলে Main Router থেকে দূরের এলাকাতেও Network Coverage পাওয়া যায়।

11

Networking Device

Hub


A  **Hub**  is a basic networking device used to connect multiple devices in a  **Local Area Network (LAN)** .
A hub operates at the  **Physical Layer (Layer 1)**  of the  **OSI Model** . It does not examine MAC addresses or make decisions about where to forward data.
When a hub receives a signal from one device, it repeats the signal to  **all other connected ports** . Therefore, it cannot send data only to the intended destination device.
Because all connected devices share the same  **collision domain**  and bandwidth, network performance decreases as the number of connected devices increases. Collisions can also occur when multiple devices transmit at the same time.
Traditional Ethernet hubs operate in  **Half-Duplex**  mode, meaning a device can either send or receive data at a time, but it cannot perform both simultaneously.

**Types of Hub:**
**1. Passive Hub:**

Provides a physical connection between network devices.
Does not amplify or regenerate the incoming signal.
Generally does not require an external power supply.
Suitable for short-distance connections.

**2. Active Hub:**

Receives the incoming signal and regenerates or strengthens it before retransmitting it.
Requires a power source.
Works similarly to a repeater.
Can help extend the network's transmission distance.

**3. Intelligent Hub:**

Provides additional network management and monitoring features.
Can monitor network traffic and the status of ports.
May support management protocols such as  **SNMP**  and use a  **MIB (Management Information Base)**  for network management information.
Helps administrators monitor and troubleshoot network problems.

**Advantages of Hub:**

Simple to install and configure.
Less expensive than many managed networking devices.
Can connect multiple Ethernet devices in a small network.
Broadcasting behavior can sometimes be useful for basic network troubleshooting.

**Disadvantages of Hub:**

Broadcasts incoming data to all connected ports.
Creates a single collision domain.
Shares available bandwidth among connected devices.
Supports only  **Half-Duplex**  communication.
Provides no intelligent traffic filtering or MAC-address-based forwarding.
Generally offers lower performance and security than a modern  **Switch** .

**Hub**  হলো একটি Basic Networking Device, যা  **Local Area Network (LAN)** -এ একাধিক Device সংযুক্ত করতে ব্যবহৃত হয়।
Hub  **OSI Model** -এর  **Physical Layer (Layer 1)** -এ কাজ করে। এটি MAC Address পরীক্ষা করে না এবং কোন Device-এর কাছে Data পাঠাতে হবে সে বিষয়ে কোনো Decision নিতে পারে না।
Hub একটি Device থেকে Signal গ্রহণ করলে তা  **Connected সব Port-এ**  পুনরায় পাঠায়। ফলে এটি শুধুমাত্র নির্দিষ্ট Destination Device-এ Data পাঠাতে পারে না।
Hub-এর সাথে সংযুক্ত সব Device একই  **Collision Domain**  এবং Bandwidth Share করে। ফলে Device-এর সংখ্যা বাড়লে Network Performance কমে যায় এবং একই সময়ে একাধিক Device Data পাঠালে Collision হতে পারে।
Traditional Ethernet Hub  **Half-Duplex**  Mode-এ কাজ করে। অর্থাৎ একটি Device একই সময়ে Data Send এবং Receive—দুটো কাজ একসাথে করতে পারে না।

**Hub-এর প্রকারভেদ:**
**১. Passive Hub:**

Network Device-এর মধ্যে Physical Connection প্রদান করে।
Incoming Signal Amplify বা Regenerate করে না।
সাধারণত আলাদা Power Supply প্রয়োজন হয় না।
Short-distance Connection-এর জন্য উপযোগী।

**২. Active Hub:**

Incoming Signal গ্রহণ করে তা Regenerate বা Strengthen করে পুনরায় পাঠায়।
Power Source প্রয়োজন হয়।
Repeater-এর মতো কাজ করে।
Network-এর Transmission Distance বৃদ্ধি করতে সাহায্য করে।

**৩. Intelligent Hub:**

অতিরিক্ত Network Management ও Monitoring সুবিধা প্রদান করে।
Network Traffic এবং Port-এর Status Monitor করতে পারে।
Network Management-এর জন্য  **SNMP**  এবং  **MIB (Management Information Base)** -এর মতো প্রযুক্তি ব্যবহার করতে পারে।
Network Problem Monitor ও Troubleshooting করতে সাহায্য করে।

**Hub-এর সুবিধাসমূহ:**

Install ও Configure করা সহজ।
অনেক Managed Networking Device-এর তুলনায় কম খরচে ব্যবহার করা যায়।
ছোট Network-এ একাধিক Ethernet Device সংযুক্ত করা যায়।
Broadcasting-এর কারণে Basic Network Troubleshooting-এ কখনো কখনো সহায়ক।

**Hub-এর অসুবিধাসমূহ:**

একটি Port-এ আসা Data সব Connected Port-এ Broadcast করে।
একটি Single Collision Domain তৈরি করে।
Connected Device-গুলোর মধ্যে Available Bandwidth Share হয়।
শুধুমাত্র  **Half-Duplex**  Communication সমর্থন করে।
Intelligent Traffic Filtering বা MAC Address ভিত্তিক Forwarding করতে পারে না।
Modern  **Switch** -এর তুলনায় Performance ও Security কম।

12

Networking Device

Bridge


A  **Bridge**  is a networking device that connects two or more network segments and allows them to communicate with each other.
A traditional bridge operates at the  **Data Link Layer (Layer 2)**  of the  **OSI Model** . It uses  **MAC Addresses**  to make forwarding and filtering decisions.
The main purpose of a bridge is to divide a large LAN into smaller network segments, reduce unnecessary traffic, and improve network performance.

**How Bridge Works:**

The bridge receives a data frame and examines its  **Source MAC Address**  and  **Destination MAC Address** .
It learns the location of devices by recording Source MAC Addresses in its  **MAC Address Table** .
If the destination device is on the same segment from which the frame came, the bridge  **filters**  the frame and does not forward it to the other segment.
If the destination device is on another segment, the bridge  **forwards**  the frame to the appropriate segment.
If the destination MAC address is unknown, the bridge generally  **floods**  the frame to the other segments, except the segment from which the frame was received.
This filtering and forwarding process reduces unnecessary traffic between network segments.

**Key Characteristics of Bridge:**

Operates at  **Layer 2 (Data Link Layer)** .
Uses  **MAC Addresses** .
Maintains a  **MAC Address Table** .
Can perform  **Frame Filtering**  and  **Frame Forwarding** .
Separates  **Collision Domains** .
Does not normally separate  **Broadcast Domains** .

**Note:**  A modern  **Network Switch**  performs the basic functions of a multi-port bridge and is commonly considered a multi-port bridge.

**Bridge**  হলো একটি Networking Device, যা দুই বা ততোধিক Network Segment-কে সংযুক্ত করে এবং তাদের মধ্যে Communication করতে সাহায্য করে।
একটি Traditional Bridge  **OSI Model** -এর  **Data Link Layer (Layer 2)** -এ কাজ করে। এটি Forwarding এবং Filtering Decision নেওয়ার জন্য  **MAC Address**  ব্যবহার করে।
Bridge-এর প্রধান উদ্দেশ্য হলো একটি বড় LAN-কে ছোট ছোট Network Segment-এ ভাগ করা, অপ্রয়োজনীয় Traffic কমানো এবং Network Performance উন্নত করা।

**Bridge কীভাবে কাজ করে:**

Bridge একটি Data Frame গ্রহণ করে এবং এর  **Source MAC Address**  ও  **Destination MAC Address**  পরীক্ষা করে।
Source MAC Address-এর তথ্য  **MAC Address Table** -এ সংরক্ষণ করে Device-এর অবস্থান শিখে নেয়।
যদি Destination Device একই Segment-এ থাকে যেখান থেকে Frame এসেছে, তাহলে Bridge Frame-টি  **Filter**  করে এবং অন্য Segment-এ পাঠায় না।
যদি Destination Device অন্য Segment-এ থাকে, তাহলে Bridge Frame-টি সংশ্লিষ্ট Segment-এ  **Forward**  করে।
যদি Destination MAC Address অজানা থাকে, তাহলে Bridge সাধারণত যে Segment থেকে Frame এসেছে সেটি বাদ দিয়ে অন্যান্য Segment-এ Frame-টি  **Flood**  করে।
এই Filtering ও Forwarding প্রক্রিয়ার মাধ্যমে Network Segment-এর মধ্যে অপ্রয়োজনীয় Traffic কমানো যায়।

**Bridge-এর প্রধান বৈশিষ্ট্য:**

**Layer 2 (Data Link Layer)** -এ কাজ করে।
**MAC Address**  ব্যবহার করে।
**MAC Address Table**  সংরক্ষণ করে।
**Frame Filtering**  এবং  **Frame Forwarding**  করতে পারে।
**Collision Domain**  আলাদা করে।
সাধারণত  **Broadcast Domain**  আলাদা করে না।

**Note:**  আধুনিক  **Network Switch**  মূলত একটি Multi-port Bridge-এর মতো কাজ করে এবং একটি Switch-কে সাধারণভাবে  **Multi-port Bridge**  হিসেবে বিবেচনা করা হয়।

13

Networking Device

Switch


A  **Switch**  is a networking device that connects multiple devices such as computers, printers, and servers within a  **Local Area Network (LAN)**  and forwards data between them.
A switch primarily operates at the  **Data Link Layer (Layer 2)**  of the  **OSI Model** . Some advanced  **Layer 3 Switches**  can also perform routing functions at the Network Layer.
A switch uses  **MAC Addresses**  to determine the destination of Ethernet frames. It maintains a  **MAC Address Table**  that maps MAC addresses to switch ports.
When a switch receives a frame, it examines the destination MAC address and forwards the frame only through the appropriate port when the destination is known. This reduces unnecessary traffic compared with a  **Hub** , which broadcasts incoming signals to all ports.
Each switch port generally represents a separate  **Collision Domain** . Modern switches support  **Full-Duplex**  communication, allowing data to be transmitted and received simultaneously.
**Advantages of Switch:**

Provides better network performance than a traditional hub.
Supports  **Full-Duplex**  communication.
Reduces unnecessary network traffic by forwarding frames to the intended port.
Each port is a separate collision domain, which greatly reduces collisions.
Easy to expand by adding more switches or connecting additional devices.
Failure of one connected node normally does not affect the other connected devices.

**Disadvantages of Switch:**

Generally more expensive than basic devices such as hubs.
Configuration and management can be more complex than a hub.
A switch primarily connects devices within a LAN; communication between different networks generally requires a  **Router**  or Layer 3 switching.
If a central switch fails, all devices connected through that switch may lose network connectivity.

**Key Exam Points:**

**OSI Layer:**  Data Link Layer (Layer 2) for a traditional switch.
**Address Used:**  MAC Address.
**Table Used:**  MAC Address Table.
**Duplex:**  Full-Duplex is supported by modern switches.
**Collision Domain:**  Each switch port is a separate collision domain.
**Broadcast Domain:**  A normal switch does not separate broadcast domains; VLANs can create separate broadcast domains.

**Switch**  হলো একটি Networking Device, যা Computer, Printer, Server ইত্যাদি একাধিক Device-কে  **Local Area Network (LAN)** -এর মধ্যে সংযুক্ত করে এবং তাদের মধ্যে Data Forward করে।
একটি সাধারণ  **Switch**  প্রধানত  **OSI Model** -এর  **Data Link Layer (Layer 2)** -এ কাজ করে। তবে Advanced  **Layer 3 Switch**  Network Layer-এ Routing-এর কাজও করতে পারে।
Switch Destination নির্ধারণের জন্য  **MAC Address**  ব্যবহার করে। এটি একটি  **MAC Address Table**  সংরক্ষণ করে, যেখানে MAC Address-এর সাথে সংশ্লিষ্ট Switch Port-এর তথ্য থাকে।
Switch কোনো Frame গ্রহণ করলে তার Destination MAC Address পরীক্ষা করে। Destination পরিচিত হলে Frame-টি শুধুমাত্র সংশ্লিষ্ট Port-এর মাধ্যমে Forward করে। ফলে  **Hub** -এর মতো সব Port-এ Data Broadcast করতে হয় না এবং Network Traffic কমে যায়।
একটি Switch-এর প্রতিটি Port সাধারণত একটি পৃথক  **Collision Domain**  তৈরি করে। আধুনিক Switch  **Full-Duplex**  Communication সমর্থন করে, ফলে একই সময়ে Data Send ও Receive করা যায়।
**Switch-এর সুবিধাসমূহ:**

Traditional Hub-এর তুলনায় ভালো Network Performance প্রদান করে।
**Full-Duplex**  Communication সমর্থন করে।
প্রয়োজনীয় Port-এ Frame Forward করে অপ্রয়োজনীয় Network Traffic কমায়।
প্রতিটি Port পৃথক Collision Domain হওয়ায় Collision অনেক কমে যায়।
অতিরিক্ত Device যুক্ত করার মাধ্যমে সহজে Network Expand করা যায়।
একটি Connected Node নষ্ট হলেও সাধারণত অন্য Connected Device-গুলোর উপর প্রভাব পড়ে না।

**Switch-এর অসুবিধাসমূহ:**

Basic Hub-এর মতো Device-এর তুলনায় সাধারণত বেশি ব্যয়বহুল।
Hub-এর তুলনায় Configuration ও Management কিছুটা জটিল।
Switch মূলত একটি LAN-এর মধ্যে Device সংযুক্ত করে; বিভিন্ন Network-এর মধ্যে Communication-এর জন্য সাধারণত  **Router**  বা Layer 3 Switching প্রয়োজন হয়।
একটি Central Switch নষ্ট হলে সেই Switch-এর সাথে সংযুক্ত সব Device Network Connectivity হারাতে পারে।

**গুরুত্বপূর্ণ পরীক্ষার তথ্য:**

**OSI Layer:**  Data Link Layer (Layer 2) — Traditional Switch-এর ক্ষেত্রে।
**Address:**  MAC Address।
**Table:**  MAC Address Table।
**Duplex:**  আধুনিক Switch Full-Duplex সমর্থন করে।
**Collision Domain:**  প্রতিটি Switch Port একটি পৃথক Collision Domain তৈরি করে।
**Broadcast Domain:**  সাধারণ Switch Broadcast Domain আলাদা করে না; তবে VLAN ব্যবহার করে পৃথক Broadcast Domain তৈরি করা যায়।

14

Networking Device

Router


A  **Router**  is a networking device that connects two or more different networks and forwards  **data packets**  between them.A traditional router operates at the  **Network Layer (Layer 3)**  of the  **OSI Model** . It uses  **IP Addresses**  to identify source and destination networks and determine where packets should be forwarded.
A router uses a  **Routing Table**  to select an appropriate or best available path for forwarding packets toward their destination. The routing table contains information about available networks, next-hop addresses, interfaces, and routing metrics.

**How Router Works:**

The router receives a data packet from an incoming interface.
It examines the packet's  **Destination IP Address** .
It checks the  **Routing Table**  to determine the best matching route.
It forwards the packet through the appropriate outgoing interface toward the destination network.
If no suitable route is available, the router may discard the packet or use a default route if one is configured.

**Advantages of Router:**

Connects different networks and enables communication between them.
Uses routing information to select an appropriate path for data packets.
Separates  **Broadcast Domains** , helping control broadcast traffic between networks.
Can provide security features such as  **Access Control Lists (ACLs)** , firewall functions, and traffic filtering depending on the router.
Supports large and scalable networks.

**Disadvantages of Router:**

Configuration and management can require technical knowledge.
High-performance routers can be expensive.
Packet processing and complex configurations can affect performance if the router is overloaded or underpowered.
A poorly configured or unsecured router can become a security risk.
If a critical router fails and there is no backup path, communication between the affected networks may be interrupted.

**Key Exam Points:**

**OSI Layer:**  Network Layer (Layer 3).
**Address Used:**  IP Address.
**Table Used:**  Routing Table.
**Data Unit:**  Packet.
**Main Function:**  Routing and forwarding packets between different networks.
**Broadcast Domain:**  A router separates Broadcast Domains.

**Router**  হলো একটি Networking Device, যা দুই বা ততোধিক ভিন্ন Network-কে সংযুক্ত করে এবং তাদের মধ্যে  **Data Packet**  Forward করে।
একটি Traditional Router  **OSI Model** -এর  **Network Layer (Layer 3)** -এ কাজ করে। এটি Source ও Destination Network শনাক্ত করতে এবং Packet কোথায় পাঠাতে হবে তা নির্ধারণ করতে  **IP Address**  ব্যবহার করে।
Router Packet Forward করার জন্য একটি  **Routing Table**  ব্যবহার করে। Routing Table-এ বিভিন্ন Network, Next-hop Address, Interface এবং Routing Metric সম্পর্কিত তথ্য থাকে, যা Router-কে উপযুক্ত বা সর্বোত্তম Available Path নির্বাচন করতে সাহায্য করে।

**Router কীভাবে কাজ করে:**

Router একটি Incoming Interface-এর মাধ্যমে Data Packet গ্রহণ করে।
এটি Packet-এর  **Destination IP Address**  পরীক্ষা করে।
এরপর  **Routing Table**  পরীক্ষা করে সবচেয়ে উপযুক্ত Route নির্ধারণ করে।
Router উপযুক্ত Outgoing Interface-এর মাধ্যমে Packet-টি Destination Network-এর দিকে Forward করে।
উপযুক্ত Route না পাওয়া গেলে Router Packet Drop করতে পারে অথবা Configured থাকলে Default Route ব্যবহার করতে পারে।

**Router-এর সুবিধাসমূহ:**

বিভিন্ন Network-কে সংযুক্ত করে এবং তাদের মধ্যে Communication করতে সাহায্য করে।
Routing Information ব্যবহার করে Data Packet-এর জন্য উপযুক্ত Path নির্বাচন করে।
**Broadcast Domain**  আলাদা করে এবং Network-এর মধ্যে Broadcast Traffic নিয়ন্ত্রণে সাহায্য করে।
Router-এর ধরন অনুযায়ী  **Access Control List (ACL)** , Firewall এবং Traffic Filtering-এর মতো Security Feature প্রদান করতে পারে।
বড় ও Scalable Network তৈরি করতে সহায়তা করে।

**Router-এর অসুবিধাসমূহ:**

Configuration ও Management-এর জন্য Technical Knowledge প্রয়োজন হতে পারে।
High-performance Router তুলনামূলকভাবে ব্যয়বহুল।
Router Overloaded বা Underpowered হলে Packet Processing-এর কারণে Network Performance কমে যেতে পারে।
Router সঠিকভাবে Configure বা Secure না করলে এটি Network Security-এর জন্য ঝুঁকিপূর্ণ হতে পারে।
কোনো গুরুত্বপূর্ণ Router নষ্ট হলে এবং Backup Path না থাকলে সংশ্লিষ্ট Network-গুলোর মধ্যে Communication বন্ধ হয়ে যেতে পারে।

**গুরুত্বপূর্ণ পরীক্ষার তথ্য:**

**OSI Layer:**  Network Layer (Layer 3)।
**Address:**  IP Address।
**Table:**  Routing Table।
**Data Unit:**  Packet।
**প্রধান কাজ:**  বিভিন্ন Network-এর মধ্যে Packet Routing ও Forwarding করা।
**Broadcast Domain:**  Router Broadcast Domain আলাদা করে।

15

Networking Device

Brouter


A  **Brouter**  (Bridging Router) is a networking device that combines the basic functions of a  **Bridge**  and a  **Router** .
A brouter can operate at both the  **Data Link Layer (Layer 2)**  and the  **Network Layer (Layer 3)**  of the  **OSI Model** .
At the Data Link Layer, a brouter can perform  **bridging**  functions such as filtering and forwarding frames based on  **MAC Addresses** .
At the Network Layer, it can perform  **routing**  functions by forwarding packets between different networks based on  **IP Addresses**  and routing information.
Therefore, a brouter can route routable protocols while bridging non-routable protocols. It is useful when a network requires both bridging and routing capabilities.
**Key Characteristics of Brouter:**

Combines the functions of a  **Bridge**  and a  **Router** .
Operates at  **Layer 2 and Layer 3**  of the OSI Model.
Uses  **MAC Addresses**  for bridging operations.
Uses  **IP Addresses**  for routing operations.
Can perform both  **Frame Forwarding**  and  **Packet Forwarding** .

**Brouter**  (Bridging Router) হলো একটি Networking Device, যা  **Bridge**  এবং  **Router** -এর প্রধান কার্যাবলিকে একত্রিত করে।
একটি Brouter  **OSI Model** -এর  **Data Link Layer (Layer 2)**  এবং  **Network Layer (Layer 3)** —উভয় Layer-এ কাজ করতে পারে।
Data Link Layer-এ Brouter  **MAC Address**  ব্যবহার করে Bridge-এর মতো Frame Filtering ও Forwarding করতে পারে।
Network Layer-এ এটি  **IP Address**  এবং Routing Information ব্যবহার করে বিভিন্ন Network-এর মধ্যে Packet Forward করার মাধ্যমে Router-এর মতো Routing করতে পারে।
অর্থাৎ Brouter Routable Protocol-এর জন্য Routing এবং Non-routable Protocol-এর জন্য Bridging করতে পারে। তাই একই Network-এ Bridging এবং Routing—উভয় ধরনের সুবিধা প্রয়োজন হলে Brouter ব্যবহার করা যেতে পারে।
**Brouter-এর প্রধান বৈশিষ্ট্য:**

**Bridge**  ও  **Router** -এর কার্যাবলিকে একত্রিত করে।
OSI Model-এর  **Layer 2 এবং Layer 3** -এ কাজ করতে পারে।
Bridging-এর জন্য  **MAC Address**  ব্যবহার করে।
Routing-এর জন্য  **IP Address**  ব্যবহার করে।
**Frame Forwarding**  এবং  **Packet Forwarding** —উভয় কাজ করতে পারে।

16

Networking Device

Access point


An  **Access Point (AP)**  is a networking device that allows wireless devices such as smartphones, laptops, tablets, and other Wi-Fi-enabled devices to connect to a wired network.
An access point creates a  **Wi-Fi network**  and provides wireless connectivity between wireless devices and the wired network. It commonly connects to a  **Switch**  or Router through an Ethernet cable.
An AP works mainly at the  **Data Link Layer (Layer 2)**  of the  **OSI Model** , although its exact functionality can vary depending on the device.
Access points are commonly used to provide wireless network coverage in  **homes, offices, schools, hotels, airports, and public spaces** .
Multiple access points can be deployed in a large area to provide wider  **Wi-Fi coverage** . This allows users to connect to the network from different locations without using physical network cables.
**Functions of Access Point:**

Creates a wireless LAN (Wi-Fi network).
Connects wireless devices to a wired network.
Transmits and receives wireless signals.
Provides wireless network coverage within a specific area.
Supports multiple wireless devices simultaneously.

**Advantages of Access Point:**

Provides convenient wireless connectivity without physical cables.
Allows multiple wireless devices to connect to the network.
Can extend Wi-Fi coverage when multiple APs are deployed.
Useful in places where wired connections are difficult or impractical.

**Key Exam Points:**

**Abbreviation:**  AP = Access Point.
**Main Purpose:**  Connects wireless devices to a network.
**Technology:**  Wi-Fi / IEEE 802.11.
**Common Layer:**  Data Link Layer (Layer 2).
**Connection:**  Usually connects to a wired LAN through Ethernet.

**Access Point (AP)**  হলো একটি Networking Device, যা Smartphone, Laptop, Tablet এবং অন্যান্য Wi-Fi-enabled Device-কে একটি Wired Network-এর সাথে সংযুক্ত হতে সাহায্য করে।
Access Point একটি  **Wi-Fi Network**  তৈরি করে এবং Wireless Device ও Wired Network-এর মধ্যে Wireless Connectivity প্রদান করে। এটি সাধারণত Ethernet Cable-এর মাধ্যমে একটি  **Switch**  বা Router-এর সাথে সংযুক্ত থাকে।
Access Point প্রধানত  **OSI Model** -এর  **Data Link Layer (Layer 2)** -এ কাজ করে, যদিও Device-এর ধরন অনুযায়ী এর Functionality ভিন্ন হতে পারে।
Access Point সাধারণত  **Home, Office, School, Hotel, Airport এবং বিভিন্ন Public Space** -এ Wireless Network Coverage প্রদানের জন্য ব্যবহৃত হয়।
বড় এলাকায় একাধিক Access Point স্থাপন করে  **Wi-Fi Coverage**  বৃদ্ধি করা যায়। ফলে Physical Network Cable ছাড়াই বিভিন্ন স্থান থেকে Network-এ সংযুক্ত থাকা সম্ভব হয়।
**Access Point-এর প্রধান কাজ:**

একটি Wireless LAN বা Wi-Fi Network তৈরি করা।
Wireless Device-কে Wired Network-এর সাথে সংযুক্ত করা।
Wireless Signal Transmit ও Receive করা।
নির্দিষ্ট এলাকায় Wireless Network Coverage প্রদান করা।
একসাথে একাধিক Wireless Device-কে Network-এ সংযুক্ত করা।

**Access Point-এর সুবিধাসমূহ:**

Physical Cable ছাড়াই Wireless Connectivity প্রদান করে।
একাধিক Wireless Device-কে Network-এ সংযুক্ত করতে পারে।
একাধিক AP ব্যবহার করে Wi-Fi Coverage বৃদ্ধি করা যায়।
যেসব স্থানে Wired Connection স্থাপন করা কঠিন বা অসুবিধাজনক, সেখানে কার্যকর।

**গুরুত্বপূর্ণ পরীক্ষার তথ্য:**

**পূর্ণরূপ:**  AP = Access Point।
**প্রধান কাজ:**  Wireless Device-কে Network-এর সাথে সংযুক্ত করা।
**Technology:**  Wi-Fi / IEEE 802.11।
**সাধারণ Layer:**  Data Link Layer (Layer 2)।
**Connection:**  সাধারণত Ethernet-এর মাধ্যমে Wired LAN-এর সাথে সংযুক্ত থাকে।

17

Networking Device

Hub  vs Switch vs Router


18

Networking Device

Router vs Gateway


19

Networking Device

Network Security Device (Firewall & it types)


A  **firewall**  is a security mechanism that monitors and controls network traffic entering or leaving a system or network. It applies predefined security rules to determine whether network traffic should be allowed or blocked. Firewalls provide protection against unauthorized access and help control communication between trusted and untrusted networks.
**Purpose of a Firewall**  The main purpose of a firewall is to control network traffic and protect systems from unauthorized access. Depending on its type, a firewall can filter packets, track network connections, inspect application data, detect malicious activity, control web access, and protect individual devices or entire networks.
**1. Packet Filtering Firewall**  A  **packet filtering firewall**  is one of the oldest and simplest types of firewall. It examines individual data packets as they enter or leave a network and compares them with a set of predefined rules. These rules can allow or block traffic based on factors such as  **IP address, port number, and protocol** .  It mainly examines packet headers rather than the actual contents of communication. Therefore, it is generally  **fast and efficient**  and does not require significant computing resources. It was widely used in early computer networks for providing basic network protection.
**2. Stateful Inspection Firewall**  A  **stateful inspection firewall**  improves upon packet filtering by keeping track of the  **state of active network connections** . Instead of treating every packet independently, it remembers previous packets and determines whether incoming traffic belongs to an established or legitimate session. Because it maintains connection context, it can make more intelligent security decisions than a basic packet filtering firewall. It provides a balance between  **security and performance**  and became popular as Internet applications became more complex.
**3. Circuit-Level Gateway Firewall**  A  **circuit-level gateway firewall**  operates at the  **session layer**  of network communication. It does not deeply inspect the actual contents of data packets. Instead, it verifies whether communication sessions are legitimate before allowing them to proceed. After a connection is established, traffic can pass without deep content inspection. This reduces processing overhead while helping to hide internal network details from external systems.
**4. Application Layer Firewall**  An  **application layer firewall**  examines network traffic at the application level. It understands specific application protocols such as  **HTTP, FTP, and SMTP**  and can inspect the actual content being exchanged. Because it performs deeper analysis, it can detect suspicious activities that lower-level firewalls may not detect. It provides stronger protection against many application and web-based threats, but the deeper inspection requires more processing power.
**5. Proxy Firewall**  A  **proxy firewall**  acts as an intermediary between users and the Internet. Instead of allowing a user to communicate directly with an external destination, the proxy firewall receives the user's request, evaluates it, and forwards the request to the destination on the user's behalf. This separation helps  **hide internal systems**  and provides an additional layer of security. Proxy firewalls are particularly useful for organizations that require greater control over web access and user activity.
**6. Next-Generation Firewall (NGFW)**  A  **Next-Generation Firewall**  combines traditional firewall functions with advanced security features. In addition to filtering network traffic, it can  **detect malware, identify applications, inspect encrypted connections, and integrate with threat intelligence systems** . NGFWs were developed to address increasingly sophisticated cyber attacks. They provide security beyond simple network rules and have become an important component of enterprise cybersecurity strategies.
**7. Network Firewall**  A  **network firewall**  protects an entire network by monitoring traffic moving between internal systems and external networks. It is commonly placed at the  **edge of an organization's network** , where Internet traffic enters and exits. Because access control is applied at a central location, a network firewall can protect multiple devices simultaneously. Businesses commonly use network firewalls as a primary defense against unauthorized external access.
**8. Host-Based Firewall**  A  **host-based firewall**  runs directly on an individual device rather than protecting an entire network. It monitors traffic entering and leaving a specific  **computer, server, or workstation** . Because it operates locally, it can apply security rules specifically designed for that device. Modern operating systems often provide built-in host-based firewalls, giving individual devices an additional layer of protection.
**9. Cloud Firewall**  A  **cloud firewall**  is designed to protect resources in cloud computing environments. Instead of depending on physical firewall hardware, it operates as a  **virtual security service**  that protects cloud applications, servers, and other cloud resources. As organizations moved their infrastructure to cloud environments, traditional perimeter-based security became less effective. Cloud firewalls provide flexible protection that can  **scale with cloud services and remote workloads** .
**10. Web Application Firewall (WAF)**  A  **Web Application Firewall (WAF)**  is specifically designed to protect websites and web applications. It analyzes  **HTTP and HTTPS traffic**  to identify attacks targeting web-based systems. Common web attacks such as  **SQL injection, Cross-Site Scripting (XSS), and malicious web requests**  can be detected and blocked before they reach the application. WAFs are therefore an important security component for modern web applications.
**11. Unified Threat Management (UTM) Firewall**  A  **Unified Threat Management firewall**  combines several security functions into a single platform. In addition to firewall capabilities, it may provide  **antivirus scanning, intrusion prevention, content filtering, and VPN support** . This all-in-one approach simplifies security management because an organization does not need separate products for every security function. UTM systems are particularly useful for small and medium-sized organizations that require broad protection through a centralized solution.
**12. Distributed Firewall**  A  **distributed firewall**  extends firewall protection across multiple devices and locations instead of depending on one centralized firewall. Security policies are enforced directly on  **endpoints, servers, or virtual machines**  throughout the network. This approach is particularly useful in environments involving  **remote work, cloud infrastructure, and decentralized resources** . By placing security controls closer to individual systems, distributed firewalls can maintain protection even when users and resources are located in different places.
**Important Differences Among Firewall Types**   **Packet Filtering:**  Filters individual packets using IP addresses, ports, and protocols.  **Stateful Inspection:**  Tracks active connections and considers the state of network sessions.  **Circuit-Level Gateway:**  Validates communication sessions without deeply inspecting packet contents.  **Application Layer:**  Inspects application-level protocols and actual data content.  **Proxy Firewall:**  Acts as an intermediary between users and external destinations.  **Next-Generation Firewall:**  Combines traditional filtering with advanced threat detection features.  **Network Firewall:**  Protects an entire network at a central network boundary.  **Host-Based Firewall:**  Protects an individual computer, server, or workstation.  **Cloud Firewall:**  Protects cloud-based applications, servers, and resources.  **WAF:**  Protects websites and web applications from web-based attacks.  **UTM Firewall:**  Combines multiple security functions into one platform.  **Distributed Firewall:**  Enforces security policies across multiple devices and locations.
**Quick Revision**   **Packet Filtering →**  IP + Port + Protocol  **Stateful →**  Connection State  **Circuit-Level →**  Session Validation  **Application Layer →**  Application Protocol & Content  **Proxy →**  Intermediary  **NGFW →**  Advanced Threat Protection  **Network Firewall →**  Entire Network  **Host-Based →**  Individual Device  **Cloud Firewall →**  Cloud Resources  **WAF →**  Web Applications  **UTM →**  Multiple Security Functions  **Distributed →**  Multiple Devices/Locations

**Firewall**  হলো একটি security mechanism যা network-এর incoming এবং outgoing traffic পর্যবেক্ষণ ও নিয়ন্ত্রণ করে। এটি predefined security rules-এর ভিত্তিতে নির্ধারণ করে কোন traffic অনুমোদিত হবে এবং কোন traffic block করা হবে। Firewall মূলত unauthorized access প্রতিরোধ এবং trusted ও untrusted network-এর মধ্যে communication নিয়ন্ত্রণে ব্যবহৃত হয়।
**Firewall-এর উদ্দেশ্য**  Firewall-এর প্রধান উদ্দেশ্য হলো network traffic নিয়ন্ত্রণ করা এবং unauthorized access থেকে system ও network-কে সুরক্ষিত রাখা। Firewall-এর ধরন অনুযায়ী এটি packet filter করতে, active connection track করতে, application data inspect করতে, malicious activity শনাক্ত করতে, web access নিয়ন্ত্রণ করতে এবং individual device বা entire network সুরক্ষিত করতে পারে।
**১. Packet Filtering Firewall**   **Packet filtering firewall**  হলো সবচেয়ে পুরোনো ও সহজ ধরনের firewall-এর একটি। এটি network-এ প্রবেশ বা network থেকে বের হওয়া প্রতিটি data packet পরীক্ষা করে এবং predefined rules-এর সাথে তুলনা করে। Rules-এর ভিত্তিতে  **IP address, port number এবং protocol**  অনুযায়ী traffic allow বা block করা যায়। এটি মূলত packet-এর header পরীক্ষা করে, communication-এর মূল content গভীরভাবে পরীক্ষা করে না। তাই এটি  **দ্রুত ও efficient**  এবং তুলনামূলকভাবে কম computing resources প্রয়োজন করে।
**২. Stateful Inspection Firewall**   **Stateful inspection firewall**  packet filtering firewall-এর উন্নত রূপ। এটি active network connection-এর  **state বা অবস্থা track**  করে। প্রতিটি packet আলাদাভাবে পরীক্ষা করার পরিবর্তে এটি পূর্ববর্তী packet-এর তথ্য মনে রাখে এবং incoming traffic কোনো established বা legitimate session-এর অংশ কি না তা নির্ধারণ করে। Connection-এর context বিবেচনা করার কারণে এটি basic packet filtering-এর তুলনায় আরও intelligent security decision নিতে পারে এবং  **security ও performance-এর মধ্যে ভালো balance**  প্রদান করে।
**৩. Circuit-Level Gateway Firewall**   **Circuit-level gateway firewall**  network communication-এর  **session layer** -এ কাজ করে। এটি data packet-এর actual content গভীরভাবে পরীক্ষা না করে communication session বৈধ কি না তা যাচাই করে। Connection established হওয়ার পর traffic গভীর inspection ছাড়াই pass করতে পারে। ফলে processing overhead কম থাকে এবং external system-এর কাছ থেকে internal network-এর কিছু details গোপন রাখতে সাহায্য করে।
**৪. Application Layer Firewall**   **Application layer firewall**  network traffic-এর application level-এ inspection করে। এটি  **HTTP, FTP এবং SMTP** -এর মতো specific application protocol বুঝতে পারে এবং exchanged data-এর actual content পরীক্ষা করতে পারে। গভীর analysis করার কারণে lower-level firewall যেসব suspicious activity শনাক্ত করতে ব্যর্থ হতে পারে, application layer firewall সেগুলো শনাক্ত করতে পারে। তবে গভীর inspection-এর কারণে বেশি processing power প্রয়োজন হয়।
**৫. Proxy Firewall**   **Proxy firewall**  user এবং Internet-এর মধ্যে একটি  **intermediary**  হিসেবে কাজ করে। User সরাসরি destination-এর সাথে যোগাযোগ না করে প্রথমে proxy firewall-এর কাছে request পাঠায়। Firewall request পরীক্ষা করে এবং user-এর হয়ে destination-এ request forward করে। এটি internal system-কে external system থেকে আড়াল করতে সাহায্য করে এবং অতিরিক্ত security layer প্রদান করে। Web access এবং user activity-এর ওপর বেশি control প্রয়োজন এমন organization-এ এটি কার্যকর।
**৬. Next-Generation Firewall (NGFW)**   **Next-Generation Firewall**  traditional firewall-এর traffic filtering-এর সাথে advanced security features যুক্ত করে। এটি  **malware detection, application identification, encrypted connection inspection এবং threat intelligence integration** -এর মতো কাজ করতে পারে। আধুনিক ও sophisticated cyber attack মোকাবিলার জন্য NGFW তৈরি হয়েছে। Enterprise cybersecurity-তে এটি একটি গুরুত্বপূর্ণ security component।
**৭. Network Firewall**   **Network firewall**  একটি সম্পূর্ণ network-কে সুরক্ষিত করে। এটি internal system এবং external network-এর মধ্যে চলাচলকারী traffic monitor করে। সাধারণত এটি organization-এর network-এর  **edge বা boundary** -তে স্থাপন করা হয়, যেখানে Internet traffic network-এ প্রবেশ ও বের হয়। একটি central location থেকে access control করার ফলে একই সঙ্গে অনেকগুলো device সুরক্ষিত করা যায়।
**৮. Host-Based Firewall**   **Host-based firewall**  সম্পূর্ণ network-এর পরিবর্তে একটি নির্দিষ্ট device-এর ওপর সরাসরি কাজ করে। এটি নির্দিষ্ট  **computer, server বা workstation** -এ incoming এবং outgoing traffic monitor করে। এটি localভাবে কাজ করার কারণে নির্দিষ্ট device-এর প্রয়োজন অনুযায়ী security rules প্রয়োগ করতে পারে। আধুনিক operating system-এ অনেক সময় built-in host-based firewall থাকে।
**৯. Cloud Firewall**   **Cloud firewall**  cloud computing environment-এর resource সুরক্ষার জন্য তৈরি। Physical hardware-এর ওপর নির্ভর করার পরিবর্তে এটি একটি  **virtual security service**  হিসেবে cloud-based application, server এবং resource সুরক্ষিত করে। Cloud infrastructure এবং remote workload বৃদ্ধি পাওয়ার সাথে সাথে cloud firewall scalable ও flexible security প্রদান করে।
**১০. Web Application Firewall (WAF)**   **Web Application Firewall (WAF)**  বিশেষভাবে website ও web application সুরক্ষার জন্য ব্যবহৃত হয়। এটি  **HTTP এবং HTTPS traffic**  বিশ্লেষণ করে web-based attack শনাক্ত করার চেষ্টা করে।  **SQL Injection, Cross-Site Scripting (XSS)**  এবং malicious web request-এর মতো attack application-এ পৌঁছানোর আগেই detect ও block করা যেতে পারে।
**১১. Unified Threat Management (UTM) Firewall**   **UTM firewall**  একটি platform-এর মধ্যে একাধিক security function একত্র করে। Firewall-এর পাশাপাশি এতে  **antivirus scanning, intrusion prevention, content filtering এবং VPN support**  থাকতে পারে। এই all-in-one approach security management সহজ করে এবং আলাদা আলাদা security product-এর প্রয়োজন কমায়। Small ও medium-sized organization-এর জন্য এটি বিশেষভাবে উপযোগী।
**১২. Distributed Firewall**   **Distributed firewall**  একটি কেন্দ্রীয় firewall-এর ওপর নির্ভর না করে একাধিক device ও location-এ firewall protection ছড়িয়ে দেয়। Security policy সরাসরি  **endpoint, server বা virtual machine** -এর ওপর প্রয়োগ করা যায়। Remote work, cloud infrastructure এবং decentralized environment-এর ক্ষেত্রে এটি গুরুত্বপূর্ণ। Security control individual system-এর কাছাকাছি থাকায় বিভিন্ন location-এ থাকা resource ও user-কেও সুরক্ষিত রাখা যায়।
**Firewall-এর ধরনগুলোর গুরুত্বপূর্ণ পার্থক্য**   **Packet Filtering:**  IP, Port ও Protocol-এর ভিত্তিতে packet filter করে।  **Stateful Inspection:**  Active connection-এর state track করে।  **Circuit-Level Gateway:**  Communication session validate করে।  **Application Layer:**  Application protocol ও content inspect করে।  **Proxy Firewall:**  User ও external destination-এর মধ্যবর্তী intermediary হিসেবে কাজ করে।  **Next-Generation Firewall:**  Traditional filtering-এর সাথে advanced threat protection প্রদান করে।  **Network Firewall:**  সম্পূর্ণ network সুরক্ষিত করে।  **Host-Based Firewall:**  একটি নির্দিষ্ট device সুরক্ষিত করে।  **Cloud Firewall:**  Cloud resource সুরক্ষিত করে।  **WAF:**  Website ও web application সুরক্ষিত করে।  **UTM Firewall:**  এক platform-এ একাধিক security function প্রদান করে।  **Distributed Firewall:**  বিভিন্ন device ও location-এ security policy প্রয়োগ করে।
**দ্রুত রিভিশন**   **Packet Filtering →**  IP + Port + Protocol  **Stateful →**  Connection State  **Circuit-Level →**  Session Validation  **Application Layer →**  Application Protocol & Content  **Proxy →**  Intermediary  **NGFW →**  Advanced Threat Protection  **Network Firewall →**  Entire Network  **Host-Based →**  Individual Device  **Cloud Firewall →**  Cloud Resources  **WAF →**  Web Applications  **UTM →**  Multiple Security Functions  **Distributed →**  Multiple Devices/Locations

20

Networking Device

Traditional Firewall vs Next generation firewall


**Traditional Firewall**  A  **traditional firewall**  controls incoming and outgoing network traffic according to predefined security rules. It can be implemented through hardware or software and primarily performs packet filtering based on  **source/destination IP addresses, protocols, and port numbers** . It mainly operates at the  **Network Layer (Layer 3)**  of the OSI model.
**Advantages of Traditional Firewall**   **Simplicity:**  Traditional firewalls are relatively easy to set up, configure, and manage because they provide basic traffic filtering.  **Cost-effective:**  They are generally less expensive and suitable for small networks with limited security requirements.  **Performance:**  Since they perform minimal packet inspection, they generally provide high-speed network performance.
**Disadvantages of Traditional Firewall**   **Limited Security:**  Traditional firewalls mainly provide packet filtering and cannot effectively detect application-layer threats or advanced attacks such as malware and Advanced Persistent Threats (APTs).  **No Deep Packet Inspection (DPI):**  They generally do not inspect the actual content of data in transit, making them less effective against modern threats.  **No Application Awareness:**  They cannot identify specific applications and therefore cannot enforce detailed application-level security policies.
**Next-Generation Firewall (NGFW)**  A  **Next-Generation Firewall (NGFW)**  is an advanced firewall that provides multiple layers of security beyond traditional packet filtering. It can perform  **Deep Packet Inspection (DPI), Intrusion Prevention, Application Control, and Identity-Based Access Control** . According to the reference, NGFW operates across  **Layers 3 to 7**  of the OSI model, providing more granular control over network traffic.
**Advantages of Next-Generation Firewall**   **Advanced Threat Protection:**  NGFW can detect and prevent modern threats such as malware, ransomware, and Advanced Persistent Threats (APTs) using DPI, IDS/IPS, and sandboxing.  **Application Awareness:**  It can identify and control traffic based on specific applications rather than relying only on IP addresses and ports.  **Unified Security:**  NGFW can integrate several security functions, including firewall protection, VPN, and antivirus capabilities.  **Identity Awareness:**  It can apply security policies based on user identity, allowing role-based access control.
**Disadvantages of Next-Generation Firewall**   **Higher Cost:**  NGFWs are more expensive than traditional firewalls because of their advanced features and security functions.  **Complex Management:**  They are more difficult to configure and administer because they provide many security features.  **Performance Impact:**  Advanced inspection techniques such as DPI require additional processing and may reduce network performance, although they can be optimized.
**Traditional Firewall vs Next-Generation Firewall**

Feature
Traditional Firewall
Next-Generation Firewall (NGFW)

**Primary Function**
Packet filtering based on IP, port, and protocol
Advanced security including DPI, malware detection, and intrusion prevention

**Layer of Operation**
Network Layer (Layer 3)
Layers 3 to 7

**Application Awareness**
No
Yes

**Threat Detection**
Basic and limited
Advanced, including malware detection, IDS/IPS, and sandboxing

**DPI**
No
Yes

**User Identity Awareness**
No
Yes

**VPN Support**
Yes
Yes, with additional security/encryption features

**Cost**
Generally lower
Higher

**Performance**
Generally high due to minimal inspection
May be affected by deep inspection

**Intrusion Prevention System (IPS)**
No
Yes

**Granular Control**
Limited
High; provides application and traffic-level control

**Threat Updates**
Rare or manual
Frequent updates for new and evolving threats

**Quick Revision**   **Traditional Firewall →**  Basic packet filtering → IP + Port + Protocol → Layer 3 → Fast and inexpensive → Limited security.  **NGFW →**  Advanced inspection → DPI + Application Control + IDS/IPS + Identity Awareness → Layers 3–7 → Stronger security → Higher cost and complexity.

**Traditional firewall**  predefined security rules-এর ভিত্তিতে incoming ও outgoing network traffic নিয়ন্ত্রণ করে। এটি hardware অথবা software-এর মাধ্যমে বাস্তবায়ন করা যায় এবং মূলত  **source/destination IP address, protocol ও port number** -এর ভিত্তিতে packet filtering করে। এটি প্রধানত OSI model-এর  **Network Layer (Layer 3)** -এ কাজ করে।
**Traditional Firewall-এর সুবিধা**   **সহজতা:**  Basic traffic filtering করার কারণে এটি setup, configure ও manage করা তুলনামূলকভাবে সহজ।  **কম খরচ:**  Traditional firewall সাধারণত কম ব্যয়বহুল এবং ছোট network-এর জন্য উপযোগী।  **ভালো Performance:**  Minimal packet inspection করার কারণে এটি সাধারণত দ্রুত network performance প্রদান করে।
**Traditional Firewall-এর অসুবিধা**   **সীমিত Security:**  এটি মূলত packet filtering করে এবং application-layer threat বা malware ও Advanced Persistent Threats (APTs)-এর মতো advanced attack কার্যকরভাবে শনাক্ত করতে পারে না।  **DPI নেই:**  সাধারণত data-এর actual content গভীরভাবে inspect করে না। ফলে আধুনিক threat মোকাবিলায় কার্যকারিতা সীমিত।  **Application Awareness নেই:**  নির্দিষ্ট application শনাক্ত করতে পারে না এবং detailed application-level security policy প্রয়োগ করতে পারে না।
**Next-Generation Firewall (NGFW)**   **Next-Generation Firewall (NGFW)**  হলো traditional firewall-এর তুলনায় আরও উন্নত firewall, যা একাধিক স্তরের security প্রদান করে। এটি  **Deep Packet Inspection (DPI), Intrusion Prevention, Application Control এবং Identity-Based Access Control**  প্রদান করতে পারে। Reference অনুযায়ী NGFW OSI model-এর  **Layer 3 থেকে Layer 7**  পর্যন্ত কাজ করে এবং network traffic-এর ওপর আরও granular control প্রদান করে।
**NGFW-এর সুবিধা**   **Advanced Threat Protection:**  DPI, IDS/IPS এবং sandboxing ব্যবহার করে malware, ransomware এবং Advanced Persistent Threats (APTs)-এর মতো আধুনিক threat শনাক্ত ও প্রতিরোধ করতে পারে।  **Application Awareness:**  শুধু IP address ও port-এর পরিবর্তে নির্দিষ্ট application-এর ভিত্তিতে traffic শনাক্ত ও নিয়ন্ত্রণ করতে পারে।  **Unified Security:**  Firewall, VPN এবং antivirus-এর মতো একাধিক security function একসাথে integrate করতে পারে।  **Identity Awareness:**  User identity-এর ভিত্তিতে security policy প্রয়োগ করতে পারে এবং role-based access control বাস্তবায়ন করতে পারে।
**NGFW-এর অসুবিধা**   **বেশি খরচ:**  Advanced features থাকার কারণে NGFW traditional firewall-এর তুলনায় বেশি ব্যয়বহুল।  **জটিল Management:**  অনেকগুলো security functionality থাকায় configure ও administer করা তুলনামূলকভাবে কঠিন।  **Performance Impact:**  DPI-এর মতো advanced inspection-এর জন্য বেশি processing power প্রয়োজন হওয়ায় network performance কিছুটা কমতে পারে।
**Traditional Firewall বনাম Next-Generation Firewall**

বিষয়
Traditional Firewall
NGFW

**মূল কাজ**
IP, Port ও Protocol-এর ভিত্তিতে packet filtering
DPI, malware detection ও intrusion preventionসহ advanced security

**OSI Layer**
Layer 3
Layer 3–7

**Application Awareness**
নেই
আছে

**Threat Detection**
Basic ও সীমিত
Advanced

**DPI**
নেই
আছে

**User Identity Awareness**
নেই
আছে

**VPN Support**
আছে
আছে, additional security/encryption featuresসহ

**Cost**
কম
বেশি

**Performance**
সাধারণত বেশি
Deep inspection-এর কারণে প্রভাবিত হতে পারে

**IPS**
নেই
আছে

**Granular Control**
সীমিত
অনেক বেশি

**Threat Updates**
কম বা manual
নতুন threat অনুযায়ী frequent updates

**দ্রুত রিভিশন**   **Traditional Firewall →**  Basic Packet Filtering → IP + Port + Protocol → Layer 3 → Fast ও কম খরচ → Limited Security।  **NGFW →**  Advanced Inspection → DPI + Application Control + IDS/IPS + Identity Awareness → Layer 3–7 → Strong Security → বেশি Cost ও Complexity।



**Previous Job Question:**  Network Topology & Devices



Topic Wise Question Bank

Computer Network

- ☆

1

Computer Network
Network Topology & Devices

Describe the functions of a Switch and a Router and explain two key differences between these networking devices.

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

2

Computer Network
Network Topology & Devices

Briefly describe the following network devices: Repeater, Hub, Bridge, Switch and Router.

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

3

Computer Network
Network Topology & Devices

Write connection type? i. Router to Router ii. Router to switch iii. Computer to computer iv. Hub to Switch

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

4

Computer Network
Network Topology & Devices

Difference among Switch, Bridge and Router.

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

5

Computer Network
Network Topology & Devices

What is Topology in data communication? What are differences between Bus, Ring, Tree and Star topology? Purpose of IEEE 802.11 committee. 10

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

6

Computer Network
Network Topology & Devices

A network administrator is replacing a hub-based LAN with a switch-based LAN. Explain the differences between half-duplex and full-duplex communication and discuss how the change affects network performance.[assume]

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

7

Computer Network
Network Topology & Devices

What is Network Topology? Distinguish between Bus, Ring, Tree and Star topology. Discuss how the Bus topology works.

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

**Assigment:**   Network Topology and Devices

- What is Network Topology? Explain the different types of Network Topology with suitable diagrams. Discuss the advantages and disadvantages of  **Bus, Ring, Star, Tree, Mesh, and Hybrid Topology** .
- What is a  **Networking Device** ? Explain the functions and OSI layers of  **Hub, Repeater, Bridge, Switch, Router, Modem, Gateway, and Brouter** .
- What is a  **Repeater** ? Explain  **Signal Attenuation**  and describe how a repeater helps extend the communication distance.
- What is a  **Firewall** ? Explain its purpose and discuss the major types of firewalls, including  **Packet Filtering, Stateful Inspection, Circuit-Level Gateway, Application Layer, Proxy, NGFW, WAF, UTM, and Host-Based Firewall** .
- Differentiate between a  **Traditional Firewall and a Next-Generation Firewall (NGFW)**  based on packet inspection, application awareness, threat detection, OSI layers, IPS, cost, and performance.
- What is a  **Gateway** ? Explain its functions and discuss how a gateway enables communication between networks using different protocols or architectures.
- What is an  **Access Point (AP)** ? Explain how an access point connects wireless devices to a wired LAN. Mention its functions, advantages, and common applications.
- A large organization needs a network that is  **reliable, scalable, and fault-tolerant** . Which network topology and networking devices would you recommend? Justify your answer based on cost, redundancy, performance, and network management.

📘 Network Topology and Devices

#### 1. Which type of topology describes the actual physical arrangement of cables and devices?

#### 2. Which type of topology describes how data flows between devices?

#### 3. Which topology connects all devices to a single backbone cable?

#### 4. Which cable is the main shared communication path in a bus topology?

#### 5. In a bus topology, what happens when a device transmits data?

#### 6. What is a major disadvantage of bus topology?

#### 7. Which topology connects each device to exactly two neighboring devices in a closed loop?

#### 8. Which mechanism is historically associated with Token Ring networks?

#### 9. What is a major advantage of token-based ring transmission?

#### 10. Which topology connects all devices to a central hub or switch?

#### 11. What is a major advantage of star topology?

#### 12. What is the major single point of failure in a traditional star topology?

#### 13. Which topology organizes devices in a hierarchical structure with branches?

#### 14. Which two topology concepts are commonly associated with tree topology?

#### 15. Which topology provides multiple communication paths between devices?

#### 16. In which type of mesh topology is every device directly connected to every other device?

#### 17. What is the main advantage of full mesh topology?

#### 18. What is the main disadvantage of full mesh topology?

#### 19. What is a partial mesh topology?

#### 20. What is hybrid topology?

#### 21. Which topology is most suitable when different parts of a network need different structural designs?

#### 22. Which topology is generally the most scalable among traditional topologies when designed hierarchically?

#### 23. Which networking device broadcasts an incoming signal to all connected ports?

#### 24. At which OSI layer does a traditional hub operate?

#### 25. Which networking device uses MAC addresses to forward Ethernet frames?

#### 26. Which OSI layer is primarily associated with a traditional Ethernet switch?

#### 27. Which device is essentially a multi-port bridge in modern Ethernet networks?

#### 28. Which device connects different IP networks and forwards packets using destination IP addresses?

#### 29. Which table does a router primarily use to select a path for a packet?

#### 30. Which OSI layer is primarily associated with a traditional router?

#### 31. Which device regenerates or retransmits a weakened signal to extend communication distance?

#### 32. At which OSI layer does a traditional repeater operate?

#### 33. Which device converts digital signals to analog and analog signals to digital?

#### 34. What is the main purpose of a Network Interface Card (NIC)?

#### 35. Which address is commonly associated with a network interface for local network identification?

#### 36. Which device allows wireless clients to connect to a wired LAN?

#### 37. Which technology is primarily provided by a wireless access point?

#### 38. Which device combines basic bridging and routing functions?

#### 39. Which OSI layers are associated with a brouter?

#### 40. Which device is designed to connect dissimilar networks and may translate between different protocols?

#### 41. Which networking device is primarily used to divide a LAN into smaller segments using MAC addresses?

#### 42. Which firewall type examines individual packets using parameters such as IP address, port, and protocol?

#### 43. Which firewall keeps track of the state of active network connections?

#### 44. Which firewall acts as an intermediary between an internal client and an external destination?

#### 45. Which firewall is specifically designed to protect web applications from attacks such as SQL injection and XSS?

#### 46. Which firewall type combines traditional firewall functions with application awareness and integrated intrusion prevention?

#### 47. What is the main difference between a traditional stateful firewall and an NGFW?

#### 48. Which feature is most closely associated with an NGFW rather than a basic packet-filtering firewall?

#### 49. Which firewall is mainly deployed to protect an individual computer or server?

#### 50. Which firewall is designed specifically to protect cloud-based resources?

#### 51. Which statement best distinguishes a WAF from an NGFW?

#### 52. Which firewall approach combines several security functions such as firewall, antivirus, and intrusion prevention in one platform?

#### 53. Which statement best describes a distributed firewall?
