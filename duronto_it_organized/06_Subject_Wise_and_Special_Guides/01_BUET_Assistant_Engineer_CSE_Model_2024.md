# BUET Pattern - Assistant Engineer (CSE) Model Exam

| Field | Details |
| :--- | :--- |
| **Organization** | BUET |
| **Post Name** | Assistant Engineer (CSE) |
| **Exam Date** | Model Pattern |
| **Exam Taker** | BUET |
| **Marks / Format** | 100 Marks (60 Non + 40 Dept) |
| **Source** | Duronto IT Academy / Smart IT Job Solution |

---

Assistant Engineer (CSE) Exam Taker: BUET Time: 10-11 AM Marks: 60 (Non)+Dept (40) 

Total Question dept: 08 Date: 17.05.2024 

**1 a) Insert the data into BST from given Nodes b) Print the tree in post order traversal of the BST**  **c) Structure of the BST after deleting one node.** 

Suppose we have some values: 10, 100, 30, 20, 500, 40 Then BST will look like: 

Post Order: 10 40 30 20 500 100 Suppose we want to delete 40 node: 

**2 Write C code** **x - x^3/3! + x^5/5! - x^7/7!............**  #include <stdio.h> #include <math.h> 

// Function to calculate factorial 

double factorial(int n) { double result = 1.0; for (int i = 1; i <= n; i++) { result *= i; } return result; } 

// Function to calculate sine using the series expansion double sine_series(double x, int terms) { double sum = 0.0; for (int n = 0; n < terms; n++) { int sign = (n % 2 == 0) ? 1 : -1; // Alternating signs double term = pow(x, 2 * n + 1) / factorial(2 * n + 1); sum += sign * term; } return sum; 

} 

int main() { double x; int terms; 

// Input angle in radians and number of terms printf("Enter the value of x (in radians): "); scanf("%lf", &x); printf("Enter the number of terms: "); scanf("%d", &terms); 

#### **3 a) How many bits in IPv4 and IPv6 Address? b) Why doesn’t NAT used in IPv6?**  **c) Difference between https and http** 

IPV4 = 32 

IPV6 = 128 

The primary reasons NAT is not used in IPv6 are the vast address space, which eliminates the need for address conservation, and the preservation of end-to-end connectivity, which simplifies network configuration and management. IPv6 was designed to overcome the limitations of IPv4 and to enable a more straightforward, scalable, and secure Internet. 

|Feature|HTTP|HTTPS|

|---|---|---|

|Security|Unsecured|Secured (using SSL/TLS)|

|Port Number|80|443|

|URL Prefix|http://|https://|

|Encryption|No|Yes|

|Certificate Required|No|Yes|

|Common Use Cases|General web browsing|Secure transaction|

1. **Calculate Hit Rate:** Since miss rate is the opposite of hit rate, we can find the hit rate by subtracting the miss rate from 1 (100%). 

Hit Rate = 1 - (Instruction Miss Rate + Data Miss Rate) Hit Rate = 1 - (1% + 5%) Hit Rate = 1 - 0.06 (converted percentages to decimals for calculation) Hit Rate = 0.94 

2. **Calculate Access Times Weighted by Hit Rate and Miss Rate:** 

Average Access Time = (Hit Rate * Hit Time) + (Miss Rate * Miss Time) 

- Hit Time = 1 nanosecond (given) 

- Miss Time (combined instruction and data miss) = 25 nanoseconds (given) 

- Miss Rate = 1 - Hit Rate = 0.06 (calculated earlier) 

Average Access Time = (0.94 * 1 ns) + (0.06 * 25 ns) 

3. **Calculate Average Access Time:** 

Average Access Time = 0.94 ns + 1.5 ns Average Access Time = 2.44 nanoseconds (rounded to two decimal places) 

Therefore, the average access time for the system is approximately 2.44 nanoseconds **6. Given DB table with Employee (NID, Company_id, Name, Mobile Number), Assume every record has a unique mobile number. Find the number of super**  **key, candidate and give example of two candidate key.** To find the number of super keys, candidate keys, and examples of candidate keys for the given 

table Employee(NID, Company_id, Name, Mobile Number), we need to understand the concepts of super keys and candidate keys. 

###### **Definitions** 

**Super Key** : A set of one or more columns (attributes) that can uniquely identify a row in the table. **Candidate Key** : A minimal super key, which means it cannot be reduced further without losing the property of uniquely identifying a row. 

**Analysis** 

Given the table attributes: NID (presumably a unique identifier for each employee) Company_id (identifier for the company the employee works for) Name (name of the employee) Mobile Number (unique mobile number for each employee) 

###### **Unique Attributes** 

NID is unique. Mobile Number is unique. 

###### **Candidate Keys** 

- Candidate keys are minimal sets of attributes that can uniquely identify a row. Based on the unique attributes: 

- 1. NID (since it's unique and minimal) 2. Mobile Number (since it's unique and minimal) _Thus, the candidate keys are: NID_ 

_Mobile Number_ **Super Keys** 

Super keys include all candidate keys and any superset of candidate keys. For the given table: All candidate keys themselves are super keys. 

Any combination of the attributes that includes a candidate key is also a super key. 

###### **Number of Super Keys** 

To calculate the total number of super keys, we need to consider all possible combinations of attributes that include at least one candidate key (NID or Mobile Number). 

Given the attributes: NID, Company_id, Name, Mobile Number, let's calculate the combinations: 

1. **Single Attribute Super Keys** : NID Mobile Number 

2. **Two Attribute Super Keys** : 

NID, Company_id NID, Name NID, Mobile Number (already a candidate key) Mobile Number, Company_id Mobile Number, Name Mobile Number, NID (already a candidate key) 

3. **Three Attribute Super Keys** : NID, Company_id, Name NID, Company_id, Mobile Number NID, Name, Mobile Number Mobile Number, Company_id, Name Mobile Number, Company_id, NID Mobile Number, Name, NID 

4. **Four Attribute Super Key** : NID, Company_id, Name, Mobile Number 

**Total Number of Super Keys** 

If we count all the combinations above, we get: 

2 (single attribute super keys) 

- 4 (two attribute super keys excluding duplicates) 

- 4 (three attribute super keys excluding duplicates) 1 (four attribute super key) Total = 2 + 4 + 4 + 1 = 11 super keys 

**Summary Number of Super Keys** : 11 **Number of Candidate Keys** : 2 **Examples of Candidate Keys** : NID 

Mobile Number 

###### **7. a) Difference between Alfa, Beta, Gamma testing.**  

|**Aspect**|**Alpha Testing**|**Beta Testing**|**Gamma Testing**|

|---|---|---|---|

|**Conducted by**|Internal team<br>(developers, QA<br>testers)|Selected group of<br>external users (beta<br>testers)|Select group of users<br>(similar to beta testing)|

|**Environment**|Controlled internal<br>environment|Real-world environment|Controlled but real-<br>world environment|

|**Aspect**|**Alpha Testing**|**Beta Testing**|**Gamma Testing**|

|---|---|---|---|

|**Focus**|Functional and non-<br>functional testing|Usability, functionality,<br>reliability|Final verification,<br>readiness for release|

|**Purpose**|Identify early bugs<br>and issues|Gather user feedback,<br>identify real-world issues|Ensure no critical<br>issues, final acceptance|

|**Outcome**|Stable enough for<br>beta testing|Refined based on user<br>feedback|Ready for production<br>deployment|

###### **b) What is Demilitarized Zone (DMZ) and sanbox for security test ?**  

A DMZ or demilitarized zone is a perimeter network that protects and adds an extra layer of security to an organization's internal local-area network from untrusted traffic. 

Sandboxes serve as a development testing environment, enabling organizations to run applications in a secure space before they are introduced into the production stage. This safe space ensures that any damaging issues are addressed without compromising or slowing down critical resources. 

**Titas Gas Transmission and Distribution Company Limited (TGTDCL) Assistant Engineer (CSE), Exam Taker: BUET Exam Time: 1 hour, 09-10 AM Date: 24/05/2024 Non Dept: 20, Dept: 40** **Nusrat & Raihan Tarek** 

**1. a) Write recursive function for the given scenario:                                 [2] for (int i=1,i<n;i++){ For ( int j=0 ; j<i ; j ++){ For ( int k =0; k<i ; k++ ) x= x+1;** **}}};** 

#include <iostream> 

void innerLoop(int i, int k, int &count) { if (k < i) { count++;       // Equivalent to X = X + 1 innerLoop(i, k + 1, count); } } void middleLoop(int i, int j, int &count) { if (j < i) { innerLoop(i, 0, count); middleLoop(i, j + 1, count); } } 

void outerLoop(int i, int n, int &count) { if (i < n) { middleLoop(i, 0, count); outerLoop(i + 1, n, count); } } int main() { int n = 5; // Example value for n int count = 0; // Initialize count outerLoop(1, n, count); cout << "Number of times x = x + 1 is executed: " << count <<endl; return 0; } 

**b) If a complete binary tree is a proper binary tree, then prove that number of leaf** **node is one more than internal nodes. [3]** 

**Total Nodes (N):** The total nodes in the tree are the sum of internal nodes and leaf nodes. N = I + L 

**Relationship in Full Binary Tree:** In a full binary tree, the number of total nodes is given by: N = 2I + 1 

This is because each internal node contributes exactly two children, and there is one additional internal node. 

###### **Proof** 

1. Starting with the relationship between the total number of nodes (N) and the internal nodes (I): 𝑁=2𝐼+1 

2. From the total nodes equation, we also have: 𝑁=𝐼+𝐿 

3. Equating the two expressions for 𝑁: 𝐼+𝐿=2𝐼+1 4. Solving for 𝐿: 𝐿=2𝐼+1−𝐼 𝐿=𝐼+1 

###### **Conclusion** 

The number of leaf nodes (L) in a complete binary tree that is full is exactly one more than the number of internal nodes (I): 

𝐿=𝐼+1 _L_ = _I_ +1 

Thus, we have proven that in a complete binary tree, the number of child nodes (leaf nodes) is one more than the number of internal nodes. 

**c) Problem A can be reduced to problem B in polynomial time, which problem is** **harder and why? [3]** 

**Given this reduction, the relative hardness of the problems can be assessed:** 

###### Hardness Comparison 

Problem B is at least as hard as Problem A: If problem A can be reduced to problem B in polynomial time, solving problem B must be at least as hard as solving problem A. This is because, if we had an efficient (polynomial-time) solution for problem B, we could use the reduction to efficiently solve problem A as well. 

###### **Why Problem B is Considered Harder** 

_Efficiency of Reduction:_ Since the reduction from A to B is polynomial-time, it doesn't significantly increase the overall complexity. Therefore, if we can solve B efficiently (in polynomial time), we can also solve A efficiently by first transforming it into an instance of B and then solving B. 

Implications for Complexity Classes: If problem A is in a lower complexity class (e.g., P) and problem B is in a higher complexity class (e.g., NP-complete), then the reduction implies that problem B is at least as hard as problem A. Specifically, if problem A is NP-complete and we can reduce A to B in polynomial time, then B must be NP-hard (and possibly NP-complete if it's also in NP). 

Example 

_Consider problems A and B where:_ 

Problem A: 3-SAT (which is NP-complete) 

Problem B: Some other problem 

If 3-SAT (problem A) can be reduced to problem B in polynomial time, this suggests that problem B is at least as hard as 3-SAT 

###### **2. a) A 4*1 MUX is given, write down its expression in SOM form.  [4]**  

According to Raihan Tarek Question collection and answer 

###### **b) Write down which is related to CISC or RISC from given description [2]**  

|Easy to pipe line-|RISC|

|---|---|

|More Addressing mode|CISC|

|fixed instruction format.|RISC|

|More memory efficient|CISC|

A page fault is an event that occurs in a computer system's memory management when a program tries to access a specific piece of data (a page) that is not currently loaded in physical memory (RAM). This means the data is either: 

1. **Not yet loaded:** The program might be referencing a page from disk for the first time. 

2. **Swapped out:** The page was previously in RAM but was removed to make space for other data and needs to be retrieved from secondary storage (like a hard disk). 

###### **3. a)  Briefly explain Circular wait in dead lock.                                          [2]**  

Circular wait, also known as a circular dependency, is a necessary condition for a deadlock to occur in a computer system. It's a situation where multiple processes are waiting for resources that are currently held by other processes in the system, creating a loop of dependencies. Here's a breakdown of circular wait and its role in deadlock: 

###### **Circular Wait:** 

- A set of processes are each waiting for a resource that is held by another process in the sequence. 

- This creates a circular chain of dependencies, where each process is blocked because it needs a resource held by the next process in the chain. 

###### **3 (b) What is the appropriate pairing of items in the two columns listing various** **activities encountered in a software life cycle?** 

P - 2, Q - 3, R - 1, S – 4; 

**c) How to prevent XSS And CSRF attack? [2]**  

Prevention XSS: 

- **Prevention:** 

   - **Input Validation:** Sanitize all user input (form data, URL parameters, etc.) to remove potentially harmful scripts. 

   - **Output Encoding:** Encode special characters in user input before displaying it on the website to prevent them from being interpreted as code. 

   - **Content Security Policy (CSP):** Define a whitelist of allowed sources for scripts to run on your website. This restricts the execution of any unauthorized scripts. 

Prevention CSRF: Cross-Site Request Forgery (CSRF): 

- **Prevention:** 

   - **CSRF Tokens:** Embed a unique, random token in every form on your website. Include this token in the request body or a hidden form field. The server verifies the token to ensure the request originated from your website and not a forged link. 

   - **SameSite Cookie Attribute:** Set the SameSite attribute of cookies to Lax or Strict to restrict how cookies are sent in cross-site requests. 

###### **4. a) A log file keeps record of the updates, how to get the last line of the log file? [2]**  

tail -n 1 /path/to/logfile.log 

|**b)**|**traceroute to reach marketplace.com where the traceroute sequence is given**<br>**bellow,**<br>**1. gateway.titasgas.gov.bd ip time**<br>**2. backup.titasgas.gov.bd ip time**<br>**.**<br>**.**<br>**.**<br>**.**<br>**8. global.com ip time**<br>**9. * * ***<br>**10. * * ***<br>**11. * * ***|

|---|---|

||**12. marketplace.com**<br>**How many hops are required to reach 12? what will be in line 9 to 11? Explain.**<br>**[4]**|

**Hops Required:** It takes **12 hops** to reach marketplace.com. 

**Lines 9-11: Timeouts or Packet Filtering** 

**c) How Man In The Middle attack affect on DHCP server?** **[2]**  In a MITM attack on DHCP, an attacker inserts themselves into the communication between a DHCP server and clients. The attacker can achieve this by spoofing DHCP messages, either acting as a rogue DHCP server or intercepting and modifying DHCP traffic. Here are a few common scenarios: 

1. **Rogue DHCP Server** : The attacker sets up a rogue DHCP server on the network. When a client requests an IP address, the rogue server responds faster than the legitimate server, providing the client with malicious configuration settings. 

2. **DHCP Spoofing** : The attacker intercepts DHCP requests and responses, modifying them before they reach the intended recipient. This can include altering IP addresses, DNS servers, gateways, etc **5. a) Write query to find out supliers name who supplies 'wheel' at least cost. [4] Suppliers (sid, sname, address) Parts (pid, pname, color)** **Catalog (sid, pid, cost)** 

SELECT S.sname FROM Suppliers S JOIN Catalog C ON S.sid = C.sid JOIN Parts P ON C.pid = P.pid WHERE P.pname = 'wheel' AND C.cost = ( SELECT MIN(C2.cost) FROM Catalog C2 JOIN Parts P2 ON C2.pid = P2.pid WHERE P2.pname = 'wheel' 

**b) Write a program to findout an expression is ended correctly or not. [4] Input: ((a+b)+(a-b)  Output: Matched Input: (a+b)+a-c) Output : Not matched** 

```

#include <iostream>

#include <string>

using namespace std;

bool isMatched(const string& expression) {

```

```

    int balance = 0;

    for (char ch : expression) {

        if (ch == '(') {

            balance++;

        } else if (ch == ')') {

            balance--;

        }

        if (balance < 0) {

            return false;

        }

    }

    return balance == 0;

}

int main() {

    string expr1 = "((a+b)+(a-b)";

    string expr2 = "(a+b)+a-c)";

cout << "Input: " << expr1 << "  Output: " << (isMatched(expr1)

? "Matched" : "Not matched") << endl;

cout << "Input: " << expr2 << "  Output: " << (isMatched(expr2)

? "Matched" : "Not matched") << endl;

    return 0;

}

```

**1(a). A C program is given. You have to write the output of the program when the value of a = 85.**  

If(a>=90) printf(“A”); If(a>=80) printf(“B”); If(a>=70) printf(“C”); If(a>=60) printf(“D”); Else printf (“F”) **Output: BCD** Analyzing the Code 

1. **Initial Condition Check (a >= 90)** : 

   - When a = 85, the condition a >= 90 is false. 

   - Therefore, printf("A"); will not execute. 

2. **Second Condition Check (a >= 80)** : 

   - The condition a >= 80 is true because 85 >= 80. 

   - Therefore, printf("B"); will execute, and "B" will be printed. 

3. **Third Condition Check (a >= 70)** : 

   - The condition a >= 70 is true because 85 >= 70. 

   - • Therefore, printf("C"); will execute, and "C" will be printed. 

4. **Fourth Condition Check (a >= 60)** : 

   - The condition a >= 60 is true because 85 >= 60. 

   - Therefore, printf("D"); will execute, and "D" will be printed. 

|**1(b).**|**You have**<br>**language. Y**<br>**with Public,**<br>**right Y and**|**three access**<br>**ou have to fin**<br>**Private and**<br>**If Noyou hav**|**specifiers in java o**<br>**d which access specifie**<br>**Protected Mode. If y**<br>**e to write N.**|**bject oriented**<br>**rs are worked**<br>**es you have to**|

|---|---|---|---|---|

||Within Class|Within<br>Package|Outside<br>package<br>by sub class only|Outside<br>Package|

|Public|Y|Y|Y|Y|

**fb.com/groups/govtcse.itjob** ee | 

**1- 1** 

|---|---|---|---|---|

|Private|Y|N|N|N|

|Protected|Y|Y|Y|N|

- **2.(a) You are given a binary tree (a, b,c,d,e,f,g,h,i) nodes. The post order of the binary tree is:a b f c h d e g i nodes. Now draw the binary tree** **and show the array representation of this binary tree.** 

Array Representation: [a, b, c, d, e, f, g, h, i] 

- **2(b) In a quicksort algorithm taking first element as a pivot element. Now Analyze the time complexity of quicksort algorithm when all services of the quicksort algorithm are already sorted.** 

###### **Steps of Quicksort:** 

Choose the first element as the pivot. 

Partition the array such that elements less than the pivot are on the left and elements greater than or equal to the pivot are on the right. 

Recursively apply the same procedure to the sub-arrays formed by partitioning. 

###### **Worst-Case Scenario (Already Sorted Array)** 

###### Partitioning Step 

When the array is already sorted, choosing the first element as the pivot results in highly unbalanced partitions: 

One sub-array will contain all the elements except the pivot. 

The other sub-array will be empty. 

For an array of n elements: 

The first partitioning step will result in one sub-array of size n-1 and an empty subarray. 

The second partitioning step will result in one sub-array of size n-2 and an empty sub-array. 

This process continues until the base case of a 1-element array is reached. 

**fb.com/groups/govtcse.itjob** ee | 

**Number of Comparisons** 

During each partitioning step, the algorithm makes n-1 comparisons to partition the array: 

First step: n-1 comparisons. Second step: n-2 comparisons. ... Last step: 1 comparison. Summing these comparisons gives the total number of comparisons 𝑛(𝑛−1) (n-1) + (n-2)+…..+1 = 2 This summation is a well known arithmetic series. 𝑛(𝑛−1) Time Complexity: 2 O(n<sup>2</sup> ) 

**3 Employee (empno, PK, empname, monthlysalary, deptno, FK, mqrnd(FK)) Department(deptno, deptname,deptlocation) Course(crscode,pk, crd desc, crs category, crs duration);** **Offering(off begingate, crscode fk, offeringlocation, empno fk)** 

**(a) Dept has averageMonthlySalary greater than 1000;** SELECT d.deptno, d.deptname, AVG(e.monthlysalary) AS average_salary FROM Department d JOIN Employee e ON d.deptno = e.deptno GROUP BY d.deptno, d.deptname HAVING AVG(e.monthlysalary) > 1000; **(b) Course contain 2 course offering** SELECT c.crscode, c.crsdesc, c.crscategory, c.crsduration, COUNT(o.crscode) AS offering_count FROM Course c JOIN Offering o ON c.crscode = o.crscode GROUP BY c.crscode, c.crsdesc, c.crscategory, c.crsduration HAVING COUNT(o.crscode) = 2; 

**4(a) A traffic signal cycles from GREEN to YELLOW, YELLOW to RED and RED to GREEN. In each cycle, GREEN is turned on for 70 seconds, YELLOW is turned on for 5 seconds and the RED is turned on for 75 seconds. This traffic light has to be implemented using a finite state machine (FSM). The only input to this FSM is a clock of 5 second period. The minimum number of flip-flops required to implement this FSM .** 

**fb.com/groups/govtcse.itjob** ee | 

Green is turned ON for 70 seconds Yellow is turned ON for 5 seconds. Red is turned ON for 75 seconds 

∴ Total time to complete one cycle for all 3 lights = (70 + 5 +75) seconds = 150 seconds 

Available time period of clock = 5 seconds Total number of clock cycles in one complete cycle = 150/5 = 30 Assume number of flip-flops required = n We know possible number of states using n flip-flops = 2<sup>𝑛</sup> So to get 30 clock cycle or 30 states, 2<sup>𝑛</sup> ≥ 30 

⇒ n ≥ 4.90 

∴ Minimum number of required flip-flops is = 5 

**4(b) Given 5 scenario of a software engineering (Unit test, Regression Test, Smoke Test, Integration testing, Load Testing). One is done for you. Write the name of the testing and whether it is function/non function or both.** 

|Verifying smallest part of a software system|Unit Testing|Functional|

|---|---|---|

|Re-running functional and non-functional<br>tests to ensure that a software application still<br>works as expected after changes.|Regression<br>Testing|Functional|

|Testing specific amount of traffic|Load Testing|Non-<br>Functional|

|Preliminary<br>test<br>of<br>basic<br>functional<br>requirements|Smoke Testing|Functional|

|Verify if different modules or services work<br>together as expected.|Integration<br>testing|Functional|

###### **5.(a) What is the difference between Shell and kernel ?**  

Shell is the outer layer of OS. Kernel is the inner layer of OS. 

**fb.com/groups/govtcse.itjob** ee | 

Shell acts as an intermediary between the user and the kernel, Operates at a lower level than the shell and interacts with hardware. 

###### **b How to solve when drive failure in RAID?**  

- **Identify the Failed Drive:** Your RAID controller software or BIOS should 

- identify the failed drive. Look for error messages or warnings. 

- **Power Down the System:** If possible, shut down the system to prevent further 

- damage to the RAID array. 

- **Consult Your RAID Documentation:** Refer to your RAID controller's manual 

- for specific instructions on how to handle drive failures. 

- **Replace the Failed Drive:** If your RAID level tolerates drive failures (RAID 1, 

- 5, or 6), obtain a replacement drive with the same specifications (capacity, speed, etc.). Replace the failed drive according to the RAID controller's instructions. 

- **Data Recovery (if necessary):** If data recovery is necessary (RAID 0 failure or multiple drive failures in RAID 5/6), consider professional data recovery services. They have specialized tools and techniques for recovering data from damaged RAID arrays. 

######  **(c) What is the use of mmWaves in IoT?** 

IoT devices use mmWaves, as their high bandwidth capacity is ideal for applications such as short-distance wireless transmission of ultra-high-definition video and communications. 

**(d) What is the need of an edge server?**  An edge server is a computing system that's located at the edge of a network, close to data sources or end-users. Edge servers can act as an entry point into a network, connecting two or more distinct networks. They can also store cached versions of content and deliver it as quickly as possible. 

Uses: Reduced Latency, Improved Bandwidth Efficiency, Enhanced Security, Offline Functionality, Scalability, Real-Time Insights: 

**fb.com/groups/govtcse.itjob** ee |
