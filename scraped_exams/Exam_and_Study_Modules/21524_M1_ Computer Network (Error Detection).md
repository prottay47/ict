# M1: Computer Network (Error Detection)

- **Original URL:** [https://it.jobqns.com/computer-network-error-detection/](https://it.jobqns.com/computer-network-error-detection/)
- **Date:** 2026-08-21T23:10:04
- **Categories:** Uncategorized, IT Preparation Module

---

Error Detection in Data Link Layer (ET: 2.5 hours)



**Video Tutorial:**  Error Detection



- **Watch Video:**   Error Detection

- **Watch Video:**   Error Detection: Parity Bit

- **Watch Video:**   Error Detection: Checksum

- **Watch Video:**   Error Detection : CRC (Part-1)

- **Watch Video:**   Error Detection : CRC(Part-2)

- **Watch Video:**   Error Detection : CRC (Part-3)

Topic Wise Question Bank


Error Detection


- 1

Error Detection

Error Detection

Error Detection in Data Link Layer


Data Link Layer

**Error Detection**  is the process of identifying whether the data received by a receiver has been corrupted during transmission. In a computer network, data may be changed or corrupted while traveling through a communication medium. Therefore, reliable communication requires mechanisms to detect and, when necessary, correct these errors.
**Transmission Error:**  When data is transmitted from one network node to another, the data may be corrupted because of noise, interference, signal problems, or other transmission issues. The errors caused during data transmission are called  **Transmission Errors** .
**Error Control in OSI Model:**  Error control is mainly associated with the  **Data Link Layer**  and  **Transport Layer**  of the OSI model. These layers provide mechanisms for detecting and/or handling errors to support reliable data communication.
**Types of Transmission Errors**
There are mainly two types of transmission errors:

**Bit Error**
**Burst Error**

**1. Bit Error:**  A bit error occurs when only one bit of a data unit is changed during transmission. It is also called a  **Single-Bit Error** .
**Example:**
Sender sends:  **00000010**
Receiver receives:  **00001010**
Here, only one bit has changed from  **0 to 1** . Therefore, this is a  **Bit Error** .
**2. Burst Error:**  A burst error occurs when two or more bits within a data unit are affected or corrupted during transmission.
The important point is that the  **burst length**  is measured from the first corrupted bit to the last corrupted bit, including all bits between them, whether every bit in between is actually corrupted or not.
For example, if the first corrupted bit occurs at position 3 and the last corrupted bit occurs at position 10, the burst length is  **8 bits** .
**Error Detection:**  Error detection is the process by which the receiver determines whether the received data contains an error. The receiver normally does not have a copy of the original message, so additional information must be transmitted along with the original data.
To make error detection possible, the sender adds some  **extra bits**  to the original data. These extra bits are called  **Redundant Bits**  or  **Redundancy** .
**Basic Error Detection Process:**
**Original Data → Generator → Redundant Bits → Data + Redundancy → Transmission → Receiver → Checker → Accept / Reject**
At the sender side, a generating function or algorithm calculates the redundant information from the original message. The redundant bits are then appended to the original data and transmitted to the receiver.
At the receiver side, a checking function or algorithm examines the received data and calculates or verifies the redundancy. The result is compared with the expected value.
If the check indicates that the data is correct, the receiver  **accepts**  the data. If an error is detected, the receiver  **rejects or discards**  the data and may request retransmission depending on the protocol.
**Redundancy:**  Redundancy means adding extra information to the original data so that the receiver can detect or correct transmission errors.
For example, if the sender has a message, it passes the message through a generating algorithm. The algorithm produces redundant bits. These redundant bits are appended to the original message and the complete data is transmitted through the communication medium.
The receiver separates or processes the received information using a checking algorithm. If the calculated check matches the expected check, the data is considered valid. Otherwise, an error is detected.
**Error Detection vs Error Correction**
**Error Detection:**  Error detection determines whether an error has occurred in the received data. It generally results in a simple decision:  **Accept**  if the data is valid or  **Reject**  if an error is detected.
**Error Correction:**  Error correction attempts to recover the correct data after detecting an error. It is more complex than simple error detection.
There are two common approaches to error correction:

**Retransmission:**  The receiver detects an error and requests the sender to retransmit the entire data unit.
**Error-Correcting Code:**  Additional redundancy allows the receiver to identify and automatically correct certain types of errors without retransmission.

**Important:**  Both error detection and error correction require some form of redundancy because the receiver needs additional information to determine whether the received data is correct and, in some systems, to determine how to correct it.
**Error Detection Techniques**
There are four commonly discussed error detection techniques in data communication:

**Vertical Redundancy Check (VRC)**
**Longitudinal Redundancy Check (LRC)**
**Checksum**
**Cyclic Redundancy Check (CRC)**

**1. Vertical Redundancy Check (VRC):**  VRC is an error detection technique that adds an additional parity bit to a group of data bits. The parity bit is used to make the number of 1s either even or odd, depending on the selected parity scheme. VRC is commonly known as the  **Parity Check** .
**2. Longitudinal Redundancy Check (LRC):**  LRC organizes data into rows and columns and adds redundancy based on the bits in each column. It can detect certain errors that may not be detected by a simple parity check.
**3. Checksum:**  In the checksum technique, the sender divides the data into fixed-size units and performs arithmetic operations on those units to generate a checksum value. The checksum is transmitted along with the data. The receiver performs a similar calculation and compares the result to determine whether an error has occurred.
**4. Cyclic Redundancy Check (CRC):**  CRC is a powerful error detection technique based on binary polynomial division. The sender performs a calculation using a predefined generator polynomial and appends the resulting remainder to the data. The receiver performs a similar calculation to determine whether the received data has been corrupted.
**CRC and Checksum**  are widely used error detection mechanisms in computer networks and communication protocols. CRC is particularly effective at detecting burst errors.

**Error Detection**  হলো এমন একটি প্রক্রিয়া যার মাধ্যমে Receiver নির্ণয় করে যে Transmission-এর সময় প্রাপ্ত Data Corrupted হয়েছে কি না। Computer Network-এ Communication Medium-এর মধ্য দিয়ে Data যাওয়ার সময় Noise, Interference, Signal Problem বা অন্যান্য Transmission সমস্যার কারণে Data পরিবর্তিত বা Corrupted হতে পারে। তাই Reliable Communication-এর জন্য Error Detect এবং প্রয়োজন হলে Error Correct করার ব্যবস্থা প্রয়োজন।
**Transmission Error:**  যখন Data একটি Network Node থেকে অন্য Network Node-এ পাঠানো হয়, তখন Noise, Interference, Signal Problem বা অন্যান্য Transmission সমস্যার কারণে Data Corrupted হতে পারে। Data Transmission-এর সময় সৃষ্ট এই ধরনের Error-কে  **Transmission Error**  বলা হয়।
**Error Control in OSI Model:**  OSI Model-এর  **Data Link Layer**  এবং  **Transport Layer** -এর সঙ্গে Error Control প্রধানত সম্পর্কিত। এই Layer-গুলো Reliable Data Communication নিশ্চিত করার জন্য Error Detection এবং প্রয়োজন অনুযায়ী Error Handling-এর ব্যবস্থা প্রদান করে।
**Types of Transmission Errors**
Transmission Error প্রধানত দুই ধরনের:
**১. Bit Error**   **২. Burst Error**
**১. Bit Error:**  Transmission-এর সময় কোনো Data Unit-এর মাত্র একটি Bit পরিবর্তিত হলে তাকে  **Bit Error**  বলা হয়। একে  **Single-Bit Error** -ও বলা হয়।
**Example:**  Sender sends:  **00000010**  Receiver receives:  **00001010**  এখানে শুধুমাত্র একটি Bit  **0 থেকে 1**  পরিবর্তিত হয়েছে। তাই এটি একটি  **Bit Error** ।
**২. Burst Error:**  Transmission-এর সময় কোনো Data Unit-এর মধ্যে দুই বা ততোধিক Bit প্রভাবিত বা Corrupted হলে তাকে  **Burst Error**  বলা হয়।
**Burst Length**  প্রথম Corrupted Bit থেকে শেষ Corrupted Bit পর্যন্ত গণনা করা হয়। মাঝখানের প্রতিটি Bit Corrupted না হলেও সেগুলো Burst Length-এর মধ্যে গণনা করা হয়।
উদাহরণস্বরূপ, যদি প্রথম Corrupted Bit-এর অবস্থান  **3**  এবং শেষ Corrupted Bit-এর অবস্থান  **10**  হয়, তাহলে Burst Length হবে  **8 bits** ।
**Error Detection:**  Error Detection হলো এমন একটি প্রক্রিয়া যার মাধ্যমে Receiver নির্ণয় করে যে প্রাপ্ত Data-তে কোনো Error রয়েছে কি না। সাধারণত Receiver-এর কাছে Original Message-এর একটি Copy থাকে না। তাই Error শনাক্ত করার জন্য Original Data-এর সঙ্গে অতিরিক্ত কিছু Information পাঠাতে হয়।
Error Detection সম্ভব করার জন্য Sender Original Data-এর সঙ্গে কিছু  **Extra Bits**  যুক্ত করে। এই Extra Bits-কে  **Redundant Bits**  বা  **Redundancy**  বলা হয়।
**Basic Error Detection Process:**   **Original Data → Generator → Redundant Bits → Data + Redundancy → Transmission → Receiver → Checker → Accept / Reject**
Sender Side-এ একটি Generating Function বা Algorithm Original Message থেকে Redundant Information তৈরি করে। এরপর Redundant Bits-কে Original Data-এর সঙ্গে যুক্ত করে Receiver-এর কাছে পাঠানো হয়।
Receiver Side-এ একটি Checking Function বা Algorithm প্রাপ্ত Data পরীক্ষা করে এবং Redundancy Calculate বা Verify করে। এরপর প্রাপ্ত Result-কে Expected Value-এর সঙ্গে Compare করা হয়।
যদি Check থেকে বোঝা যায় যে Data সঠিক, তাহলে Receiver Data  **Accept**  করে। যদি Error শনাক্ত হয়, তাহলে Receiver Data  **Reject বা Discard**  করতে পারে এবং Protocol অনুযায়ী Retransmission-এর জন্য Request করতে পারে।
**Redundancy:**  Redundancy বলতে Original Data-এর সঙ্গে অতিরিক্ত Information যুক্ত করাকে বোঝায়, যাতে Receiver Transmission Error Detect বা Correct করতে পারে।
উদাহরণস্বরূপ, Sender-এর কাছে একটি Message থাকলে সেটিকে একটি Generating Algorithm-এর মাধ্যমে Process করা হয়। Algorithm থেকে Redundant Bits তৈরি হয়। এরপর এই Redundant Bits Original Message-এর সঙ্গে যুক্ত করে সম্পূর্ণ Data Communication Medium-এর মাধ্যমে পাঠানো হয়।
Receiver প্রাপ্ত Information-কে একটি Checking Algorithm-এর মাধ্যমে Process করে। Calculated Check যদি Expected Check-এর সঙ্গে মিলে যায়, তাহলে Data Valid হিসেবে বিবেচিত হয়। অন্যথায় Error শনাক্ত হয়।
**Error Detection vs Error Correction**
**Error Detection:**  Error Detection নির্ণয় করে যে Received Data-তে কোনো Error ঘটেছে কি না। সাধারণত এর ফলাফল দুটি সিদ্ধান্তের মাধ্যমে প্রকাশ করা হয়: Data সঠিক হলে  **Accept**  এবং Error শনাক্ত হলে  **Reject** ।
**Error Correction:**  Error Correction হলো Error শনাক্ত হওয়ার পর সঠিক Data পুনরুদ্ধার করার প্রক্রিয়া। এটি সাধারণ Error Detection-এর তুলনায় বেশি Complex।
**Error Correction-এর দুটি সাধারণ পদ্ধতি:**
**১. Retransmission:**  Receiver Error শনাক্ত করে এবং Sender-এর কাছে সম্পূর্ণ Data Unit পুনরায় পাঠানোর জন্য Request করে।
**২. Error-Correcting Code:**  অতিরিক্ত Redundancy ব্যবহার করে Receiver নির্দিষ্ট ধরনের Error শনাক্ত এবং স্বয়ংক্রিয়ভাবে Correct করতে পারে, ফলে Retransmission-এর প্রয়োজন হয় না।
**Important:**  Error Detection এবং Error Correction উভয়ের জন্যই কোনো না কোনো ধরনের  **Redundancy**  প্রয়োজন। কারণ Received Data সঠিক কি না এবং কিছু ক্ষেত্রে Error কীভাবে Correct করতে হবে তা নির্ণয়ের জন্য Receiver-এর অতিরিক্ত Information প্রয়োজন হয়।
**Error Detection Techniques**
Data Communication-এ সাধারণত চারটি Error Detection Technique বেশি আলোচনা করা হয়:
**১. Vertical Redundancy Check (VRC)**   **২. Longitudinal Redundancy Check (LRC)**   **৩. Checksum**   **৪. Cyclic Redundancy Check (CRC)**
**১. Vertical Redundancy Check (VRC):**  VRC হলো একটি Error Detection Technique যেখানে Data Bits-এর একটি Group-এর সঙ্গে একটি অতিরিক্ত  **Parity Bit**  যুক্ত করা হয়। নির্বাচিত Parity Scheme অনুযায়ী এই Parity Bit এমনভাবে নির্ধারণ করা হয় যাতে 1-এর সংখ্যা  **Even**  অথবা  **Odd**  হয়। VRC-কে সাধারণভাবে  **Parity Check**  বলা হয়।
**২. Longitudinal Redundancy Check (LRC):**  LRC-তে Data-কে বিভিন্ন Row এবং Column-এ সাজানো হয় এবং প্রতিটি Column-এর Bits-এর ওপর ভিত্তি করে Redundancy যুক্ত করা হয়। এটি এমন কিছু Error শনাক্ত করতে পারে যা সাধারণ Parity Check দ্বারা শনাক্ত নাও হতে পারে।
**৩. Checksum:**  Checksum Technique-এ Sender Data-কে নির্দিষ্ট আকারের কয়েকটি Unit-এ ভাগ করে সেই Unit-গুলোর ওপর Arithmetic Operation সম্পন্ন করে একটি Checksum Value তৈরি করে। Checksum-কে Data-এর সঙ্গে Receiver-এর কাছে পাঠানো হয়। Receiver একই ধরনের Calculation করে Result Compare করে এবং Error হয়েছে কি না তা নির্ণয় করে।
**৪. Cyclic Redundancy Check (CRC):**  CRC হলো একটি শক্তিশালী Error Detection Technique, যা  **Binary Polynomial Division** -এর ওপর ভিত্তি করে কাজ করে। Sender একটি নির্ধারিত  **Generator Polynomial**  ব্যবহার করে Calculation সম্পন্ন করে এবং প্রাপ্ত Remainder-কে Data-এর সঙ্গে যুক্ত করে। Receiver একই ধরনের Calculation করে Received Data Corrupted হয়েছে কি না তা নির্ণয় করে।
**CRC and Checksum**  Computer Network এবং বিভিন্ন Communication Protocol-এ বহুল ব্যবহৃত Error Detection Mechanism। বিশেষ করে  **CRC**  বিভিন্ন ধরনের  **Burst Error**  শনাক্ত করার ক্ষেত্রে অত্যন্ত কার্যকর।

- 2

Error Detection

Parity

Explain Parity Bit. How error is detected by Parity Biit?


Data Link Layer

**Parity Bit:**  A parity bit is an additional bit added to a data sequence to detect errors during data transmission. It is the simplest type of error-detecting code.

There are two types of parity:  **Even Parity**  and  **Odd Parity** .
**Even Parity:**  The parity bit is selected so that the total number of 1s in the transmitted code, including the parity bit, becomes even.
**Example:**
Data = 10101
Number of 1s = 3 (odd)
Therefore, parity bit = 1
Transmitted code =  **101011**
Total number of 1s = 4 (even)
**Odd Parity:**  The parity bit is selected so that the total number of 1s in the transmitted code, including the parity bit, becomes odd.
**Example:**
Data = 10101
Number of 1s = 3 (odd)
Therefore, parity bit = 0
Transmitted code =  **101010**
Total number of 1s = 3 (odd)
**Error Detection:**  At the receiver side, a parity checker checks the number of 1s in the received code. If the required parity is not maintained, an error is detected.
**Example:**  Suppose even parity is used and the transmitted code is  **101011** . If one bit changes during transmission and the receiver gets  **101001** , the number of 1s becomes 3, which is odd. Therefore, the receiver detects an error.
**Important Points:**
• Parity can detect  **odd numbers of bit errors** .
• Parity cannot detect an  **even number of bit errors** .
• A parity bit can detect an error, but it  **cannot identify the exact location**  of the error.
• Therefore, a simple parity bit  **cannot correct**  the error.

**Parity Bit:**  ডেটা ট্রান্সমিশনের সময় error শনাক্ত করার জন্য মূল ডেটার সাথে একটি অতিরিক্ত bit যোগ করা হয়, যাকে  **Parity Bit**  বলে। এটি একটি সহজ ধরনের error-detecting code.
Parity দুই ধরনের:  **Even Parity**  এবং  **Odd Parity** ।
**Even Parity:**  Parity bit এমনভাবে নির্ধারণ করা হয় যাতে parity bit-সহ সম্পূর্ণ code-এ মোট 1-এর সংখ্যা  **জোড়**  হয়।
**উদাহরণ:**  Data = 10101 1-এর সংখ্যা = 3 (বিজোড়) তাই parity bit = 1 Transmitted code =  **101011**  মোট 1-এর সংখ্যা = 4 (জোড়)
**Odd Parity:**  Parity bit এমনভাবে নির্ধারণ করা হয় যাতে parity bit-সহ সম্পূর্ণ code-এ মোট 1-এর সংখ্যা  **বিজোড়**  হয়।
**উদাহরণ:**  Data = 10101 1-এর সংখ্যা = 3 (বিজোড়) তাই parity bit = 0 Transmitted code =  **101010**  মোট 1-এর সংখ্যা = 3 (বিজোড়)
**Error Detection:**  Receiver-এর parity checker প্রাপ্ত code-এ 1-এর সংখ্যা গণনা করে। নির্ধারিত parity বজায় না থাকলে receiver error শনাক্ত করতে পারে।
**উদাহরণ:**  ধরা যাক, Even Parity ব্যবহার করা হয়েছে এবং transmitted code হলো  **101011** । Transmission-এর সময় একটি bit পরিবর্তিত হয়ে receiver  **101001**  পেল। এখানে 1-এর সংখ্যা 3, অর্থাৎ বিজোড়। তাই receiver বুঝতে পারে যে একটি error হয়েছে।
**গুরুত্বপূর্ণ বিষয়:**  • Parity দ্বারা  **বিজোড় সংখ্যক bit error**  শনাক্ত করা যায়। •  **জোড় সংখ্যক bit error**  শনাক্ত করা যায় না। • Parity bit error শনাক্ত করতে পারে, কিন্তু error-এর  **সঠিক অবস্থান নির্ণয়**  করতে পারে না। • তাই simple parity bit দিয়ে error  **correct**  করা যায় না।

- 3

Error Detection

Checksum

Error Detection Technique : Checksum


Data Link Layer

**What is Checksum?**
Checksum is an  **Error Detection Technique**  used in computer networks to detect whether data has been corrupted during transmission. At the sender side, the original data is divided into fixed-size blocks, the blocks are added together, and the  **One's Complement**  of the final sum is calculated as the checksum. The checksum is then appended to the original data and transmitted to the receiver.
**How Checksum Works:**

**Divide the Data:**  Divide the original message into equal-sized blocks of  **n bits** .
**Add the Blocks:**  Add all the blocks using binary addition.
**Wrap the Carry:**  If an extra carry is produced, add that carry back to the least significant bit of the result. This is called  **End-Around Carry** .
**Find One's Complement:**  Invert every bit of the final sum. 0 becomes 1 and 1 becomes 0.
**Generate Checksum:**  The resulting value is the checksum.
**Append and Transmit:**  Append the checksum to the original data and send the complete information to the receiver.
**Receiver Verification:**  The receiver adds all received data blocks, including the checksum, using the same carry wrap-around method.
**Accept or Reject:**  If the final result contains all  **1s** , the data is considered error-free and accepted. Otherwise, an error is detected and the data is rejected.

**Checksum কী?**
**Checksum**  হলো একটি  **Error Detection Technique** , যা Computer Network-এ Data Transmission-এর সময় Data-এর কোনো অংশ Corrupted বা পরিবর্তিত হয়েছে কি না তা শনাক্ত করতে ব্যবহৃত হয়। Sender Side-এ মূল Data-কে নির্দিষ্ট আকারের কয়েকটি Block-এ ভাগ করা হয়। এরপর Block-গুলো Binary Addition-এর মাধ্যমে যোগ করা হয় এবং সর্বশেষ Sum-এর  **One's Complement**  নির্ণয় করা হয়। এই One's Complement-ই হলো  **Checksum** । এরপর Checksum-কে Original Data-এর সঙ্গে যুক্ত করে Receiver-এর কাছে পাঠানো হয়।
**Checksum কীভাবে কাজ করে:**
**১. Divide the Data:**
Original Message-কে সমান আকারের  **n bits** -এর কয়েকটি Block-এ ভাগ করা হয়।
**২. Add the Blocks:**
সবগুলো Data Block-কে  **Binary Addition**  পদ্ধতিতে যোগ করা হয়।
**৩. Wrap the Carry:**
Addition-এর ফলে অতিরিক্ত Carry তৈরি হলে সেই Carry-কে আবার Result-এর Least Significant Bit-এর সঙ্গে যোগ করা হয়। এই পদ্ধতিকে  **End-Around Carry**  বলা হয়।
**৪. Find One's Complement:**
Final Sum-এর প্রতিটি Bit-এর Complement নির্ণয় করা হয়। অর্থাৎ  **0 হলে 1**  এবং  **1 হলে 0**  করা হয়।
**৫. Generate Checksum:**
One's Complement থেকে পাওয়া Result-ই হলো  **Checksum** ।
**৬. Append and Transmit:**
Checksum-কে Original Data-এর সঙ্গে যুক্ত করে সম্পূর্ণ Data Receiver-এর কাছে পাঠানো হয়।
**৭. Receiver Verification:**
Receiver প্রাপ্ত সব Data Block এবং Checksum-কে একই  **Binary Addition**  পদ্ধতিতে যোগ করে এবং অতিরিক্ত Carry থাকলে  **End-Around Carry**  পদ্ধতিতে তা আবার যোগ করে।
**৮. Accept or Reject:**
Final Result-এ যদি সবগুলো Bit  **1**  হয়, তাহলে Data-কে সাধারণভাবে  **Error-Free**  হিসেবে গ্রহণ করা হয়। অন্যথায় Error শনাক্ত হয় এবং Data Reject করা হয়।

4

Error Detection

Checksum

Example & Performance of Checksum


Data Link Layer

**Example:**  Suppose the original data is:
**10011001111000100010010010000100**
Assume the data is divided into four  **8-bit blocks** :

**10011001**
**11100010**
**00100100**
**10000100**

**Step 1 — Add the Blocks:**

```
10011001
11100010
00100100
10000100
-----------------
00100011
+     10
---------------
00100101
```

The resulting 8-bit sum is:  **00100101**
**Step 2 — One's Complement** (invert) **: 00100101→ 11011010 (** It is Checksum **)**
**Step 3 — Transmitted Data:**
The sender appends the checksum to the original data:  **1101101010011001111000100010010010000100**
**Step 4 — Receiver Verification:**
The receiver adds all four data blocks and the received checksum. If the final result is:  **11111111**
then the receiver assumes that no transmission error has been detected and accepts the data. otherwise rejected.

**Performance of Checksum**

Simple and easy to implement.
Requires relatively little computational overhead.
Can detect many single-bit, multiple-bit, and burst errors.
Widely used in network and communication protocols.

**Limitation:**  Checksum cannot detect every possible error. If certain bit errors occur in such a way that their effects cancel each other during the addition, the final checksum may remain unchanged and the error can go undetected.

- 5

Error Detection

CRC

CRC and Step of CRC


Data Link Layer

CRC (Cyclic Redundancy Check) is an error-detection technique used in the Data Link Layer to detect whether data has been corrupted during transmission.Steps of CRC Process
Choose a Generator Polynomial — Sender and receiver agree on a binary divisor called the Generator.  **Append Zeros**  — Add n-1 zeros to the original data, where n is the number of bits in the generator.  **Binary Division**  — Divide the resulting bit sequence by the generator using XOR division.  **Find Remainder**  — The remainder obtained from the division is called the CRC.  **Create Codeword —**  Append the CRC remainder to the original data.  **Transmit**  — Send the resulting data + CRC to the receiver.
**Receiver Checks**  — Receiver divides the received codeword by the same generator.    Check Remainder:        Remainder = 0 → No error detected.        Remainder ≠ 0 → Error detected. **Shortcut:** Data → Append Zeros → XOR Division → CRC Remainder → Append CRC → Transmit → Divide → Check Remainder

**CRC (Cyclic Redundancy Check)**  হলো একটি  **Error Detection Technique** , যা  **Data Link Layer** -এ Data Transmission-এর সময় Data Corrupted হয়েছে কি না তা শনাক্ত করতে ব্যবহৃত হয়। **CRC Process-এর ধাপসমূহ**   **১. Choose a Generator Polynomial**  — Sender এবং Receiver একটি Binary Divisor-এর বিষয়ে সম্মত থাকে, যাকে  **Generator**  বলা হয়।  **২. Append Zeros**  — Original Data-এর শেষে  **n-1** টি Zero যোগ করা হয়, যেখানে  **n**  হলো Generator-এর Bit সংখ্যা।  **৩. Binary Division**  — Zero যুক্ত Bit Sequence-কে Generator দিয়ে  **XOR Division**  করা হয়।  **৪. Find Remainder**  — Division-এর মাধ্যমে প্রাপ্ত Remainder-কে  **CRC**  বলা হয়।  **৫. Create Codeword**  — CRC Remainder-কে Original Data-এর শেষে যুক্ত করা হয়।  **৬. Transmit**  — Data + CRC Receiver-এর কাছে পাঠানো হয়।
**Receiver Checks**  — Receiver একই Generator ব্যবহার করে প্রাপ্ত Codeword-কে Divide করে।  **Check Remainder:**  Remainder = 0 → No error detected. Remainder ≠ 0 → Error detected.

6

Error Detection

CRC

Find the CRC for the data blocks 100100 with the divisor 1101?


Data Link Layer

7

Error Detection

CRC

Receiver received data 100100001 and the divisor is 1101 , Check the received Data will be accepted or not.


Data Link Layer

8

Error Detection

CRC

The message 11001001 is to be transmitted using CRC polynomial x3+1 to protect it from errors. Find the message that should be transmitted.


Data Link Layer

Error Detection and Correction Code Example ( Hamming Code)

- **Watch Video:**   Error Detection and Correction Code : Hamming Code (Part 1)

- **Watch Video:**   Error Detection and Correction Code : Hamming Code (Part 2)

**Hamming Code Error Detection and Correction**

**1. Finding the Number of Redundant Bits (r)**

**Given Data (m):**  1011 → Length of data, $m = 4$

Formula:  **2r ≥ m + r + 1**

For r = 1: 21 ≥ 4 + 1 + 1 ⇒ 2 ≥ 6 (False)

For r = 2: 22 ≥ 4 + 2 + 1 ⇒ 4 ≥ 7 (False)

For r = 3: 23 ≥ 4 + 3 + 1 ⇒ 8 ≥ 8 (True)


**Selected r = 3** . Total bits = $m + r = 4 + 3 = 7$ bits.

**2. Bit Positions and Parity Bit Calculation (Even Parity)**

Place parity bits at positions that are powers of 2 (1, 2, 4):

7
6
5
4
3
2
1

1
0
1
R3
1
R2
R1

### Binary Position Table

Position
R3 (4)
R2 (2)
R1 (1)

0000
1 (R1)001
2 (R2)010
3011
4 (R3)100
5101
6110
7111

### Parity Bit Values

**Bit Coverages:**

- **R1**  covers positions (1, 3, 5, 7)

- **R2**  covers positions (2, 3, 6, 7)

- **R3**  covers positions (4, 5, 6, 7)

**Even Parity Calculation:**

R1 → (R1, Bit3, Bit5, Bit7) → (R1, 1, 1, 1) ⇒  **R1 = 1**  (to make count of 1s even)

R2 → (R2, Bit3, Bit6, Bit7) → (R2, 1, 0, 1) ⇒  **R2 = 0**  (already even)

R3 → (R3, Bit5, Bit6, Bit7) → (R3, 1, 0, 1) ⇒  **R3 = 0**  (already even)

### Final Transmitted Hamming Code:

7
6
5
4
3
2
1

1
0
1
0
1
0
1

**Transmitted Data: 1010101**

**3. Error Detection on Received Data**

**Received Data:**  1110101

7
6
5
4
3
2
1

1
1
1
0
1
0
1

### Even Parity Check:

**P1**  (Positions 1, 3, 5, 7) → bits (1, 1, 1, 1) → Total 1s = 4 (Even) ⇒  **0**

**P2**  (Positions 2, 3, 6, 7) → bits (0, 1, 1, 1) → Total 1s = 3 (Odd) ⇒  **1**

**P3**  (Positions 4, 5, 6, 7) → bits (0, 1, 1, 1) → Total 1s = 3 (Odd) ⇒  **1**

### Error Location Calculation:

Syndrome Bits:  **(P3, P2, P1) = (1, 1, 0)2**

Binary (110)2 = 1 × 22 + 1 × 21 + 0 × 20 = 4 + 2 + 0 =  **6**

**Conclusion: Yes, there is an error! The error is located at Bit Position 6.**

Correcting bit position 6 from 1 to 0 restores the original data:  **1010101** .





**Previous Job Question:**  Error Detection



Topic Wise Question Bank

All Topics

- ☆

1

Computer Network
Error Detection

Explain the logic of a "Checksum". How is it used to verify data integrity during file transfer?

Combined Bank, AP-22, 26
| Assistant Programmer

**Logic of a Checksum**
A checksum is a small, fixed-size value calculated from a block of data using a mathematical algorithm. It represents a summary of the data and is used to detect errors that may occur during data transmission or storage.
**How a Checksum Works**

1) The sender divides the data into fixed-size blocks (such as bytes or words).
2) These blocks are added together (or processed using a checksum algorithm).
3) The final result is the checksum value, which is sent along with the data.

**Verification During File Transfer**

• The receiver recalculates the checksum from the received data using the same algorithm.
• The newly calculated checksum is compared with the checksum sent by the sender.
• If both values match, the data is assumed to be intact.
• If they do not match, it indicates that the data was corrupted during transmission.

**Purpose**
Checksums provide a simple and fast way to ensure  **data integrity** , helping detect transmission errors in file transfers.

**Checksum এর Logic**
Checksum হলো একটি ছোট, নির্দিষ্ট আকারের value যা একটি data block থেকে গাণিতিকভাবে হিসাব করা হয়। এটি data এর একটি summary হিসেবে কাজ করে এবং data transmission বা storage এর সময় কোনো error হয়েছে কিনা তা শনাক্ত করতে ব্যবহৃত হয়।
**Checksum কীভাবে কাজ করে**

1) Sender data কে ছোট ছোট block এ ভাগ করে।
2) প্রতিটি block যোগ করে (বা checksum algorithm ব্যবহার করে) একটি মান বের করা হয়।
3) এই মানটিই checksum, যা data এর সাথে পাঠানো হয়।

**File Transfer এ Verification**

• Receiver প্রাপ্ত data থেকে একই algorithm ব্যবহার করে checksum পুনরায় গণনা করে।
• Sender পাঠানো checksum এর সাথে receiver এর checksum তুলনা করা হয়।
• দুইটি মান মিললে data ঠিক আছে ধরা হয়।
• মিল না হলে বোঝা যায় data transmission এর সময় corrupted হয়েছে।

**উদ্দেশ্য**
Checksum দ্রুত এবং সহজভাবে  **data integrity**  নিশ্চিত করতে সাহায্য করে এবং file transfer এর সময় error শনাক্ত করে।

☆

2

Data Communication
Error Detection

CRC is a redundancy error technique used to determine the error. Suppose the original data is 11100 and divisor is 1001

CB, AP, 23
| Assistant Programmer

Solution: **Step 1: Represent Data and Divisor in Polynomial Form**
**Data (11100):**

```
x4 + x3 + x2
```

**Divisor (1001):**

```
x3 + 1
```

**Step 2: Append Zeros to the Original Data**
Since the divisor is 4 bits, we append 3 zeros to the original data (one less than the number of bits in the divisor). The new data is:
**Data after appending zeros:**
```
11100000
```

**Step 3: Perform Binary Division**
Now we divide the modified data  **11100000**  by the divisor  **1001** .
Division Process:

```
11111                  ← Quotient
-----------------------------
11100000             ← Dividend (data with zeros)
1001                 ← Divisor
----------------------
1110000
1001
----------------
111000
1001
---------------
11100
1001
------------
1110
1001
------------
111
```

**Step 4: Determine the Transmitted Value**
The remainder  **111**  is the CRC code. To get the transmitted value, append the remainder to the original data:
**Original data:**
```
11100
```

**Remainder:**
```
111
```

**Transmitted Value:**
```
11100111
```

☆

3

Data Communication
Error Detection

Explain parity method for error detection. Write down the bit strings of "Delta" using ASCII.

BB, AME, 23
| AME/ANE/AE

**Parity Bit and Error Detection**
During data transmission, electrical noise may change the logic level of a signal, causing errors. To detect such errors, a  **parity bit**  (an extra bit 0 or 1) is added to the original data.
**Even Parity Method:**  The sender counts the number of 1s in the data. If the count is odd, the parity bit is set to 1 to make the total number of 1s even. If the count is already even, the parity bit is set to 0. The receiver again counts the number of 1s (including the parity bit). If the total is even, the data is assumed correct; otherwise, an error is detected.
**Example:**  Suppose the data  **1101**  is transmitted with parity bit  **1** . If due to noise the receiver gets  **1111** , the total number of 1s becomes odd. Hence, the receiver detects an error and may request retransmission.
**ASCII Code for “Delta”**

Character
Decimal ASCII
8-bit Binary

D
68
01000100

e
101
01100101

l
108
01101100

t
116
01110100

a
97
01100001

The complete binary bit stream for  **“Delta”**  is:
01000100 01100101 01101100 01110100 01100001

**Parity Bit এবং Error Detection**
Data transmission-এর সময় electrical noise signal-এর logic level পরিবর্তন করতে পারে, ফলে error তৈরি হয়। এই error শনাক্ত করার জন্য মূল data-এর সাথে একটি অতিরিক্ত bit যোগ করা হয়, যাকে  **parity bit**  বলা হয়।
**Even Parity পদ্ধতি:**  Sender data-এর মধ্যে কতগুলো 1 আছে তা গণনা করে। যদি 1-এর সংখ্যা odd হয়, তাহলে parity bit = 1 দেওয়া হয় যাতে মোট সংখ্যা even হয়। Receiver আবার parity bit সহ 1-এর সংখ্যা গণনা করে। যদি মোট সংখ্যা even হয়, data সঠিক ধরা হয়; নাহলে error ধরা পড়ে।
**উদাহরণ:**  ধরা যাক  **1101**  data parity bit  **1**  সহ পাঠানো হলো। Noise-এর কারণে receiver যদি  **1111**  পায়, তাহলে মোট 1-এর সংখ্যা odd হবে। তাই receiver বুঝবে যে error হয়েছে।
**“Delta” শব্দের ASCII Code**

Character
Decimal ASCII
8-bit Binary

D
68
01000100

e
101
01100101

l
108
01101100

t
116
01110100

a
97
01100001

**“Delta”** -এর সম্পূর্ণ binary bit string হলো:
01000100 01100101 01101100 01110100 01100001



**Assigment:**  Error Detection



- Briefly explain Error Detection Technique in Data Link Layer . (Key Point)
- Find the CRC for 1110010101 with the divisor x3+x2+1?
- Suppose we want to transmit the message 11001001 and protect it from errors using the CRC polynomial x3+1. Use polynomial long division to determine the message that should be transmitted. Corrupt the left-most third bit of the transmitted message and show that the error is detected by the receiver using CRC technique.
- Suppose the sender wants to transmit 4 frames of 8 bits each: 11001100, 10101010, 11110000, and 11000011. Find the Checksum,and also Verify if Receiver1 Received Data as :1100110010101010111100001100001111010011Is received data is error free or not? Explain your Answer.

📘 Error Control

#### 1. Which layer of the OSI model is mainly responsible for error control at the frame level?

#### 2. Which of the following is a type of transmission error?

#### 3. Which error occurs when only one bit of a data unit is changed?

#### 4. What is a burst error?

#### 5. If the first corrupted bit is at position 3 and the last corrupted bit is at position 10, what is the burst length?

#### 6. What is the main purpose of error detection?

#### 7. What are the extra bits added to data for error detection called?

#### 8. Which of the following is NOT an error-detection technique?

#### 9. What does VRC stand for?

#### 10. VRC is commonly known as what?

#### 11. What does a parity bit do?

#### 12. In even parity, the total number of 1s including the parity bit should be:

#### 13. In odd parity, the total number of 1s including the parity bit should be:

#### 14. Data = 10101. Using even parity, what is the parity bit?

#### 15. Data = 10101. Using odd parity, what is the parity bit?

#### 16. If even parity is used and the received code contains an odd number of 1s, what does the receiver conclude?

#### 17. Parity checking can reliably detect:

#### 18. Simple parity checking cannot detect:

#### 19. Can a simple parity bit identify the exact position of an error?

#### 20. Can a simple parity bit correct an error?

#### 21. What does LRC stand for?

#### 22. LRC organizes data mainly into:

#### 23. What is the main idea behind a checksum?

#### 24. In the checksum method, data is divided into:

#### 25. Which operation is commonly used to generate the checksum from the final sum?

#### 26. What is an end-around carry in checksum calculation?

#### 27. During receiver verification of a checksum, what result indicates error-free data?

#### 28. If the checksum verification result is not all 1s, the receiver should conclude that:

#### 29. Which error-detection technique uses binary polynomial division?

#### 30. What does CRC stand for?

#### 31. In CRC, what is the binary divisor called?

#### 32. If the generator has n bits, how many zeros are appended to the original data before CRC division?

#### 33. What operation is primarily used in CRC binary division?

#### 34. What is the remainder obtained from CRC division called?

#### 35. After calculating the CRC remainder, what is appended to the original data?

#### 36. At the receiver, the received codeword is divided by:

#### 37. In CRC, a remainder of zero at the receiver generally means:

#### 38. In CRC, a non-zero remainder at the receiver means:

#### 39. Find the CRC for data 100100 using divisor 1101. How many zeros should be appended before division?

#### 40. For data 100100 and divisor 1101, the data before CRC division becomes:

#### 41. Data 11100 is to be transmitted using CRC with divisor 1001. How many zeros are appended?

#### 42. For data 11100 and divisor 1001, the dividend used for CRC division is:

#### 43. For data 11100 with divisor 1001, if the CRC remainder is 111, what is the transmitted codeword?

#### 44. Which error-detection technique is particularly effective for detecting burst errors?

#### 45. What is the main difference between error detection and error correction?

#### 46. Which of the following is a method of error correction through retransmission?

#### 47. Which statement about redundancy is correct?

#### 48. Which sequence correctly represents the basic error-detection process?
