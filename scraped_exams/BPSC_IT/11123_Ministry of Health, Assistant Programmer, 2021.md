# Ministry of Health, Assistant Programmer, 2021

- **Original URL:** [https://it.jobqns.com/ministry-of-health-assistant-programmer-2021/](https://it.jobqns.com/ministry-of-health-assistant-programmer-2021/)
- **Date:** 2026-02-04T19:49:57
- **Categories:** BPSC IT Job Solution, BPSC IT Job Solution 2021, Job Solution 2021

---

#### Ministry of Health
Post: Assistant ProgrammerExam Date: 16/03/2021, Exam Taker: BPSC



1.Solve the recurrence relation: T(n) = 3T (n-1) + 2 subject to T(o) = 1.

**Given Recurrence Relation** T(n) = 3T(n − 1) + 2, with T(0) = 1

**Step-by-Step Solution** Expand the recurrence by substitution:

T(1) = 3T(0) + 2 = 3(1) + 2 = 5T(2) = 3T(1) + 2 = 3(5) + 2 = 17T(3) = 3T(2) + 2 = 3(17) + 2 = 53

Now expand generally:T(n) = 3T(n−1) + 2= 3[3T(n−2) + 2] + 2= 3²T(n−2) + 3·2 + 2= 3³T(n−3) + 3²·2 + 3·2 + 2

Continuing this process,T(n) = 3ⁿT(0) + 2(3ⁿ⁻¹ + 3ⁿ⁻² + … + 1)

Since T(0) = 1 and the sum is a geometric series:3ⁿ⁻¹ + 3ⁿ⁻² + … + 1 = (3ⁿ − 1) / (3 − 1) = (3ⁿ − 1) / 2

**Final Solution** T(n) = 3ⁿ + (3ⁿ − 1) = 2·3ⁿ − 1

2. Briefly describe unit testing, smoke testing and stress testing in the context of software engineering.

**Unit Testing** Unit testing focuses on testing  **individual components or functions**  of a software application. Each unit is tested separately to ensure it works as expected. It is usually performed by developers during the coding phase.

**Smoke Testing** Smoke testing is a  **preliminary testing**  technique used to verify whether the basic functionalities of the software are working correctly. It ensures that the build is stable enough for further testing.

**Stress Testing** Stress testing evaluates how a system behaves under  **extreme or heavy load conditions** . It checks the system’s stability, reliability, and error handling when resources are pushed beyond normal limits.

**Unit Testing** Unit testing হলো software এর  **ছোট ছোট অংশ বা function**  আলাদাভাবে পরীক্ষা করার পদ্ধতি। এটি সাধারণত developer দ্বারা coding পর্যায়ে করা হয় যাতে প্রতিটি অংশ সঠিকভাবে কাজ করে কিনা নিশ্চিত করা যায়।

**Smoke Testing** Smoke testing হলো একটি  **প্রাথমিক testing**  পদ্ধতি, যেখানে software এর মূল feature গুলো ঠিকভাবে কাজ করছে কিনা তা যাচাই করা হয়। এর মাধ্যমে বোঝা যায় build টি পরবর্তী testing এর জন্য উপযুক্ত কিনা।

**Stress Testing** Stress testing এ system কে  **অস্বাভাবিক বা অতিরিক্ত চাপের মধ্যে**  চালানো হয়। এতে system এর stability, performance এবং failure handling ক্ষমতা যাচাই করা হয়।

3. What do you mean by DHCP server? Explain the benefits of using a dedicated DHCP server. Briefly describe the main benefits of using IPv6 protocol.

**DHCP Server** A DHCP (Dynamic Host Configuration Protocol) server is a network server that  **automatically assigns IP addresses**  and other network configuration details (such as subnet mask, default gateway, and DNS server) to devices on a network. This eliminates the need for manual IP configuration.

**Benefits of Using a Dedicated DHCP Server** •  **Automatic IP Assignment:**  Reduces manual configuration errors.•  **Centralized Management:**  All IP address management is controlled from one place.•  **Efficient IP Utilization:**  Prevents IP address conflicts and wastage.•  **Scalability:**  Easily supports a large number of devices joining or leaving the network.•  **Time-Saving:**  Simplifies network administration.

**Main Benefits of Using IPv6** •  **Larger Address Space:**  Uses 128-bit addresses, providing a vast number of IP addresses.•  **No Need for NAT:**  Each device can have a unique public IP address.•  **Improved Security:**  Built-in support for IPsec.•  **Better Performance:**  Simplified header structure for faster routing.•  **Auto-Configuration:**  Devices can configure their own IP addresses automatically.

**DHCP Server কী?** DHCP (Dynamic Host Configuration Protocol) server হলো একটি network server যা  **স্বয়ংক্রিয়ভাবে device গুলোকে IP address**  এবং অন্যান্য network তথ্য (যেমন subnet mask, gateway, DNS) প্রদান করে। এতে manual IP সেট করার প্রয়োজন হয় না।

**Dedicated DHCP Server ব্যবহারের সুবিধা** •  **Automatic IP Assignment:**  Manual ভুল কমে যায়।•  **Centralized Management:**  এক জায়গা থেকে সব IP নিয়ন্ত্রণ করা যায়।•  **Efficient IP ব্যবহার:**  IP conflict ও অপচয় রোধ করে।•  **Scalability:**  অনেক device সহজে network এ যুক্ত করা যায়।•  **Time Saving:**  Network পরিচালনা সহজ হয়।

**IPv6 ব্যবহারের প্রধান সুবিধাসমূহ** •  **বৃহৎ Address Space:**  128-bit address ব্যবহার করে।•  **NAT প্রয়োজন হয় না:**  প্রতিটি device এর জন্য আলাদা IP থাকে।•  **উন্নত Security:**  Built-in IPsec সমর্থন।•  **ভালো Performance:**  Routing আরও দ্রুত হয়।•  **Auto Configuration:**  Device নিজে নিজেই IP configure করতে পারে।

4. Analyze and compare the quick-sort and Merge sort algorithms in terms of their time and space complexity.

**Comparison between Quick Sort and Merge Sort**  **Quick Sort** Quick Sort is a  **divide and conquer**  algorithm that selects a pivot element and partitions the array around the pivot.•  **Best Case Time Complexity:**  O(n log n)•  **Average Case Time Complexity:**  O(n log n)•  **Worst Case Time Complexity:**  O(n²) (when the pivot selection is poor, e.g., already sorted array)•  **Space Complexity:**  O(log n) (in-place sorting due to recursion stack)

**Merge Sort** Merge Sort is a  **divide and conquer**  algorithm that divides the array into halves, sorts them, and then merges them.•  **Best Case Time Complexity:**  O(n log n)•  **Average Case Time Complexity:**  O(n log n)•  **Worst Case Time Complexity:**  O(n log n)•  **Space Complexity:**  O(n) (requires extra memory for merging)

**Key Comparison** • Quick Sort is generally faster in practice but has a worst-case of O(n²).• Merge Sort guarantees O(n log n) time in all cases.• Quick Sort uses less memory than Merge Sort.• Merge Sort is more suitable for large datasets and linked lists.

**Quick Sort এবং Merge Sort এর তুলনামূলক বিশ্লেষণ**

**Quick Sort** Quick Sort একটি  **divide and conquer**  algorithm যেখানে একটি pivot নির্বাচন করে array কে ভাগ করা হয়।•  **Best Case Time Complexity:**  O(n log n)•  **Average Case Time Complexity:**  O(n log n)•  **Worst Case Time Complexity:**  O(n²) (যখন pivot সঠিকভাবে নির্বাচন হয় না)•  **Space Complexity:**  O(log n) (in-place sorting হওয়ায় কম memory লাগে)

**Merge Sort** Merge Sort একটি  **divide and conquer**  algorithm যেখানে array কে ভাগ করে sort করে পরে merge করা হয়।•  **Best Case Time Complexity:**  O(n log n)•  **Average Case Time Complexity:**  O(n log n)•  **Worst Case Time Complexity:**  O(n log n)•  **Space Complexity:**  O(n) (extra memory প্রয়োজন হয়)

**মূল পার্থক্য** • Quick Sort বাস্তবে দ্রুত কাজ করে কিন্তু worst case এ ধীর হতে পারে।• Merge Sort সব ক্ষেত্রেই নির্দিষ্ট সময়ে কাজ করে।• Quick Sort কম memory ব্যবহার করে।• Merge Sort বড় dataset ও linked list এর জন্য বেশি উপযোগী।

5. How can you (implement AND, OR and NOT gates using only NAND NOR gates? What is the main difference between Flip Flops and latches?

**Comparison between Quick Sort and Merge Sort**  **Quick Sort** Quick Sort is a  **divide and conquer**  algorithm that selects a pivot element and partitions the array around the pivot.•  **Best Case Time Complexity:**  O(n log n)•  **Average Case Time Complexity:**  O(n log n)•  **Worst Case Time Complexity:**  O(n²) (when the pivot selection is poor, e.g., already sorted array)•  **Space Complexity:**  O(log n) (in-place sorting due to recursion stack)

**Merge Sort** Merge Sort is a  **divide and conquer**  algorithm that divides the array into halves, sorts them, and then merges them.•  **Best Case Time Complexity:**  O(n log n)•  **Average Case Time Complexity:**  O(n log n)•  **Worst Case Time Complexity:**  O(n log n)•  **Space Complexity:**  O(n) (requires extra memory for merging)

**Key Comparison** • Quick Sort is generally faster in practice but has a worst-case of O(n²).• Merge Sort guarantees O(n log n) time in all cases.• Quick Sort uses less memory than Merge Sort.• Merge Sort is more suitable for large datasets and linked lists.

**Quick Sort এবং Merge Sort এর তুলনামূলক বিশ্লেষণ**

**Quick Sort** Quick Sort একটি  **divide and conquer**  algorithm যেখানে একটি pivot নির্বাচন করে array কে ভাগ করা হয়।•  **Best Case Time Complexity:**  O(n log n)•  **Average Case Time Complexity:**  O(n log n)•  **Worst Case Time Complexity:**  O(n²) (যখন pivot সঠিকভাবে নির্বাচন হয় না)•  **Space Complexity:**  O(log n) (in-place sorting হওয়ায় কম memory লাগে)

**Merge Sort** Merge Sort একটি  **divide and conquer**  algorithm যেখানে array কে ভাগ করে sort করে পরে merge করা হয়।•  **Best Case Time Complexity:**  O(n log n)•  **Average Case Time Complexity:**  O(n log n)•  **Worst Case Time Complexity:**  O(n log n)•  **Space Complexity:**  O(n) (extra memory প্রয়োজন হয়)

**মূল পার্থক্য** • Quick Sort বাস্তবে দ্রুত কাজ করে কিন্তু worst case এ ধীর হতে পারে।• Merge Sort সব ক্ষেত্রেই নির্দিষ্ট সময়ে কাজ করে।• Quick Sort কম memory ব্যবহার করে।• Merge Sort বড় dataset ও linked list এর জন্য বেশি উপযোগী।

6. What is domain in a relational database? Explain with an example. Show how you would use Alter table SQL command to add a domain on a database table  **Domain in a Relational Database**
A  **domain**  in a relational database is a set of valid values that an attribute (column) is allowed to take. It defines the  **data type, range, and constraints**  for a column, ensuring data consistency and integrity.

**Example:**

If we have a  **STUDENT**  table, the domain of the Age attribute can be defined as integers between 18 and 60.

**Using ALTER TABLE to Add a Domain (Constraint)**

```
ALTER TABLE STUDENT
ADD CONSTRAINT age_domain
CHECK (Age BETWEEN 18 AND 60);
```

This ensures that only values between 18 and 60 can be inserted into the  **Age**  column.

**Relational Database-এ Domain**

**Domain**  হলো একটি relational database-এর attribute (column)-এর জন্য নির্ধারিত বৈধ মানগুলোর সেট। এটি column-এর  **data type, range এবং constraint**  নির্ধারণ করে, যাতে data সঠিক ও consistent থাকে।

**উদাহরণ:**

**STUDENT**  table-এ Age attribute-এর domain হতে পারে 18 থেকে 60-এর মধ্যে integer মান।

**ALTER TABLE ব্যবহার করে Domain যোগ করা**

```
ALTER TABLE STUDENT
ADD CONSTRAINT age_domain
CHECK (Age BETWEEN 18 AND 60);
```

এতে করে  **Age**  column-এ শুধুমাত্র 18 থেকে 60-এর মধ্যে মান insert করা যাবে।

7. Write a program in java/c to find out the factorial of a number using recursion. Also write its iterative equivalent program.
```
#include <stdio.h>

int factorial(int n) {
if (n == 0)
return 1;              // base case
else
return n * factorial(n - 1);
}

int main() {
int num = 5;
printf("Factorial = %d", factorial(num));
return 0;
}
```



8. Suppose we have a 100 RPM disk with 8 heads and 480 cylinders. It Is divided into 120-cylinder zones with the cylinder in different zones containing 200, 240 and 320 sectors. Assume each sector contains 4096 bytes and seek time between adjacent cylinders of 2 ms.



a)What is the disk capacity?

**1) Disk Capacity**

Capacity = Σ (Cylinders in zone × Heads × Sectors/track × Bytes/sector)

= 120×8×200×4096 + 120×8×240×4096 + 120×8×320×4096 + 120×8×320×4096

=  **4,246,732,800 bytes**  ≈  **4.25 GB**  (decimal) ≈  **3.95 GiB**

b) What is the maximum transfer rate?

**2) Maximum Transfer Rate**

Rotation time per revolution = 60/100 =  **0.6 s**

Max sectors/track occurs in outer zone =  **320 sectors**

Data per revolution (one track) = 320 × 4096 =  **1,310,720 bytes**

Max transfer rate = 1,310,720 / 0.6 =  **2,184,533 bytes/s**  ≈  **2.18 MB/s**

**Note:**  2 ms seek affects access time between cylinders, but peak transfer rate is determined mainly by rotation speed and sectors/track (highest in the outer zone).
