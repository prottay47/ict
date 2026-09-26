# DESCO, Sub Assistant Engineer, 2025

- **Original URL:** [https://it.jobqns.com/desco-sub-assistant-engineer-2025/](https://it.jobqns.com/desco-sub-assistant-engineer-2025/)
- **Date:** 2026-03-02T12:17:51
- **Categories:** Job Solution 2025, Power Sector IT Job Solution 2025

---

#### DESCO Post: Sub-Assistant Engineer Exam Date: 20.6.2025Exam Taker: BUET



1.Explain with proper example of singly linked list.

**Singly Linked List**
A singly linked list is a linear collection of data items called nodes, where each node is divided into two parts.

- Data

- Link

- The first node has a special name called HEAD.

- The data part stores the data item.

- The link part stores the address of the next node.

- The last node is called the tail node.

- The linked list starts with a special pointer called the HEAD pointer and terminates with a NULL pointer.

**Singly Linked List**
Singly linked list হলো একটি linear collection of data items, যেগুলোকে node বলা হয়। প্রতিটি node দুইটি অংশে বিভক্ত থাকে।

- Data

- Link

- প্রথম node-টির একটি বিশেষ নাম রয়েছে, যাকে HEAD বলা হয়।

- Data part-এ data item store করা হয়।

- Link part-এ পরবর্তী node-এর address store করা হয়।

- শেষ node-টিকে tail node বলা হয়।

- Linked list একটি বিশেষ pointer দিয়ে শুরু হয় যাকে HEAD pointer বলা হয় এবং এটি NULL pointer-এ শেষ হয়।

Declaration of Singly linked list:

```
struct node
{
int data;
struct node *next;
};
```

2. What is CLI?

**What is CLI?**
**CLI (Command Line Interface)**  is a text-based interface that allows users to interact with a computer system by typing commands.

**Main Features:**

- Users type commands using a keyboard.

- The system executes the command and displays the result in text form.

- Requires knowledge of command syntax.

**Examples:**

- Command Prompt (Windows)

- Terminal (Linux/macOS)

- Bash Shell

**Advantages:**

- Fast and efficient for advanced users.

- Uses fewer system resources.

**CLI কী?**
**CLI (Command Line Interface)**  হলো একটি text-based interface যার মাধ্যমে ব্যবহারকারী command লিখে computer system-এর সাথে যোগাযোগ করে।

**প্রধান বৈশিষ্ট্য:**

- Keyboard ব্যবহার করে command টাইপ করতে হয়।

- System text আকারে ফলাফল দেখায়।

- Command-এর syntax জানা প্রয়োজন।

**উদাহরণ:**

- Windows Command Prompt

- Linux/macOS Terminal

- Bash Shell

**সুবিধা:**

- দক্ষ ব্যবহারকারীদের জন্য দ্রুত ও কার্যকর।

- কম system resource ব্যবহার করে।

3. What is OSPF? Briefly explain. **What is OSPF?**
**OSPF কী?**

4. State the working protocol of VRRP. **Working Protocol of VRRP**

**VRRP (Virtual Router Redundancy Protocol)**  is a network protocol used to provide automatic default gateway redundancy in a LAN.

**How VRRP Works:**

- **Virtual Router Creation:**  Multiple physical routers form a group and create a  **Virtual Router**  with a single Virtual IP (VIP) address.
- **Master and Backup Election:**  One router is elected as the  **Master**  (highest priority), and others act as  **Backup**  routers.
- **Advertisement Messages:**  The Master router periodically sends VRRP advertisement packets (using IP protocol number 112) to inform backups that it is active.
- **Failure Detection:**  If backups stop receiving advertisements within a specific time, they assume the Master has failed.
- **Automatic Failover:**  The Backup router with the next highest priority becomes the new Master and takes over the Virtual IP address.

**Key Features:**

- Provides gateway redundancy.
- Ensures high availability.
- Minimizes network downtime.

**VRRP-এর কাজের প্রোটোকল**

**VRRP (Virtual Router Redundancy Protocol)**  হলো একটি network protocol যা LAN-এ default gateway redundancy প্রদান করে।

**কাজের ধাপসমূহ:**

- **Virtual Router তৈরি:**  একাধিক router মিলে একটি  **Virtual Router**  তৈরি করে এবং একটি Virtual IP (VIP) ব্যবহার করে।
- **Master ও Backup নির্বাচন:**  সর্বোচ্চ priority সম্পন্ন router Master হয় এবং অন্যরা Backup হিসেবে থাকে।
- **Advertisement পাঠানো:**  Master router নিয়মিত VRRP advertisement message পাঠায় (IP protocol 112)।
- **Failure সনাক্তকরণ:**  Backup router advertisement না পেলে ধরে নেয় Master router ব্যর্থ হয়েছে।
- **Automatic Failover:**  পরবর্তী উচ্চ priority router Master হয়ে Virtual IP গ্রহণ করে।

**প্রধান বৈশিষ্ট্য:**

- Gateway redundancy প্রদান করে।
- High availability নিশ্চিত করে।
- Network downtime কমায়।

5. Write JavaScript code to check NID validity.
```
function isValidBDNID(nid) {
// Remove extra spaces
nid = nid.trim();

// Check if contains only digits and valid length (10, 13, or 17)
if (!/^\d{10}$|^\d{13}$|^\d{17}$/.test(nid)) {
return false;
}

// If 17-digit Smart NID, validate birth year (first 4 digits)
if (nid.length === 17) {
const year = parseInt(nid.substring(0, 4), 10);
const currentYear = new Date().getFullYear();

if (year < 1900 || year > currentYear) {
return false;
}
}

return true;
}

// Example
let nid = "19981234567890123";

if (isValidBDNID(nid)) {
console.log("Valid NID");
} else {
console.log("Invalid NID");
}
```

6.Find out the network address and broadcast address of the address: 192.168.0.0/28. **Given Address:**  192.168.0.0/28

**Step 1: Subnet Mask**

/28 means 28 bits for network.

Subnet Mask = 255.255.255.240

Block Size = 256 − 240 = 16

**Step 2: Network Address (NA)**

Since the given IP is 192.168.0.0 and /28 creates blocks of 16,

The first subnet range is:

192.168.0.0 – 192.168.0.15

**Network Address (NA):**  192.168.0.0

**Step 3: Broadcast Address (BA)**

Broadcast Address is the last address in the subnet range.

**Broadcast Address (BA):**  192.168.0.15

**Valid Host Range:**

Minimum Host = 192.168.0.1

Maximum Host = 192.168.0.14

Total Usable Hosts = 14

7. Differentiate between Load Testing and Stress Testing. **Difference Between Load Testing and Stress Testing**
- **Definition:**  Load Testing checks system performance under expected user load; Stress Testing evaluates system behavior under extreme or beyond-normal load.
- **Purpose:**  Load Testing ensures the system works properly during normal peak usage; Stress Testing identifies breaking point and failure behavior.
- **Load Level:**  Load Testing uses realistic and expected traffic; Stress Testing applies excessive or abnormal traffic.
- **Focus:**  Load Testing focuses on response time and throughput; Stress Testing focuses on system stability and recovery.
- **Result:**  Load Testing verifies performance requirements; Stress Testing determines system limits and robustness.
- **Example:**  Load Testing simulates 1,000 users logging in simultaneously; Stress Testing simulates 10,000+ users to observe system crash behavior.

**Load Testing এবং Stress Testing-এর পার্থক্য**

- **সংজ্ঞা:**  Load Testing স্বাভাবিক প্রত্যাশিত load-এ system-এর performance পরীক্ষা করে; Stress Testing অত্যধিক load-এ system-এর আচরণ পরীক্ষা করে।
- **উদ্দেশ্য:**  Load Testing নিশ্চিত করে system peak সময়েও সঠিকভাবে কাজ করছে; Stress Testing system-এর সীমা ও ভেঙে পড়ার অবস্থান নির্ণয় করে।
- **Load মাত্রা:**  Load Testing বাস্তবসম্মত load ব্যবহার করে; Stress Testing অতিরিক্ত load ব্যবহার করে।
- **ফোকাস:**  Load Testing response time ও throughput যাচাই করে; Stress Testing stability ও recovery যাচাই করে।
- **ফলাফল:**  Load Testing performance নিশ্চিত করে; Stress Testing system-এর সহনশীলতা নির্ধারণ করে।
- **উদাহরণ:**  Load Testing-এ ১,০০০ user একসাথে login; Stress Testing-এ ১০,০০০+ user দিয়ে system crash পরীক্ষা।

8. What are CSRF and XSS?

**What are CSRF and XSS?**

**1) CSRF (Cross-Site Request Forgery):**

**CSRF**  is a web security attack in which a malicious website tricks a user’s browser into performing unwanted actions on another trusted website where the user is already authenticated.

**How it works:**

- The victim logs into a trusted site (e.g., bank account).
- The attacker sends a malicious link or script.
- When the victim clicks it, the browser automatically sends a request using the stored session.

**Example:**  A hidden request transfers money from the victim’s bank account without their knowledge. **Prevention:**  CSRF tokens, SameSite cookies, and re-authentication. **2) XSS (Cross-Site Scripting):**

**XSS**  is a web vulnerability where an attacker injects malicious scripts into a trusted website, which then executes in the victim’s browser.

**How it works:**

- The attacker inserts malicious JavaScript into input fields.
- The script runs in other users’ browsers.
- It can steal cookies, session IDs, or sensitive data.

**Types:**  Stored XSS, Reflected XSS, DOM-based XSS. **Prevention:**  Input validation, output encoding, Content Security Policy (CSP).

**১) CSRF (Cross-Site Request Forgery):**

**CSRF**  হলো একটি web security attack যেখানে attacker ব্যবহারকারীর browser-কে ব্যবহার করে তার অজান্তে কোনো trusted website-এ অনাকাঙ্ক্ষিত কাজ করায়।

**কাজের পদ্ধতি:**

- ব্যবহারকারী আগে থেকেই কোনো trusted site-এ login করা থাকে।
- Attacker একটি ক্ষতিকর link পাঠায়।
- Click করলে browser স্বয়ংক্রিয়ভাবে request পাঠায়।

**প্রতিরোধ:**  CSRF token, SameSite cookie, পুনরায় authentication। **২) XSS (Cross-Site Scripting):**

**XSS**  হলো একটি web vulnerability যেখানে attacker একটি trusted website-এ malicious script inject করে, যা ব্যবহারকারীর browser-এ execute হয়।

**কাজের পদ্ধতি:**

- Input field-এ ক্ষতিকর JavaScript যুক্ত করা হয়।
- Script অন্য ব্যবহারকারীর browser-এ চালু হয়।
- এটি cookie বা sensitive data চুরি করতে পারে।

**প্রকারভেদ:**  Stored, Reflected, DOM-based XSS। **প্রতিরোধ:**  Input validation, output encoding, Content Security Policy (CSP)।

9. Consider a Student Table like (StudentID, StudentName, Age, Department) now write below queries:
i) Show only specific department students.
ii) All students age highest to lowest.
iii) Student numbers in each department.
```
-- i) Show only specific department students
SELECT *
FROM Student
WHERE Department = 'CSE';

-- ii) All students age highest to lowest
SELECT *
FROM Student
ORDER BY Age DESC;

-- iii) Student numbers in each department
SELECT Department, COUNT(*) AS TotalStudents
FROM Student
GROUP BY Department;
```
