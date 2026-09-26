# IDRA, Assistant Network Administrator, 2022ok

- **Original URL:** [https://it.jobqns.com/idra-assistant-network-administrator-2022/](https://it.jobqns.com/idra-assistant-network-administrator-2022/)
- **Date:** 2026-02-05T22:57:50
- **Categories:** Bank IT Job Solution, Bank IT Job Solution 2022, Job Solution 2022

---

#### Insurance Development and Regulatory AuthorityPost: Assistant Network Administrator (ANA) Exam Date:2022



1. Write Full form: DHCP, POP3, VSAT, and LCD

**DHCP:**  Dynamic Host Configuration Protocol **POP3:**  Post Office Protocol Version 3 **VSAT:**  Very Small Aperture Terminal **LCD:**  Liquid Crystal Display

2. What are Public and Private IP?

**Public IP Address**

A  **Public IP address**  is an IP address that is accessible over the Internet. It is assigned by an Internet Service Provider (ISP) and uniquely identifies a device or network on the global Internet.

- Used for communication over the Internet.
- Must be unique worldwide.
- Example: 8.8.8.8

**Private IP Address**

A  **Private IP address**  is used within a local network (LAN) and cannot be accessed directly from the Internet. These addresses are reused across different private networks.

- Used inside homes, offices, and organizations.
- Not unique globally.
- Example ranges: 192.168.x.x, 10.x.x.x, 172.16.x.x – 172.31.x.x

**Public IP Address**

**Public IP address**  হলো এমন একটি IP address যা Internet-এর মাধ্যমে সরাসরি accessible। এটি ISP দ্বারা প্রদান করা হয় এবং Internet-এ device বা network-কে uniquely identify করে।

- Internet communication-এর জন্য ব্যবহৃত হয়।
- বিশ্বব্যাপী unique হতে হয়।
- উদাহরণ: 8.8.8.8

**Private IP Address**

**Private IP address**  local network (LAN)-এর মধ্যে ব্যবহৃত হয় এবং সরাসরি Internet থেকে access করা যায় না। একই Private IP বিভিন্ন network-এ পুনরায় ব্যবহার করা যায়।

- Home, office এবং organization-এর ভিতরে ব্যবহৃত হয়।
- Globalভাবে unique নয়।
- উদাহরণ range: 192.168.x.x, 10.x.x.x, 172.16.x.x – 172.31.x.x

3. An IP address is: 172.162.100.25/27. Now find the following:
(i)Network Address?
(ii) IP Class
(iii)Subnet mask
(iv)Broadcast Address
(v) Hosts per Subnet

**Answers:**

**Network Address:**  172.162.100.0/27 **IP Class:**  Class B **Subnet Mask:**  255.255.255.224 **Broadcast Address:**  172.162.100.31 **Hosts per Subnet:**  30

Explanation

**(i) Network Address:** Network address হলো subnet-এর প্রথম address, যেখানে সব host bit 0 করা হয়। /27 হলে host bit থাকে 5টি, তাই block size = 25 = 32।

- **Calculation:**  25-এর সমান বা ছোট nearest multiple of 32 হলো 0। তাই network address = 172.162.100.0/27।

**(ii) IP Class:** First octet 172 হওয়ায় এটি 128–191 range-এর মধ্যে পড়ে, তাই এটি  **Class B** । Default mask 255.255.0.0 হলেও এখানে /27 ব্যবহার করা হয়েছে।

**(iii) Subnet Mask:** /27 মানে network অংশে 27 bit। Binary mask 11111111.11111111.11111111.11100000, যা decimal-এ  **255.255.255.224** ।

**(iv) Broadcast Address:** Broadcast address হলো subnet-এর শেষ address, যেখানে সব host bit 1 করা হয়। এই subnet-এর range 172.162.100.0–172.162.100.31, তাই broadcast address  **172.162.100.31** ।

**(v) Hosts per Subnet:** Total address = 25 = 32। Valid host = 32 − 2 =  **30**  (network ও broadcast বাদ দিয়ে)

4. How dose a Network works?

**How a Network Works**

A  **computer network**  works by connecting multiple devices (such as computers, servers, and smartphones) so they can communicate and share data and resources.

**Working Process:**

- Devices are connected using wired or wireless communication media.
- Each device is assigned a unique address (IP address) for identification.
- When a device sends data, the data is broken into small units called packets.
- Packets travel through network devices such as switches and routers.
- The destination device receives the packets and reassembles them into the original data.
- Network protocols (like TCP/IP) ensure correct delivery and error control.

**Conclusion:**  A network enables efficient communication, data sharing, and resource utilization among connected devices.

**Network কীভাবে কাজ করে**

**Computer network**  একাধিক device (যেমন computer, server, smartphone) সংযুক্ত করে যাতে তারা data ও resource আদান-প্রদান করতে পারে।

**Working Process:**

- Device-গুলো wired বা wireless media ব্যবহার করে সংযুক্ত থাকে।
- প্রতিটি device-এর একটি unique IP address থাকে।
- Data পাঠানোর সময় তা ছোট ছোট packet-এ ভাগ করা হয়।
- Packet গুলো switch ও router-এর মাধ্যমে গন্তব্যে পৌঁছায়।
- Receiver device packet গুলো একত্র করে আসল data তৈরি করে।
- TCP/IP-এর মতো network protocol data delivery ও error control নিশ্চিত করে।

**উপসংহার:**  Network connected device-এর মধ্যে দ্রুত ও কার্যকর communication নিশ্চিত করে।

5. What is Network Address Translation? Explain briefly.

**Network Address Translation (NAT)**

**NAT (Network Address Translation)**  is a technique used to map multiple private IP addresses within a local network to a single public IP address. It allows internal devices to access the Internet while conserving public IP addresses and improving security.

**How NAT Works:**

- **Translation Process:**  NAT uses a gateway device such as a router or firewall to translate private IP addresses into a public IP address. This gateway acts as an intermediary between internal and external networks.
- **Address Representation:** Private IP addresses (e.g., 10.0.0.1, 192.168.0.1) are used inside local networks and are not routable on the Internet.NAT assigns one or a few public IP addresses to represent all internal devices.
- **Data Flow:** Outgoing traffic: NAT replaces the private IP with a public IP before sending data to the Internet.Incoming traffic: NAT maps the public IP back to the correct private IP so the data reaches the intended device.
- **Security:**  NAT hides private IP addresses from external networks, reducing direct exposure of internal devices.

**Network Address Translation (NAT)**

**NAT (Network Address Translation)**  হলো একটি technique যেখানে local network-এর একাধিক private IP address-কে একটি public IP address-এর সাথে map করা হয়। এর মাধ্যমে internal device Internet access করতে পারে এবং public IP address সাশ্রয় ও security নিশ্চিত হয়।

**NAT কীভাবে কাজ করে:**

- **Translation Process:**  NAT একটি gateway device (router বা firewall) ব্যবহার করে private IP address-কে public IP address-এ translate করে। এই gateway internal ও external network-এর মধ্যে মধ্যস্থতাকারী হিসেবে কাজ করে।
- **Address Representation:** Private IP address (যেমন 10.0.0.1, 192.168.0.1) local network-এর ভিতরে ব্যবহৃত হয় এবং Internet-এ routable নয়।NAT একটি বা কয়েকটি public IP address ব্যবহার করে সব internal device-কে represent করে।
- **Data Flow:** Outgoing traffic-এর সময় NAT private IP-এর জায়গায় public IP বসিয়ে Internet-এ data পাঠায়।Incoming traffic-এর ক্ষেত্রে NAT public IP থেকে সঠিক private IP-তে data পৌঁছে দেয়।
- **Security:**  NAT internal device-এর private IP address গোপন রাখে, ফলে external network থেকে সরাসরি access কঠিন হয়।

6. What is SDN?

**Software Defined Networking (SDN)**

**SDN (Software Defined Networking)**  is a modern networking approach where the network control plane is separated from the data plane. This allows network administrators to manage and control the network using software instead of manually configuring hardware devices.

**Key Features of SDN:**

- Centralized network control using a software-based controller.
- Improved network flexibility and scalability.
- Easier network management and automation.
- Faster configuration and reduced operational cost.

**Software Defined Networking (SDN)**

**SDN (Software Defined Networking)**  হলো একটি আধুনিক networking ধারণা যেখানে network-এর control plane এবং data plane আলাদা করা হয়। এর ফলে software ব্যবহার করে network সহজে manage ও control করা যায়।

**SDN-এর প্রধান বৈশিষ্ট্য:**

- Software-based controller-এর মাধ্যমে centralized network control।
- Network-এর flexibility এবং scalability বৃদ্ধি পায়।
- Network management এবং automation সহজ হয়।
- Configuration দ্রুত হয় এবং operational cost কমে যায়।
