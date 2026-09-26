# PGCB, Assistant Engineer(CSE), 2024ok

- **Original URL:** [https://it.jobqns.com/pgcb-assistant-engineercse-2024/](https://it.jobqns.com/pgcb-assistant-engineercse-2024/)
- **Date:** 2026-03-05T14:23:27
- **Categories:** Job Solution 2024, Power Sector IT Job Solution 2024

---

#### Power Grid Company of Bangladesh
Post: Assistant Engineer (CSE) Exam Date: 17.05.2024, Exam Taker: BUET



1. a) Insert the data into BST from given Nodes
b) Print the tree in post order traversal of the BST
c) Structure of the BST after deleting one node.

**Binary Search Tree (BST)**

A Binary Search Tree (BST) is a tree that follows these rules:

- The left sub-tree of a node contains values less than or equal to the parent node’s value.

- The right sub-tree of a node contains values greater than or equal to the parent node’s value.

BST from these values insertion : [27, 14, 35, 10, 19, 31, 42]

```
27
/  \
14    35
/  \   /  \
10   19 31  42
```

**The post-order traversal of the given Binary Search Tree (BST) is:**

```
10, 19, 14, 31, 42, 35, 27
```

BST Deletion:

To delete a node from a Binary Search Tree (BST), we follow these steps:

- **Node has no children** : Just remove the node.

- **Node has one child** : Remove the node and link its parent to its child.

- **Node has two children** : Find the in-order successor (smallest node in the right subtree) or in-order predecessor (largest node in the left subtree), replace the node to be deleted with the successor or predecessor, and delete the successor or predecessor.

**Deleting Node 35 from the BST:**

We are deleting node 35, which has two children (31 and 42). The in-order successor of 35 is 42. So, we replace 35 with 42 and then remove node 42, which has no children.

```
27
/  \
14    42
/  \   /
10   19 31
```

2. Write C code  x - x^3/3! + x^5/5! - x^7/7!+............
```
#include <stdio.h>
#include <math.h>

// Function to calculate factorial
double factorial(int n) {
double result = 1.0;
for (int i = 1; i <= n; i++) {
result *= i;
}
return result;
}

// Function to calculate sine using the series expansion
double sine_series(double x, int terms) {
double sum = 0.0;
for (int n = 0; n < terms; n++) {
int sign = (n % 2 == 0) ? 1 : -1; // Alternating signs
double term = pow(x, 2 * n + 1) / factorial(2 * n + 1);
sum += sign * term;
}
return sum;
}

int main() {
double x;
int terms;

// Input angle in radians and number of terms
printf("Enter the value of x (in radians): ");
scanf("%lf", &x);
printf("Enter the number of terms: ");
scanf("%d", &terms);

// Calculate sine using the series expansion
double result = sine_series(x, terms);

// Output the result
printf("The sine of %.2lf using %d terms is: %.6lf\n", x, terms, result);

return 0;
}
```

3. a) How many bits in IPv4 and IPv6 Address?
b) Why doesn’t NAT used in IPv6?
c) Difference between https and http

**(a) Number of Bits in IPv4 and IPv6 Address**

- **IPv4 Address:**  IPv4 uses  **32 bits**  address.
- It is usually written in dotted decimal format (e.g., 192.168.1.1).
- **IPv6 Address:**  IPv6 uses  **128 bits**  address.
- It is written in hexadecimal format separated by colons (e.g., 2001:0db8:85a3::8a2e:0370:7334).

**(b) Why NAT is Not Used in IPv6**

- **Large Address Space:**  IPv6 provides a huge address space (128-bit), so there is no shortage of IP addresses.
- **Direct End-to-End Communication:**  Every device can have a unique public IP address, allowing direct communication without translation.
- **Simplified Network Design:**  NAT adds complexity to network configuration, which IPv6 avoids.
- **Better Security and Performance:**  IPv6 supports built-in features like IPsec and avoids delays caused by address translation.

**(a) IPv4 এবং IPv6 Address-এ কত bit থাকে**

- **IPv4 Address:**  IPv4 address-এ  **32 bit**  থাকে।
- এটি সাধারণত dotted decimal format-এ লেখা হয় (যেমন: 192.168.1.1)।
- **IPv6 Address:**  IPv6 address-এ  **128 bit**  থাকে।
- এটি hexadecimal format-এ colon দ্বারা পৃথক করে লেখা হয় (যেমন: 2001:0db8:85a3::8a2e:0370:7334)।

**(b) IPv6-এ কেন NAT ব্যবহার করা হয় না**

- **Large Address Space:**  IPv6-এ 128-bit address থাকায় পর্যাপ্ত IP address পাওয়া যায়।
- **Direct End-to-End Communication:**  প্রতিটি device একটি unique public IP address পেতে পারে, তাই NAT প্রয়োজন হয় না।
- **Simplified Network Design:**  NAT network configuration জটিল করে, কিন্তু IPv6 এটি এড়িয়ে যায়।
- **Better Security এবং Performance:**  IPv6-এ IPsec-এর মতো built-in security feature থাকে এবং address translation-এর delay থাকে না।

c)

4. Draw a class diagram for a E commerce website where customer can view  different products, can pay either card or cash.

5. Given,   Hit- 1 nano second
Miss- 25 ns
1% instruction miss
5℅ data miss
Total input data 15%  Find the average access time

Given Data:

- Hit Time = 1 ns

- Miss Penalty = 25 ns

- Instruction Miss Rate = 1% (0.01)

- Data Miss Rate = 5% (0.05)

- Percentage of memory accesses that are data = 15% (0.15)

- Percentage of memory accesses that are instructions = 85% (0.85)

Step 1: Calculate the Effective Miss Rate

The effective miss rate is the weighted average of the instruction and data miss rates:

Effective Miss Rate = (Instruction Miss Rate × Instruction Access Percentage) + (Data Miss Rate × Data Access Percentage)
Effective Miss Rate = (0.01 × 0.85) + (0.05 × 0.15)
Effective Miss Rate = 0.0085 + 0.0075 = 0.016

Step 2: Calculate AMAT

AMAT = Hit Time + (Effective Miss Rate × Miss Penalty)
AMAT = 1 + (0.016 × 25)
AMAT = 1 + 0.4 = 1.4 ns Answer:

6. Given DB table with Employee (NID, Company_id, Name, Mobile Number),  Assume every record has a unique mobile number. Find the number of super  key, candidate and give example of two candidate key.

A  **candidate key**  is a minimal set of attributes that can uniquely identify a record in the table. Based on the given information:

- **```
Mobile Number
```** :

Since every record has a unique mobile number,
```
Mobile Number
```
alone can uniquely identify a record. Therefore, it is a candidate key.

- **```
NID
```** :

If
```
NID
```
is unique for each employee, it can also uniquely identify a record. Therefore, it is another candidate key.

A  **super key**  is any set of attributes that can uniquely identify a record. It may include additional attributes beyond the candidate key.

- The total number of attributes in the table is  **4**  (
```
NID
```
,
```
Company_id
```
,
```
Name
```
,
```
Mobile Number
```
).

- The candidate keys are:

```
Mobile Number
```

```
NID
```

Super Keys Based on
```
Mobile Number
```
:

- Since
```
Mobile Number
```
is a candidate key, any superset of
```
Mobile Number
```
is a super key.

- The remaining attributes are
```
NID
```
,
```
Company_id
```
, and
```
Name
```
.

- The number of possible super keys based on
```
Mobile Number
```
is:
2^3=8
(Each of the 3 attributes can either be included or excluded.)

Super Keys Based on
```
NID
```
:

- Similarly, since
```
NID
```
is a candidate key, any superset of
```
NID
```
is a super key.

- The remaining attributes are
```
Company_id
```
,
```
Name
```
, and
```
Mobile Number
```
.

- The number of possible super keys based on
```
NID
```
is:
2^3=8

Overlap Between Super Keys:

- Some super keys are counted in both cases (based on
```
NID
```
and
```
Mobile Number
```
). These are the super keys that include  **both
```
NID
```
and
```
Mobile Number
```** .

- The number of overlapping super keys is:
2^2=4
(These are combinations of
```
Company_id
```
and
```
Name
```
with
```
NID
```
and
```
Mobile Number
```
.)

Total Super Keys:

- Using the principle of inclusion-exclusion:
Total Super Keys=8+8−4=12

7(a) Difference between Alfa, Beta, Gamma testing

7(b) What is Demilitarized Zone (DMZ) and sanbox for security test ?

**DMZ (Demilitarized Zone)**

A  **DMZ**  is a network area that acts as a buffer between the internal network and external networks like the internet.

- **Purpose:**  To provide an extra layer of security.

- **Working:**  Public servers (web, email) are placed in DMZ to prevent direct access to internal network.

- **Benefit:**  Protects internal systems from external attacks.

**Sandbox**

A  **sandbox**  is an isolated environment used for testing software or applications safely.

- **Purpose:**  To test unknown or risky programs securely.

- **Working:**  Runs code in isolation so it cannot affect the main system.

- **Benefit:**  Detects errors or malware before deployment.

**DMZ (Demilitarized Zone)**
**DMZ**  হলো একটি network অংশ যা internal network এবং external network (internet)-এর মধ্যে buffer হিসেবে কাজ করে।

- **Purpose:**  অতিরিক্ত security layer প্রদান করা।

- **Working:**  Public server (web, email) DMZ-তে রাখা হয় যাতে internal network সরাসরি attack না হয়।

- **Benefit:**  Internal system-কে external attack থেকে সুরক্ষিত রাখে।

**Sandbox**
**Sandbox**  হলো একটি isolated environment যেখানে software নিরাপদভাবে test করা যায়।

- **Purpose:**  Unknown বা risky program নিরাপদভাবে পরীক্ষা করা।

- **Working:**  Code আলাদা environment-এ run হয়, তাই main system প্রভাবিত হয় না।

- **Benefit:**  Deployment-এর আগে error বা malware শনাক্ত করা যায়।

8. F1 = A+B, F2 = AB
Create the functions using NAND and NOR gate
