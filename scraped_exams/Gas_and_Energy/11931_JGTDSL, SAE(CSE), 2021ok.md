# JGTDSL, SAE(CSE), 2021ok

- **Original URL:** [https://it.jobqns.com/jgtdsl-saecse-2021/](https://it.jobqns.com/jgtdsl-saecse-2021/)
- **Date:** 2026-02-12T19:44:44
- **Categories:** Gas Field IT Job Solution, Job Solution 2021

---

#### Jalalabad Gas Transmission and Distribution System Ltd
Post: Sub Assistant Engineer (Computer)
Exam Date: 17/09/2021, Exam Taker: BUET



1. Describe software development waterfall model design .

**Waterfall Model in Software Development** The Waterfall Model is a linear and sequential software development approach. In this model, development progresses step-by-step through clearly defined phases. Each phase must be completed before moving to the next one. It is best suited for projects where requirements are clear, fixed, and well-documented from the beginning.

**Phases of the Waterfall Model:**

**1) Requirements Analysis:** All customer requirements are gathered and documented in a Software Requirement Specification (SRS) document.

**2) Design:** The requirements are converted into system design documents, including high-level design (HLD) and low-level design (LLD), to define architecture and components.

**3) Development (Implementation):** The actual source code is written according to the approved design documents.

**4) Testing and Deployment:** All modules are integrated and tested through alpha, beta, and acceptance testing. After successful testing, the software is deployed for users.

**5) Maintenance:** After deployment, bugs are fixed, performance is improved, and updates or enhancements are made as required.

In short, the Waterfall Model is simple and structured, but it works best when project requirements are stable and unlikely to change.

**Software Development-এ Waterfall Model** Waterfall Model হলো একটি linear এবং sequential software development পদ্ধতি। এই মডেলে কাজ ধাপে ধাপে সম্পন্ন হয় এবং একটি ধাপ শেষ না হলে পরবর্তী ধাপে যাওয়া যায় না। এটি এমন প্রকল্পের জন্য উপযুক্ত যেখানে requirement শুরু থেকেই পরিষ্কার ও স্থির থাকে।

**Waterfall Model-এর ধাপসমূহ:**

**1) Requirements Analysis:** Customer-এর সব requirement সংগ্রহ করে Software Requirement Specification (SRS) document-এ লিখিতভাবে সংরক্ষণ করা হয়।

**2) Design:** Requirement অনুযায়ী system-এর High-Level Design (HLD) এবং Low-Level Design (LLD) তৈরি করা হয়, যেখানে architecture ও component নির্ধারণ করা হয়।

**3) Development (Implementation):** Design document অনুসারে actual source code লেখা হয়।

**4) Testing and Deployment:** সব module একত্রিত করে alpha, beta এবং acceptance testing করা হয়। সফলভাবে testing শেষ হলে software user-এর জন্য deploy করা হয়।

**5) Maintenance:** Deployment-এর পরে bug fix, performance উন্নয়ন এবং নতুন feature সংযোজন করা হয়।

সংক্ষেপে, Waterfall Model একটি সহজ ও শৃঙ্খলাপূর্ণ পদ্ধতি, যা তখনই ভালো কাজ করে যখন requirement শুরু থেকেই স্থির ও পরিবর্তনহীন থাকে।

2. Reverse polish notation এর মাধ্যমে গাণিতিক বিশ্লেষণ করঃ (7+1)*(6+(3-2)).

ধাপ ১: ইনফিক্স থেকে পোস্টফিক্সে রূপান্তর(7+1)∗(6+(3−2)) হবে পোস্টফিক্সে: 7 1 + 6 3 2 – + *

ধাপ ২: পোস্টফিক্স এক্সপ্রেশন বিশ্লেষণExpression: 7 1 + 6 3 2 – + *

Stack ব্যবহার করে গণনা:

Push 7Stack: [7]

Push 1Stack: [7, 1]

Encounter +: Pop 1 and 7, calculate 7+1=8, Push 8Stack: [8]

Push 6Stack: [8, 6]

Push 3Stack: [8, 6, 3]

Push 2Stack: [8, 6, 3, 2]

Encounter -: Pop 2 and 3, calculate 3-2=1, Push 1Stack: [8, 6, 1]

Encounter +: Pop 1 and 6, calculate 6+1=7, Push 7Stack: [8, 7]

Encounter *: Pop 7 and 8, calculate 8*7=56, Push 56Stack: [56]

উত্তর: 56

3.  OSI model এর চারটি ধাপ লিখুন ।

**OSI Model (Open Systems Interconnection Model)** The OSI Model is a conceptual framework used to understand and standardize network communication. It divides the entire communication process into seven separate layers. Each layer has specific responsibilities and works together to ensure data is transmitted properly from one system to another over a network.

**The Seven Layers of the OSI Model:**

**1) Application Layer (Layer 7):** Provides network services directly to end users such as email (SMTP), web browsing (HTTP), and file transfer (FTP).

**2) Presentation Layer (Layer 6):** Responsible for data translation, encryption, and compression. It converts data into a format that the application layer can understand.

**3) Session Layer (Layer 5):** Establishes, manages, and terminates communication sessions between devices.

**4) Transport Layer (Layer 4):** Ensures reliable data transmission, error detection, and flow control. Protocols like TCP and UDP operate at this layer.

**5) Network Layer (Layer 3):** Handles logical addressing and routing. It determines the best path for data transmission using IP addresses.

**6) Data Link Layer (Layer 2):** Provides framing, error detection, and physical addressing (MAC address) for data transmission over the network.

**7) Physical Layer (Layer 1):** Responsible for transmitting raw bits over the physical medium such as cables, switches, and electrical signals.

In short, the OSI Model helps in understanding how data moves from one device to another through a structured layered approach.

**OSI Model (Open Systems Interconnection Model)** OSI Model হলো একটি conceptual framework যা network communication বুঝতে এবং standardize করতে ব্যবহৃত হয়। এটি পুরো communication প্রক্রিয়াকে সাতটি আলাদা layer-এ বিভক্ত করে। প্রতিটি layer-এর নির্দিষ্ট দায়িত্ব থাকে এবং সবগুলো একসাথে কাজ করে data সঠিকভাবে এক system থেকে অন্য system-এ পৌঁছায়।

**OSI Model-এর সাতটি Layer:**

**1) Application Layer (Layer 7):** End user-এর জন্য সরাসরি network service প্রদান করে, যেমন email (SMTP), web browsing (HTTP), এবং file transfer (FTP)।

**2) Presentation Layer (Layer 6):** Data translation, encryption এবং compression-এর কাজ করে। এটি data-কে এমন format-এ রূপান্তর করে যা application layer বুঝতে পারে।

**3) Session Layer (Layer 5):** Device-এর মধ্যে communication session স্থাপন, নিয়ন্ত্রণ এবং সমাপ্ত করে।

**4) Transport Layer (Layer 4):** Reliable data transmission, error detection এবং flow control নিশ্চিত করে। TCP এবং UDP এই layer-এ কাজ করে।

**5) Network Layer (Layer 3):** Logical addressing এবং routing পরিচালনা করে। IP address ব্যবহার করে data কোন পথে যাবে তা নির্ধারণ করে।

**6) Data Link Layer (Layer 2):** Framing, error detection এবং physical addressing (MAC address) প্রদান করে।

**7) Physical Layer (Layer 1):** Raw bit stream-কে physical medium (যেমন cable, switch, electrical signal) এর মাধ্যমে প্রেরণ করে।

সংক্ষেপে, OSI Model একটি structured layered পদ্ধতি যার মাধ্যমে data এক device থেকে অন্য device-এ পৌঁছায়।

4.  8086 Microprocessor এর দুটি Hardware Interrupt এবং দুটি Flag Register এর নাম লিখুন।   **Hardware Interrupts:**

- INTR (Interrupt Request)

- NMI (Non-Maskable Interrupt)

**Flag Registers:**

- Carry Flag (CF)

- Zero Flag (ZF)

5. Design the form using html.
```
<form action="#" method="post">

<label>Full Name:</label>
<input type="text" name="fullname">

<br><br>

<label>Email:</label>
<input type="email" name="email">

<br><br>

<input type="submit" value="Submit">

</form>
```

6. We have two relation Depositor and Borrower. Now write a SQL command to Find customers with an account but not a loan.
```
SELECT DISTINCT customer_name
FROM Depositor
WHERE customer_name NOT IN (
SELECT customer_name
FROM Borrower
);
```

7. library function use না করে তিনটি সংখ্যার মধ্যে দ্বিতীয় বৃহত্তম সংখ্যা নির্ণয়ের একটি জাভা প্রোগ্রাম লিখ।
```
import java.util.Scanner;

public class SecondLargest {

public static void main(String[] args) {

Scanner sc = new Scanner(System.in);

int a, b, c, second;

System.out.print("Enter first number: ");
a = sc.nextInt();

System.out.print("Enter second number: ");
b = sc.nextInt();

System.out.print("Enter third number: ");
c = sc.nextInt();

// দ্বিতীয় বৃহত্তম নির্ণয়
if ((a > b && a < c) || (a < b && a > c)) {
second = a;
}
else if ((b > a && b < c) || (b < a && b > c)) {
second = b;
}
else {
second = c;
}

System.out.println("Second largest number is: " + second);

sc.close();
}
}
```
