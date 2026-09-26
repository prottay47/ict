# Combined 3 Bank, AE (IT), 2021

- **Original URL:** [https://it.jobqns.com/combined-3-bank-ae-it-2021/](https://it.jobqns.com/combined-3-bank-ae-it-2021/)
- **Date:** 2026-03-09T00:48:29
- **Categories:** Bank IT Job Solution 2021, Job Solution 2021

---

AME/ANE/AE • Year 2021

Comined Bank

💼Post Name: AE(IT)/ AHME/ SO

🏛Exam Taker: ANZA

📅Exam Date: 24-Dec-2021

- ☆

1

Computer Network
Subnetting

A Classless IP Address is: 105.38.89.230/20. Find out the answer of the following question.(i) What is Net id and Host id?(ii) What is network address and broadcast address?(ii) What is network size?(iv) If this classless IP address is used to classfull IP address what will be the class?

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

- ☆

2

Operating System
Process Scheduling Algorithm

Operating System Round Robin: (Quantum number =3), 4 job (job1, job2, job3, job4), Arrival time: 0,2,8,5; Burst time: 9, 7, 2, 3. What is the average waiting time?



**Gantt Chart:**

Average Time: 25/4 = 6.25

- ☆

3

Miscellaneous

Difference between impact and nonimpact printer with example.

**Examples**
**Impact:**  Dot matrix printer, Daisy wheel printer,
**Non Impact:**  Inkjet printer, Laser printer

**Examples**
**Impact:**  Dot matrix printer, Daisy wheel printer,
**Non Impact:**  Inkjet printer, Laser printer


☆

4

Microprocessor & Computer Architecture

Hits ratio 75%, RAM time 10 ns , SSD time 10 ms for each instruction. Calcualte access time.

**Given:**

Hit Ratio = 75% = 0.75
RAM Access Time = 10 ns = 10 × 10-9 seconds
SSD Access Time = 10 ms = 10 × 10-3 seconds

**We Know**
Average Access Time = (Hit Ratio × RAM Time) + (Miss Ratio × SSD Time)
Miss Ratio = 1 - Hit Ratio = 1 - 0.75 = 0.25
**Calculation:**
Average Access Time = (0.75 × 10 × 10-9) + (0.25 × 10 × 10-3)
= 7.5 × 10-9 + 2.5 × 10-3
= 0.0000000075 + 0.0025 = 0.0025000075 seconds
=0.0025000075 × 1000 = 2.5000075 ms
**Average Access Time ≈ 2.5 milliseconds**

**Given:**

Hit Ratio = 75% = 0.75
RAM Access Time = 10 ns = 10 × 10-9 seconds
SSD Access Time = 10 ms = 10 × 10-3 seconds

**We Know**
Average Access Time = (Hit Ratio × RAM Time) + (Miss Ratio × SSD Time)
Miss Ratio = 1 - Hit Ratio = 1 - 0.75 = 0.25
**Calculation:**
Average Access Time = (0.75 × 10 × 10-9) + (0.25 × 10 × 10-3)
= 7.5 × 10-9 + 2.5 × 10-3
= 0.0000000075 + 0.0025 = 0.0025000075 seconds
=0.0025000075 × 1000 = 2.5000075 ms
**Average Access Time ≈ 2.5 milliseconds**

- ☆

5

Object Oriented Programming
Basic

What is the difference between object oriented programming and procedural object programming.

☆

6

Object Oriented Programming
Basic

Explain Method Overloading and Method Overriding.

**Method Overloading and Method Overriding**
**Method Overloading**

**Method Overloading**  is an Object-Oriented Programming (OOP) feature that allows a class to have multiple methods with the same name but different parameter lists. The methods must differ in the number, type, or order of parameters. This enables the same method name to perform different tasks based on the arguments passed to it. Method Overloading is an example of  **Compile-time Polymorphism (Static Polymorphism)** .

**Characteristics of Method Overloading**

• Methods have the same name.
• Methods must have different parameter lists (number, type, or order of parameters).
• Return type alone cannot distinguish overloaded methods.
• It occurs within the same class.
• It is resolved during compile time.

**Example**

Suppose a class has a method named  **add()** .
add(int a, int b) → Adds two integers.
add(int a, int b, int c) → Adds three integers.
add(double a, double b) → Adds two decimal numbers.

Although all methods have the same name  **add()** , they perform different operations depending on the parameters supplied.

**Method Overriding**

**Method Overriding**  is an Object-Oriented Programming (OOP) feature in which a subclass provides its own implementation of a method that is already defined in its superclass. The overriding method must have the same name, same parameter list, and compatible return type as the parent method. Method Overriding is an example of  **Run-time Polymorphism (Dynamic Polymorphism)** .

**Characteristics of Method Overriding**

• Occurs between a superclass and a subclass.
• The method name, parameters, and return type remain the same.
• The child class provides a new implementation of the inherited method.
• It is resolved during runtime using dynamic method dispatch.

**Example**

Suppose a parent class  **Animal**  contains a method named  **sound()**  that prints "Animal makes a sound".
A child class  **Dog**  overrides the  **sound()**  method to print "Dog barks".
When the  **sound()**  method is called using a Dog object, the overridden method in the Dog class is executed.

**Difference Between Method Overloading and Method Overriding**

Feature
Method Overloading
Method Overriding

Definition
Same method name with different parameters.
Child class redefines a parent class method.

Inheritance
Not required.
Required.

Parameters
Must be different.
Must be the same.

Return Type
Can be different, but not only difference.
Must be the same or compatible.

Polymorphism
Compile-time (Static).
Run-time (Dynamic).

Binding
Early Binding.
Late Binding.



**Method Overloading এবং Method Overriding**
**Method Overloading**

**Method Overloading**  হলো  **Object-Oriented Programming (OOP)** -এর একটি বৈশিষ্ট্য, যেখানে একই  **Class** -এর মধ্যে একই নামের একাধিক  **Method**  তৈরি করা যায়, তবে প্রতিটি Method-এর  **Parameter List**  ভিন্ন হতে হবে। Parameter-এর সংখ্যা, ধরন (Type) অথবা ক্রম (Order) ভিন্ন হতে পারে। এর ফলে একই Method Name বিভিন্ন ধরনের Input অনুযায়ী ভিন্ন কাজ করতে পারে।  **Method Overloading**  হলো  **Compile-time Polymorphism (Static Polymorphism)** -এর উদাহরণ।

**Method Overloading-এর বৈশিষ্ট্য**

• একই Class-এর মধ্যে ঘটে।
• সকল Method-এর নাম একই থাকে।
• Parameter-এর সংখ্যা, Type অথবা Order অবশ্যই ভিন্ন হতে হবে।
• শুধুমাত্র Return Type পরিবর্তন করলে Overloading হয় না।
• এটি Compile Time-এ নির্ধারিত হয়।

**উদাহরণ**

ধরা যাক একটি Class-এ  **add()**  নামে একাধিক Method রয়েছে।
add(int a, int b) → দুটি Integer যোগ করে।
add(int a, int b, int c) → তিনটি Integer যোগ করে।
add(double a, double b) → দুটি Decimal Number যোগ করে।

এখানে সব Method-এর নাম  **add()**  হলেও Parameter ভিন্ন হওয়ার কারণে এগুলো  **Method Overloading** -এর উদাহরণ।

**Method Overriding**

**Method Overriding**  হলো  **Object-Oriented Programming (OOP)** -এর একটি বৈশিষ্ট্য, যেখানে একটি  **Subclass**  তার  **Superclass** -এ বিদ্যমান একটি Method-কে একই নাম, একই Parameter List এবং Compatible Return Type রেখে নতুনভাবে বাস্তবায়ন (Implementation) করে। অর্থাৎ Child Class Parent Class-এর Method-এর নিজস্ব সংস্করণ প্রদান করে।  **Method Overriding**  হলো  **Run-time Polymorphism (Dynamic Polymorphism)** -এর উদাহরণ।

**Method Overriding-এর বৈশিষ্ট্য**

• Superclass এবং Subclass-এর মধ্যে ঘটে।
• Method-এর নাম, Parameter এবং Return Type একই বা Compatible থাকে।
• Child Class Parent Class-এর Method-এর নতুন Implementation প্রদান করে।
• এটি Runtime-এ Dynamic Method Dispatch-এর মাধ্যমে নির্ধারিত হয়।

**উদাহরণ**

ধরা যাক  **Animal**  নামে একটি Parent Class-এ  **sound()**  নামে একটি Method রয়েছে, যা "Animal makes a sound" প্রদর্শন করে।
**Dog**  নামে একটি Child Class একই  **sound()**  Method Override করে "Dog barks" প্রদর্শন করে।
যখন Dog Object দিয়ে  **sound()**  Method Call করা হয়, তখন Child Class-এর Override করা Method-টি Execute হয়।

**Method Overloading এবং Method Overriding-এর পার্থক্য**

বিষয়
Method Overloading
Method Overriding

সংজ্ঞা
একই নামের Method, কিন্তু Parameter ভিন্ন।
Child Class Parent Class-এর Method পুনরায় বাস্তবায়ন করে।

Inheritance
প্রয়োজন হয় না।
অবশ্যই প্রয়োজন।

Parameter
ভিন্ন হতে হবে।
একই হতে হবে।

Return Type
শুধু Return Type পরিবর্তন যথেষ্ট নয়।
একই বা Compatible হতে হবে।

Polymorphism
Compile-time (Static).
Run-time (Dynamic).

Binding
Early Binding.
Late Binding.

- ☆

7

Computer Network
NAT Concept

What is NAT? Why we used it and how NAT translate?

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

- ☆

8

Operating System
Memory Management

What is Swapping from virtual memory in the primary memory.

**Swapping in Operating System**
**Swapping**  is a memory management technique used by an operating system to efficiently manage the limited  **primary memory (RAM)**  and the larger but slower  **secondary memory**  such as a hard disk or SSD.
**What is Swapping?**
Swapping is the process of moving entire processes between  **primary memory (RAM)**  and  **secondary memory** . When the RAM becomes full and the system needs memory to run active programs, the operating system moves some inactive or low-priority processes from RAM to secondary memory. This process is called  **swapping out** .
Later, when the swapped-out process is required again, the operating system brings the process back into RAM from secondary memory. This process is called  **swapping in** .
Through this back-and-forth movement of processes between RAM and secondary memory, the operating system can run more processes than the physical memory can normally support.

**Operating System-এ Swapping**
**Swapping**  হলো একটি memory management technique যা operating system ব্যবহার করে সীমিত  **primary memory (RAM)**  এবং তুলনামূলক বড় কিন্তু ধীর  **secondary memory**  (hard disk বা SSD) দক্ষভাবে পরিচালনা করতে।
**Swapping কী?**
Swapping হলো এমন একটি প্রক্রিয়া যেখানে সম্পূর্ণ process-কে  **primary memory (RAM)**  এবং  **secondary memory** -এর মধ্যে স্থানান্তর করা হয়। যখন RAM পূর্ণ হয়ে যায় এবং নতুন program চালানোর জন্য memory প্রয়োজন হয়, তখন operating system কিছু inactive বা কম গুরুত্বপূর্ণ process-কে RAM থেকে secondary memory-তে সরিয়ে দেয়। এই প্রক্রিয়াকে  **swapping out**  বলা হয়।
পরে যখন সেই process আবার প্রয়োজন হয়, তখন operating system সেটিকে secondary memory থেকে আবার RAM-এ নিয়ে আসে। এই প্রক্রিয়াকে  **swapping in**  বলা হয়।
এইভাবে RAM এবং secondary memory-এর মধ্যে process আদান-প্রদানের মাধ্যমে operating system একসাথে অনেকগুলো process পরিচালনা করতে পারে।

- ☆

9

Computer Security
CIA

Explain Confidentiality and integrity. Can you have integrity without confidentiality? Justify your answer.

**Confidentiality:**
Confidentiality means keeping information  **secret**  and accessible only to authorized users. It ensures that sensitive data is not viewed or accessed by unauthorized people.
**Example:**  Encrypting emails so that only the intended receiver can read the message.
**Integrity:**
Integrity means that the information is  **accurate, complete, and unchanged** . It ensures that data is not modified or tampered with during storage or transmission.
**Example:**  Using checksums or digital signatures to verify that a file has not been altered.
**Relationship Between Confidentiality and Integrity**

**Integrity without Confidentiality:**  It is possible to have integrity without confidentiality. For example, a public website may allow everyone to view the data (no confidentiality), but it uses checksums or digital signatures to ensure the data has not been altered.
**Confidentiality without Integrity:**  It is also possible to have confidentiality without integrity. For example, data may be encrypted so that only authorized users can read it, but if someone modifies the encrypted message without detection, the integrity of the data is compromised.

**Confidentiality:**
Confidentiality বলতে বোঝায় তথ্যকে  **গোপন রাখা**  এবং শুধুমাত্র অনুমোদিত ব্যবহারকারীদের জন্য প্রবেশযোগ্য করা। এটি নিশ্চিত করে যে sensitive data unauthorized user দ্বারা দেখা বা ব্যবহার করা যাবে না।
**Example:**  Email encryption করা যাতে শুধুমাত্র নির্দিষ্ট receiver সেই message পড়তে পারে।
**Integrity:**
Integrity বলতে বোঝায় তথ্যের  **সঠিকতা, সম্পূর্ণতা এবং অপরিবর্তিত থাকা** । এটি নিশ্চিত করে যে data storage বা transmission-এর সময় পরিবর্তিত বা বিকৃত হয়নি।
**Example:**  File পরিবর্তন হয়েছে কিনা যাচাই করার জন্য checksum বা digital signature ব্যবহার করা।
**Confidentiality এবং Integrity-এর সম্পর্ক**

**Integrity without Confidentiality:**  Integrity থাকতে পারে কিন্তু confidentiality নাও থাকতে পারে। যেমন একটি public website-এ data সবার জন্য উন্মুক্ত থাকে (confidentiality নেই), কিন্তু checksum বা digital signature ব্যবহার করে নিশ্চিত করা হয় যে data পরিবর্তিত হয়নি।
**Confidentiality without Integrity:**  Confidentiality থাকতে পারে কিন্তু integrity নাও থাকতে পারে। যেমন encrypted data শুধুমাত্র authorized user পড়তে পারে, কিন্তু যদি কেউ encrypted message পরিবর্তন করে ফেলে এবং তা ধরা না পড়ে, তাহলে integrity নষ্ট হয়।

- ☆

10

Digital Logic Design
Kmap

Make a boolean expression using Karnaugh map: ∑m = (3,5,7,9,11,13,14,15)

- ☆

11

Data Communication
TDM

How long does it take to send a file of 640,000 bits from host A to host B over a circuit-switched network?- All links are 1.536 Mbps  - Each link uses TDM with 24 slots/sec- 500msec to establish end to end circuit.

Each circuit has a transmission rate of (1.536 Mbps)/24 = 64kbps
It takes 640,000 bits/64 kbps = 10 seconds to transmit the file.
To this time, we have to add the time taken to establish the connection. That makes it 10.5 seconds.

Each circuit has a transmission rate of (1.536 Mbps)/24 = 64kbps
It takes 640,000 bits/64 kbps = 10 seconds to transmit the file.
To this time, we have to add the time taken to establish the connection. That makes it 10.5 seconds.

- ☆

12

Database Management System
ER Diagram

From an E-R , Draw the schema diagram also indicate primary key with mapping constraints.

**ER-Diagram:**

**Schema Diagram:**

**ER-Diagram:**

**Schema Diagram:**

- ☆

13

Design Analysis of Algorithm
Sorting Algorithm

Write Merge short function.

**Merge Sort Algorithm**
Merge Sort is a  **divide and conquer**  algorithm. It recursively splits an array into two halves, sorts each half, and then merges the sorted halves back together.
**Merge Sort Function**

```
void MergeSort(int A[], int p, int r) {
if (p < r) {
int q = (p + r) / 2;  // Find the middle index
MergeSort(A, p, q);    // Recursively sort the left half
MergeSort(A, q + 1, r); // Recursively sort the right half
merge(A, p, q, r);      // Merge the sorted halves
}
}
```

**Merge Function**

```
void merge(int A[], int p, int q, int r) {
int n1 = q - p + 1;
int n2 = r - q;
int L[n1], R[n2];

// Copy data into temporary arrays
for (int i = 0; i < n1; i++) L[i] = A[p + i];
for (int j = 0; j < n2; j++) R[j] = A[q + 1 + j];

int i = 0, j = 0, k = p;
// Merge the two subarrays
while (i < n1 && j < n2) {
if (L[i] <= R[j]) A[k++] = L[i++];
else A[k++] = R[j++];
}

// Copy remaining elements of L[]
while (i < n1) A[k++] = L[i++];
// Copy remaining elements of R[]
while (j < n2) A[k++] = R[j++];
}
```

**Merge Sort Algorithm**
Merge Sort is a  **divide and conquer**  algorithm. It recursively splits an array into two halves, sorts each half, and then merges the sorted halves back together.
**Merge Sort Function**

```
void MergeSort(int A[], int p, int r) {
if (p < r) {
int q = (p + r) / 2;  // Find the middle index
MergeSort(A, p, q);    // Recursively sort the left half
MergeSort(A, q + 1, r); // Recursively sort the right half
merge(A, p, q, r);      // Merge the sorted halves
}
}
```

**Merge Function**

```
void merge(int A[], int p, int q, int r) {
int n1 = q - p + 1;
int n2 = r - q;
int L[n1], R[n2];

// Copy data into temporary arrays
for (int i = 0; i < n1; i++) L[i] = A[p + i];
for (int j = 0; j < n2; j++) R[j] = A[q + 1 + j];

int i = 0, j = 0, k = p;
// Merge the two subarrays
while (i < n1 && j < n2) {
if (L[i] <= R[j]) A[k++] = L[i++];
else A[k++] = R[j++];
}

// Copy remaining elements of L[]
while (i < n1) A[k++] = L[i++];
// Copy remaining elements of R[]
while (j < n2) A[k++] = R[j++];
}
```

- ☆

14

Operating System
Paging

Consider a machine with 64 MB physical memory and a 32 bit virtual address space. If the page size is 4 KB, what is the approximate size of the page table.

Physical Address Space = 64MB = \(2^{26}\text{B}\)
Virtual Address = 32-bits, \(\therefore\) Virtual Address Space = \(2^{32}\text{B}\)
Page Size = 4KB = \(2^{12}\text{B}\)
Number of pages = \(\frac{2^{32}}{2^{12}} = 2^{20}\) pages.
Number of frames = \(\frac{2^{26}}{2^{12}} = 2^{14}\) frames.
\(\therefore\) Page Table Size = \(2^{20} \times 14\text{-bits} \approx 2^{20} \times 16\text{-bits} \approx 2^{20} \times 2\text{B} = 2\text{MB}\).

Physical Address Space = 64MB = \(2^{26}\text{B}\)
Virtual Address = 32-bits, \(\therefore\) Virtual Address Space = \(2^{32}\text{B}\)
Page Size = 4KB = \(2^{12}\text{B}\)
Number of pages = \(\frac{2^{32}}{2^{12}} = 2^{20}\) pages.
Number of frames = \(\frac{2^{26}}{2^{12}} = 2^{14}\) frames.
\(\therefore\) Page Table Size = \(2^{20} \times 14\text{-bits} \approx 2^{20} \times 16\text{-bits} \approx 2^{20} \times 2\text{B} = 2\text{MB}\).
