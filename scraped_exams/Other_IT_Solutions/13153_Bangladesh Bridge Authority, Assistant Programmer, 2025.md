# Bangladesh Bridge Authority, Assistant Programmer, 2025

- **Original URL:** [https://it.jobqns.com/bangladesh-bridge-authority-assistant-programmer-2025/](https://it.jobqns.com/bangladesh-bridge-authority-assistant-programmer-2025/)
- **Date:** 2026-03-01T23:52:19
- **Categories:** Job Solution 2025, Other IT Job Solution 2025

---

#### Bangladesh Bridge Authority Post: Assistant Programmer Exam Date: 12 July, 2025; Exam Taker: IBA  Written: 80 marks (Technical: 3*10 Non-tech: 50)



1. Write a C program to get max element of an array.
```
#include <stdio.h>
int main() {
int n, i;
printf("Enter number of elements: ");
scanf("%d", &n);
int arr[n];
printf("Enter %d elements:\n", n);
for(i = 0; i < n; i++) {
scanf("%d", &arr[i]);
}
int max = arr[0];
for(i = 1; i < n; i++) { if(arr[i] > max) {
max = arr[i];
}
}
printf("Maximum element = %d\n", max);
return 0;
}
```

2. SQL to find duplicate names from employee table.
```
SELECT Name, COUNT(*) AS DuplicateCount
FROM Employee
GROUP BY Name
HAVING COUNT(*) > 1;
```

3. a. What is SQL?  **What is SQL?**

**SQL (Structured Query Language)**  is a standard programming language used to manage and manipulate data in a  **Relational Database Management System (RDBMS)** .

**Main Functions of SQL:**

- **Data Querying:**  Retrieve data using commands like  **SELECT** .
- **Data Insertion:**  Insert new records using  **INSERT** .
- **Data Update:**  Modify existing records using  **UPDATE** .
- **Data Deletion:**  Remove records using  **DELETE** .
- **Database Definition:**  Create and modify tables using  **CREATE** ,  **ALTER** ,  **DROP** .

**Example:**

```
SELECT * FROM Students;
```

This command retrieves all records from the Students table.

**SQL কী?**

**SQL (Structured Query Language)**  হলো একটি standard programming language যা  **Relational Database Management System (RDBMS)** -এ data পরিচালনা ও নিয়ন্ত্রণের জন্য ব্যবহৃত হয়।

**SQL-এর প্রধান কাজ:**

- **Data Query:**   **SELECT**  ব্যবহার করে data সংগ্রহ করা।
- **Data Insert:**   **INSERT**  দিয়ে নতুন record যোগ করা।
- **Data Update:**   **UPDATE**  দিয়ে তথ্য পরিবর্তন করা।
- **Data Delete:**   **DELETE**  দিয়ে তথ্য মুছে ফেলা।
- **Table তৈরি ও পরিবর্তন:**   **CREATE** ,  **ALTER** ,  **DROP**  ব্যবহার করা।

**উদাহরণ:**

```
SELECT * FROM Students;
```

এই command Students table-এর সকল তথ্য প্রদর্শন করে।

3.b. What is API?  **What is API?**

**API কী?**

**API (Application Programming Interface)**  হলো কিছু নিয়ম ও প্রোটোকলের সমষ্টি যা বিভিন্ন software application-কে একে অপরের সাথে যোগাযোগ করতে সাহায্য করে।

**API-এর উদ্দেশ্য:**

- দুটি software system-এর মধ্যে যোগাযোগ স্থাপন করা।
- Application-গুলোর মধ্যে data আদান-প্রদান করা।
- বিদ্যমান service ব্যবহার করে development সহজ করা।

**কাজের প্রক্রিয়া:**

একটি application API-তে request পাঠায়। API সেই request server-এ পাঠায় এবং server থেকে প্রাপ্ত response আবার application-এ ফেরত দেয়।

**উদাহরণ:**

Weather app API ব্যবহার করে server থেকে আবহাওয়ার তথ্য সংগ্রহ করে।

3.  c. What is recursion? **What is Recursion?**

**Recursion**  is a programming technique in which a function calls itself repeatedly to solve a smaller part of the same problem.

**Main Components of Recursion:**

- **Base Case:**  The condition that stops the recursion.
- **Recursive Case:**  The part where the function calls itself with a smaller input.

**Example (Factorial in C):**

```
int factorial(int n)
{
if(n == 0)
return 1;        // Base case
else
return n * factorial(n - 1);  // Recursive call
}
```

**Explanation:**  The function keeps calling itself with (n-1) until n becomes 0, then it stops.

**Recursion কী?**

**Recursion**  হলো একটি programming কৌশল যেখানে একটি function নিজেই নিজেকে বারবার call করে একই সমস্যার ছোট অংশ সমাধান করে।

**Recursion-এর প্রধান অংশ:**

- **Base Case:**  যে শর্তে recursion বন্ধ হয়।
- **Recursive Case:**  যেখানে function নিজেকে ছোট মান দিয়ে call করে।

**উদাহরণ (Factorial):**

```
int factorial(int n)
{
if(n == 0)
return 1;        // Base case
else
return n * factorial(n - 1);  // Recursive call
}
```

z

**ব্যাখ্যা:**  Functionটি n-1 দিয়ে নিজেকে call করতে থাকে যতক্ষণ না n = 0 হয়।

3. d. DNS port number? **DNS Port Number**

**DNS (Domain Name System)**  uses  **Port 53**  for communication.

**Details:**

- **UDP Port 53:**  Used for most DNS queries and responses (faster and lightweight).
- **TCP Port 53:**  Used for zone transfers and large DNS responses. **DNS Port Number**

**DNS (Domain Name System)**  সাধারণত  **Port 53**  ব্যবহার করে।

**বিস্তারিত:**

- **UDP Port 53:**  অধিকাংশ DNS query ও response-এর জন্য ব্যবহৃত হয়।
- **TCP Port 53:**  Zone transfer বা বড় response-এর ক্ষেত্রে ব্যবহৃত হয়।


General Part

বাংলা-১০৪. শুদ্ধ বানান লিখ: স্বায়ত্তশাসন, ব্যাকুল, নিশীথিনী, কুসংস্কার৫. বাগধারা: বিড়াল তপস্বী **গণিত-১০ (Mathematics)** ৬. (ক) একটি বিদ্যালয়ে প্রত্যেকে ১০ পয়সা করে চাঁদা দিলে ৯০ টাকা হয়। কতজন শিক্ষার্থী ছিল?৬. (খ) a+b=7,ab=10 হলে (1/a2+1/b2)এর মান কত?

**সাধারণ জ্ঞান (General Knowledge)** ৭. (ক) চীন, যুক্তরাষ্ট্র, জাপান ও কানাডা এদের মধ্যে কে G-7 এর সদস্য নয়।৭. (খ) chat gpt এর প্রতিষ্ঠাতা কে?৭. (গ) Nam, Asian, oic এর মধ্যে বাংলাদেশ কোনটির সদস্য নয়।৭. (ঘ) বিমসটেক এর চেয়ারম্যান কোন দেশ এবং এর সদস্য সংখ্যা কয়টি?৭. (ঙ) নির্বাচন সংস্কার কমিশন ও সংবিধান সংস্কার কমিশনের প্রধান কে?৭. (চ) প্রতিবাদী তারুণ্যের জন্য ২১ শে পদক পেয়েছেন কে?৭. (ছ) wisi কোন দেশের উপজাতি?৭. (জ) নির্বাচন কমিশন সংবিধানের কত নং অনুচ্ছেদ এবং নির্বাচন কমিশন নিয়োগ দেন কে তার নাম।৭. (ঝ) বাংলাদেশ মহিলা ফুটবল দল আন্তর্জাতিক কোন টুর্নামেন্ট এর জন্য নির্বাচিত হয়েছেন?

**শর্ট প্রশ্ন (Short Questions)** ৮. (ক) থ্রি জিরো তত্ত্বের উদ্ভাবক কে? সংক্ষেপে লিখ।৮. (খ) STP কত সালে প্রণয়ন করা হয়? এর সাথে মেট্রোরেলের সম্পর্ক কি?

**ইংরেজি-১৫ (English)** ৯. Verb correction -5১১. Phrase -5১২. Sentence correction -5
