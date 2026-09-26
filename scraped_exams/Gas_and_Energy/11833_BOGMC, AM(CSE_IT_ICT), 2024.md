# BOGMC, AM(CSE/IT/ICT), 2024

- **Original URL:** [https://it.jobqns.com/bogmc-amcse-it-ict-2024/](https://it.jobqns.com/bogmc-amcse-it-ict-2024/)
- **Date:** 2026-02-12T13:55:12
- **Categories:** Gas Field IT Job Solution, Gas Field IT Job Solution 2024, Job Solution 2024

---

#### Bangladesh Oil Gas and Mineral Corporation (BOGMC)- Petrobangla
Post:  Assistant Manager (CSE/IT/ICT) Exam Date: 31.05.2024, Exam Taker: BUET



1(a) A C program is given. You have to write the output of the program  when the value of a = 85.
a =85
if a>=90 print A;
if a>=80 print B;
if a>=70 print C;
if a>=60 print D;
else print F; **Output:**

1 (b) You have three access specifiers in java object oriented  language. You have to find which access specifiers are worked  with Public, Private and Protected Mode. If yes you have to  right Y and If No you have to write N.
- **Public (
```
public
```
)**  → Accessible  **everywhere**  (inside class, package, subclass, and outside package).
- **Private (
```
private
```
)**  → Only accessible  **within the same class**  (not within the package, subclass, or outside).
- **Protected (
```
protected
```
)**  → Accessible  **within the class, package, and subclasses (even outside the package)** , but  **not outside the package**  unless it’s through inheritance.

2(a) You are given a binary tree (a, b,c,d,e,f,g,h,i) nodes. The post order  of the binary tree is:a b f c h d e g i nodes. Now draw the binary tree  and show the array representation of this binary tree. (approximate)
```
i
/ \
h   g
/ \  / \
f   c d  e
/ \
a   b
```

[ not possible to find b tree by only given post order]

Array Representation:Formula for Binary Tree Array Representation:

- Left child of node at index
```
i
```
→
```
2i + 1
```
- Right child of node at index
```
i
```
→
```
2i + 2
```

2(b) In a quicksort algorithm taking first element as a pivot element. Now  Analyze the time complexity of quicksort algorithm when all  services of the quicksort algorithm are already sorted.

**Time Complexity of QuickSort with First Element as Pivot on Sorted Array**

In  **QuickSort** , when we select the  **first element**  as the pivot, the time complexity heavily depends on the partitioning step. In the case of an  **already sorted array** , the  **first element**  is always the smallest element, leading to an unbalanced partitioning where one sub-array is always empty.

**Steps:**

- **Pivot Selection:**  The first element is chosen as the pivot.
- **Partitioning:**  The pivot is placed at its correct position, and the array is partitioned into two sub-arrays:Left sub-array: Empty (no elements smaller than the pivot).Right sub-array: Contains  **n-1**  elements (larger than the pivot).
- **Recursion:**  This process repeats for the right sub-array, reducing the problem size by 1 each time, leading to a total of  **n**  recursive calls.

**Recurrence Relation:**

```
T(n) = T(n-1) + O(n)
```

Where:

- **T(n-1)**  is the time for the next recursive call.
- **O(n)**  is the partitioning step.

This recurrence leads to:

```
T(n) = O(n) + O(n-1) + O(n-2) + ... + O(1) = O(n²)
```

**Conclusion:**

When the array is already sorted, and the first element is chosen as the pivot, the  **QuickSort**  algorithm exhibits  **worst-case time complexity**  of  **O(n²)**  due to highly unbalanced partitioning at each step.

**🎥 Video Solution:** Quick Sort Algorithm **🎥 Video Solution:** Quick Sort Performance



3. Employee (empno, PK, empname, monthlysalary, deptno, FK, mqrnd(FK))
Department(deptno, deptname,deptlocation)
Course(crscode,pk, crd desc, crs category, crs duration);
Offering(off begingate, crscode fk, offeringlocation, empno fk)

Find

3 (a) Dept has average Monthly Salary greater than 1000;
```
SELECT d.deptno, d.deptname, AVG(e.monthsalary) AS average_salary
FROM Department d
JOIN Employee e ON d.deptno = e.deptno
GROUP BY d.deptno, d.deptname
HAVING AVG(e.monthsalary) > 1000;
```

3 (b) Find Courses with more than two oferings
```
SELECT c.crscode, c.crsdesc,
c.crscategory, c.crsduration,
COUNT(o.crscode) AS offering_count
FROM Course c
JOIN Offering o ON c.crscode = o.crscode
GROUP BY c.crscode, c.crsdesc, c.crscategory, c.crsduration
HAVING COUNT(o.crscode) = 2;
```



4 (a) A traffic signal cycles from GREEN to YELLOW, YELLOW to RED and  RED to GREEN. In each cycle, GREEN is turned on for 70 seconds,  YELLOW is turned on for 5 seconds and the RED is turned on for 75  seconds. This traffic light has to be implemented using a finite state  machine (FSM). The only input to this FSM is a clock of 5 second period.  The minimum number of flip-flops required to implement this FSM .

Traffic Signal Cycle:

- GREEN: 70 seconds
- YELLOW: 5 seconds
- RED: 75 seconds
- Total cycle time = 70 + 5 + 75 = 150 seconds.

Clock Input:

The FSM is driven by a clock with a 5-second period. This means the FSM transitions every 5 seconds.

Number of States:

- GREEN: 70 seconds → 70 / 5 = 14 clock cycles
- YELLOW: 5 seconds → 5 / 5 = 1 clock cycle
- RED: 75 seconds → 75 / 5 = 15 clock cycles
- Total clock cycles in one full cycle = 14 + 1 + 15 = 30 clock cycles.

State Representation:

The FSM must cycle through 30 states to complete one full traffic signal cycle.

Calculating the Number of Flip-Flops:

The number of flip-flops required is determined by the number of states in the FSM. For N states, the minimum number of flip-flops required is:

```
Number of flip-flops = ⌈log₂(N)⌉
```

Calculating:

log₂(30) ≈ 4.906

⌈4.906⌉ = 5

4 (b) Given 5 scenario of a software engineering (Unit test, Regression  Test, Smoke Test, Integration testing, Load Testing). One is done for  you. Write the name of the testing and whether it is function/non  function or both.

5(a) What is the difference between Shell and kernel ?

Source: [Byjus.com]

5(b) How to solve when drive failure in RAID? **How to Solve Drive Failure in RAID**
When a drive fails in a RAID system, the solution depends on the RAID level being used. RAID is designed to provide fault tolerance, so data loss can often be avoided. **General Steps to Handle Drive Failure**
1)  **Identify the Failed Drive:**  RAID controller or system logs indicate which drive has failed.
2)  **Replace the Failed Drive:**  Remove the faulty drive and insert a new drive of the same capacity (hot-swappable in most RAID systems).
3)  **Rebuild the RAID:**  The RAID controller automatically rebuilds data on the new drive using parity or mirrored data.
4)  **Verify Data Integrity:**  After rebuilding, check system logs and data to ensure everything is working correctly. **RAID Level Examples**
RAID 1: Data is recovered from the mirror drive.
RAID 5: Data is rebuilt using parity information.
RAID 6: Can tolerate two drive failures using dual parity.
RAID 0: No recovery possible (no redundancy). **RAID এ Drive Failure হলে কীভাবে সমাধান করা হয়**
RAID system এ কোনো drive নষ্ট হলে সমাধানটি নির্ভর করে কোন RAID level ব্যবহার করা হয়েছে তার উপর। RAID মূলত fault tolerance দেওয়ার জন্য তৈরি, তাই বেশিরভাগ ক্ষেত্রে data loss হয় না। **Drive Failure সমাধানের সাধারণ ধাপ**
1)  **Failed Drive শনাক্ত করা:**  RAID controller বা system log থেকে কোন drive নষ্ট হয়েছে তা জানা যায়।
2)  **নষ্ট Drive পরিবর্তন করা:**  Faulty drive খুলে একই capacity এর নতুন drive বসানো হয় (অনেক ক্ষেত্রে hot-swappable)।
3)  **RAID Rebuild করা:**  RAID controller parity বা mirrored data ব্যবহার করে নতুন drive এ data পুনর্গঠন করে।
4)  **Data যাচাই করা:**  Rebuild শেষ হলে system ও data ঠিক আছে কিনা পরীক্ষা করা হয়। **RAID Level অনুযায়ী উদাহরণ**
RAID 1: Mirror drive থেকে data recover করা যায়।
RAID 5: Parity information ব্যবহার করে data rebuild হয়।
RAID 6: Dual parity থাকার কারণে দুইটি drive failure সহ্য করতে পারে।
RAID 0: কোনো recovery সম্ভব নয় (redundancy নেই)।

5(c) What is the use of mmWaves in IoT?   **Use of mmWaves in IoT**
mmWaves (millimeter waves) are high-frequency radio waves (typically 30–300 GHz) used in advanced wireless communication. In IoT, mmWaves enable ultra-fast data transfer, low latency, and support for a large number of connected devices, especially in dense environments.

**Key Uses of mmWaves in IoT**
1)  **High Data Rate:**  Supports very high-speed data transmission for video sensors and smart cameras.
2)  **Low Latency:**  Ideal for real-time IoT applications such as autonomous vehicles and industrial automation.
3)  **Massive Connectivity:**  Handles many IoT devices in smart cities and smart factories.
4)  **Precise Sensing:**  Used in radar-based IoT for motion detection and positioning.
5)  **5G IoT Support:**  mmWaves are a core technology behind 5G-enabled IoT networks. **IoT এ mmWaves এর ব্যবহার**
mmWaves (millimeter waves) হলো উচ্চ frequency এর radio wave (সাধারণত 30–300 GHz), যা আধুনিক wireless communication এ ব্যবহৃত হয়। IoT তে mmWaves ব্যবহার করা হয় দ্রুত data transfer, কম latency এবং অনেক device একসাথে connect করার জন্য।

**IoT এ mmWaves ব্যবহারের প্রধান দিক**
1)  **High Data Rate:**  Smart camera ও video sensor এর মতো IoT device এ দ্রুত data পাঠানো যায়।
2)  **Low Latency:**  Autonomous vehicle ও industrial automation এর মতো real-time IoT application এ উপযোগী।
3)  **Massive Connectivity:**  Smart city ও smart factory তে অনেক IoT device একসাথে handle করা যায়।
4)  **Precise Sensing:**  Radar-based IoT তে movement detection ও positioning এ ব্যবহার হয়।
5)  **5G IoT Support:**  5G ভিত্তিক IoT network এর একটি গুরুত্বপূর্ণ technology হলো mmWaves।

5(d) What is the need of an edge server?

**Need of an Edge Server** An Edge Server is used to process data closer to the end users instead of sending all requests to a central server. This reduces delay and improves performance, especially for real-time and high-traffic applications.

**Why Edge Server is Needed** 1)  **Reduced Latency:**  Data is processed near the user, so response time becomes faster.2)  **Reduced Bandwidth Usage:**  Less data is sent to the central server, saving network bandwidth.3)  **Better Performance:**  Improves speed for applications like video streaming, online gaming, and IoT.4)  **High Availability:**  If the central server is busy or down, edge servers can still serve users.5)  **Scalability:**  Handles large numbers of user requests efficiently.

**Edge Server এর প্রয়োজনীয়তা** Edge Server ব্যবহার করা হয় user এর কাছাকাছি data process করার জন্য, যাতে সব request central server এ পাঠাতে না হয়। এতে delay কমে এবং performance উন্নত হয়।

**Edge Server কেন প্রয়োজন** 1)  **Latency কমানো:**  User এর কাছেই data process হওয়ায় response দ্রুত আসে।2)  **Bandwidth সাশ্রয়:**  Central server এ কম data পাঠাতে হয়।3)  **Performance উন্নতি:**  Video streaming, online gaming ও IoT application এ ভালো কাজ করে।4)  **High Availability:**  Central server সমস্যা হলে edge server user কে service দিতে পারে।5)  **Scalability:**  একসাথে অনেক user request দক্ষতার সাথে handle করা যায়।
