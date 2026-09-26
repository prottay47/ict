# BREB, Assistant Programmer, 2023ok

- **Original URL:** [https://it.jobqns.com/breb-assistant-programmer-2023/](https://it.jobqns.com/breb-assistant-programmer-2023/)
- **Date:** 2026-03-07T16:33:37
- **Categories:** Job Solution 2023, Power Sector IT Job Solution 2023

---

#### Bangladesh Rural Electrification Board(BREB)
Post: Assistant Programmer Exam Date: 18.02.2023.  Exam Taker: BREB



1. Write a program to reverse string without using library function
```
#include <stdio.h>

int main() {
char str[100], temp;
int i, len = 0;

printf("Enter a string: ");
gets(str);

// Find length manually
while (str[len] != '\0') {
len++;
}

// Reverse the string
for (i = 0; i < len / 2; i++) {
temp = str[i];
str[i] = str[len - i - 1];
str[len - i - 1] = temp;
}

printf("Reversed string: %s\n", str);

return 0;
}
```

2. Define design pattern. Write about singleton pattern.

A  **design pattern**  is a reusable solution to common problems in software design that helps improve code structure and maintainability.

- **Creational Patterns:**  Deal with object creation (e.g., Factory).

- **Structural Patterns:**  Focus on object composition and relationships.

- **Behavioral Patterns:**  Handle communication between objects.

- **J2EE Patterns:**  Used in enterprise-level applications, mainly for presentation layer.

**Singleton Pattern**

The  **Singleton pattern**  ensures that a class has only  **one instance**  and provides a global access point to it.

- **Types:**

**Early Initialization:**  Instance is created at program start.
**Lazy Initialization:**  Instance is created only when needed.

- **Advantages:**

Saves memory by using a single instance.
Reduces overhead of creating multiple objects.

- **Uses:**  Logging, caching, configuration management, and database connections.

**Design pattern**  হলো software design-এর সাধারণ সমস্যার একটি reusable সমাধান যা code-এর structure এবং maintainability উন্নত করে।

- **Creational Patterns:**  Object creation নিয়ে কাজ করে (যেমন Factory)।

- **Structural Patterns:**  Object-এর মধ্যে সম্পর্ক এবং composition নির্ধারণ করে।

- **Behavioral Patterns:**  Object-এর মধ্যে communication পরিচালনা করে।

- **J2EE Patterns:**  Enterprise application-এ, বিশেষ করে presentation layer-এ ব্যবহৃত হয়।

**Singleton Pattern**
**Singleton pattern**  নিশ্চিত করে যে একটি class-এর শুধুমাত্র  **একটি instance**  থাকবে এবং সেটির জন্য একটি global access point থাকবে

- **Types:**

**Early Initialization:**  Program শুরুতেই instance তৈরি হয়।
**Lazy Initialization:**  প্রয়োজন হলে instance তৈরি হয়।

- **Advantages:**

একটি instance ব্যবহার করার কারণে memory সাশ্রয় হয়।
একাধিক object তৈরি করার overhead কমায়।

- **Uses:**  Logging, caching, configuration এবং database connection-এর ক্ষেত্রে ব্যবহৃত হয়।

3. What is private IP range class A, B and C with maximum host of each class?

**Private IP Ranges and Maximum Hosts for Classes A, B, and C**

**Class A**  **IP Range:**  10.0.0.0 – 10.255.255.255 **Maximum Hosts:**  224 – 2 = 16,777,214 hosts per network

**Class B**  **IP Range:**  172.16.0.0 – 172.31.255.255 **Maximum Hosts:**  216 – 2 = 65,534 hosts per network

**Class C**  **IP Range:**  192.168.0.0 – 192.168.255.255 **Maximum Hosts:**  28 – 2 = 254 hosts per network



4. Write short note: Network, Protocol, link, gateway, Node

**Network:**  A network is a collection of interconnected devices such as computers, printers, and servers that communicate with each other to share data and resources. Networks can be classified based on size and coverage like  **LAN, WAN,**  and the internet.

**Protocol:**  A protocol is a set of rules and standards that govern how data is transmitted and received over a network. It defines data format, transmission methods, and error handling (e.g.,  **HTTP, TCP/IP** ).

**Link:**  A link is a communication path that connects two devices in a network.

- **Physical Link:**  Actual connection using cables or wireless signals (Ethernet, Wi-Fi, Bluetooth).
- **Logical Link:**  Virtual connection created through software (VPN, VLAN).

**Gateway:**  A gateway is a network device that connects different networks and enables communication between them. It can translate data formats and protocols, for example connecting a  **LAN**  to the  **internet** .

**Node:**  A node is any device connected to a network that can send, receive, or forward data. Examples include computers, routers, and switches. Each node has a unique identifier such as an  **IP address** .

**Network:**  Network হলো একাধিক interconnected device (computer, printer, server) এর সমষ্টি যা একে অপরের সাথে communication করে data এবং resource share করে। Network বিভিন্ন ধরনের হতে পারে যেমন  **LAN, WAN**  এবং internet।

**Protocol:**  Protocol হলো কিছু নিয়ম এবং standard যা নির্ধারণ করে network-এ data কীভাবে transmit এবং receive হবে। এটি data format, transmission method এবং error handling নির্ধারণ করে (যেমন  **HTTP, TCP/IP** )।

**Link:**  Link হলো দুইটি device-এর মধ্যে communication path।

- **Physical Link:**  বাস্তব connection যেমন cable বা wireless signal (Ethernet, Wi-Fi, Bluetooth)।
- **Logical Link:**  Software দ্বারা তৈরি virtual connection (VPN, VLAN)।

**Gateway:**  Gateway হলো একটি network device যা ভিন্ন network-কে সংযুক্ত করে এবং তাদের মধ্যে communication সম্ভব করে। এটি data format ও protocol convert করতেও সক্ষম, যেমন  **LAN**  থেকে  **internet** -এ সংযোগ।

**Node:**  Node হলো network-এ সংযুক্ত যেকোনো device যা data send, receive বা forward করতে পারে। যেমন computer, router, switch। প্রতিটি node-এর একটি unique address থাকে যেমন  **IP address** ।

5. Output problem:
#include <iostream>
using namespace std;
int main () {
int i=1,j=1,k=1;
cout << ++i || ++j && ++k;
cout << i << j << k;
return 0;
}

**Given code:**

i = 1, j = 1, k = 1

Expression: **++i || ++j && ++k**

**Step 1: Operator precedence** && has higher priority than ||

So expression becomes: **++i || (++j && ++k)**

**Step 2: Evaluate ++i** ++i → i = 2 (true)

Since left side of || is  **true** , right side is  **not evaluated**  (short-circuit).

So:j = 1, k = 1 (unchanged)

Result of expression =  **1**

**Step 3: Output**

First cout prints:  **1** Second cout prints: i j k = 2 1 1

**Final Output:**  **1**

**211**

6. Output problem: #include <stdio.h>
int main () {
float p=10.5;
int a=5*p +5.0;
printf ("%d", a);
return 0;
}

**Code Analysis:**

p = 10.5a = 5 * p + 5.0

= 5 × 10.5 + 5.0= 52.5 + 5.0= 57.5

Now, a is  **int** , so decimal part is truncated:a =  **57**

**Final Output:**  **57**



7. Write a composition E-commerce in Bangladesh.
