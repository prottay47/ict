# BEPZA, Programmer, 2023, ok

- **Original URL:** [https://it.jobqns.com/bepza-programmer-2023/](https://it.jobqns.com/bepza-programmer-2023/)
- **Date:** 2026-02-10T14:26:33
- **Categories:** Job Solution 2023, Other IT Job Solution

---

#### BEPZA  Post: ProgrammerExam Date: 03/11/2023



1.  Write a C Program to delete duplicate element from array.
```
#include<stdio.h>
#include<stdlib.h>
int main() {
int a[50], i, j, k, count = 0, dup[50], number, isDuplicate;
printf("Enter size of the array\n");
scanf("%d", &number);
printf("Enter Elements of the array:\n");
for(i = 0; i < number; i++) {
scanf("%d", &a[i]);
dup[i] = 0; // Initialize helper array
}
printf("Entered elements are: \n");
for(i = 0; i < number; i++) {
printf("%d ", a[i]);
}
for(i = 0; i < number; i++) {
if(dup[i] == 0) { // Check if already marked as duplicate
for(j = i + 1; j < number; j++) {
if(a[i] == a[j]) {
dup[j] = 1; // Mark as duplicate
}
}
}
}
printf("\nAfter deleting the duplicate elements, the Array is:\n");
for(i = 0; i < number; i++) {
if(dup[i] == 0) { // Print non-duplicate elements
printf("%d ", a[i]);
}
}
return 0;
}
```

2. Explain Algorithm of Binary search.

**Algorithm of Binary Search**

Binary Search is an efficient searching technique used to find an element in a sorted array by dividing the search interval into halves. This algorithm reduces the search space significantly with each step, making it faster than linear search. Here’s how it works:

- **Initial Step:** Begin by selecting the middle element of the sorted array. Compare this middle element with the key value (the element you are searching for).
- **Comparison:** If the middle element matches the key, the search is successful, and the position of the element is returned.If the key is greater than the middle element, focus on the right half of the array.If the key is smaller than the middle element, focus on the left half of the array.
- **Repeat the Process:** Continue dividing the array and comparing the key with the new middle element of the reduced sub-array.
- **Termination Condition:** Repeat the process until the sub-array size reduces to 1. If the key is not found by then, the search is unsuccessful, and the algorithm returns “not found.”

3.  Difference between symmetric and asymetric key encryption.

**Difference between Symmetric and Asymmetric Key Encryption**

AspectSymmetric Key EncryptionAsymmetric Key EncryptionNumber of KeysUses a single shared keyUses two keys (public key and private key)Key UsageSame key is used for encryption and decryptionPublic key encrypts data, private key decrypts dataSpeedFaster encryption and decryptionSlower compared to symmetric encryptionSecurityLess secure due to key sharing problemMore secure as private key is not sharedExamplesAES, DES, BlowfishRSA, ECC, DSA

**Symmetric ও Asymmetric Key Encryption-এর পার্থক্য**

বিষয়Symmetric Key EncryptionAsymmetric Key Encrypt

4. Difference between active and passive attack.

**Difference between active and passive attack**

5.  What is gateway? Is router and gateway have any difference?

**Gateway**

A gateway is a network device that acts as an entry and exit point between two different networks, often using different communication protocols. It translates data from one protocol to another so that different networks can communicate with each other.

**Difference between Router and Gateway**

Aspect
Router
Gateway

Function
Forwards data packets between similar networks
Connects and translates between different networks

Protocol Handling
Uses the same protocol (usually IP)
Can translate between different protocols

OSI Layer
Operates at Network Layer (Layer 3)
Can operate at multiple OSI layers

Usage
Used to connect LANs and WANs
Used to connect dissimilar networks

**Gateway**

Gateway হলো একটি network device যা দুইটি ভিন্ন network-এর মধ্যে প্রবেশ ও প্রস্থান পথ হিসেবে কাজ করে। এটি বিভিন্ন protocol ব্যবহারকারী network-এর মধ্যে data আদান-প্রদানের জন্য protocol translation করে।

**Router ও Gateway-এর পার্থক্য**

বিষয়
Router
Gateway

কাজ
একই ধরনের network-এর মধ্যে data forward করে
ভিন্ন ধরনের network-এর মধ্যে সংযোগ ও translation করে

Protocol
সাধারণত একই protocol ব্যবহার করে (IP)
ভিন্ন protocol-এর মধ্যে translation করতে পারে

OSI Layer
Network Layer (Layer 3)-এ কাজ করে
একাধিক OSI Layer-এ কাজ করতে পারে

ব্যবহার
LAN ও WAN সংযোগের জন্য ব্যবহৃত
অসম ধরনের network সংযোগের জন্য ব্যবহৃত

6. What is CSS? What is CSS framework? Write down 3 CSS framework name?

**What is CSS?**

CSS (Cascading Style Sheets) is a stylesheet language used to control the layout, design, colors, fonts, and overall appearance of web pages written in HTML.

**What is a CSS Framework?**

A CSS framework is a pre-prepared library that contains ready-made CSS code, components, and layout styles to help developers design responsive and attractive websites quickly and efficiently.

**Examples of CSS Frameworks**

The three popular CSS frameworks are  **Bootstrap** ,  **Tailwind CSS** , and  **Foundation** .

**CSS কী?**

CSS (Cascading Style Sheets) হলো একটি stylesheet language যা HTML দিয়ে তৈরি web page-এর layout, design, color, font এবং overall appearance নিয়ন্ত্রণ করতে ব্যবহৃত হয়।

**CSS Framework কী?**

CSS framework হলো একটি প্রস্তুত CSS library যেখানে আগে থেকেই লেখা CSS code, component এবং layout style থাকে, যা ব্যবহার করে দ্রুত ও সহজে responsive website তৈরি করা যায়।

**CSS Framework-এর উদাহরণ**

তিনটি জনপ্রিয় CSS framework হলো  **Bootstrap** ,  **Tailwind CSS**  এবং  **Foundation** ।
