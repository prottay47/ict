# ICB, Assistant Programmer, 2026

- **Original URL:** [https://it.jobqns.com/icb-assistant-programmer-2026/](https://it.jobqns.com/icb-assistant-programmer-2026/)
- **Date:** 2026-06-28T00:55:28
- **Categories:** Bank IT Job Solution 2026, Uncategorized

---

Assistant Programmer • Year 2026

Investment Corporation of Bangladesh

💼Post Name: Assistant Programmer

📅Exam Date: 27-Jun-2026

- ☆

1

Programming Concept

Write pseudocode or code in any programming language where every character of a string increases by 1 alphabetically, such as a -> b and z -> a.

The problem requires character-wise transformation of a string where each alphabet is shifted by one position in the alphabet. This is commonly known as a Caesar cipher with shift 1. **Logic:** Each character is checked individually. If it is 'z', it wraps to 'a'. If it is 'Z', it wraps to 'A'. Otherwise, ASCII value is incremented by 1. **Pseudocode:**
```
FUNCTION shiftString(S) RESULT = " FOR EACH character c IN S IF c == 'z' THEN RESULT = RESULT + 'a' ELSE IF c == 'Z' THEN RESULT = RESULT + 'A' ELSE RESULT = RESULT + (c + 1) END IF END FOR RETURN RESULTEND FUNCTION
```
**Conclusion:**  This algorithm runs in O(n) time complexity where n is the length of the string.

**Pseudocode Solution**
```
FUNCTION shiftString(S) RESULT = " FOR EACH CHAR c IN S IF c == 'z' THEN RESULT = RESULT + 'a' ELSE IF c == 'Z' THEN RESULT = RESULT + 'A' ELSE RESULT = RESULT + (c + 1) END IF END FOR RETURN RESULTEND FUNCTION
```
প্রতিটি character কে ASCII অনুযায়ী +1 shift করা হয় এবং z/Z হলে wrap করে a/A তে নেয়া হয়।

☆

2

Structure Query Language

Given Student(sid, name, dept) and Course(sid, cid, cname, marks), Find the student name, department, course name, and marks where marks are greater than 80.  Find department-wise and subject-wise students where marks are not less than 30.

We are given two relations: Student(sid, name, dept) and Course(sid, cid, cname, marks). The common attribute sid is used to join both tables. **1. Students with marks greater than 80:** This query retrieves high-performing students by applying a selection condition on marks.
```
SELECT S.name, S.dept, C.cname, C.marksFROM Student SJOIN Course C ON S.sid = C.sidWHERE C.marks > 80;
```
**2. Department-wise and subject-wise students (marks ≥ 30):** This query filters moderately passed students and organizes output by department and course.
```
SELECT S.dept, C.cname, S.name, C.marksFROM Student SJOIN Course C ON S.sid = C.sidWHERE C.marks >= 30;
```
**Conclusion:**  JOIN operation is essential to combine student identity with course performance data.

**SQL Solution** ১. Marks 80 এর বেশি:
```
SELECT S.name, S.dept, C.cname, C.marksFROM Student SJOIN Course C ON S.sid = C.sidWHERE C.marks > 80;
```
২. Department-wise ও subject-wise (marks ≥ 30):
```
SELECT S.dept, C.cname, S.name, C.marksFROM Student SJOIN Course C ON S.sid = C.sidWHERE C.marks >= 30;
```


☆

3

Cloud Computing

ISTCL currently supports 10,000 active users and expects traffic to surge to 80,000 concurrent users. The legacy on-premises system already suffers from severe performance degradation and latency during peak hours. The engineering team proposes migrating to a scalable cloud architecture, but executive management denies cloud migration due to budget constraints and data sovereignty policies. What solution should be proposed, and why?

The system faces scalability limitations due to increased concurrent users. Since full cloud migration is restricted, an alternative architecture must be proposed. **Proposed Solution:**  Hybrid scalability model using optimized on-prem infrastructure. **Components:** Load balancing across multiple serversHorizontal scaling using additional on-prem serversMicroservices architecture for modular scalingCDN for static content deliveryDatabase replication and caching layers **Reason:**  This ensures scalability, cost efficiency, and compliance with data sovereignty policies. **Conclusion:**  Hybrid architecture provides near-cloud scalability without violating organizational constraints.

**Proposed Solution** Full cloud migration সম্ভব নয়, তাই  **hybrid scalable architecture**  ব্যবহার করা উচিত।মূল কৌশল:Load

- ☆

4

Computer Network
Subnetting

A company named ICB has been allotted the IP address 192.198.10.0/22. Using subnetting, allocate subnets for Finance, Admin, IT, Loan, and HR requiring 250, 125, 120, 250, and 60 hosts respectively. Find the subnet mask, valid host addresses, and network address for each subnet.

The given network is 192.198.10.0/22, which provides 1024 IP addresses (from 192.198.8.0 to 192.198.11.255). VLSM is used to allocate different subnet sizes based on host requirements. **Step 1: Sort requirements (descending)** 250, 250, 125, 120, 60 hosts **Step 2: Required subnet sizes** 250 hosts → /24 (256 addresses)250 hosts → /24125 hosts → /25 (128 addresses)120 hosts → /2560 hosts → /26 (64 addresses) **Step 3: Subnet allocation**  **Finance:**  192.198.8.0/24Mask: 255.255.255.0Valid hosts: 192.198.8.1 – 192.198.8.254 **Loan:**  192.198.9.0/24Mask: 255.255.255.0Valid hosts: 192.198.9.1 – 192.198.9.254 **Admin:**  192.198.10.0/25Mask: 255.255.255.128Valid hosts: 192.198.10.1 – 192.198.10.126 **IT:**  192.198.10.128/25Mask: 255.255.255.128Valid hosts: 192.198.10.129 – 192.198.10.254 **HR:**  192.198.11.0/26Mask: 255.255.255.192Valid hosts: 192.198.11.1 – 192.198.11.62 **Conclusion:**  VLSM minimizes wastage by allocating IPs according to requirement.

- ☆

5

Digital Logic Design
Basic

Determine whether the logical statement (P -> Q) -> (P' -> Q') is a tautology, contradiction, or contingency.

**Determine whether the logical statement:**
(P → Q) → (P' → Q')
**Apply implication rules**

P → Q ≡ ¬P ∨ Q
P' = ¬P
Q' = ¬Q

Therefore,
P' → Q' = ¬P → ¬Q

**Construct the Truth Table**

P
Q
P → Q
P' → Q'
(P → Q) → (P' → Q')

T
T
T
T
T

T
F
F
T
T

F
T
T
F
F

F
F
T
T
T

**Conclusion**

Final column values:  **T, T, F, T**

Since the statement is  **true in some cases**  and  **false in one case** , it is neither a tautology nor a contradiction.
**Therefore, the logical statement (P → Q) → (P' → Q') is a Contingency.**
In discrete mathematics, a contingency is a compound proposition whose truth value is neither always true (a tautology) nor always false (a contradiction). Its final outcome depends entirely on the specific truth values of its individual variables, meaning its truth table contains at least one True (T) and at least one False (F).

☆

6

Microprocessor & Computer Architecture
Basic

A server has a fast CPU and abundant RAM, but despite low CPU and memory utilization, the system suffers from severe instruction execution delays and high latency during processing tasks. What needs to be updated, and what is the solution?

When CPU and RAM utilization are low but system latency is high, the bottleneck is not compute or memory, but input/output performance. **Step 1: Identify bottleneck** Low CPU usage → not compute-boundLow memory usage → not memory-boundHigh latency → likely I/O-bound system **Step 2: Root cause** Slow disk storage (HDD), high I/O wait time, and limited throughput are common causes. **Solution:** Upgrade storage subsystem to SSD or NVMe and optimize I/O scheduling. **Conclusion:**  I/O subsystem is the critical bottleneck, not CPU or RAM.

**Performance Bottleneck Analysis** CPU ও RAM কম ব্যবহার হলেও latency বেশি হলে এটি I/O bottleneck নির্দেশ করে। **সমস্যা:** Slow HDD storageHigh I/O wait **Solution:**  SSD/NVMe storage upgrade ও I/O optimization।

- ☆

7

Computer Security
Different Attacks

When an IT firm announces a system exploit and developers rush to implement a patch, the organization enters a vulnerable window of exposure. If a zero-day attack occurs simultaneously and the system is financial, what may happen?

A zero-day vulnerability refers to an exploit that is unknown to vendors and has no available patch at the time of attack. During patch deployment, systems often experience temporary exposure. **Scenario Impact:** Attackers exploit unpatched vulnerabilitiesSecurity controls may be partially disabled during updatesFinancial systems become high-value targets **Possible Consequences:** Unauthorized transactions and fraudLeakage of sensitive financial dataSystem downtime and integrity lossRegulatory penalties and trust damage **Conclusion:**  A simultaneous zero-day attack can lead to critical financial breach and operational collapse.

**Security Impact Analysis** Patch চলাকালীন zero-day exploit হলে system vulnerability window তৈরি হয়।Financial system এ হতে পারে:Unauthorized fund transferFinancial data breachSystem integrity compromiseCompliance violation **Result:**  বড় financial loss ও security breach।

- ☆

8

Big Data, ML & AI
Probability

Server X and Server Y distribute incoming web traffic. Server X handles 60% of requests, while Server Y handles the remaining 40%. The probability of high latency is 2% for Server X and 4% for Server Y. Determine the total probability that a randomly selected request encounters high latency and the conditional probability that a delayed request was handled by Server X.

This is a conditional probability problem using the law of total probability and Bayes' theorem. **Given:** P(X)=0.6, P(Y)=0.4P(L|X)=0.02, P(L|Y)=0.04 **Step 1: Total probability of latency** P(L) = P(X)P(L|X) + P(Y)P(L|Y)= 0.6×0.02 + 0.4×0.04= 0.012 + 0.016 = 0.028 **Step 2: Conditional probability** P(X|L) = (P(X)P(L|X)) / P(L)= 0.012 / 0.028 = 3/7 ≈ 0.4286 **Conclusion:**  Overall latency probability is 2.8%, and delayed request is more likely from Server Y.

**Probability Solution** Given:P(X)=0.6, P(Y)=0.4P(L|X)=0.02, P(L|Y)=0.04Total probability:P(L)=0.028Conditional probability:P(X|L)=3/7 ≈ 0.4286

9. Write about ‘Social Media’ oportunities,challenge ,employment

10. Write about 150 word environment and economic impact of Renewable Energy

11. Translation Bangla to English:  ২১শে ফেব্রুয়ারি আমাদের জাতীয় ইতিহাসে একটি গৌরবময় এবং স্মরণীয় দিন। প্রতি বছর আমরা এই দিনটিকে শহীদ দিবস এবং আন্তর্জাতিক মাতৃভাষা দিবস হিসেবে পালন করি . এই দিনটি তাদের সেই মহান ত্যাগকে স্মরণ করিয়ে দেয়।
