# National Skills Development Authority, Assistant Programmer, 2024ok

- **Original URL:** [https://it.jobqns.com/national-skills-development-authority-assistant-programmer-2024/](https://it.jobqns.com/national-skills-development-authority-assistant-programmer-2024/)
- **Date:** 2026-03-04T21:08:21
- **Categories:** Job Solution 2024, Other IT Job Solution 2024

---

#### National Skill Development Authority
Post: Assistant Programmer;  Date: 10 March, 2024Exam taker: NSDA; Total: 100; GK: 60; T:40



1. You are given the IP address 192.168.10.100/26. Answer the following questions:
a) What is the subnet address?
b) What is the first valid host address?
c) What is the last valid host address?
d) What is the broadcast address?
e) What is the subnet mask?

**Given:** IP address = 192.168.10.100/26

**a) Subnet address:** /26 means subnet mask = 255.255.255.192Block size = 64Subnets are: 0, 64, 128, 192100 falls in 64–127So, subnet address =  **192.168.10.64**

**b) First valid host address:** 192.168.10.65

**c) Last valid host address:** 192.168.10.126

**d) Broadcast address:** 192.168.10.127

**e) Subnet mask:** 255.255.255.192

2. Mention the public and private address ranges of IPv4 for class A, class B and class C.

**IPv4 Public and Private Address Ranges:**

**Class A:** Public range:  **1.0.0.0 – 126.255.255.255** Private range:  **10.0.0.0 – 10.255.255.255**

**Class B:** Public range:  **128.0.0.0 – 191.255.255.255** Private range:  **172.16.0.0 – 172.31.255.255**

**Class C:** Public range:  **192.0.0.0 – 223.255.255.255** Private range:  **192.168.0.0 – 192.168.255.255**

3. Write a C/C++/Java program to print the prime numbers from 1 to n.
```
#include <stdio.h>

int main() {
int n, i, j, isPrime;

printf("Enter the value of n: ");
scanf("%d", &n);

printf("Prime numbers from 1 to %d are:\n", n);

for (i = 2; i <= n; i++) {
isPrime = 1;

for (j = 2; j <= i / 2; j++) {
if (i % j == 0) {
isPrime = 0;
break;
}
}

if (isPrime == 1) {
printf("%d ", i);
}
}

return 0;
}
```

4(a) Explain Three-Way Handshaking in TCP Protocol.

**3-Way Handshake Protocol in TCP Connection Establishment** The  **3-way handshake**  is a mechanism used by TCP to establish a reliable connection between a client and a server.

**Step 1: SYN (Synchronization)**

- **Client → Server:**  The client initiates the connection by sending a SYN packet to the server.
- The SYN packet contains a randomly generated sequence number.

**Step 2: SYN-ACK (Synchronization and Acknowledgment)**

- **Server → Client:**  The server responds with a SYN-ACK packet.
- The packet contains: **ACK**  flag to acknowledge the client’s SYN. **SYN**  flag with the server’s own sequence number.
- The server also advertises its window size and maximum segment size.

**Step 3: ACK (Acknowledgment)**

- **Client → Server:**  The client sends an ACK packet confirming receipt of the SYN-ACK.
- After this step, the TCP connection is established and data transmission begins.

**TCP Connection Establishment-এ 3-Way Handshake Protocol**

**3-way handshake**  হলো TCP-তে ব্যবহৃত একটি process যা client এবং server-এর মধ্যে একটি reliable connection স্থাপন করে।

**Step 1: SYN (Synchronization)**

- **Client → Server:**  Client server-এর কাছে একটি SYN packet পাঠিয়ে connection শুরু করে।
- এই SYN packet-এ একটি randomly generated sequence number থাকে।

**Step 2: SYN-ACK (Synchronization and Acknowledgment)**

- **Server → Client:**  Server, client-এর SYN পাওয়ার পর একটি SYN-ACK packet পাঠায়।
- এই packet-এ থাকে: **ACK**  flag, যা client-এর SYN acknowledge করে। **SYN**  flag, যা server-এর sequence number নির্দেশ করে।
- Server তার window size এবং maximum segment size-ও পাঠায়।

**Step 3: ACK (Acknowledgment)**

- **Client → Server:**  Client, server-এর SYN-ACK পাওয়ার পর একটি ACK packet পাঠায়।
- এই ধাপের পর TCP connection সম্পূর্ণভাবে establish হয় এবং data transmission শুরু হয়।

4(b) Draw the TCP/IP and OSI reference model diagram.

5. Write the full form of the protocols: NAT, DHCP, MAC, TCP-IP, HTTPS.

**Full Forms:**

• NAT =  **Network Address Translation** • DHCP =  **Dynamic Host Configuration Protocol** • MAC =  **Media Access Control** • TCP/IP =  **Transmission Control Protocol / Internet Protocol** • HTTPS =  **HyperText Transfer Protocol Secure**
