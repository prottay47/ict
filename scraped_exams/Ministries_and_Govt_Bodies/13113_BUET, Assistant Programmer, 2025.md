# BUET, Assistant Programmer, 2025

- **Original URL:** [https://it.jobqns.com/buet-assistant-programmer-2025/](https://it.jobqns.com/buet-assistant-programmer-2025/)
- **Date:** 2026-03-01T17:17:10
- **Categories:** Job Solution 2025, Other IT Job Solution 2025

---

#### Bangladesh University of Engineering and Tecnology(BUET) Post: Assistant Programmer Exam Date: 21.6.2025



1.Write a C program to check whether a given string is a palindrome or not.
```
#include <stdio.h>
int main() {
char str[100];
int i, length;
int isPalindrome = 1;

printf("Enter a string: ");
fgets(str, sizeof(str), stdin);

str[strcspn(str, "\n")] = '\0';

length = strlen(str);

for(i = 0; i < length / 2; i++) {
if(str[i] != str[length - i - 1]) {
isPalindrome = 0;
break;
}
}

if(isPalindrome)
printf("The string is a palindrome.\n");
else
printf("The string is not a palindrome.\n");

return 0;
}
```

2. Consider a database scheme consisting of two tables: Students and Enrollment. Write the SQL queries to perform the following tasks:
(i) Display a list containing the names of all students, their enrolled courses, and their corresponding grades.
(ii) Retrieve only the names of the students who have achieved a grade of 'A'.

**Assumption:**

Students(StudentID, Name)

Enrollment(StudentID, CourseName, Grade)

**(i) Display names of all students, their enrolled courses, and corresponding grades:**

```
SELECT S.Name, E.CourseName, E.Grade
FROM Students S
JOIN Enrollment E
ON S.StudentID = E.StudentID;
```

**Explanation:**

- JOIN is used to combine Students and Enrollment tables.

- The common attribute is StudentID.

- The query displays student name, course name, and grade.

**(ii) Retrieve names of students who achieved grade ‘A’:**

```
SELECT DISTINCT S.Name
FROM Students S
JOIN Enrollment E
ON S.StudentID = E.StudentID
WHERE E.Grade = 'A';
```

**Explanation:**

- WHERE clause filters only Grade = ‘A’.

- DISTINCT ensures no duplicate names appear.

**ধরা যাক টেবিলের কাঠামো:**

Students(StudentID, Name)

Enrollment(StudentID, CourseName, Grade)

**(i) সকল শিক্ষার্থীর নাম, তাদের course এবং grade প্রদর্শন:**

```
SELECT S.Name, E.CourseName, E.Grade
FROM Students S
JOIN Enrollment E
ON S.StudentID = E.StudentID;
```

**ব্যাখ্যা:**

- JOIN ব্যবহার করে দুটি table যুক্ত করা হয়েছে।

- StudentID common field হিসেবে ব্যবহৃত হয়েছে।

- ফলাফলে নাম, course ও grade দেখানো হবে।

**(ii) যেসব শিক্ষার্থী ‘A’ grade পেয়েছে তাদের নাম প্রদর্শন:**

```
SELECT DISTINCT S.Name
FROM Students S
JOIN Enrollment E
ON S.StudentID = E.StudentID
WHERE E.Grade = 'A';
```

**ব্যাখ্যা:**

- WHERE clause দ্বারা Grade = ‘A’ নির্ধারণ করা হয়েছে।

- DISTINCT ব্যবহার করে পুনরাবৃত্ত নাম বাদ দেওয়া হয়েছে।

3. What is Deadlock? Write the conditions for deadlock and explain deadlock. **What is Deadlock?**

**Deadlock কী?**

**Deadlock**  হলো এমন একটি অবস্থা যেখানে দুই বা ততোধিক process স্থায়ীভাবে আটকে যায়, কারণ প্রত্যেক process অন্য process-এর দখলে থাকা resource-এর জন্য অপেক্ষা করে। ফলে কোনো process-ই তার কাজ সম্পন্ন করতে পারে না।

**উদাহরণ:**

Process P1 Resource R1 ধরে রেখেছে এবং R2-এর জন্য অপেক্ষা করছে। অন্যদিকে Process P2 Resource R2 ধরে রেখেছে এবং R1-এর জন্য অপেক্ষা করছে। ফলে উভয় process আটকে যায়।

**Deadlock-এর শর্তসমূহ (Coffman’s Conditions):**

নিচের চারটি শর্ত একসাথে সত্য হলে Deadlock ঘটে:

- **Mutual Exclusion:**  কোনো resource এক সময়ে শুধুমাত্র একটি process ব্যবহার করতে পারে।
- **Hold and Wait:**  একটি process একটি resource ধরে রেখে অন্য resource-এর জন্য অপেক্ষা করে।
- **No Preemption:**  Resource জোরপূর্বক কেড়ে নেওয়া যায় না।
- **Circular Wait:**  একটি চক্র তৈরি হয় যেখানে প্রতিটি process পরবর্তী process-এর resource-এর জন্য অপেক্ষা করে।

4. Differentiate between SRAM and DRAM. Also write the differences between Cache Memory and Flash Memory. **Difference Between SRAM and DRAM**
- **Full Form:**  SRAM = Static Random Access Memory; DRAM = Dynamic Random Access Memory.
- **Storage Method:**  SRAM uses flip-flops to store data; DRAM uses capacitors.
- **Speed:**  SRAM is faster; DRAM is slower.
- **Refresh Requirement:**  SRAM does not require refreshing; DRAM needs periodic refresh.
- **Cost:**  SRAM is expensive; DRAM is cheaper.
- **Density:**  SRAM has lower storage density; DRAM has higher density.
- **Usage:**  SRAM is used in Cache Memory; DRAM is used as Main Memory (RAM).

**Difference Between Cache Memory and Flash Memory**

- **Type:**  Cache Memory is volatile memory; Flash Memory is non-volatile memory.
- **Purpose:**  Cache improves CPU speed; Flash is used for data storage.
- **Speed:**  Cache is very fast; Flash is slower than cache.
- **Location:**  Cache is located near or inside CPU; Flash is used in USB drives, SSDs, memory cards.
- **Data Retention:**  Cache loses data when power is off; Flash retains data without power.
- **Technology:**  Cache usually uses SRAM; Flash uses EEPROM-based technology.

**SRAM এবং DRAM-এর পার্থক্য**

- **পূর্ণরূপ:**  SRAM = Static Random Access Memory; DRAM = Dynamic Random Access Memory।
- **ডেটা সংরক্ষণ পদ্ধতি:**  SRAM flip-flop ব্যবহার করে; DRAM capacitor ব্যবহার করে।
- **গতি:**  SRAM দ্রুত; DRAM তুলনামূলক ধীর।
- **Refresh:**  SRAM-এ refresh দরকার হয় না; DRAM-এ নিয়মিত refresh করতে হয়।
- **খরচ:**  SRAM ব্যয়বহুল; DRAM সস্তা।
- **Density:**  SRAM কম storage ধারণ করে; DRAM বেশি ধারণ করে।
- **ব্যবহার:**  SRAM Cache Memory-তে ব্যবহৃত হয়; DRAM Main Memory হিসেবে ব্যবহৃত হয়।

**Cache Memory এবং Flash Memory-এর পার্থক্য**

- **ধরণ:**  Cache volatile memory; Flash non-volatile memory।
- **উদ্দেশ্য:**  Cache CPU-এর গতি বাড়ায়; Flash data সংরক্ষণে ব্যবহৃত হয়।
- **গতি:**  Cache খুব দ্রুত; Flash তুলনামূলক ধীর।
- **অবস্থান:**  Cache CPU-এর ভিতরে বা কাছাকাছি থাকে; Flash USB, SSD, memory card-এ ব্যবহৃত হয়।
- **ডেটা সংরক্ষণ:**  Cache power বন্ধ হলে ডেটা মুছে যায়; Flash power ছাড়াই ডেটা সংরক্ষণ করে।
- **প্রযুক্তি:**  Cache সাধারণত SRAM ব্যবহার করে; Flash EEPROM ভিত্তিক প্রযুক্তি ব্যবহার করে।

5. Difference between circuit switching and packet switching. **Difference Between Circuit Switching and Packet Switching**
- **Definition:**  Circuit Switching establishes a dedicated communication path between sender and receiver before data transfer. Packet Switching divides data into small packets and sends them independently over the network.
- **Connection Type:**  Circuit Switching requires a fixed, dedicated connection; Packet Switching uses dynamic routing without a dedicated path.
- **Resource Usage:**  Circuit Switching reserves bandwidth for the entire session; Packet Switching shares network resources among users.
- **Data Transmission:**  In Circuit Switching, data flows continuously after connection setup; In Packet Switching, data is transmitted in packets.
- **Delay:**  Circuit Switching has initial setup delay but low transmission delay; Packet Switching has variable delay due to routing and congestion.
- **Efficiency:**  Circuit Switching is less efficient for bursty data; Packet Switching is more efficient and flexible.
- **Example:**  Traditional telephone network uses Circuit Switching; Internet uses Packet Switching.

**Circuit Switching এবং Packet Switching-এর পার্থক্য**

- **সংজ্ঞা:**  Circuit Switching-এ data পাঠানোর আগে একটি নির্দিষ্ট communication path স্থাপন করা হয়। Packet Switching-এ data ছোট ছোট packet-এ ভাগ করে পাঠানো হয়।
- **সংযোগের ধরন:**  Circuit Switching-এ dedicated connection থাকে; Packet Switching-এ নির্দিষ্ট পথ থাকে না।
- **Resource ব্যবহার:**  Circuit Switching পুরো সময়ের জন্য bandwidth সংরক্ষণ করে; Packet Switching-এ একাধিক ব্যবহারকারী resource ভাগাভাগি করে।
- **Data প্রেরণ:**  Circuit Switching-এ ধারাবাহিকভাবে data প্রবাহিত হয়; Packet Switching-এ packet আকারে পাঠানো হয়।
- **বিলম্ব:**  Circuit Switching-এ শুরুতে setup delay থাকে; Packet Switching-এ congestion-এর কারণে delay পরিবর্তনশীল।
- **কার্যকারিতা:**  Circuit Switching কম কার্যকর; Packet Switching বেশি কার্যকর ও নমনীয়।
- **উদাহরণ:**  Telephone network Circuit Switching ব্যবহার করে; Internet Packet Switching ব্যবহার করে।

6. Identify which of the two is predominantly used in Internet communication and justify why. **Predominantly Used in Internet Communication**

**Packet Switching**  is predominantly used in Internet communication.

**Justification:**

- **Efficient Bandwidth Utilization:**  Internet traffic is bursty (data is not sent continuously). Packet switching allows multiple users to share the same network resources efficiently.
- **Dynamic Routing:**  Packets can take different paths to reach the destination, making the network more flexible and reliable.
- **Scalability:**  The Internet connects millions of devices worldwide, and packet switching easily supports large-scale communication.
- **Fault Tolerance:**  If one path fails, packets can be rerouted through another path.
- **Supports Data Services:**  Modern applications such as web browsing, email, streaming, and cloud services are well suited for packet-based transmission.

**Internet Communication-এ প্রধানত কোনটি ব্যবহৃত হয়**

**Packet Switching**  Internet communication-এ প্রধানত ব্যবহৃত হয়।

**কারণ:**

- **Bandwidth-এর দক্ষ ব্যবহার:**  Internet-এ data ধারাবাহিকভাবে প্রবাহিত হয় না। Packet Switching-এ একাধিক ব্যবহারকারী একই resource ভাগ করে ব্যবহার করতে পারে।
- **Dynamic Routing:**  Packet বিভিন্ন পথ ব্যবহার করে গন্তব্যে পৌঁছাতে পারে, ফলে network আরও নমনীয় ও নির্ভরযোগ্য হয়।
- **Scalability:**  লক্ষ লক্ষ device সংযুক্ত থাকলেও packet switching সহজে সমর্থন করতে পারে।
- **Fault Tolerance:**  কোনো পথ নষ্ট হলে অন্য পথ দিয়ে packet পাঠানো যায়।
- **Data Service উপযোগী:**  Web browsing, email, streaming ইত্যাদি packet ভিত্তিক transmission-এর জন্য উপযুক্ত।
