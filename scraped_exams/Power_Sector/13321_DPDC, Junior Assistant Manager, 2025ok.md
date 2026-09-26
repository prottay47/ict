# DPDC, Junior Assistant Manager, 2025ok

- **Original URL:** [https://it.jobqns.com/dpdc-junior-assistant-manager-2025/](https://it.jobqns.com/dpdc-junior-assistant-manager-2025/)
- **Date:** 2026-03-03T21:44:15
- **Categories:** Job Solution 2025, Power Sector IT Job Solution 2025

---

#### Dhaka Power Distribution Company (DPDC)
Post:  Junior Assistant Manager Exam Date: 27.06.2025, Exam Taker: BUET



1. Write a C/JAVA program to determine if a given year is a leap year or not.
```
#include <stdio.h>

int main() {
int year;

printf("Enter a year: ");
scanf("%d", &year);

if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
printf("%d is a leap year.\n", year);
} else {
printf("%d is not a leap year.\n", year);
}

return 0;
}
```

2. What is the difference between Supervised and Unsupervised learning?

**Difference Between Supervised and Unsupervised Learning**

- **Definition:**  Supervised Learning uses labeled data for training; Unsupervised Learning uses unlabeled data.
- **Training Data:**  In supervised learning, input data is provided with correct output; in unsupervised learning, only input data is provided.
- **Goal:**  Supervised learning predicts output from input data; unsupervised learning finds hidden patterns or relationships in data.
- **Common Tasks:**  Supervised learning is used for Classification and Regression; Unsupervised learning is used for Clustering and Association.
- **Accuracy Measurement:**  Supervised learning can measure accuracy using known labels; Unsupervised learning does not have predefined labels to measure accuracy directly.
- **Examples:**  Linear Regression, Decision Tree (Supervised); K-Means, Apriori Algorithm (Unsupervised).

**Supervised Learning এবং Unsupervised Learning-এর পার্থক্য**

- **সংজ্ঞা:**  Supervised Learning labeled data ব্যবহার করে; Unsupervised Learning unlabeled data ব্যবহার করে।
- **Training Data:**  Supervised learning-এ input-এর সাথে সঠিক output দেওয়া থাকে; Unsupervised learning-এ শুধুমাত্র input data থাকে।
- **উদ্দেশ্য:**  Supervised learning input থেকে output predict করে; Unsupervised learning data-এর মধ্যে hidden pattern বা relationship খুঁজে বের করে।
- **Common Task:**  Supervised learning Classification ও Regression-এর জন্য ব্যবহৃত হয়; Unsupervised learning Clustering ও Association-এর জন্য ব্যবহৃত হয়।
- **Accuracy Measurement:**  Supervised learning-এ known label থাকায় accuracy মাপা যায়; Unsupervised learning-এ predefined label না থাকায় সরাসরি accuracy নির্ধারণ কঠিন।
- **উদাহরণ:**  Linear Regression, Decision Tree (Supervised); K-Means, Apriori Algorithm (Unsupervised)।

3. Write down the difference between informed and uninformed search algorithm.

**Difference Between Informed and Uninformed Search Algorithm**

- **Knowledge Used:**  Informed search uses additional heuristic information to guide the search; Uninformed search does not use any domain knowledge.
- **Search Strategy:**  Informed search selects paths based on an evaluation function; Uninformed search explores nodes systematically without guidance.
- **Efficiency:**  Informed search is generally faster and more efficient; Uninformed search is slower as it may explore unnecessary nodes.
- **Optimality:**  Informed search can be optimal if the heuristic is admissible; Uninformed search like BFS can also be optimal under certain conditions.
- **Examples:**  A*, Greedy Best First Search (Informed); BFS, DFS, Uniform Cost Search (Uninformed).

**Informed এবং Uninformed Search Algorithm-এর পার্থক্য**

- **Knowledge ব্যবহার:**  Informed search অতিরিক্ত heuristic information ব্যবহার করে; Uninformed search কোনো domain knowledge ব্যবহার করে না।
- **Search Strategy:**  Informed search evaluation function-এর ভিত্তিতে path নির্বাচন করে; Uninformed search কোনো দিকনির্দেশনা ছাড়া node অনুসন্ধান করে।
- **দক্ষতা (Efficiency):**  Informed search সাধারণত দ্রুত ও কার্যকর; Uninformed search অপ্রয়োজনীয় node explore করতে পারে, তাই ধীর।
- **Optimality:**  Heuristic admissible হলে Informed search optimal হতে পারে; Uninformed search যেমন BFS নির্দিষ্ট ক্ষেত্রে optimal হতে পারে।
- **উদাহরণ:**  A*, Greedy Best First Search (Informed); BFS, DFS, Uniform Cost Search (Uninformed)।

4. Given IP address 10.10.0.0/16, you have divided the network into eight equal subnets. Find the subnet mask in dotted decimal and CIDR notation. Also find the first and last usable IP address of the third subnet.

**Subnetting of 10.10.0.0/16 into 8 Equal Subnets**

- **Given Network:**  10.10.0.0/16
- **Number of Subnets:**  8 = 23 ⇒ need  **3 subnet bits**
- **New CIDR:**  /16 + 3 =  **/19**
- **Subnet Mask (dotted decimal):**   **255.255.224.0**
- **Subnet Mask (CIDR):**   **/19**

**Third Subnet (1st subnet = 10.10.0.0/19)**

- **Block size in 3rd octet:**  256 − 224 =  **32**
- **Subnets:**  10.10.0.0, 10.10.32.0,  **10.10.64.0** , 10.10.96.0, …
- **Network Address (3rd subnet):**   **10.10.64.0**
- **Broadcast Address (3rd subnet):**   **10.10.95.255**
- **First Usable IP:**   **10.10.64.1**
- **Last Usable IP:**   **10.10.95.254**

**10.10.0.0/16 Network-কে 8টি Equal Subnet-এ ভাগ**

- **Given Network:**  10.10.0.0/16
- **Subnet সংখ্যা:**  8 = 23 ⇒  **3 subnet bit**  লাগবে
- **New CIDR:**  /16 + 3 =  **/19**
- **Subnet Mask (dotted decimal):**   **255.255.224.0**
- **Subnet Mask (CIDR):**   **/19**

**Third Subnet (1st subnet = 10.10.0.0/19 ধরে)**

- **3rd octet-এর Block size:**  256 − 224 =  **32**
- **Subnets:**  10.10.0.0, 10.10.32.0,  **10.10.64.0** , 10.10.96.0, …
- **Network Address (3rd subnet):**   **10.10.64.0**
- **Broadcast Address (3rd subnet):**   **10.10.95.255**
- **First usable IP:**   **10.10.64.1**
- **Last usable IP:**   **10.10.95.254**

5. Analyze the following C function and determine its Big O Time Complexity and Space Complexity. Explain your reasoning.

#include <stdio.h>

void findDuplicates(int arr[], int n) {
// Outer loop to pick an element
for (int i = 0; i < n; i++) {
// Inner loop to compare it with the rest of the elements
for (int j = i + 1; j < n; j++) {
if (arr[i] == arr[j]) {
printf("Duplicate found: %d\n", arr[i]);
}
}
}
}

**Time and Space Complexity Analysis**

**Given Function:**  findDuplicates(int arr[], int n)

**Time Complexity:**

- The outer loop runs from i = 0 to n-1 ⇒ approximately  **n times** .
- The inner loop runs from j = i+1 to n-1.
- For each iteration of the outer loop, the inner loop runs roughly (n − i − 1) times.
- Total comparisons ≈ (n−1) + (n−2) + (n−3) + … + 1
- This forms the sum of first (n−1) natural numbers ⇒  **n(n−1)/2**
- Therefore, Time Complexity =  **O(n²)**

**Space Complexity:**

- No extra data structures are used.
- Only a few loop variables (i, j) are used.
- Space used does not depend on input size.
- Therefore, Space Complexity =  **O(1)**  (Constant Space)

**Final Answer:** Time Complexity =  **O(n²)** Space Complexity =  **O(1)**

**Time এবং Space Complexity বিশ্লেষণ**

**প্রদত্ত Function:**  findDuplicates(int arr[], int n)

**Time Complexity:**

- Outer loop i = 0 থেকে n-1 পর্যন্ত চলে ⇒ প্রায়  **n বার** ।
- Inner loop j = i+1 থেকে n-1 পর্যন্ত চলে।
- প্রতিটি outer loop-এর জন্য inner loop প্রায় (n − i − 1) বার চলে।
- মোট comparison ≈ (n−1) + (n−2) + … + 1
- এটি n(n−1)/2 এর সমান।
- সুতরাং Time Complexity =  **O(n²)**

**Space Complexity:**

- কোনো অতিরিক্ত data structure ব্যবহার করা হয়নি।
- শুধু i ও j variable ব্যবহার করা হয়েছে।
- Input size বাড়লেও অতিরিক্ত memory প্রয়োজন হয় না।
- সুতরাং Space Complexity =  **O(1)**  (Constant Space)

**চূড়ান্ত উত্তর:** Time Complexity =  **O(n²)** Space Complexity =  **O(1)**

6. Explain Different types of Cyber-attack.

**Different Types of Cyber-Attack**

- **Phishing Attack:**  Fraudulent emails or messages are sent to trick users into revealing sensitive information such as passwords or credit card details.
- **Malware Attack:**  Malicious software such as Virus, Worm, Trojan, or Spyware is used to damage or gain unauthorized access to systems.
- **Ransomware Attack:**  A type of malware that encrypts files and demands payment (ransom) to restore access.
- **Denial of Service (DoS) / Distributed DoS (DDoS):**  Attackers flood a server or network with traffic to make it unavailable to legitimate users.
- **Man-in-the-Middle (MITM) Attack:**  The attacker secretly intercepts and possibly alters communication between two parties.
- **SQL Injection:**  Malicious SQL queries are inserted into input fields to manipulate or access a database.
- **Brute Force Attack:**  Attackers repeatedly try different password combinations to gain access.
- **Cross-Site Scripting (XSS):**  Malicious scripts are injected into trusted websites to steal user data.

**Cyber-attack-এর বিভিন্ন প্রকার**

- **Phishing Attack:**  ভুয়া email বা message পাঠিয়ে user-এর password, credit card তথ্য ইত্যাদি সংগ্রহ করা হয়।
- **Malware Attack:**  Virus, Worm, Trojan, Spyware ইত্যাদি malicious software ব্যবহার করে system ক্ষতিগ্রস্ত বা unauthorized access নেওয়া হয়।
- **Ransomware Attack:**  এক ধরনের malware যা file encrypt করে এবং access ফিরিয়ে দেওয়ার জন্য ransom দাবি করে।
- **Denial of Service (DoS) / Distributed DoS (DDoS):**  অতিরিক্ত traffic পাঠিয়ে server বা network অচল করে দেওয়া হয়।
- **Man-in-the-Middle (MITM) Attack:**  দুই পক্ষের communication-এর মাঝে attacker গোপনে intercept বা পরিবর্তন করে।
- **SQL Injection:**  Input field-এ malicious SQL query প্রবেশ করিয়ে database manipulate বা access করা হয়।
- **Brute Force Attack:**  বিভিন্ন password combination বারবার চেষ্টা করে access নেওয়া হয়।
- **Cross-Site Scripting (XSS):**  Trusted website-এ malicious script inject করে user-এর data চুরি করা হয়।

7. A communication channel has a signal power of Ps=50mW and a noise power of Pn = 5 mW.
a) Find the signal to noise ratio in linear form and decibels (dB)
b) If the bandwidth of the channel is B = 3 MHz , calculate the channel capacity using Shannon's formula

**Given:** Signal Power (Ps) = 50 mWNoise Power (Pn) = 5 mWBandwidth (B) = 3 MHz = 3 × 106 Hz

**(a) Signal to Noise Ratio (SNR)**

- **SNR (linear) = Ps / Pn**
- SNR = 50 / 5 =  **10**
- **SNR (dB) = 10 log10(SNR)**
- = 10 log10(10)
- = 10 × 1 =  **10 dB**

**(b) Channel Capacity using Shannon’s Formula**

Shannon Capacity Formula: **C = B log2(1 + SNR)**

- C = 3 × 106 × log2(1 + 10)
- = 3 × 106 × log2(11)
- log2(11) ≈ 3.46
- C ≈ 3 × 106 × 3.46
- C ≈  **10.38 Mbps**

**Final Answer:** SNR (linear) =  **10** SNR (dB) =  **10 dB** Channel Capacity ≈  **10.38 Mbps**
