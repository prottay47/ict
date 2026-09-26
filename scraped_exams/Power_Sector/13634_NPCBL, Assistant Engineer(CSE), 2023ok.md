# NPCBL, Assistant Engineer(CSE), 2023ok

- **Original URL:** [https://it.jobqns.com/npcbl-assistant-engineercse-2023/](https://it.jobqns.com/npcbl-assistant-engineercse-2023/)
- **Date:** 2026-03-07T16:45:45
- **Categories:** Job Solution 2023, Power Sector IT Job Solution 2023

---

#### Nuclear Powerplant Company Bangladesh Limited(NPCBL)
Post: Assistant Engineer (CSE), Exam Date: 26-05-2023



1. Write a program find prime number between 1 to 100.
```
#include <iostream>
using namespace std;

int main() {
cout << "Prime numbers between 1 and 100 are:" << endl;

for (int num = 2; num <= 100; num++) {
bool isPrime = true;

for (int divisor = 2; divisor * divisor <= num; divisor++) {
if (num % divisor == 0) {
isPrime = false;
break;
}
}
if (isPrime) {
cout << num << " ";
}
}
cout << endl;
return 0;
}
```

**Output:**

Prime numbers between 1 and 100 are:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97

2. What is Symmetric and Asymmetric Encryption? Explain with example.

**Symmetric Encryption**

- Uses the  **same key**  for both encryption and decryption.
- Faster and efficient for large data processing.
- **Example:**  Sender encrypts data with a secret key and receiver uses the same key to decrypt.
- **Algorithms:**  AES, DES, Triple DES.

**Asymmetric Encryption**

- Uses  **two keys** : public key (encryption) and private key (decryption).
- More secure for communication but slower than symmetric encryption.
- **Example:**  Sender encrypts using receiver’s public key, and only receiver can decrypt using private key.
- **Algorithms:**  RSA, ECC, Diffie-Hellman.

**Symmetric Encryption**

- একই  **key**  encryption এবং decryption উভয়ের জন্য ব্যবহৃত হয়।
- বড় data encrypt করার জন্য দ্রুত এবং efficient।
- **Example:**  Sender একটি secret key দিয়ে data encrypt করে এবং receiver একই key দিয়ে decrypt করে।
- **Algorithms:**  AES, DES, Triple DES।

**Asymmetric Encryption**

- দুটি  **key**  ব্যবহার করে: public key (encryption) এবং private key (decryption)।
- Communication-এর জন্য বেশি secure কিন্তু symmetric-এর তুলনায় ধীর।
- **Example:**  Sender receiver-এর public key দিয়ে data encrypt করে এবং receiver private key দিয়ে decrypt করে।
- **Algorithms:**  RSA, ECC, Diffie-Hellman।

3. What is SDLC? Briefly explain its phase.

**SDLC**  is a structured process used to develop, maintain, and improve software in a systematic and efficient way

**Phases of SDLC**

- **Planning & Requirement Analysis:**  Collect and analyze requirements, check feasibility, identify risks.

- **Defining Requirements:**  Requirements are documented in  **SRS (Software Requirement Specification)** .

- **Designing:**  System design is prepared using  **DDS (Design Document Specification)** .

- **Development:**  Coding is done using programming languages like C++, Java, Python.

- **Testing:**  Software is tested to find and fix errors and ensure quality.

- **Deployment & Maintenance:**  Software is released and later maintained with updates and bug fixes.

**SDLC**  হলো একটি structured process যা software develop, maintain এবং improve করার জন্য ব্যবহৃত হয়।

**SDLC-এর ধাপসমূহ**

- **Planning & Requirement Analysis:**  Requirement সংগ্রহ ও বিশ্লেষণ করা হয়, feasibility যাচাই এবং risk নির্ধারণ করা হয়।

- **Defining Requirements:**  Requirement গুলো  **SRS (Software Requirement Specification)** -এ document করা হয়।

- **Designing:**  System design  **DDS (Design Document Specification)** -এর মাধ্যমে তৈরি করা হয়।

- **Development:**  C++, Java, Python ইত্যাদি language ব্যবহার করে coding করা হয়।

- **Testing:**  Software test করে error খুঁজে বের করা এবং ঠিক করা হয়।

- **Deployment & Maintenance:**  Software release করা হয় এবং পরে update ও bug fix করা হয়।

4. UNIX command with example: File move, Change Directory and search from a specific line.

**UNIX Commands with Examples**   **1. File Move (
```
mv
```
)**

The
```
mv
```
command is used to move or rename files and directories.

**Syntax:**

mv [source] [destination]

**Example 1:**  Move a file named
```
example.txt
```
to the
```
documents
```
directory.

```
mv example.txt documents/
```

**Example 2:**  Rename a file from
```
oldname.txt
```
to
```
newname.txt
```
.

```
mv oldname.txt newname.txt
```

**2. Change Directory (
```
cd
```
)**

The
```
cd
```
command is used to change the current working directory.

**Syntax:**

cd [directory_path]

**Example 1:**  Change to the
```
home
```
directory.

```
cd /home
```

**Example 2:**  Navigate to the parent directory.

```
cd ..
```

**Example 3:**  Return to the home directory.

```
cd ~
```

**3. Search from a Specific Line (
```
sed
```
or
```
grep
```
)**

**Using
```
sed
```
:**  Search for text from a specific line number.

**Syntax:**

sed -n ‘[line_number],$p’ [file] | grep [search_term]

**Example:**  Search for the word
```
error
```
starting from line 10 in
```
logfile.txt
```
.

```
sed -n '10,$p' logfile.txt | grep "error"
```

**Using
```
grep
```
with
```
-A
```
:**  Display lines after a match starting at a specific line.

**Example:**  Search for
```
error
```
starting from line 10.

```
grep -n "error" logfile.txt | awk -F: '$1 >= 10 {print $0}'
```

5. What is blockchain technology? Why it is more secure( Such type

**Blockchain technology**  is a decentralized and distributed digital ledger that records transactions securely across multiple computers.

- **Decentralized System:**  No central authority controls the system; all participants share the data.
- **Distributed Ledger:**  Each participant has a copy of the ledger, ensuring transparency.
- **Working:**  Data is stored in blocks and linked together forming a chain.
- **Application:**  Used in finance, supply chain, and other industries for secure record-keeping.

**Why Blockchain is More Secure**

- **Decentralization:**  No single point of failure since data is shared across multiple nodes.
- **Immutability:**  Once data is recorded, it cannot be changed or deleted.
- **Transparency:**  All participants can verify transactions, making the system trustworthy.
- **Cryptographic Security:**  Data is protected using cryptography, preventing unauthorized access.

**Blockchain technology**  হলো একটি decentralized এবং distributed digital ledger যা একাধিক computer-এ নিরাপদভাবে transaction সংরক্ষণ করে।

- **Decentralized System:**  এখানে কোনো central authority নেই, সব participant data share করে।
- **Distributed Ledger:**  প্রতিটি participant-এর কাছে ledger-এর copy থাকে, ফলে transparency নিশ্চিত হয়।
- **Working:**  Data block আকারে সংরক্ষণ হয় এবং একটির সাথে আরেকটি যুক্ত হয়ে chain তৈরি করে।
- **Application:**  এটি finance, supply chain সহ বিভিন্ন ক্ষেত্রে secure record রাখার জন্য ব্যবহৃত হয়।

**Blockchain কেন বেশি Secure**

- **Decentralization:**  Data অনেক node-এ ছড়িয়ে থাকে, তাই single point failure নেই।
- **Immutability:**  একবার data record হলে তা পরিবর্তন বা মুছে ফেলা যায় না।
- **Transparency:**  সব participant transaction যাচাই করতে পারে, ফলে system trustworthy হয়।
- **Cryptographic Security:**  Data cryptography দ্বারা সুরক্ষিত থাকে, ফলে unauthorized access সম্ভব নয়।

6. Write Short Note: (i) About Digital Bangladesh (ii) About March Month Importance1

7. What is complexity? Find the Complexity from code and explain.<Question not fully collected1
