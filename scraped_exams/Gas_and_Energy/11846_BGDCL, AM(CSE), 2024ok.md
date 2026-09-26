# BGDCL, AM(CSE), 2024ok

- **Original URL:** [https://it.jobqns.com/bgdcl-amcse-2024/](https://it.jobqns.com/bgdcl-amcse-2024/)
- **Date:** 2026-02-12T16:03:39
- **Categories:** Gas Field IT Job Solution, Gas Field IT Job Solution 2024, Job Solution 2024

---

#### Bakhrabad Gas Distribution Company Limited (BGDCL)
Post: Assistant Manager (CSE), Exam Date: 15.03.2024, Exam Taker: BUET



1. How to represent binary tree using array

**Representation of Binary Tree Using Array** A Binary Tree can be represented using an array by storing tree elements level by level (level order). This method is very efficient for complete or nearly complete binary trees.

**Array Representation Rules** • If a node is stored at index  **i** :• Left child is stored at index  **2i** • Right child is stored at index  **2i + 1** • Parent node is stored at index  **⌊i/2⌋**

**Example** Binary Tree:

```
A
/ \
B   C
/ \   \
D   E   F
```

Array Representation (1-based index):Index: 1 2 3 4 5 6 7Array: A B C D E – F

**Note** This representation is best suited for complete binary trees. For sparse trees, it may waste memory.

**Array ব্যবহার করে Binary Tree উপস্থাপন** Binary Tree কে array ব্যবহার করে level-by-level (level order) সংরক্ষণ করা যায়। এই পদ্ধতি complete বা প্রায় complete binary tree এর জন্য খুব কার্যকর।

**Array Representation এর নিয়ম** • যদি কোনো node index  **i**  তে থাকে:• Left child থাকবে index  **2i**  তে• Right child থাকবে index  **2i + 1**  তে• Parent node থাকবে index  **⌊i/2⌋**  তে

**উদাহরণ** Binary Tree:

```
A
/ \
B   C
/ \   \
D   E   F
```

Array Representation (1-based index):Index: 1 2 3 4 5 6 7Array: A B C D E – F

**নোট** এই পদ্ধতিটি complete binary tree এর জন্য উপযুক্ত। Sparse tree হলে কিছু memory অপচয় হতে পারে।

2. You have given two 16*16 metrics but your processor support 8*8  matrices how can you multiply write algorithm

**Step 1: Divide the Matrices**

Divide each \(16 \times 16\) matrix into four \(8 \times 8\) submatrices:

\[ A = \begin{bmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{bmatrix}, \quad B = \begin{bmatrix} B_{11} & B_{12} \\ B_{21} & B_{22} \end{bmatrix} \]

Where:

- \(A_{11}, A_{12}, A_{21}, A_{22}\) are \(8 \times 8\) submatrices of \(A\).
- \(B_{11}, B_{12}, B_{21}, B_{22}\) are \(8 \times 8\) submatrices of \(B\).

**Step 2: Multiply the Submatrices**

The product \(C = A \times B\) can also be expressed in terms of the submatrices:

\[ C = \begin{bmatrix} C_{11} & C_{12} \\ C_{21} & C_{22} \end{bmatrix} \]

Where:

- \(C_{11} = A_{11} \times B_{11} + A_{12} \times B_{21}\)
- \(C_{12} = A_{11} \times B_{12} + A_{12} \times B_{22}\)
- \(C_{21} = A_{21} \times B_{11} + A_{22} \times B_{21}\)
- \(C_{22} = A_{21} \times B_{12} + A_{22} \times B_{22}\)

Each of these multiplications (\(A_{11} \times B_{11}\), \(A_{12} \times B_{21}\), etc.) is an \(8 \times 8\) matrix multiplication, which your processor can handle.

**Step 3: Combine the Results**

After computing all the submatrix products, combine them to form the final \(16 \times 16\) result matrix \(C\):

\[ C = \begin{bmatrix} C_{11} & C_{12} \\ C_{21} & C_{22} \end{bmatrix} \]  **Algorithm**

**Explanation of Functions**

- **matrix_multiply(X, Y)** : Performs \(8 \times 8\) matrix multiplication using the processor’s capabilities.
- **combine_submatrices(C11, C12, C21, C22)** : Combines the four \(8 \times 8\) submatrices into a single \(16 \times 16\) matrix.

**🎥 Video Solution:**  16*16 Matrix multiplication by 8*8 matrix

3. Find the output from the following: take input and looks the output: Suppose
Input: 6789
Output: 9876
```
#include <stdio.h>

int main() {
int number, rev = 0, remainder;

// Taking input
printf("Enter a number: ");
scanf("%d", &number);

// Reversing the number
while (number != 0) {
remainder = number % 10;   // Get the last digit
rev = rev * 10 + remainder; // Append to reversed number
number /= 10;              // Remove last digit
}

// Printing the reversed number
printf("Reversed Number: %d\n", rev);

return 0;
}
```

```
Sample I/O:
Enter a number: 9876
Reversed Number: 6789
=== Code Execution Successful ===
```

🔗 Run Online: Reverse Number

4. How can multiprogramming be achieved on a uniprocessor system?  explain

**Multiprogramming on a Uniprocessor System** Multiprogramming on a uniprocessor system is achieved by allowing multiple programs (processes) to reside in main memory at the same time and by rapidly switching the CPU among them. Although there is only one CPU, the operating system creates the illusion that multiple programs are running simultaneously.

**How Multiprogramming is Achieved** 1)  **Multiple Processes in Memory:**  The operating system loads several processes into main memory at once.2)  **CPU Scheduling:**  The OS uses a scheduling algorithm to decide which process will use the CPU at any given time.3)  **Context Switching:**  When a running process needs to wait (for I/O, for example), the CPU state of that process is saved, and the CPU is given to another ready process.4)  **Overlap of CPU and I/O:**  While one process is waiting for I/O, another process uses the CPU, ensuring efficient CPU utilization.

**Result** This rapid switching makes it appear that multiple programs are executing at the same time, even though only one CPU exists.

**Uniprocessor System এ Multiprogramming** Uniprocessor system এ multiprogramming অর্জন করা হয় একই সময়ে একাধিক program (process) কে main memory তে রেখে এবং দ্রুতগতিতে CPU কে process গুলোর মধ্যে পরিবর্তন (switch) করার মাধ্যমে। যদিও CPU মাত্র একটি, তবুও operating system এমন ধারণা দেয় যে একাধিক program একসাথে চলছে।

**Multiprogramming কীভাবে অর্জিত হয়** 1)  **একাধিক Process Memory তে রাখা:**  Operating system একই সাথে একাধিক process main memory তে load করে।2)  **CPU Scheduling:**  OS একটি scheduling algorithm ব্যবহার করে নির্ধারণ করে কোন process কখন CPU পাবে।3)  **Context Switching:**  কোনো process I/O এর জন্য অপেক্ষা করলে তার CPU state সংরক্ষণ করে CPU অন্য process কে দেওয়া হয়।4)  **CPU এবং I/O Overlap:**  একটি process I/O এর জন্য অপেক্ষা করার সময় অন্য process CPU ব্যবহার করে, ফলে CPU utilization বাড়ে।

**ফলাফল** এই দ্রুত switching এর কারণে মনে হয় একাধিক program একসাথে চলছে, যদিও বাস্তবে CPU একটি মাত্র।

5. Employee & department table given. 2 query’s.
(i) Write the employee name who got same salary named Rahim but  not same job of Rahim.
(ii)  Write the employee’s name who's average salary is more than  company's average salary

(i)

```
SELECT e.name
FROM employees e
JOIN employees r
ON e.salary = r.salary
AND e.name <> 'Rahim'
AND e.job <> r.job
WHERE r.name = 'Rahim';
```

Explanation:

- We join the
```
employees
```
table with itself.
- We match employees (
```
e
```
) who have the same salary as
```
Rahim
```
(
```
r
```
).
- We exclude
```
Rahim
```
himself.
- We ensure that the job of the selected employee is different from Rahim’s.

(ii)

```
SELECT name
FROM employees
GROUP BY name
HAVING AVG(salary) > (SELECT AVG(salary) FROM employees);
```

- We calculate the average salary for each employee.
- We compare it with the  **company’s overall average salary** .
- We select only those employees whose average salary is  **higher**  than the company’s average.

6. Library management class diagram

7. Write different parts of 8086 micropreocessor:
ABus Interface UnitBExecution UnitCALUDC-BUSEControl Unit

8. There are given 5 network ID and IP address.  Match which is loopback, host, this host, Network broadcast,  broadcast out bound address. (appox.)

**Loopback Address:**  This refers to IP addresses within the 127.0.0.0/8 range, commonly starting with 127. It is used for testing and internal communication within the same device.

**Host Address:**  These are IP addresses assigned to specific devices within a network, allowing communication between them.

**This Host:**  Identifies the IP address of the local machine currently in use.

**Network Broadcast Address:** This is determined based on the network ID and subnet mask, and it is used to send data to all devices within a network.

**Broadcast Outbound Address:** This address is used to send data packets outside the current network, typically reaching all nodes in a broader network scope.
