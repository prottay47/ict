# Jamuna Oil Company Limited, Junior Officer (MIS & IT), 2024ok

- **Original URL:** [https://it.jobqns.com/jamuna-oil-company-limited-junior-officer-mis-it-2024/](https://it.jobqns.com/jamuna-oil-company-limited-junior-officer-mis-it-2024/)
- **Date:** 2026-03-05T19:25:28
- **Categories:** Job Solution 2024

---

#### Jamuna Oil Company Limited
Post: Junior Officer (MIS & IT);  Date: 23 May, 2024 Exam Taker: JOCL



1. In a 3-input logic circuit (inputs A, B, and C), the output F is 1 if at least two of all three inputs are 1.     a) Construct the truth table.     b) Use the truth table to find the POS (Product of Sums) expression using K-map simplification.

**Given:**  F = 1 when at least two of the three inputs A, B, and C are 1.

**a) Truth table**

ABCF00000010010001111000101111011111

So, F = 1 for minterms:m(3, 5, 6, 7)

And F = 0 for maxterms:M(0, 1, 2, 4)

Simplification by K-map:

Simplified POS= (A+B)(A+C)(B+C)

2. Computer A has a 2 GHz processor and takes 250 picoseconds to execute a single instruction, while Computer B has a 2.5 GHz processor and takes 500 picoseconds per instruction. Which computer is faster?

**Given:** Computer A: Clock speed = 2 GHz, Time per instruction = 250 psComputer B: Clock speed = 2.5 GHz, Time per instruction = 500 ps

**Step 1: Convert picoseconds to seconds** 1 picosecond = 10-12 seconds

For Computer A:250 ps = 250 × 10-12 = 2.5 × 10-10 seconds

For Computer B:500 ps = 500 × 10-12 = 5 × 10-10 seconds

**Step 2: Calculate instructions per second** For Computer A:Instructions per second = 1 / (2.5 × 10-10) = 4 × 109

For Computer B:Instructions per second = 1 / (5 × 10-10) = 2 × 109

**Step 3: Compare** Computer A = 4 × 109 instructions/secondComputer B = 2 × 109 instructions/second

**Conclusion:** Computer A is faster because it executes about  **twice as many instructions per second**  as Computer B.

3. Which software development model is more suitable when a company has only a few months to complete a project: Agile or Waterfall? Justify your answer.

When a company has only a few months to complete a project, the  **Agile model**  is generally more suitable than the  **Waterfall model** .

Agile development focuses on  **iterative development**  and  **continuous delivery** . The project is divided into small parts called iterations or sprints, allowing developers to deliver working features quickly and improve them based on feedback.

In contrast, the Waterfall model follows a  **sequential process**  where each phase (requirements, design, development, testing) must be completed before moving to the next stage. This approach can take more time and is less flexible when quick changes are required.

Therefore,  **Agile is more suitable for short deadlines**  because it allows faster development, flexibility, and early delivery of functional software.

**Short Deadline Project-এর জন্য Agile না Waterfall?**

যখন কোনো কোম্পানির কাছে project সম্পন্ন করার জন্য অল্প সময় থাকে, তখন সাধারণত  **Agile model**  বেশি উপযুক্ত।

Agile model-এ project ছোট ছোট  **iteration বা sprint** -এ ভাগ করে কাজ করা হয়। এতে দ্রুত feature develop করা যায় এবং feedback অনুযায়ী দ্রুত পরিবর্তন করা সম্ভব।

অন্যদিকে  **Waterfall model**  একটি sequential পদ্ধতি যেখানে প্রতিটি ধাপ (requirement, design, development, testing) ধারাবাহিকভাবে শেষ করতে হয়। এতে সময় বেশি লাগে এবং পরিবর্তন করা কঠিন।

তাই অল্প সময়ে project সম্পন্ন করার ক্ষেত্রে  **Agile model বেশি কার্যকর**  কারণ এটি দ্রুত development, flexibility এবং early delivery নিশ্চিত করে।

4. Write a program that takes a single alphanumeric string as input. The string may contain both letters (a–z, A–Z) and digits (0–9). Your task is to calculate and print the sum of all numeric digit characters in the string.
```
#include <stdio.h>#include <ctype.h>

int main() {
char str[100];
int sum = 0;

printf("Enter an alphanumeric string: ");
scanf("%s", str);

for (int i = 0; str[i] != '\0'; i++) {
if (isdigit(str[i])) {
sum += str[i] - '0';   // convert char digit to integer
}
}

printf("Sum of digits = %d\n", sum);

return 0;
}
```

```
Sample Input:
Enter an alphanumeric string: a1b2c3d4

Sample Output:
Sum of digits = 10
```

5. What are the data units of the Physical layer, Data Link layer, Network layer, and Transport layer?

**Data Units of Different OSI Layers**

In computer networking, each layer of the  **OSI model**  uses a specific type of data unit called a  **Protocol Data Unit (PDU)** .

- **Physical Layer:**  The data unit of the Physical layer is  **Bits** . This layer transmits raw binary data (0 and 1) over the communication medium.
- **Data Link Layer:**  The data unit of the Data Link layer is  **Frame** . This layer organizes bits into frames and handles error detection and physical addressing.
- **Network Layer:**  The data unit of the Network layer is  **Packet** . This layer is responsible for logical addressing and routing of data across networks.
- **Transport Layer:**  The data unit of the Transport layer is  **Segment**  (in TCP) or  **Datagram**  (in UDP). This layer ensures reliable end-to-end communication.

**OSI Model-এর বিভিন্ন Layer-এর Data Unit**

Computer networking-এ  **OSI model** -এর প্রতিটি layer একটি নির্দিষ্ট ধরনের data unit ব্যবহার করে যাকে  **Protocol Data Unit (PDU)**  বলা হয়।

- **Physical Layer:**  Physical layer-এর data unit হলো  **Bits** । এই layer communication medium-এর মাধ্যমে raw binary data (0 এবং 1) transmit করে।
- **Data Link Layer:**  Data Link layer-এর data unit হলো  **Frame** । এই layer bits-কে frame আকারে সংগঠিত করে এবং error detection ও physical addressing পরিচালনা করে।
- **Network Layer:**  Network layer-এর data unit হলো  **Packet** । এই layer logical addressing এবং data routing-এর জন্য দায়ী।
- **Transport Layer:**  Transport layer-এর data unit হলো  **Segment**  (TCP-এর ক্ষেত্রে) অথবা  **Datagram**  (UDP-এর ক্ষেত্রে)। এই layer end-to-end communication নিশ্চিত করে।

6. Apply the Merge Sort algorithm using the divide and conquer approach to sort the following list of numbers: 5, 1, 6, 3, 7, 2, 8, and 4.


7. What are the four necessary conditions for a deadlock to occur?

For a  **deadlock**  to occur in a system, four conditions known as  **Coffman Conditions**  must be present simultaneously.

- **Mutual Exclusion:**  At least one resource must be held in a non-shareable mode. Only one process can use the resource at a time.
- **Hold and Wait:**  A process holding one resource is waiting to acquire additional resources held by other processes.
- **No Preemption:**  Resources cannot be forcibly taken away from a process; they must be released voluntarily.
- **Circular Wait:**  A circular chain of processes exists where each process is waiting for a resource held by the next process.

**Deadlock হওয়ার চারটি প্রয়োজনীয় শর্ত**

কোনো system-এ  **deadlock**  ঘটার জন্য চারটি শর্ত একসাথে থাকতে হয়। এই শর্তগুলোকে  **Coffman Conditions**  বলা হয়।

- **Mutual Exclusion:**  একটি resource এক সময়ে কেবল একটি process ব্যবহার করতে পারে।
- **Hold and Wait:**  একটি process একটি resource ধরে রেখে অন্য resource-এর জন্য অপেক্ষা করে।
- **No Preemption:**  কোনো process থেকে resource জোর করে নেওয়া যায় না; process নিজে release না করা পর্যন্ত resource তার কাছেই থাকে।
- **Circular Wait:**  একাধিক process এমনভাবে অপেক্ষা করে যেখানে প্রতিটি process অন্য process-এর resource-এর জন্য অপেক্ষা করে।

8. What are the five states of a process in an operating system?

**Five States of a Process in Operating System**

In an  **Operating System** , a process goes through several states during its execution. The five basic states of a process are:

- **New:**  The process is being created and initialized.
- **Ready:**  The process is prepared and waiting in the ready queue to be assigned to the CPU.
- **Running:**  The process is currently being executed by the CPU.
- **Waiting (Blocked):**  The process is waiting for an event such as input/output operation to complete.
- **Terminated:**  The process has finished execution and is removed from the system.

**Operating System-এ Process-এর পাঁচটি State**

Operating System-এ একটি  **process**  তার execution চলাকালে বিভিন্ন state-এর মধ্য দিয়ে যায়। প্রধান পাঁচটি state হলো:

- **New:**  Process নতুনভাবে তৈরি হচ্ছে।
- **Ready:**  Process CPU পাওয়ার জন্য ready queue-এ অপেক্ষা করছে।
- **Running:**  Process বর্তমানে CPU দ্বারা execute হচ্ছে।
- **Waiting (Blocked):**  Process কোনো event বা input/output operation সম্পন্ন হওয়ার জন্য অপেক্ষা করছে।
- **Terminated:**  Process-এর execution শেষ হয়েছে এবং system থেকে সরিয়ে ফেলা হয়েছে।

9. Draw diagrams of Bus, Star, and Mesh network topologies.

**Bus, Star, and Mesh Network Topologies**

- **Bus Topology:**  In a bus topology, all devices are connected to a single main cable called the  **bus** . Data travels through this central cable and all devices receive the signal, but only the intended device accepts it.
- **Star Topology:**  In a star topology, all devices are connected to a central device such as a  **hub or switch** . All communication between devices passes through this central node.
- **Mesh Topology:**  In a mesh topology, every device is connected to every other device in the network. This provides multiple paths for data transmission and increases reliability.

**Bus, Star এবং Mesh Network Topology**

- **Bus Topology:**  Bus topology-তে সব device একটি প্রধান cable বা  **bus** -এর সাথে সংযুক্ত থাকে। Data এই cable দিয়ে transmit হয় এবং সব device signal পায়, তবে নির্দিষ্ট device তা গ্রহণ করে।
- **Star Topology:**  Star topology-তে সব device একটি central device যেমন  **hub বা switch** -এর সাথে সংযুক্ত থাকে। সব communication এই central device-এর মাধ্যমে হয়।
- **Mesh Topology:**  Mesh topology-তে প্রতিটি device অন্য সব device-এর সাথে সংযুক্ত থাকে। এতে data transmission-এর জন্য একাধিক পথ থাকে এবং network-এর reliability বৃদ্ধি পায়।

10. Write the names of three linear and three non-linear data structures. Also, mention which type is more memory efficient — linear or non-linear?

**Linear Data Structures:** In linear data structures, elements are arranged sequentially and each element is connected to the next element in a single line.

Examples of linear data structures:

- Array
- Stack
- Queue

**Non-Linear Data Structures:** In non-linear data structures, elements are not arranged sequentially. Instead, elements are connected in hierarchical or network form.

Examples of non-linear data structures:

- Tree
- Graph
- Heap

**Memory Efficiency:** Generally,  **linear data structures**  are more memory efficient because they store data sequentially and require less memory overhead compared to non-linear data structures.

**Linear Data Structure:** Linear data structure-এ element গুলো ধারাবাহিকভাবে একটি লাইনে সাজানো থাকে এবং প্রতিটি element পরবর্তী element-এর সাথে সংযুক্ত থাকে।

Linear data structure-এর উদাহরণ:

- Array
- Stack
- Queue

**Non-Linear Data Structure:** Non-linear data structure-এ element গুলো ধারাবাহিকভাবে সাজানো থাকে না। বরং element গুলো hierarchical বা network আকারে সংযুক্ত থাকে।

Non-linear data structure-এর উদাহরণ:

- Tree
- Graph
- Heap

**Memory Efficiency:** সাধারণত  **linear data structure**  বেশি memory efficient কারণ এতে data sequentialভাবে সংরক্ষণ করা হয় এবং অতিরিক্ত memory overhead কম থাকে।

11. Write the following queries
(a) Write an SQL query to show the top 10 highest marks from the Result table.
(b) Write an SQL query to show the number of male and female students who passed, individually.
(c) Write an SQL query to show the absent students in the Result table.
```
-- (a) Show the top 10 highest marks from the Result table
SELECT *
FROM Result
ORDER BY Marks DESC
LIMIT 10;

-- (b) Show the number of male and female students who passed individually
SELECT Gender, COUNT(*) AS TotalPassed
FROM Result
WHERE Status = 'Pass'
GROUP BY Gender;

-- (c) Show the absent students in the Result table
SELECT *
FROM Result
WHERE Status = 'Absent';
```



General Partসাধারণ জ্ঞান:
