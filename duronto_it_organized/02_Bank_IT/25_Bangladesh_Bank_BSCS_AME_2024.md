# Bangladesh Bank BSCS - Assistant Maintenance Engineer (200 Marks) - 2024/2026

| Field | Details |
| :--- | :--- |
| **Organization** | Bangladesh Bank BSCS |
| **Post Name** | Assistant Maintenance Engineer / AE (IT) |
| **Exam Date** | 2024/2026 |
| **Exam Taker** | BSCS |
| **Marks / Format** | 200 Marks (15 Questions) |
| **Source** | Duronto IT Academy / Smart IT Job Solution |

---

###### **Bangladesh Bank Banker's Selection Committee Secretariat (BSCS) Assistant Maintenance Engineer/Assistant Engineer (IT) Exam Date: 08/05/2026** 

There are 15 (fifteen) questions in this section with total marks 200. Answer ALL. The symbols have their usual meanings. Marks of each question are written in brackets. 

Assume any reasonable value if required. 

Write all your answers within the space provided in the separate answer script. 

**1. A maintenance engineer is setting up a RAID 5 array with five hard drives, each having a capacity of 4 TB. What is the total usable storage capacity, and why is it not 20 TB?** **(15 Marks)** 

In a RAID 5 array, the usable storage capacity is calculated as: 

Therefore, the total usable storage capacity is: (5 −1) × 4 TB = 16 TB 

###### **Why is it not 20 TB?** 

RAID 5 uses **distributed parity** for fault tolerance. The equivalent capacity of **one drive** is reserved for storing parity information, which allows the system to recover data if one drive fails. CSE CAREER • Total raw capacity = 5 × 4 = 20TB • Parity overhead = 4 TB (capacity of one drive) — MASTER GUIDE— • Usable capacity = 20 −4 = 16TB Thus, RAID 5 sacrifices the space of one disk to provide redundancy and data protection. ‘a e "te e “oa e a **2. Distinguish between Preventive and Corrective maintenance with a real-world example for each in a data center environment. A critical system consists of three components (Power Supply, Motherboard, and Storage) connected in a series configuration. If each component has a reliability of 0.95, what is the total reliability of the system?** **(15 Marks)** 

###### **Difference Between Preventive and Corrective Maintenance** 

Page | 1 

**CSE Career Master Guide                                         BSCS-AME/AE** 

|**Preventive Maintenance**|**Corrective Maintenance**|

|---|---|

|Maintenance performed**before a failure**<br>**occurs**to reduce the chance of breakdown.|Maintenance performed**after a**<br>**failure occurs**to restore operation.|

|Planned and scheduled regularly.|Unplanned and done when a problem<br>appears.|

|هدف is to improve reliability and avoid<br>downtime.|Goal is to repair and recover the failed<br>system.|

|Usually lower long-term cost.|Can cause higher downtime and<br>emergency repair cost.|

- **Real-World Examples in a Data Center** • **Preventive Maintenance Example:** Regularly cleaning server dust filters, checking UPS batteries, updating firmware, and monitoring server temperature to prevent overheating and failures. 

- • **Corrective Maintenance Example:**  Replacing a failed hard disk or repairing a damaged power supply after a server suddenly stops working. 

###### **Real-World Examples in a Data Center** 

###### **Reliability of the System** 

For components connected in a series configuration, the total system reliability is the product of the reliabilities of all components. Given: 

- Reliability of Power Supply = 0.95 

- Reliability of Motherboard = 0.95 

- Reliability of Storage = 0.95 

So, 

Final Answer 

or about 85.7% reliability. 

**3. At which layer of the OSI model does a standard Router primarily operate, and what is the specific name of the Protocol Data Unit (PDU) at this layer? A router has four contiguous /24 routing table entries: 10.1.0.0/24, 10.1.1.0/24, 10.1.2.0/24, and 10.1.3.0/24. If you summarize (supernet) these into a single route,what will be the new CIDR notation?** **(15 Marks)** 

A standard **Router** primarily operates at the **Network Layer (Layer 3)** of the OSI model. 

- **OSI Layer:** Network Layer (Layer 3) 

- **PDU at this layer: Packet** 

Page | 2 

**CSE Career Master Guide                                         BSCS-AME/AE** 

###### **Route Summarization (Super netting)** 

Given routes: 

- 10.1.0.0/24 

- 10.1.1.0/24 

- 10.1.2.0/24 

- 10.1.3.0/24 

These are four contiguous /24 networks. Since: 4 = 2<sup>2</sup> we can combine 4 networks by reducing the subnet mask by 2 bits: /24 −2 =/22 So the summarized route becomes: 10.1.0.0/22 **4. What does the Consistency property in ACID guarantee during a bank fund transfer transaction? You are designing the schema for a Savings_Accounts table. Write the specific SQL constraint clause to ensure that the current_balance column can never drop below zero.** **(15 Marks) Consistency Property in ACID**   The **Consistency** property in ACID ensures that a database transaction always moves the database from one **valid state** to another **valid state** while maintaining all defined rules, constraints, and integrity conditions. 

###### **In a Bank Fund Transfer** 

During a fund transfer: 

- The amount deducted from one account must be correctly added to the other account. 

- • The database must never remain in a partial or invalid state. CSE CAREER 

- • If any step fails, the entire transaction is rolled back. 

- For example: — MASTER GUIDE — • Account A = 10,000 

   - LEARN» 

   - • Account B = 5,000 

   - • Transfer = 2,000 Be 

After successful transaction: 

- Account A = 8,000 

- Account B = 7,000 

Total money remains unchanged, preserving database consistency. 

###### **SQL Constraint Clause** 

To ensure that the current_balance column never becomes negative, use a CHECK constraint. 

CHECK (current_balance >= 0) 

Page | 3 

**CSE Career Master Guide                                         BSCS-AME/AE** 

Example inside table creation: CREATE TABLE Savings_Accounts ( account_no INT PRIMARY KEY, account_holder VARCHAR(100), current_balance DECIMAL(12,2), CHECK (current_balance >= 0) ); 

**5. Briefly explain "Circular Wait." In a Resource Allocation Graph (RAG), if a cycle exists, does it absolutely guarantee that a Deadlock has occurred? Explain briefly.** **(15 Marks)** 

###### **Circular Wait** 

- **Circular Wait** is one of the four necessary conditions for deadlock. It occurs when a set of processes are waiting for resources in a circular chain. Example: • Process (P_1) is waiting for a resource held by (P_2) 

- • (P_2) is waiting for a resource held by (P_3) 

- • (P_3) is waiting for a resource held by (P_1) 

- Thus, each process waits indefinitely for another process in the cycle. SI pe y | 

###### **Does a Cycle in RAG Always Mean Deadlock? Answer:** 

**No, not always.** 

- If the Resource Allocation Graph (RAG) has **only one instance of each resource type** , then a cycle **guarantees deadlock** . 

- If there are **multiple instances of a resource type** , a cycle may exist without deadlock. **Brief Explanation** CSE CAREER With multiple resource instances, another free instance may become available and break the waiting chain, allowing processes to continue execution. — MASTER GUIDE— Therefore: 

   - **Cycle + single instance resources → Deadlock guaranteed** 

   - **Cycle + multiple instance resources → Deadlock may or may not occur** 

**6. A server suddenly starts sending abnormal traffic to external systems. Analyze the possible cause and suggest immediate actions.** **(15 Marks)** 

Page | 4 

**CSE Career Master Guide                                         BSCS-AME/AE** 

A server suddenly sending abnormal traffic to external systems may indicate a **security compromise, malware infection, or misconfiguration** . 

###### **Possible Causes** 

1. **Malware or Botnet Infection** 

   - ➢ The server may be infected with malware or ransomware and used to send spam, DDoS traffic, or malicious requests. 

2. **Unauthorized Access / Hacking** ➢ An attacker may have gained access through weak passwords, unpatched vulnerabilities, or stolen credentials. 

3. **Compromised Application** ➢ A vulnerable web application or service may be exploited to generate abnormal outbound traffic. 

4. **Misconfigured Software or Scripts** i> ➢ Faulty automation scripts, backup tools, or applications may accidentally create excessive network traffic. 

5. **Data Exfiltration** ➢ Sensitive data may be transferred to external attackers. 

**Immediate Actions 1. Isolate the Server** • Disconnect the server from the network or restrict outbound traffic using firewall rules to prevent further damage. 

**2. Analyze Network Traffic** • Check logs, running processes, active connections, and unusual ports using tools like: Ee 

###### **Immediate Actions** 

**1. Isolate the Server** 

   - Disconnect the server from the network or restrict outbound traffic using firewall rules to prevent further damage. 

###### 

- Check logs, running processes, active connections, and unusual ports using tools like: 

➢ netstat 

         - ➢ tcpdump 

         - ➢ Firewall/SIEM logs 

**3. Scan for Malware** 

   - Run antivirus and anti-malware scans to detect malicious software. 

   - **4. Check User Accounts and Access** • Review recent logins, privilege escalations, and suspicious accounts. 

   - • Change passwords and revoke compromised credentials. CSE CAREER 

**4. Check User Accounts and Access** 

      - Change passwords and revoke compromised credentials. 

**5. Identify the Root Cause** 

   - Examine application logs, security logs, and recent configuration changes. 

**6. Apply Security Fixes** 

   - Patch vulnerabilities, update software, and close unnecessary services or ports. 

**7. Restore if Necessary** 

   - If heavily compromised, restore the system from a clean backup. 

###### **8. Monitor Continuously** 

- Enable continuous monitoring and intrusion detection to ensure the threat is removed. 

###### **Conclusion** 

Page | 5 

###### **CSE Career Master Guide                                         BSCS-AME/AE** 

Abnormal outbound traffic is often a sign of cyberattack or malware activity. Immediate isolation, investigation, malware scanning, and security remediation are essential to protect the server and network. 

**7 Mapreduce,hadoop (repeat previous) Assumption of the question are: "A financial institution needs to process massive server logs to detect fraud in real-time and perform predictive maintenance using ML. Identify 5 components of the Hadoop ecosystem suitable for this architecture and justify their** **roles."** 

###### **Hadoop Ecosystem Components and Their Roles** 

|**Component**|**Role in the**<br>**Architecture**|**Justification**|

|---|---|---|

|**HDFS**<br>**(Hadoop**<br>**Distributed File**<br>**System)**|Distributed storage of<br>massive server logs<br>and transaction data|HDFS can store huge volumes of<br>structured and unstructured data reliably<br>across multiple nodes with fault tolerance<br>and replication.|

|**MapReduce**|Parallel processing of<br>large datasets|Processes massive log files efficiently by<br>dividing tasks into Map and Reduce<br>phases, enabling distributed computation<br>for analytics and fraud detection.|

|**Apache Spark**|Real-time<br>data<br>processing<br>and<br>Machine Learning|Spark supports in-memory computation,<br>fast stream processing, and ML libraries<br>(MLlib), making it ideal for real-time<br>fraud<br>detection<br>and<br>predictive<br>maintenance.|

|**YARN**<br>**(Yet**<br>**Another**<br>**Resource**<br>**Negotiator)**|Resource management<br>and job scheduling|YARN<br>manages<br>cluster<br>resources<br>efficiently and schedules Hadoop/Spark<br>jobs<br>across<br>nodes<br>for<br>optimized<br>performance.|

|**Apache Hive**|SQL-like<br>querying<br>and analysis|Hive allows analysts to run SQL-style<br>queries on large datasets for reporting, log<br>analysis, and fraud investigation without<br>complexprogramming.|

###### **8 Http status code** 

###### **HTTP Status Codes** 

HTTP status codes are standard response codes returned by a web server to indicate the result of a client’s request. 

###### **Categories of HTTP Status Codes** 

|Code Range|Meaning|

|---|---|

|1xx|Informational|

|2xx|Success|

Page | 6 

**CSE Career Master Guide                                         BSCS-AME/AE** 

|3xx<br>|Redirection<br>|

|---|---|

|4xx<br>|Client Error<br>|

|5xx<br>|Server Error<br>|

|**1xx– Informational**<br>||

|Code<br>|Meaning<br>|

|100<br>|Continue<br>|

|101<br>|Switching Protocols<br>|

|**2xx– Success**<br>||

|Code<br>|Meaning<br>|

|200<br>|OK<br>|

|201<br>|Created<br>|

|204<br>|No Content<br>|

|**3xx– Redirection**<br><br>||

|Code<br>|Meaning<br>|

|301<br>|Moved Permanently<br>|

|302<br>|Found (Temporary Redirect)<br>|

|304<br>|Not Modified<br>|

|**4xx– Client Errors**<br>||

|Code<br>|Meaning<br>|

|400|Bad Request|

|401|Unauthorized|

|403|Forbidden|

|404|Not Found|

|405|Method Not Allowed|

|**5xx– Server Errors**<br>||

|Code<br>|Meaning<br>|

|500<br>|Internal Server Error<br>|

|502<br>|Bad Gateway<br>|

|503<br>|Service Unavailable<br>|

|504<br>|Gateway Timeout<br>|

|**Example**||

If a user requests a webpage that does not exist, the server may respond with: HTTP/1.1 404 Not Found 

This means the server could not find the requested resource. 

###### **9. Zero-day attack, data in transit & Data at rest technology,** 

A zero-day attack exploits a previously unknown vulnerability in software or hardware. These vulnerabilities are termed "zero day" because developers have had zero days to fix the flaw before it is exploited by hackers. Unlike more traditional attacks, zero day exploits are unique in that they take advantage of weaknesses that are not yet known to the public or the vendor. This makes them incredibly difficult to defend against, as there are no existing patches or updates that can prevent the attack. 

Page | 7 

###### **CSE Career Master Guide                                         BSCS-AME/AE** 

Zero-day attacks can manifest in various forms, including malware, viruses, or even direct network intrusions. They often remain undetected until significant damage has been done. Once an exploit is identified, developers rush to create a patch, but by then, the damage might already be extensive. This urgency and the element of surprise are what make zero day attacks particularly dangerous and challenging to combat. 

###### **Data at Rest vs Data in Transit** 

**Data in transit** is actively moving across networks—such as emails, file transfers, or API communications—making it vulnerable to interception. In contrast, **data at rest** remains stored on devices, databases, or cloud environments, where unauthorized 

access is the primary concern. 

###### **Data in Transit Security** 

- **Data in Transit Security** • **Encryption protocols (TLS, SSL, IPsec):** Cryptographic protocols to secure data transmission by encrypting network traffic to prevent unauthorized access 

- • **Secure transmission protocols (HTTPS with TLS):** i> Encrypt data in transit to protect it from interception 

- **Authentication mechanisms (MFA, digital certificates):** Verify user identities and ensure that only authorized parties can access transmitted data 

###### **Data at Rest Security** 

- **Encryption of stored files and databases:** Encrypting stored data ensures that even if unauthorized access occurs, the data remains unreadable without the correct decryption key 

- **Access control policies (least privilege, role-based permissions):** Implementing strict access controls limits data exposure by ensuring only authorized users can access sensitive information 

- **Physical security measures (restricted server access, hardware encryption):** Securing physical data storage locations and using hardware-based encryption protects data from unauthorized access to hardware 

###### **Data at Rest** 

- Hard drives 

- Databases 

- • Cloud storage 

- • Unauthorized access CSE CAREER • Data breaches 

###### **Data in Transit** 

- Emails 

- File transfers 

- API communications 

- Interception 

- MITM attacks 

access is the primary concern. **Data in Transit Security Encryption protocols (TLS, SSL, IPsec):** transmission by encrypting network traffic to prevent unauthorized access **Secure transmission protocols (HTTPS with TLS):** i> protect it from interception **Authentication mechanisms (MFA, digital certificates):** and ensure that only authorized parties can access transmitted data **Encryption of stored files and databases:** even if unauthorized access occurs, the data remains unreadable without the correct decryption key **Access control policies (least privilege, role-based permissions):** strict access controls limits data exposure by ensuring only authorized users can access sensitive information Ee **security measures (restricted** 

Page | 8 

**CSE Career Master Guide                                         BSCS-AME/AE** 

###### **10. Preventive and corrective maintenance, series system reliability** **calculation** 

###### **Preventive Maintenance** 

Preventive maintenance is the maintenance performed **before a failure occurs** to reduce the possibility of system breakdown and improve reliability. 

###### **Features** 

- Planned and scheduled 

- Helps avoid unexpected failures 

- Reduces downtime 

- Increases equipment lifespan 

###### **Example** 

Regularly cleaning servers, checking UPS batteries, updating firmware, and monitoring cooling systems in a data center. 

###### **Corrective Maintenance** 

Corrective maintenance is the maintenance performed **after a failure occurs** to restore the system to normal operation. 

###### **Features** 

- Unplanned maintenance 

- Done after detecting faults 

- May cause temporary downtime 

- Focuses on repair and recovery 

###### **Example** 

Replacing a failed hard disk or repairing a damaged server power supply after a system crash. 

###### **Difference Between Preventive and Corrective Maintenance** 

|**Preventive**|**Corrective Maintenance**|

|---|---|

|**Maintenance**||

|Done before failure|Done after failure|

|Planned and scheduled|Unplanned|

|Prevents breakdown|Repairs breakdown|

|Lower downtime|Higher downtime|

|Improves reliability|Restores operation|

###### **Series System Reliability Calculation** 

In a **series system** , all components must work properly for the system to function. Therefore, total reliability is the product of the reliabilities of all components. 

###### **Formula** 

𝑅𝑠𝑦𝑠𝑡𝑒𝑚 = 𝑅1 × 𝑅2 × 𝑅3 × ⋯× 𝑅𝑛 

###### **Example Calculation** 

Suppose: 

- Power Supply reliability = 0.95 

- Motherboard reliability = 0.95 

- Storage reliability = 0.95 

Then, 

Page | 9 

**CSE Career Master Guide                                         BSCS-AME/AE** 

###### **Final Reliability** 

or approximately **85.7%** . 

General part: Math: 

Page | 10 

Give short answers for the following questions. 1. (a) What is the use of cache memory? (b) How can you define SSD? 

(c) What is the function of GPU? 

(d) Define the principle of data transmission through the fiber optic cable. 

(e) What do you understand by the resolution of a computer screen? 

(f) Why do we need database normalization? 

(g) How can you define E-R model in (h) What is the differences between "Call-by-value" and "Call-by-reference" DBMS? 

(i) When a constructor is invoked in OOP? 

(j) Differentiate between interpreter and compiler. 

2.(a) Describe briefly the Cloud based Database. 

(b) What do you mean by National Data Center? Define its purpose. (c) Name and define the characteristics properties for deadlock situation in a computer system. 

3. (a) Explain Software Development Life Cycle (SDLC). 

(b) Which factors are to be considered for software pricing? 

(c) What is digital signature? Describe its role in digital security? 

4.(a) What is API? Explain with example. (b) What do you mean by Recursion? Calculate Factorial function using recursion with C programming code. 

(c) Differentiate between Array and Structure data type. 

5.(a) Describe data communication system with necessary diagram. 

(b) Write short note on i) Web Server ii) ISP iii) Router iv) Search engine 6.(a) How can you define loT? What are the basic components of loT? (b) What do you mean by machine learning? Name three machine learning applications in our daily life. 

(c) Write the differences between Machine learning and Deep learning. 7(a) Explain the difference between a database administrator and a data administrator. 

(b) Describe the advantages and disadvantages of DBMS-provided and Application-provided security. 

(c) What do you mean by the terms: roll back and roll forward? 8.(a) Why packet switching is suitable for digital data communication?) 

(b) Explain the differences between depth-first and breadth-first search. 9.Design a circuit that counts the number of 1's presence in 3-inputs A, B and C. Its output is a two-bit number X1 X0  representing that count in binary. Assume active-High logic. 

(a) Write the truth table for this circuit. 

- (b) Find the minimized logic expression for output. 

- (c) Draw the corresponding logic diagram for the circuit. 10.Write a C function for the following: 

- (a) Determine whether a given number is prime or not. 

- (b) Print the following matrix using for loop. 

1 22 333 4444 55555 

- (c) Find the largest number within the array of N elements 

- (d) Determine even or odd numbers 

fafea **িবিভ� ম�ণালয়** sactere **, িবভাগ, অিধদ�েরর** whnecat **সহকারী ��া�ামার** caftenettt **33 তািরখঃ ১৯.০৭.২০২৩; পূণ�মান** RoR; AefaT **- ২০০; সময়-৪.০০** Col **ঘ�া [�িত� িবষেয়র জন� পৃথক উ�র প� ব�বহার ক�ন]** 

`বাংলা িবষয় �কাডঃ ১০১ মানঃ ৪০ ১.` ‘ orgie `আধুিনক জীবন ও �যুি�` ’ `িবষেয় �ব� রচনা ক�ন। ১৫` feaq GHGS 09 HAZ 80 `২.সারমম� িলখুনঃ  ০৫` ware Giza ¢ age faeces ataa ADA FPA OC “ `আিম চাই মহে�র মহৎ পরাণ` fy freA o¢ `মু�তা মািলকা িনিধ` Hor aferDiS REGfeHRS PAT `আমাের িদওনা িবিধ` DIR `চািহেন এ জগেতর রাজ� স�ান` 4 Gricwa ANY FATA aifaee `বাি�ত পরাণ �পেল` oral corcet `�মেখ �নব ম���- ��� উপাদান` A A TG: 1S Boreas One `�ােণর সাধক আিম, সাধনীয় �াণ।` ATS SHAR, TATA Te | “ `৩. বষ�ায় �ভে� যাওয়া আপনার এলাকার রা�ািট �মরামেতর জ� �ানীয় কতৃ�প� বরাবের একিট আেবদন পত` ©. THY SH MSM HATA LATA AVG GAGA SAT SANT SH Aled LAG OCA AS ADA `রচনা ক�ন।০৫` PPA IO `৪. বাংলায় অ�বাদ ক�নঃ ০৫` 8. AKT SAM FHA Oo Smoking is very harmful. It is expensive too. It pollutes the environment. Those who smoke cannot live long. So everyone should give up smoking. 

@. `৫. িনেচর �� �েলার উ�র িদনঃ ৫*২ = ১০` Frcba aft eral Gea fas @*2 = 30 `(ক) শ� গঠেনর পাঁচিট িনয়ম উদাহরণসহ িলখুন।` (&) =I sacra *itDAB free OrTeacrrR Ferg `(খ) অথ� িনেদ�শ কের বাগধারা�েলা িদেয় বাক� রচনা ক�ন।` (2) BE Freer Sea aaTAVOTAT Perel TT ADA PAPA | SO `কংস মামা, কিলর স��া, তীেথ�র কাক, ধামাধরা, প�া ভােত িঘ।` AAT, Shara HAT, Glos Se, ePTAAT, AT wTES Fe 

###### **English** 

###### **Subject Code: 102 Marks:40** 

1. Write an essay on   15 

Online Business in Bangladesh: [Hints: Introduction-How to start an Online Business- How businesses were done during Covid-19?- What is the future of E-commerce in Bangladesh?-What is it’s main hindrance ?- Conclusion] 

2.Write an application to the Bank Manager of your locality requesting to provide you ‘Annual Statement’ of your account.  05 

3.Change the following Sentences as directed: 1*10 = 10 

(i) We eat, we want to live. (Join the sentences) 

(ii) You are requested to switch off your mobile now. (Make it active) 

(iii) Shakespeare was a great than any poet. (Correct the sentence) 

(iv) He told me to go there. (Change the narration) 

(v) Don’t touch it (Make it passive) 

(vi) He is not qualified on the post. (Correct the sentence) 

(vii) If you help us, we will win. (Make it Compound) (viii) What a terrible news it was! (Make it Assertive) 

(ix) One of the girls---- absent yesterday (Use a verb) 

(x) The man is out and ----- a scoundrel. (Use an appropriate preposition) 

4.Read the following passage and answer the questions that follow: 

Books are man’s best companion in life. You may have many good friends. But you may not get 

Them when you need them. They may not speak gently to you, one or two prove false and do you much harm. But books are always ready to your side. Some books may make you laugh, some other may give you much pleasure, others, again give you knowledge and new ideas and make you a noble and thorough man. They are your friends throughout your life. 

Questions: 2*5 = 10 

(a) Are all friends good and faithful ? 

(b) Can we always get our friends by our side in times of need? 

(c) How are books our best friends? 

(d) How do books always benefit us ? 

- (e) How long do books remain with us? 

```

বাংলােদশ

```

`১. বাংলােদেশর ভেগািলক অব�ােনর বণ�না িলখুন। ৩` >. Meters weonerss OeBIC Sat FAT 

`২. মুিজবনগর সরকােরর অ�ায়ী রাজধানীর নাম িক? ৩` 2. Bferareis Aasieaa SR areata ATT FF? © `�বাসী বাংলােদশ সরকােরর রাজধানী �কাথায় িছল?` SATAY AAT AAPTCATA ATTA CHT PRAT? `অ�ায়ী সরকােরর উপেদ�া ম�লীর সদ� সংখ�া কত িছল ?` Ahh Hasreas BacnBl eats WHAT Heel Fw feet 2 `৩. ব�ভ� কখন হয় ? ব�ভ� রদ কখন হয়? ব�ভ� রেদর কারণ িক িছল ? ৩` ©. THSH BAY 7 THSF IM SAY VAI? THSF AeA Fiat FS fT? © `৪. বাংলােদেশ �ীন হাউজ ইেফে�র �িতকােরর ৫ িট উপায় উে�খ ক�ন। ৩` 8. Tee A VSG ercss afer ¢ fF Gory Great FPA © `৫. �ক, কখন লােহার ��াব কেরন? লােহার ��ােবর মূল ব�ব� কী িছেলা ? ৩` ©. , BAA ALAA ABA BAN? ANIA AIC TT TST FI vA? © wsetifos `আ�জ�ািতক` 

`৬. জািতসে�র �ধান অ� সংগঠন �েলার নাম িলখুন। কত জন িবচারপিত িনেয় আ�জ�ািতক অপরাধ আদালত` &. CIPTTRTST OF ALT eta `গিঠত হয় ? এ আদালেতর �ধান কায�ালয় �কাথায়? ৩` SSI? g OMAR SAT PTT HAT?ATT rea© Fo Ga oat fea oeRifos oearY BMT `৭. �ানিজট ও কিরেডার িক? উদাহরণসহ বণ�না ক�ন। ৩` 4. Fafad 6 sfacura fe? Creag aft SHAT © be. `৮. সাফটা (SAFTA) �থেক বাংলােদশ িকভােব �িবধা �পেত পাের? ৩` APPGT (SAFTA) calce areeticw™t frwica Bae craw ATA?© `৯. ILO এর পূণ� �প িক? সদর দফতর �কাথায়? বাংলােদেশ এর একিট উে�খেযাগ� কায` d. ILO aa of a9) F? HTS HOA CHAN? TALC A ALG GeerAaT A PPA `ম উে�খ ক�ন। ৩` Geet FPA | `১০. G-7 �জােটর �দেশর নাম িলখুন। �দশ �েলার রাজধানীর নাম িক িক? ৩` 0. G-7 CRIES CHES ATT FETT CHT VTHTIA ATerATATA ATT FR FE? | fran `িব�ান ও �যুি�` s age 

`১১. ক�া�ার িচিকৎসায় �য িবিকরণ ব�বহার করা হয় তার ভােলা ও ম� িদক িনেয় আেলাচনা ক�ন। ৫` >>. aria ffs fafsat aaa Fal VI SrA SICA @ WH fas FCA SATA FAT `১২. �মাবাইল কল িকভােব দাতা হেত �িহতা �পেয় থােক ? ২` DR. HARA FH HSI AIST AOS AST cre ATH 2d `১৩. নারভাস িসে�েমর �াকচারাল এবং ফাংশনাল ইউিনটেক িক বেল ? ৩` DO. AAO PrerBeaa APTA ae SICA SOG TS FH <7 © 

Goran `�টকিনক�াল (কি�উটার সােয়�/কি�উটার সােয়� এ�ড ইি�িনয়ািরং)` FPieols ASIST `িবষয় �কাডঃ ১০৫ মানঃ ৮০` feaq HITE SOG TZ vo Iw Sheefernfae) 

1. (a) List down the layers of OSI model in top-down-manner. 4 

- (b) Find out the default mask, network address and broadcast address of the classical ipv4 address: 172.16.99.45  6 

2. (a) How do you define packet fragmentation ? Explain briefly the transparent and non transparent fragmentation with necessary diagram. 6 

- (b) Describe briefly the TCP/IP tunneling using appropriate diagram. 4 

3. (a) How does a compiler handle comments in source code? 5 

- (b) What is the difference between sizeof ‘c’+1 and sizeof(‘c’+1)? 5 

4. (a) What are the tasks of linker and loader? Describe briefly using examples. 5 (b) The complexity of merge sort is T(n) = 2T (n/2) + n. Explain how the above equation is derived ?  5 

5. (a) How does dynamic programming relate with divide and conquer approach? 5 

- (b) Does greedy algorithm always achieve optimal solution? If not, when does greedy approach achieve optimal solution? 5 

6. (a) Compare array and singly linked list with necessary diagram. 3 

- (b) Draw a binary tree of 15 elements and list out the elements in (i) Preorder (ii) In order (iii) Post order. 7 

7. (a) What do you mean by agile ? Mention its four values. 5 

- (b) How do you define 2-factor authentication? Give example. 5 

8. (a) Define electronic payment system (EPS) with necessary diagram. Name 5 type of EPS. 5 

- (b) Name and define five components of Data Communication System with necessary diagram.5 

`বাংলা` faea `িবষয় �কাডঃ ১০১ মানঃ ৪০` GTS S09 AIAZ 80 

`১. '�নিতক িশ�া ও মূল�েবাধ' িবষেয় �ব� রচনা ক�ন। ১৫` >. Cafes Prat e qencate fraca eta ADA PHA OC `২. সারমম� িলখুন : ৫` 2. Fare FAA & aefnr `ব�িদন ধের ব� ��াশ দূের` ta FR RT CA QO `ব� ব�য় কির ব� �দশ ঘুের` RO `�দিখেত িগেয়িছ পব�তমালা,` cafes fate earn,TA cafes `�দিখেত িগেয়িছ িস�ু।` freate Fra 

HA `�দখা হয় নাই চ�ু �মিলয়া` RA TS DE afer 

Mea `ঘের হেত �ধু �ই পা �ফিলয়া` ROS WY BS ml CHEAT `একিট ধােনর িশেষর উপের একিট িশিশর িব�।` att Fata FR 

`৩. িব��ৎ িব�াট িনরসনকে� সংি�� কতৃ�পে�র দৃি� আকষ�েণর জ� সংবাদপে� �কােশর উপেযাগী একিট প�` ©. Fags feeb Paracel APE PHC IB TER rayATESTON Bacal aah ofa `িলখুন। ৫` 

`৪. বাংলায় অ�বাদ ক�ন:` 8. SRAOA Pa: 

```

In Bangladesh only one person in every four can write. Many people who leave school

before they finish class five forget what they have learnt. After ten or fifteen years it is very

easy to forget how to write.

```

- @. `৫. িনেচর ���েলার উ�র িদন: ৫*২=১০` Frba ertevatiaGea far: @*2=30 

**1- 115** 

S. `ক. সি� ও সমােসর মেধ� উদাহরণসহ পাথ�ক� িলখুন।` Fh 8 FATA TET BrRaeAR mT FTA `খ. �িতশ� িলখুন:` 4. ofiors ferga: `সমু�, �মঘ, �কশ, �ঢউ গ. বাগধারা�েলার অথ�সহ বাক� গঠন ক�ন:` Ff, THMSTTSTMA AAS TAT BPA: `উ�র: ঝাঁেকর কই , হােড় হােড় , উনপ�াশ বায়ু , �চােখর বািল` W. `ঘ. �� কের বানান িলখুন:` BG Bes TAA ferge: `উ�র:মিরচীকা, �িবেশষ, �জ��, ��তম ঙ. উপসগ� ও ি��� শে�র উদাহরণসহ সং�া িলখুন।` . Gof @ fare “cra Boreacre Hewat TET 

English Subject Code: 102 Marks: 40 

1. Write an essay on the following topic using the hints given below: Importance of Primary Education 

[Hints: Introduction - Why this stage is urgent - Which subjects are urgent- Coeducation is necessary? - Conclusion] 

2. Write a letter to a foreign friend describing how our country coped with Covid19. 5 

3. Read the following passage and answer the questions that follow: 2 x 5 = 10 The secret of success in life lies in the proper use of time. Many of us are apt to forget that every moment is precious. Life is short and time is uncertain. During this limited and uncertain period, we have a lot of things to do. If we waste the precious minutes of our life in idleness, we will suffer and success will be difficult to achieve. It is only by utilizing every minute that we can hope to achieve success. Time once lost is lost forever. The young man who is afraid of work and idles away his time, is sure to find himself in later years a burden to himself and to others. There are some people who say that they have no time for reading books. They really deceive themselves. If they are punctual and industrious, they will find time to do everything. The industrious man has, in fact, the greatest amount of leisure, because he does his work regularly without waiting idly for the next day. 

Questions: 

a. How can we make the best use of time? 

- b. What will happen if we waste time idly? 

- c. When will success be difficult to achieve? 

- d. Why does an industrious man have sufficient leisure? 

- e. What will be the proper title of the passage? 

4. Correct the following sentences:5 a. This is the most unique idea. 

- b. He excels to speak English. 

- c. My health is more better today. 

- d. He wanted to discuss about the issue. 

**1- 116** 

- e. Corruption is a barrier for growth. 

5. Make sentences with the following:5 

- a. Bell the cat (�ঃসাহসী earl কাজ করা) 

- b. Come to light ( �কািশত aie হওয়া) 

- c. Fall flat (�ত�াশা eroyrt পূরণ না হওয়া) 

- d. Pass muster (যেথ� ale বেল গৃহীত হওয়া) e. Smell a rat (খারাপ Corcniferga �কােনািকছুর আশ�া Sree করা) 

- Haat `সাধারণ �ান` BIA – `৪০ িবষয় �কাডঃ ১০৪` 80 FTN CHGS908 `বাংলােদশ িবষয়াবলী` 

- `১. প�া ব�মুখী �সতুর �দঘ` >. MAT VIN GR CHT FS? **`�`** `কত? প�া �সতুর কারেণ �িত বছর কত শতাংশ িজিডিপ বৃি� পােব?` AM AGA BAC aif Jaa Fw Tort FSloHA aha wea? `২. বাংলােদশ রাে�র �� কয়িট ও কী কী? ��সমূেহর কায�াবলী সংে�েপ িলখুন।` 2. TRO AEA BE False SH A? BorTAd Saat eww FTL `৩. গণ �জাত�ী বাংলােদেশর সংিবধান কেব গৃহীত হেয়িছল এবং �কান তািরখ �থেক কায�কর হয়? সংিবধােনর` ©. AA SRereRt AeA HAST Fe TAS AAP Ae GHIA fae calesw LA BA? efter `মূলনীিত কী কী? ৪. ২০২১-২০২২ অথ�বছের বাংেদেশর আমদািন ও র�ািনর পিরমাণ কী িছল? বাংলােদশ �কান িতনিট �দেশ` 8. 2OAd-QoRe TAs ACAeA STAT @ aerfera aifaatet S fet? ete cA foal cre 

- ACHR `সবেচেয় �বিশ র�ািন কের এবং �কান িতনিট �দশ �থেক সেব�া� আমদািন কের?` CAPA ASIA Bea ae CTA HOMIE Cr CATS HEATH TATA Sea? `৫. জািতর িপতা ৭ই মােচ�র ভাষণ �কাথায় িদেয়িছেলন? ভাষণিটেক ইউেনে�া কতৃ�ক কেব িব� �ামাণ� ঐিত�` ¢. Bites Prot 4% aIea Sra care freee? Crafers BWrcat BIS wea fos anaes Afos 

- fears `িহেসেব �ীকৃিত �দওয়া হয়? এ ভাষেণর মূল ব�ব� কী িছল?` Bohs HEM VI? 4 OAC TA TWAT F fer? 

wretifos `আ�জ�ািতক ৬. ASEAN-এর পূণ� �প কী? এিট কখন গিঠত হয়? এর সদ� সংখ�া কত?` v. ASEAN-4a 41 BH? afB BAA HIS VAI? Ga WHAT ALA FS? `৭. সােক�র সদ� �দশ কয়িট ও কী কী? সব�েশষ সদ� �দশ �কানিট এবং কত সােল সােক�র সদ� পদ লাভ কের?` 9. FICE AT OT SALT GS MN? AAC AAT OT TANG AR PS AIC HCA AAT 1 ATS BA? `৮. ��ি�ট বলেত কী বুঝায়? এিট িকভােব স�ূণ� হয়?` >. fat saree F gaa? fe fewrcs wy I? `৯. নরিডক �দশ বলা হয় �কান �দশসমুহেক?` >. AAS OL SAM RA HT HARES? `১০. িব� বািণজ� সং�া কেব �িতি�ত হেয়িছল? এর কাজসমুহ সংে�েপ িলখুন।` do. fry ater Heal ace aiff arafaer? aa STePTAR a FLAT fre `িব�ান ও �যুি�` ¢ age `১১. রে�র কাজ কী?` dd. FORA `১২. পৃিথবীর বায়ুম�ডেল কী কী গ�াস আেছ? �কান গ�ােসর পিরমাণ সবেচেয় �বিশ?` da. aftaPITAa FH?weaT SS THT VCR? caPTA ATTA aifeTaTet ACHR CAPA? `১৩. কৃি�ম বুি�ম�া বলেত িক বুঝায়?` do. Shar gfarrat sarcw fe Gara? `১৪.  খােদ�র উপাদান সমূহ কী কী? মানবেদেহ িভটািমন িস িকভােব কাজ কের?` 38. aoa Bars AIR St SH? TTACATR feo fH fewrcs Se Fea? `১৫.  �ীনহাউজ বলেত িক বুঝায়?` o¢. Snaibaaacw fe gana? Garant `�টকিনক�াল পূণ�মান` afar – `৮০ িবষয় �কাডঃ ১০৫ [�াথ�ী �য-�কােনা একিট �টকিনক�াল িবষেয়র উ�র িদেবন।` [erat a-carat sate Garawo fITTfracra CHGSGea90¢ face SPACTTS `কি�উটার সােয়�` TITH 1. Minimize the following function using K-Map: 5 F (A, B, C, D) = Σ (0, 1, 7, 8, 13,15) 

2. Differentiate among primary, secondary and tertiary memory in a computer system (with examples). 5 

3. Write down a C program to check whether a given integer is a prime number.5 

4. Consider the following description of a university :10 

There are a number of departments (i. e, CSE, BBA, ME) in a university. Each department has a number of programs (e.g, CSE dept offers B.Sc in PIS CSE and M.Sc degree in CSE). Students are admitted for each program. Basic student information includes Name, Address, ID, Date of Birth, Dept Name and Program Name. Now your tasks are 

i. Create Entity-Relationship (E-R) diagram using standard symbols. 

ii. Write DDL statements to implement the E-R diagram. 

5. Distinguish between break and continue in a PM loop. Give suitable examples. 5 

6. Wy is NAT needed for an organization? What are its drawbacks? 5 

7. Compare BFS and DFS with respect to completeness, time and space complexity.5 

8. Explain SQL injection attack with an example Why is it very harmful? 

9. Write down the network address, P range and the broadcast address of the following IPv4 address: 5 

172.16.10.0/25 

10. What is meant by page fault in memory management? How is it handled? 5 

11. Convert the following prefix notation into an equivalent postfix notation: 5 

/*A + BCD 

12. What is the difference between link-local and global unicast address in IPv6? Give their ranges. 5 

13. Write down a recursive function to find out the sum of all digits of an integer. 5 

14. Compare sparse index and dense îndex in a database system. 

15. Compare MAC address, IP address and post number in TCP/IP network. 5 

###### **[SAE of Parliament Secretariate’23] ICT** 

1 a. What is cloud computing? How it is different from traditional computing methods? 

b. Explain the concept of software testing and describe any testing method. 3. 

c. What are the roles and responsibilities of a maintenance engineer in network security? 2 

2. a. What is the purpose of a network gateway? 2 

b. What are the different types of firewall technologies used to protect a network from unauthorized access? 4 

c. Explain the difference between symmetric and asymmetric encryption and give example. 4 

3. a. What are the most common two transport layer protocols used in TCP/IP protocol stack? Give example of applications where each protocol would be most appropriate. 5 

b. Describe the different types of topologies use in Local Area Networks (LAN). What type of topology is used in a generic computer lab in a university? 5 

4. a. What is the purpose of operating custom? 2 

b. What is World Wide Web and how does it differ from the internet? 2 

c. What is a virtual machine, what is its purpose in computing? 2 

d. Write a Binary search algorithm and explain with an example. 4 

a. Suppose you are browsing www.psc.gov.bd. Please list the protocols (along with their corresponding layer) used in getting the webpage in your browser. Also mention the source and destination address type used in Transport, Network and Data Link Layer. 5 

b. Show the steps required by DNS protocol to know the IP address of www.psc.gov.bd. 5 

6. a. Consider that a block of address is granted to a small organization. We know that one of the address is 10.100.108.39 and the subnet mask is 255.255.254.0. Find the total number of addresses in the block, the first address and the last address. What will be the network address for this block? 5 

b. Why do we need Network Address Translation (NAT) mechanism? Is it possible to build a network and access Internet without NAT? 5 

7.a. What is a RAID and what are its benefits? 2 

b. Explain SDLC with a diagram and what are the responsibilities of a Software Protocol Manager? 4 

c. Write a program in C that sum of digits of a number.4 

8. Write short notes on the followings:10 

a. e-Governance 

b. Smart Bangladesh 

###### **35** 

FAT `মৎ� ও �াণীস�দ অিধদ�েরর ই��া�র` @ ath afenerata `কি�উটার সােয়�` oPebra AI SAA `তািরখঃ ২০.০৬.২০২৩` 

ae `বাংলা পূণ�মান: ৪০` ARTA: 80 fea `িবষয় �কাড। ১০১` GHGyO 

`১. রচনা িলখুন: নারীর �মতায়েন সামািজক ভূিমকা। ১৫` >. aoaT frgA: Asta TORIC ETS STs ve 

`২. সারমম� িলখুন: ৫ �জােট যিদ �মােট একিট পয়সা` 2. rae fart: © Cae ahr care até oT -aray `খাদ� িকিনেয়া �ুধার লািগ'` festa Ufo `�িট যিদ �জােট অেধ�েক তার` air cance "Eatsordte arfOIA `ফুল িকেন িনেয়া, �হ অ�রাগী।` ‘areca `বাজাের িবকায় ফল ত�ুল �স �ধু িমটায় �দেহর �ুধা` fer Fat WAT `�দেয় �ােণর �ুধা নােশ ফুল` QACF SgACI FABIAEMT ATCTCATR EATET RTS `�িনয়ার মােঝ �সই �তা �ধা।` ACA CHS COT YT 

`৩. একিট �বসরকাির �িত�ােন িহসাবর�ক পেদ চাকিরর জ� আেবদনপ� রচনা ক�ন। ৫` ©. SBE TARTS afoOICA FTES 7107 DIBA GAT OITA ADA PPA | `৪. বাংলায় অ�বাদ ক�ন: ৫` 8. TAT OA FPA: & 

- Knowledge is vaster than an ocean. The more we gather knowledge, the more our thirst for it increases. So any kind of restriction on the pursuit of knowledge is not at all desirable. Everybody has the right to walk freely in the ocean of knowledge. `৫. িন�িলিখত �ে�র উ�র িদন: ৫×২=১০` ¢. Pafifis aces Gea fra: ¢x2=30 

- &. `ক. উদাহরণসহ সাধু ও চিলত ভাষার িতনিট পাথ�ক� িলখুন।` BrRAR TY @ DTS Urals foarte oefers FILA `খ. িনেচর বাগধারা�েলার অথ� িলখুন এবং বাক� রচনা ক�নঃ` x. fra atetatecaa OMT `ঝেড়া কাক,টাকার ��া ,ঠুেটা জগ�াথ,িতিড়ংিবিড়ং ,�েধর মািছ` PS Brea Sar ALOTOe fS **e** rretT GatefofwelaSe AST ADArea SPASwife 

Write an essay on the following using the given 

hints: Necessity of Physical Exercise 15 [Hints: Introduction- Benefits- Dangers of lack of physical exercise- How to perform it- Impacts on other parts of your lifeConclusion] 

2. Write a letter to your friend describing the effects of environmental pollution in Bangladesh. 5 

3. Read the following passage carefully and answer the questions that follow : 2 x 5 = 10 

Youth is the best time of life. This is the time when it is most necessary for one to remember the maxim, "As you sow, so will you reap." A man must sow the seeds of industry, truthfulness, honesty and other virtues in this season to reap the harvest of prosperity and happiness. Whatever 

takes root in a man at this time lasts throughout the rest of his life and moulds his future. So habits formed in childhood and youth influence the later life of a man. 

Questions: 

a. What is the best time of our life? 

b. What maxim should you remember in youth? 

- c. What should you sow in youth and why? 

- d. What lasts throughout the rest of a man's life? 

- e. What does influence the later life of a man? 

4. Change the following as directed: 1x5 = 5 

- a. Do not judge a thing - its appearance. (Use appropriate preposition) 

- b. I was there. It was autumn then. (Use 'when' to join the sentences) 

- c. You enjoyed the party, -? (Fill in the blank stre with a tag question) 

- d. I ordered it for my guest. (Make it passive) 

- e. It is more than honesty. (Make it positive) 

Make sentences with the following idioms and phrases: 1x5=5 

a. For good (িচরতের) 

b. Cry over spilled milk (বদলােনা যায় না এমন িবষেয় আে�প BIR করা) 

- c. Far beyond (�ত�াশার porn বাইের) 

d. See info ( spt মম� উ�ার ala করা) 

e. Call Up ( Way �রণ কিরেয় �দওয়া meat ) IAAT `সাধারণ �ান িবষয় �কাডঃ ১০৪ মানঃ ৪০` GIA FAR HITS 08 HAZ BO `বাংলােদশ িবষয়াবিল ৩x৫=১৫ ১. গণ�জাত�ী বাংলােদেশর সংিবধােন �মাট কয়িট অ�ে�দ ও কয়িট তফিসল রেয়েছ? মুিজবনগর সরকার কতৃ�ক` >. Aelerer wat ACA ALATA CIS FAG SHAT @ Ale Wehr acacR? wera AAs PHS HPS `জািরকৃত '�াধীনতার �ঘাষণাপ�' এই সংিবধােনর �কান তফিসেল অ�ভু` AAO CAPA! AS AAAI HT SVP GIGS `রেয়েছ? ৩ ২. ১৯৭১ সােলর ১০ এি�ল গিঠত বাংলােদেশর অ�ায়ী সরকােরর রা�পিত ও �ধানম�ীর নাম কী? ১৯৭১` 2. 9B A So fart Sw ATC UAT HASH TBS @ eras AT I? sad FITS `সােলর মহান মুি�যু� চলাকােল সম� বাংলােদশ �মাট কয়িট �স�ের িবভ� িছল? ৩` TAA GS YR DANS AAA ATO CATS SalS crea fawe far? © `৩. �স�টমািট�ন �ীপ �কান �জলায় অবি�ত? গদখালী �কান �জলায় অবি�ত এবং কী জ� িবখ�াত? ৩` 0. CPO Boi CH CHAT VARS? Meee IHIA CSATA VARS ae St Gay faATS? © 

`৪. বাংলােদশেক �ে�া�ত �দশ �থেক উ�য়নশীল �দেশর কাতাের ওঠার �যাগ�তা অজ�েনর আ��ািনক �ঘাষণা` 8. MAAC ATMS OH CATS VAT NT ATA SOTA ITA AUTO OHA SAUTE CATT HS `কত তািরেখ �দওয়া হেয়েছ? এই �যাগ�তা অজ�েনর জ� বাংলােদশেক কী কী মানদ� (Criteria) পূরণ করেত` OAC MST AACR? AS AAS HACIA GAT ATTIC FI St IMAG (Criteria) at FACS `হেয়েছ? ৩ ৫. পূণ` a. af **`�`** `প িলখুন:` FIBA: ‘Oa: `উ�র: ক. BIDA: Bangladesh Investment Development Authority.` S. BIDA: Bangladesh Investment Development Authority. `খ. NBR: National Board of Revenue. গ. VAT: Value Added Tax.` 

arettifos `আ�জ�ািতক িবষয়াবিল ৩*৫ = ১৫` feaarafer o*¢ = 3 `১.জািতসংেঘর িনরাপ�া পিরষেদর �ায়ী সদ� রা� কয়িট ও কী কী? ৩` >. wifeorced arret afters Bal THT AB als e St A? © `২. দি�ণ আি�কার �থম কৃ�া� ��িসেডে�টর পূণ�নাম কী? িতিন সাি� কত সােল �স �দেশর �থম ��িসেড�ট` 2. UPR STRPaT eet Farr caProwcha years S17 FOP IPE PO ICT OH CATA BATT CAPTCET fide `িনব�ািচত হন? ৩` ZA? © `৩. মা�ষ কত তািরেখ �থম চাঁেদ অবতরণ কেরন? এই চ� অিভযান ও চ�যােনর নাম কী িছল? ৩` ©. TAT FS Cifacs aq Dio Twat SoA? AS DU SAAT 6 DAAC ATT FH fA? w `৪. উ�র ও দি�ণ িভেয়তনাম কত তািরেখ একীভূত হেয়েছ? এ �দেশর দা�িরক নাম কী? �দশিটর �থম` 8. Baa @ aft fSrTOATT SS Cified MFT VA? 4 AEA MISHAS ATM? coma ater `��িসেড�ট �ক িছেলন? ৩` aires@ fe? © ‘WEA: `৫. পূণউ�র: ক. MIGA: Multilateral Investment Guarantee Agency.` @. AS. **`�`** FIBA: `প িলখুন: ৩` MIGA:©Multilateral Investment Guarantee Agency. `খ. IDA: International Development Association গ. IFC: International Finance Corporation.` 

fewer `িব�ান ও �যুি�  ২*৫ = ১০` @ aaf@ 2*¢ = 30 `১. �েধর রং সাদা হয় �কন? �েধর ঘন� মাপার যে�র নাম কী?২` D. CAA Ae AAT BI HA? CAA TG AT ACA AT STP `২. �াকৃিতক গ�ােসর মূল উপাদান কী? পািনেত হাইে�ােজন ও অি�েজন এর অ�পাত কত? ২` R. SPSS Ta ToT Samay St? AHfeS ASIC @ SPC LA SANS FS? 2 `৩. 'কি�উটােরর কাজ' কী? কি�উটাের িহসাব-িনকাশ করার। জ� উপেযাগী ��া�ামেক কী বলা হয়? ২` ©. SPSbreata See BH? SPrCorea fra art Sata Gay Vorcareh coreracsSt IAT A? 2 `৪. মা�েষর �ৎিপে� �মাট কয়িট �েকা� থােক? মা�েষর �দেহ পািনর পিরমাণ শতকরা কত ভাগ? ২` 8. TARA ache cud sald ecard eticw? TITAS CATR *ifea aifAATAI *TOF **S** TIA?AT & `৫. উি�দ ইউিরয়া সার �থেক কী খাদ� উপাদান �হণ কের? কীেসর অভােব ফসেলর পিরপ�তা িবলি�ত হয়? ২` ¢. Bier Bohra Hr calc SF aAT Bram aiRet Bea? As MVM WA fariPfaa BI? & 

> `�টকিনক�াল (কি�উটার সােয়�)` Garant (SPSbra AI) 1. Write the full form of the following terminologies:10 TCP/IP, DHCP, XML, NAT, CDMA, DNS, NoSQL, ICMP, SMTP, DNN 

2. Write a Program in C programming language that prints summation of the following series: 1 +1/2+1/3+1/4+1/5+…1/n, where integer n will be input to your program.10 

3. a. Define the term "Indexing" in Databases. What is its major benefit? 6 b. What is the difference between CHAR and VARCHAR data types? Explain with examples. 4 

4. a. How can you define the subnet mask: 10.2.1.3./26? 5 b. What is the usable number for host IP addresses on a network that has a/26 mask? Explain. 5 

5. a. Identify the differences between 1G, 2G, 3G, and 5G, and networks? 5 

b. What is the fundamental difference between fourth industrial revolution and the other three industrial revolutions? Describe briefly.5 

6.a. Describe the differences between combinational and sequential circuits with necessary diagram. 5 

b. Simplify the following Boolean expression using NAND gates only: (A + B) (C + D) 5 

7. a. How page fault is handled by Operating System? Explain with necessary diagram. 5 

b. Compare OPT and LRU page replacement algorithms using the following reverence 

string: 0531205416235072183051 

8.a. i. In how many ways can three boys and two girls sit in a row? ii. In how many ways can they sit in a row if the boys and girls are each to sit together? iii. In how many ways can they sit in a row if just the girls are to sit together? 6 

b. A bag contains six white marbles and five red marbles. Find the number of ways four marbles can drawn form the bag if i. two be white and two red in they must all be the same color. 4 

`বাংলােদশ জাতীয় সংসদ সিচবালেয়র কি�উটার ��া�ামার` **36** `০৮.০৫.২০২৩` 

`১. �ব� িলখুন: তথ� িব�েব ই�টারেনট। ১৫` >. oem fare: Gey fazed SSATAT | ¢ `২. সারমম� িলখুন: ৫` 2. rat fare: © 

`একঝাঁক হিরয়াল পািখ সাদী` GOw `উেড় �গেল মেন হয়।` CICA YS `�ই পােয় �হঁেট` elA CEA POT `কতদূর �যেত পাের` FT `মা�ষ একাকী।` ATSGBF ACA| 

`৩. এ�েশর বইেমলা স�েক� �বাসী ব�ুেক একিট প� িলখুন। ৫` ©. AEC ACTA HC SATA TECH AAG ove FIAT © `৪. বাংলায় অ�বাদ ক�ন:` 8. TTA OAT FPA: 

Nasiruddin the emperor of Delhi lived like a poor man. He had no pride in mind. He was equally kind hearted and mild. He never cared for his brown comfort. His only thought was concerned with the wellbeing of the subjects. He copied the Quran and sewed caps by his own hand. 

`৫. িনেচর �িট �ে�র উ�র িদন: ৫×২=১০` ¢. reba afb ercsia Gea fA: @x2=30 

SB. `ক. উৎস অ�যায়ী বাংলা ভাষার শ�ভা�ার কত �কার ও কী কী? উদাহরণসহ িলখুন।` BOF OAT AUT OAs *ASISIA Fo asa @ St A? VTA fare `খ. নদীর পাঁচিট সমাথ�ক শ� িলখুন।` a. ala itl oats tH fergat 

English 

- 1.Write an essay on Your Career Planning'. 15 

[Hints: Introduction - Your dream - Rationale -How to achieve (planning) - Conclusion.] 

2. Write a letter to the Mayor of the South City Corporation drawing his attention to establish a playground in your locality.5 

3. Read the following passage and answer the questions that follow:2 x 5 = 10 The term 'diaspora' is used to refer to people who have left their homelands and settled in other parts of the world either because they were forced to do so or because they willingly migrated. The word is increasingly used for such people as a collective group or a community. The world has seen many diasporas for centuries, but scholars have been studying this phenomenon with great interest only in recent decades. 

Among the history of great diasporas is that of the Jews people, who were forced to leave their lands in ancient times. The Aryans who moved from central Europe to the Indian subcontinent thousands of years ago is also a noteworthy diaspora although the causes of their movement are still unclear. In twentieth century history, the Palestinian diaspora has attracted a lot of attention and has been a cause of concern for world leaders because of the plight of Palestinians. There have been massive diasporas in Africa too over the centuries either because of war or because of the ravages of nature. But the chief reason why the phenomenon of diaspora is attracting so much attention is globalization. 

- a. Which people are called diasporas ? 

- b. Who are the major diasporas the world has seen so far ? 

- c. What forced Aryans to become diasporas in the Indian subcontinent? 

- d. What are the causes of diaspora in Africa? 

e. What does the word 'globalization' imply in the last sentence of the passage? 

4. Make sentences with the idioms: 5x1=5 

a. A blessing in disguise (মে�র | ভােলা) - Losing that job was a blessing in disguise really-now 

b. Out of work ( Ger �বকার/কম�হীন Pa ) - He lost his job a year ago and has been out of work ever since. 

c. Catch someone's eye (�ি� fe Sareea আকষ�ণ করা) -I went shopping for a new dress but nothing caught my eyes. 

> d. On point ( We স�ক apie /�াসি�ক) you're saying is on point! Nothing that 

e. Piece of cake (খুব সহজ) - The exam was a piece of cake. 

5. Correct the following sentences: 

a. There are trees on both side of the road. 

- b. You had better not gone there 

- c. He promised he will work for our team. 

- d. I have decided to quit my job a week ago 

- e. It seemed that the day will never end. 

`সাধারণ �ান` ATTA aT `পূণ�মান: ৪০` aefarr: `িবষয় �কাড : ১০৪` fea GHG :80308 `বাংলােদশ িবষয়াবিল-১৫` 

`১. বাংলােদেশর সেব�া� আইেনর নামসহ আইনিটেত কয়িট জা ও অ�ে�দ অ�ভু` 9. TRANCE A OTRAS ATR MRA TS Palo Gl o TAN TIGS `আেছ উে�খ ক�ন।` ory Teast FPA `২. 'অসমা� আ�জীবনী' ��িটর �কাশকাল এবং �কান সাল পয�র জীবনী িলিখত হেয়েছ উে�খ ক�ন।` 2. TANS STS AalGs ocerereprey ae cH Art ona Gleatt Ferfarw eae Veal Baa | vo. `৩. 'িনিষ� �লাবান', 'হাঙর নদী ��েনড' এবং 'আমার বড় ১। রােশদ'-এ িতনিট উপ�ােসর উপর িভি� কের কী কী` fifa Grate, "Rhet THT CATTE' Gee TTA TW 91 aIa'-4 foals Gomera Ga ffs sea St St vation `চলি�� িনিম�ত হেয়েছ? ৩` FAS Brae? © `৪. গণ�জাত�ী বাংলােদশ সরকােরর বত�মান �ধানম�ী কতৃ�ক গৃহীত ১০ িট িবেশষ উেদ�েগর নাম িলখুন।` 8. AAAS MCT HAHA TSA SATA FHS TAS do 1B farmra Berroa ae Feta `৫. বাংলােদশ �ড�া ��ান (BDP) ২১০০ স�েক� সংি��ভােব িলখুন।` @. UATCBT ATTA (BDP) 2300 FATS AePRSSIC FTAA WeeHfSS-s¢ `আ�জ�ািতক-১৫` v.aretties `৬.আ�জ�ািতক স�েক�র িভি� িহেসেব �য িতনিট িবষেয়র কথা বাংলােদেশর সংিবধােন উে�খ আেছ �স�েলা কী` aire foie ord @ foal fear Set aeaticaea Aearet Grae BCR Teta FT `কী? ৭. জািত কােক বেল? জািতসংঘ সনদ �কান সােল কায�কর করা হয়? জািতসংেঘর �কান অ�সং�ার �পািরেশর` 9. Bite See eT? SforeT HAM CHA FT PLA Pal A? SHOTS CHIN SHAAN Frias fofere `িভি�েত জািতসংেঘর নূতন সদ�পদ �দওয়া হয়? ৩` MfonTed TOI ATM SAT BI? © by. `৮. িজএসিপ (GSP) কী? উ�য়নশীল �দশ িহেসেব যু�রাে�র িনকট �থেক বাংলােদেশর উ� িজএসিপ �াি�` RAPA (GSP) Ft? Garey orl ores Youre aS cates AeA GS fear ante Pee `স�েক� সংে�েপ িলখুন। ৩` ORT FAT © `৯.যু�রাে�র �কান ��িসেড�ট �ীতদাস �থা িবেলাপকারী িহেসেব �ীকৃত? তাঁর �দওয়া িবখ�াত ভাষণিট কী নােম` DISA SM cahrews Fron ater feast as APS? Cla Hea fees orais St Arcst RPO? `পিরিচত? �কান সােল যু�রাে�র �ীতদাস �থা িবলু� হয়?` CHA AIT TSA SOU aiett FAs BA? `১০. ভারত ও চীেনর মধ�কার অথ�ৈনিতক স�ক� িবষেয় সংি��ভােব আেলাচনা ক�ন। ৩` d0. BAS @ Bera Tes Uafos res fIaTT AEST UCTDAT FPA | © fata `িব�ান ও �যুি�-১০` @ agfe-yo `১১. হাইেপা-থাইরয়িডজম �রাগিট কীেসর অভােব হয়? কী কারেণ কচু �খেল গলা চুলকায়? ২` dd. Bacail-aeaafeerr cars Sed THT RI? Sh PAC PE CATA AA ASIA? & `১২. অিতির� শক�রা জাতীয় খাদ� �ািণেদেহ কী িহেসেব জমা থােক? �য সকল ��ােমােজাম জীেবর �দিহক` D2. Betas eat ESTA aT emTferTR Fr ATS STAT ACE? A AKA HTCATICT `�বিশ�� িনয়�ণ কের �স�েলা কী? ২` Cafaiey Freel Sea HUTA SY? & Giteaa Cafe `১৩. এমেবেডড িসে�ম কী? এ িসে�েম চলেত পাের এমন চারিট ব�বহািরক যে�র নাম িলখুন। ২` 20. GATSG Parrba Hh? g PacrSor pew ie ATA Drale aTaaliae Aaa AT fT S `১৪. নবায়নেযাগ� শি� কী? এ জাতীয় �য-�কােনা ৪ (চার) িট শি�র উদাহরণ িদন। ২` 98. FAA * HS BA? 4 GTS I-HICAT 8 (DIA) fF “fea Baraatfrat & `১৫. মানবেদেহর �াভািবক তাপমা�া কত িডি� ফােরনহাইট? থােম�ািমটাের পারদ ব�বহােরর কারণ কী? ২` d@. TITHE BETS WIAA FS Sf PATARS? aeMiorea aM aera Prat MN? & Geran `�টকিনক�াল (কি�উটার সােয়� এ�ড ইি�িনয়ািরং/কি�উটার সােয়�)` (SPS ATA ow Serna SPebra ACA) `পুরনমান-৮০ িবষয় �কাডঃ ১০৫` BRTAA-voFIAT HGS SO 1. a. What do you understand by polymorphism? Describe with an example.5 b. What is the difference between 'Method Overloading' and 'Method Overriding? Describe with an example.5 

2.a. In requirement analysis, there are two types of requirements among others: Functional Requirements' and 'Non-Functional Requirements Explain their needs appropriate examples. in software analysis with appropriate example. 5 

b. Give an example of 'White Box Testing' and quote an example of 'Black Box Testing 5 

3. a. What are IP classes and how can you identify the IP class of a given IP Address? 5 

b. What is meant by 127.0.0.1 and Local host. 5 

4. a. What is 'Race Condition'? Provide an example of Race condition in Banking 5 

b. How does deadlock detection algorithm work? 5 

5. a. Why do we need algorithm analysis? 5 

b. What are the differences and similarities 5 between 'Dynamic Programming' and 'Greedy Algorithms'? 

6. a. Oracle Database has two data types: CHAR and VARCHAR. What are the differences between those two data types. 5 

b. What do you understand by 'Database Normalization'? Why is it necessary to do Normalization? 5 

7.a. Write a program that will output 'EXAM' 100 times. You can use pseudo code or any programming language.5 

b. Is 'Ransomware' a virus? Explain your answer by describing Ransomware. 5 

8. a. What are the differences between 'Microprocessor' and 'Micro-Controller'? 5 b. What do you understand by 'Supervised Learning and 'Unsupervised' Learning? 5 

`১. 'ভাষা আে�ালেন ব�ব�ুর অবদান' িবষেয় একিট �ব� রচনা ক�ন। ৫` >. ORT CHITA TITER OAT A AAG ora ADA PAPA `২. সারাংশ িলখুন: ০৩` 

Bares `�ােনর �ৃহা ছাড়া িশ�া ব�থ�তায় পয�বিসত হয়। তখন পরী�া পাশটাই বড় হয়। এেত পরী�া পাশ করা �লােকর` RT IGT Pret AON a] VA GIy HAH AMGIS TW VA ATS AH AMT SAT CTA OS `অভাব না থাকেলও জনীর অভাব �দখা �দয়। পরী�া পােশর �মাহ যিদ ছা� ছা�ীেদর উৎকি�ত রােখ, তেব আন` A MSS SAA HSS OHA AA | AAT ACH GTR Alt Bla BNO Vesfow ace, Ord OIA PPA `িনব�াসেন চেল যায়। পৃিথবীেত অ�য় বাসন লােভর জ� ত�ণ সমাজেক �ােনর �িত উৎসাহী কের তুলেত হেব।` De A AACS OHA APA ALTA GAT Gee AMES BCAA aifs CeAra Heat GATS VA ART `পরী�া পােশর �মাহ �থেক মু� না হেল ত�ণ সমােজর সামেন কখেনাই �ােনর িদগ� উে�ািচত হেব না।` HCA CR CUE LS A ACT WP ACSA ACT PATS Cetera fiw Teamiidw Ae AT `৩. শহেরর যানজট িনরসেনর জ� যথাযথ কতৃ�পে�র দৃি� আকষ�ণ কের সংবাদ পে� �কােশর জে� একিট প�` ©. ARCA TAGS PPA GAT VAI SHCA AB SPS Bea ALAM AAC ABIES GEA BAS 2 `িলখুন।` 

`৪. বাংলায় অ�বাদ ক�ন: ৬` 8. AST SA FAT: Y 

Air is an important element in our environment. Clean air is essential for life. But air can be polluted in many ways. One thing that pollutes air is smoke. Smoke mixes with the air and pollutes it. 

`৫.(ক) বানান�েলা �� কের িলখুন: গীতা�লী, িনিব�েরাধী 2 (খ) সাধু ও চিলত রীিতর সব�নাম ও ি�য়াপেদর একিট কের পাথ�ক� িলখুন। ১` @.(8)(a) IGTATTOTT@ diate SifoaGH BeaASTFTA:¢ feraiordThoreet, ffacaasae ea2 arelf **e** rs > `(গ) ণ-� িবধােনর �ইিট িনয়ম িলখুন। ১` (ot) 9 faatera Wate frre fare > `(ঘ) 'কথা' শ�িট িভ� �িট অেথ� �েয়াগ কের �ইিট বাক� িলখুন। 2` (3) Sar afb for AS oed eicait wea YRIG sre fare 2 `(ঙ) বাগধারা �ইিট যথ�াথ অেথ� �েয়াগ ক�ন: কলমেপষা, উনপাঁজুের ১` (e) aietat Gate atte od eat FA: SoC, Baie 5 

English 

Subject Code: 102 Marks: 40 

1. Write an essay on the following topic using the given hints:15 Tourism in Bangladesh [Hints: Introduction- places of scenic beauty places of historical interest and cultural heritage government and non-government agencies for tourism promotion- Conclusion.] 

2. Write a letter to the Mayor of Dhaka South City Corporation requesting him to take necessary steps against mosquito menace. 2 

3. Read the following passage and answer the questions that follow: 

As his reputation as a scientist grew, he started facing challenges of a different kind. Stephen Hawking started losing control over the muscles of his body as he gradually became the victim of Gehrig's disease. Since the age of thirty, he confined himself to a wheelchair with no power to control his body except for some limited movements of his handy and head only. He could speak solely through a computer with a voice synthesizer that converted his message into sounds. Even such a challenging physical condition did not dampen his spirit or slow down his work. Stephen relentlessly worked using his computer to conduct his research on physics and give public lectures till his death on March 14, 2018. The day is now known as Pi Day. Stephen was seventy- six when he died. Throughout his illness, he received nursing service from an American organization 

Questions: 

- (a) Who was Stephen Hawking? 

- (b) What was the physical challenge faced by Hawking? 

- (c) What allowed him to work despite his illness? 

- (d) How is Hawking's death remembered today? 

- (e) Who provided the nursing facilities for Hawking? 

4. Correct the following sentences: 

- (a) He has resigned his post. 

- (b) She went to England and others. 

- (c) Mother Teresa came to India with a view to help poor. 

- (d) The quality of the students are not satisfactory. 

- (e) Good night, Madam, how do you do? 

- 5.Make Sentences with the following: 

- (a) Hard, heard 

- (b) Push back 

- (c) Deal with 

- (d) Digitization 

- (e) Stop over 

- `সাধারণ �ান` 

- `িবষয় �কাডঃ ১০৪       মানঃ ৪০` 

- freq W308Trae aT= -AIAZ 80 

- `(ক) বাংলােদশ িবষয়াবিল ১. সংিবধান কী? চারিট সাংিবধািনক �িত�ােনর নাম িলখুন। 2` >. aa A? orate aeaeaite afar are rer 2 `২. �ানীয় সরকার বলেত কী বুঝায়? বত�মােন �কান �কান পয�ােয় �ানীয় সরকার �িত�ান রেয়েছ?` ७ `৩. �মগা �ক� বলেত কী বুঝায়? বত�মান সমেয় �মগা �ক� বা�বায়েন বাংলােদেশর চ�ােল�সমূহ উে�খ ক�ন।` ©. AT AB} THLS St FAN? THT ANA UAT ABH ABTA TACT DUC PATR Veale FA | `৪.  �ড�া ��ান কী? �ড�া ��ােনর �ধান ৪িট উেদ�ােগর নাম িলখুন। ২` 8. CUeTT ATA A? WeoT aprera Ata Bio Borsiera aT fer! & `৫. �াট� বাংলােদশ স�েক� একিট টীকা িলখুন। ৩` @. FD Tree HPs CaS Bret FA © 

- `(খ) আ�জ�ািতক িবষয়াবিল` (2) oractifes farareter `৬. তাইওয়ান �ণািলিট আেমিরকার কােছ �েমই ���পূণ� হেয় উঠেছ �কন?` v. URSIN anes orators SIA HAS wHQ A’ AA CI A? `৭. িবল ও �মিল�ডা �গটস ফাউে�ডশন (BMGF) কী এবং এ ফাউে�ডশেনর ২িট মূল কােজর নাম উে�খ ক�ন।` 4. fae @ CaferwT CGH VISTI (BMGF) Ft ae g MSCs Af yer H1cera ATT Cee Fea vb. `৮. িব� খাদ� কম�সূিচ (WFP) কী? এিট কেব গিঠত হয় এবং এর সদর দ�র �কাথায় অবি�ত? 2` fog aay haf (WEP) B17 afb ara aw Ba ae aa HA HA HIATT BAAS? 2 `৯. �ােটা কী এবং কেব �িত�া করা হয়? �ােটার মূল উে�� কী? 2` d. AUC St ae Bea AAO Far A? ATTA Fat Gowns MP 2 `১০. পািক�ান ও ভারেতর মেধ� বত�মােন িবরাজমান স�েক�র উপর সংে�েপ আেলাকপাত ক�ন। ২` D0. MBA 6 Wracwa Aes ASA faery HPs Gores AHL SCBA FPA | 

`(গ) িব�ান ও �যুি�` (*1) faeereorg `১১. তাপ ও তাপমা�া কী? ২` dd. BI} SATAHM? & `১২. িভটািমন িড এর অভােব আমােদর কী কী সম�া হয়? 2:` d2. feria fe a TwICa OTIC SF HPT BI? 2: `১৩. িডেমর পুি��ণ িলখুন। ২` yo. feta afBert fra `১৪. সফটওয়�ার কী? সংে�েপ ব�াখ�া ক�ন। ২০০` 38. AHSSl? AHADAT FHA OO `১৫. OTT ��াটফম� বলেত কী বুঝায়?` d¢. OTT abet aarcw St Gary? 

Gahan **�টকিনক�াল (কি�উটার** shatita **�টকেনালিজ** cece **) িবষয় �কাডঃ** cate **১০৫** 

**মানঃ ৮০** 

1. Name and define the components of a computer system. 3. 

2. Briefly describe computer architecture with diagram 

3. Describe the classification of computer software. Differentiate between system and application software. 

4. What are the universal gates? Draw AND, OR and NOT gates by using universal gates. 

5. Write short notes on DNS, Cloud server and Fewall. 8 

6. Differentiate between traditional and electronic payment systems. 2 

7. Describe different types of electronic payment system. 2. 

- 8.Explain the importance of cyber security law. 

9. Explain the basic concepts of internet security 

10. Name and define the major tasks that a DBMS enables users to do. 2 

11. Describe the phases in the System Development Life Cycle (SDLC) 

12. Describe the challenges to application of MIS in Bangladesh. 

13. Which disciplines contribute to an intelligent system? Briefly narrate the potentials of artificial intelligence. 

14. Write short notes on ROM, RAM and Cache. 8 

15. Describe the current challenges to building a Digital Bangladesh. 2 

16. Explain access, security and privacy issues in information technology 

QT `খাদ� ম�ণালেয়র �নটওয়াক�/ওেয়বসাইট ম�ােনজার` TANT STS/STAPTADAD `পরী�ার তািরখঃ ২১.০৫.২০২৫` AIA OifAAls 29.0€.2ORETTTCTETA **38** `পূণ�মান -২০০` afar -200 WAR- `সময়- ৪ ঘ�া` `[�িতিট িবষেয়র জ� �থক উ�রপ� ব�বহার ক�ন]`  

```

বাংলা

```

- `িবষয় �কাডঃ ১০১ মানঃ ৪০` 

- 1. fice `িনেজ িশেরানাম �তির কের যু�, শাি� ও �ুধা িবষেয় একিট �ব� িলখুন।` Fras tofa aca Za, “ISfeaq CHGS6 EAT frac Gate0 HAZarea 80ferear 2. `সারমম� িলখুন: �হ মহাজীবন, আর এ কাব� নয়` RAHM, `এবার কিঠন, কেঠার গেদ� আেনা,` IF 4 PT AT 

- mm `পদ-লািলত� কংকার মুেছ যাক` SatsMET BA,OT SHIABTS A **C** HATR AS SICA, `গেদ�র কড়া হাতুিড়েক লাজ হেলা।` 

- STE `�েয়াজন �নই, কিবতার ি��তা-` AB, BST FFI sur `কিবতা �তামায় িদলাম আজেক ছুিট` com fare rece BF EMA `�ুধার রােজ� পৃিথবী গদ�ময়:` aicen oeat TATA: `পূিণ�মা-চাঁদ �যন ঝলসােনা �িট।` offan-bia 

- 3. Welfoe `�ন�ীিতমু� সমাজ গঠেন পািরবািরক িশ�ার ভূিমকা কতটু�, এ িনেয় পি�কায় �কােশর উপেযাগী একিট প�` sareGIA AePITEATcorr onfsataeAB fra Set Ses, 4 fica afaers caret Borat aete 1a `িলখুন।` 

- 4. TA `বাংলায় অ�বাদ ক�ন:` SAT Sa: 

- A gentleman is one who never causes pain to others. This description is short, but as far as it goes is correct. He is always polite and considerate. He carefully avoids whatever may cause even a slight shock. with his associates. 

- 5. (#) `(ক) ভাষায় উপসগ� ও অ�সগ� কীভােব কাজ কের আেলাচনা ক�ন।` Sra Dorf 6 EPH Shorea PIS Sea GULATTAT FPA | `(খ) বানােনর িনয়মসহ �িমত �েপ িলখুন:` (2) aratera Frenprg eifine aici erga: OS, `অংক, �সম, ইংেরজী, মনেযাগ, পদাবলী।` IPM, BAT, TACT, MATA| 

ENGLISH 

Subject Code: 102 Marks: 40 

1. Write an essay on 'The Internet' using the hints given below: (Hints: What internet is Great Communication tool-Various uses-Storehouse of information-Impact of the internet on our daily life- Social impact- Changing life Uses and abuses-Conclusion.) 

2. Write a letter to the officer-in-charge of your police station to provide regular police patrol in your locality to prevent crimes. 

3. Read the following passage and then answer the questions that follow: The Change of Climate is a major concern nowadays. The worst of all the problems that affects all the flora and fauna is the climate change. There are many plants and animals that are vulnerable to climate change. As a result of increasing temperature, they are likely to be extinct from nature. The reasons of increasing temperature are multifarious. Every day many industries, mills and factories in different countries are excreting Carbon Dioxide. Besides, a significant number of vehicles ply on the roads creating smoke which emits Carbon Dioxide. In addition to these, industrially developed countries are emitting tons of Carbon on the sea, which is indirectly responsible for producing Carbon Dioxide. The more Carbon Dioxide will increase, the more the temperature will increase. Over the last century, the sea level had risen by 1020 cm possibly in response to global warming. Question: 

   - (a) Which is the worst of the problems that affects plants and animals? 

   - (b) What may happen to plants and animals as a dire consequence of increasing temperature? 

   - (c) What are the two major reasons for increasing temperature in the world? 

   - (d) How does global warming affect the sea level? 

   - (c) What message does the passage convey? 

4. Rewrite the following sentences and use the idiom as directed: 

   - (a) The cost of all these articles have risen. [Correct the sentence] 

   - (b) The film is definitely worth to see. [Correct the sentence] 

- (c) Light alternates-darkness. [Fill in the blank with an appropriate 

- preposition] 

- (d) What he says is based-truth. [Fill in the gap with an appropriate 

- preposition] 

      - (e) I (to know) him for a long time. [Use the right form of the verb] 

      - (f) When he (takes) his food normally? [Use the correct form of the verb] 

      - (g) The doctor advised me to take complete rest. [Make it passive] 

      - (h) Our goal has been achieved. [Make it active] 

- (i) Amzad said to me, "I shall be grateful if you help me." [Turn into indirect 

- speech] 

      - (j) Make a sentence with the idiom: 'in respect of 

- `বাংলােদশ িবষয়াবলী` 

- 1. `গণ�জাত�ী বাংলােদেশর সংিবধােনর �কান ভােগ �মৗিলক অিধকারসমূহ বণ�না করা হেয়েছ? িচ�া ও িবেবেকর` AAATOR AACA ALAA CHA SC ATaTS STsrATTR Vat Fal AACR? fost e facacaat MATH `�াধীনতা এবং বাক �াধীনতা সংিবধােনর �কান অ�ে�েদ বণ�না করা হেয়েছ?` Ia AS AA Aas HA THAT IAAT Pal AACR? 

- 2. `"মন জাি�স' কী? এিট �কন ঘেট?` “a Gio BH? af cor ICH? 3. `"রাইেফল �িট আওরাত" �ে�র মূল উপজীব� িবষয় কী? �লখেকর নামসহ বাংলােদেশর মুি�যুে�র উপর` "aRora SF oleate" aga ya Voss fara MH? creacea ATTA ATTA BfeIrad Bria fats `িলিখত িতনিট উপ�ােসর নাম িলখুন।` foafé Borsmiora 

- 4. sicteg `গণত� �িত�ায় িনব�াচন অ��ােনর ��� িলখুন।` afeora ion BDICAAare fet **e** ry FTA 

- 5. `১২ এি�ল ২০২৫ তািরেখ অ�ি�ত "মাচ� ফর গাজা" এর আেয়াজক সংগঠেনর নাম কী?` 92 AFT LORE WHAT TABS "AG HI ME" LA TTA HASTA ATT BP 6. ASIC `বাংলােদেশর বত�মান অ�বত�ী সরকার কত তািরেখ গিঠত হয়?` ASIA TSI AIGA Fo wiface Io BI? 7. `২০২৫ সােল �িতবাদী তা�ণ� ��ে� '�াধীনতা পুর�ার' কােক �দান করা হয়?` LORE AN AAMT OP CHCA “ARTOT AAI PCE SMTA FAT VA? 

         - **আ�জ�ািতক** arent **িবষয়াবিল** 

8. Fearee িব�ায়ন �ি�য়ার eiferatat মূল চািলকা ~fe শি� (Driving Forces of Globalization) �েলা erat কী কী? 

9. পূণ ucla **�** প িলখুন । 

   - ক. TH-OF  খ. THAAD গ. BIMSTEC 

10. মানিবক কিরেডার কী? BOCEA ইউে�ন CH �কান ব�রেক THAT মানিবক কিরেডার �ঘাষণা careett কেরেছ? 11. সবুজ অথ�নীিত wets ' কােক বেল? কাল� ref বুরকােতর মেত সবুজ wes অথ�নীিত কয়� Fat িবষেয়র উপর িনভ�র fea কের? কী কী? 12. পৃিথবীর aegas সব�বৃহৎ �ীপ�র Writs নাম কী? এ� ab �কাথায় crane অবি�ত oAPS এবং | �কান CHIN �দেশর CHa িনয়�ণাধীন PRgAIRA, ? 13. Beare যু�রা� সরকােরর নতুন দ�র wea "িডপাট�েম� feaibors অব গভণ�েম� tertord Bec ইিফিসেয়ি�" এর ——atate �ধান িনব�াহী fidial কম�কত�া lost �ক ce ? 

14. অপােরশন আয়রণ �সাওম ones কী? 

   - **িব�ান** fer **ও �যুি�** age 

15. ন�ােনা �টকেনালিজ কী? কৃিষ ��ে� ন�ােনা �টকেনালিজর �েয়াগ স�েক� িলখুন । 16. এি�বােয়া�ক SobE ও এি�বিড PGE এর Ae মধ�কার পাথ�ক� eT িলখুন । 17. cite �রিডও-�থরািপ casi কী? Ca �কান �রােগর AICI িচিকৎসায় মূলত: এ� ab ব�বহার Baa করা হয়? 18. ১ িপেকা �সেক� AS বলেত কী বুঝায়? 

**1- 131** 

19. ' wr �ার িলংফ" কী? 

###### **�টকিনক�াল** Geert 

**িবষয় �কাড** core **: ১০৫ মান: ৮০** 

**[ইংেরিজ অথবা বাংলা �যেকােনা** etc **এক�** aeie **ভাষায়** acla **�ে�র উ�র** Gea **িদেত হেব । তেব �টকিনক�াল** cohertet **শ��েলা** ABST **ইংেরিজেত** Crt **�লখা �যেত** aCe **পাের ।** aatrice **�াথ�গণেক �টকিনক�াল** corre **িবষেয় ক, খ অথবা গ** ASIA **�যেকােনা এক�** aeib **�েপর �ে�র উ�র িদেত হেব ।** 

   - �প 6 -ক: | কি�উটার SPRACHE সােয়� AICI / কি�উটার SP সােয়� AIT aS এ� ইি�িনয়ািরং Beirne 

1. Explain the concept of polymorphism in object-oriented programming with example. 

2. Write an algorithm to detect a cycle in a directed graph. 

3. Design a full adder using two half adders and an OR gate. 

4. Compare "Paging" and "Segmentation" memory management technique. 

5. What is a Man-in-The-Middle (MitM) attack? How can it be prevented? 

6. Write a C program to find the sum of digits of an integer number using "recursion" 

7. Write down the Pseudo Code for recursive binary search algorithm. Use the following function definition: binary Search (array, target, low, high). 

8. Write down the names of different stages of instruction pipelining in a multicycle data path architecture. What is a data-hazard in a pipelined data path? 

9. There are 3 tasks P., P₂, and P. The arrival time and duration of each task is given below. Apply the round-robin scheduling algorithm with quantum size 20 to schedule the tasks in a single core machine. Calculate the turnaround time for each task. (All tasks have the same priority) 

|Task|Arrival time(ms)|Duration (ms)|

|---|---|---|

|P1|0|40|

|P2|5|40|

|P3|10|20|

10. Show the pictorial representation of TCP 3-way handshaking protocol for establishing a connection 5 between a server and a client. 

11. Find the network address, subnet mask, broadcast address, and usable host IP range for the following IP address: 

192.9.205. 31/16 

12. Explain the differences between Second Normal Form (2NF) and Third Normal Form (3NF) with 5 examples. 

13. Given a Patient table in a hospital database below. 

||Patient|

|---|---|

|Patient ID|Discase Norme|

|1|Covid-19|

|2|Dialysis|

|3|Covid-19|

|4|Dengue|

Write down an SQL query to display the total number of patients under cach disease category. 

14. Write down the differences between Agile model and Waterfall model in Software development. What is white bos testing? 

15. Briefly explain Supervised fening, unsupervised learning and reinforcement learning. 

16. Bricily explain phising attack and denial of service (DoS) attack. 

      - �প-খ: ইনফরেমশন এ� কিমউিনেকশন �টকেনালিজ 

1. a) Define the term "SSD". Briefly describe the working principle of "SSD". b) Compare and contrast between CPU and GPU. 

2. a) Write about notes on i) Virtual memory, and ii) Cache memory. b) Use the Karnaugh Map to simplify the following function. f(A,B,C)=A'B'C'+A'B'C+A'BC'+A'BC+ABC+ABC 

3. The IP address of a device in a network is 172.16.128.123/22. Answer the following questions: 

   - i) What is the network address? 

ii) What is the subnet mask for the given network? 

iii) What is the broadcast address? 

iv) What is the maximum number of devices this network can connect? 

   - v) What is the IP address of the first host device in the network? 

4. a) Suppose you are working with an array of size 10. It contains all the numbers from 1 to 10 exactly once in a random order. But accidentally, one of the numbers in the array got replaced by a zero (0). Write a C/C++ programme using functions, to restore the lost number. 

   - b) What is polymorphism in the context of an object-oriented paradigm? Explain the method of overloading and method of overriding with suitable examples. 

5. Given the following two tables (Students and Marks) in a database, write down the output of the given SQL queries and write down the SQL queries for the outputs: 

Students Marks  Studentid StudentName Studentid Subject Mark 

|||1|Math|70|

|---|---|---|---|---|

|1|Mr. A|2|Math|90|

|2|Mr. B|3|Math|30|

|3|Mr. C|1|Bangali|50|

|4|Mr. D|2|Bangali|60|

|||3|Bangali|70|

|||1|Physics|80|

|||2|Physics|70|

|||3|Physics|60|

- i) SELECT Count (*) FROM Students S LEFT JOIN Marks M; ii) SELECT StudentName From Students S JOIN Marks M ON S.StudentIdM.Studentid GROUP BY S.Studentld, S.StudentName HAVING SUM (Mark)>-200; 

iii) List all the students name and number of subjects they have completed. iv) List all the students who have not completed any subject. v) List all the subject names. 

6. a) Define the term "Data Mining". Explain supervised and unsupervised classification with suitable example. 

   - b) How can we validate and check reliability of a machine-learning model? 

7. a) What are the advantages and disadvantages of the Agile Model compared to the Waterfall Model in software development? 

   - b) Briefly discuss Generative Artificial Intelligence (GAI) and "Large Language Models (LLMs)". 

8. a) Why is Merge Sort preferred over Quick Sort in certain applications, despite having higher space complexity? 

   - b) Suppose you have a list of items: 41, 25, 87, 57, 80, 79, 19, 36, 42, 7. using Quick Sort algorithm sort this list. You should explain each step. 

**39** 

**�ালািনওখিনজস�দিবভােগরআওতাধীনহাইে�াকাব�নইউিনেটর** Gin © thre mm Metis oTeSaN gacyleda BUrIcoa **সহকারী পিরচালক (আইিস�)-৯ম ��ড পরী�ার** oareta **তািরখঃ ৩০/০৫/২০২৫ পূন�মান** ota **-২০০ সময়ঃ ০৪ ঘ�া** abt **[�িত� িবষেয়র জন� পৃথক উ�র প� ব�বহার ক�ন]** 

**বাংলা** 

**িবষয় �কাড** Cre **: ১০১ মান: ৪০** 

১. ate �ব� রচনা PPT ক�ন: "অপার স�াবনার Wes বাংলােদশ"                                                  ১৫ ২. সারমম� ae িলখুন:                                                                                          ৫ �হ awe দাির��, তুিম �মাের ara কেরছ মহান । তুিম at �মাের দািনয়াছ ি�ে�র ota স�ান ক�ক be মু�ট Agb CSI �শাভা- িদয়াছ তাপস, অসে�াচ �কােশর �র� সাহস; SCR SIC YAS উ�ত উল� �ি�; বাণী �ুরধার, Sao tery pH বাণী �মার ar শােপ তব হ'ল তরবার । 

�ঃসহ tear দাহেন তব �হ amt দপ� তাপস, অ�ান BIR �েগ�ের cafes �মার CaS কিরেল িবরস অকােল �কােল BR �মার CIR �প রস �াণ Hatley । ৩. CRIS �ছাট �বানেক CINCH �াবল�ী RTT হওয়ার অনুে�রণা Beat িদেয় এক� ea প� ote িলখুন । ৫ ৪.বাংলায় অনুবাদ ক�ন PP] :                                                                                   ৫ 

The most common causes of deforestation are cutting and burning the forestland. Though the forestlands are cut and burnt for the sake of agriculture and habitant, it has a negative effect on environment. The removal of trees causes the birds and other animals living on them to leave the place. It also causes serious damage to the soil, as trees give protection to soil as well. In the end, the soil gets sediment in the river bed and causes frequent flood. 

৫.িনেচর ���েলার ewe উ�র Ger িলখুন:                                                           ২*৫ = ১০ ক) ণ-� y িবধােনর �ই� ee িনয়ম িলখুন । খ) খা� a বাংলা উপসগ� Dorref �যােগ cares গ�ত sifow চার� Brae শ� 7 িলখুন । গ) OPT ব�াসবাক� সহ সমােসর নাম িলখুন: গােয় হলুদ, afota �িতিদন, িবষাদিস�ু RamPre , উপ�হ Cre ঘ) wae সমাথ�ক xy শ� িলখুন (এক� wet কের): অণ�ব ate , আিদত� Birey , ময়ুখ, আ�জা are . ঙ) বাগধারা �েলার Oris িনিহতাথ� Fifer িলখুন: aa ল�া �দওয়া eR , টইট�ুর EDA , তালকানা, ঘুনা�র area 

ENGLISH Subject Code: 102 Marks: 40 

1. Write an essay on "Corruption in the ICT Sector in Bangladesh" using the hints given below: [Hints: Introduction- Types of corruption- Causes of corruptionEffects of corruption- Remedies-Conclusion]                                               15 

2. Imagine that you have purchased a laptop from a local showroom a week back. The warranty period is on and the laptop is not functioning well. Write a letter of 

complaint to the manager of the showroom about it. Your letter should contain information about the problem and what you want.                                         5 

7. Read the following passage and answer the questions that follow: 2×5-10 I am convinced that inculcating of discipline at home and in the educational institutions is essential for the growth of every individual. It is however unfortunate that the need for discipline in the youth is not sufficiently appreciated in this country. People seem to believe that to insist on discipline is to be unkind to the young. I have a different opinion. For me, what is unkind is to let a young person indulge in whatever s/he wants to do without parental, educational and ethical guidance. Discipline does not mean illogical harshness or oppressive imposition of law. Discipline involves ethics, i.e. responsible concern for the well-being of oneself and the other. Discipline involves guidance from the outside and control from the inside (self-control). Lack of guidance and control may lead a young person to waste her/his strength because s/he is yet to experience things in full. I feel sad when I see our youth-often individuals of talent, spirit and imaginationtalking, behaving and acting as if they are their own judge and have the vision of predicting the future. I consider it as a wrong trend because it is detrimental to the physical, mental and social well-being of theirs and others as well. 

- (a) At what points do the author's and people's beliefs are different? 

- (b) How does the author perceive discipline? 

- (c) What according to the author, may befall when a youth lacks discipline? 

- (d) What do you think is the dominant tone of the passage- prescriptive or dialogic engaging or 

- (e) Write in brief your response to the author's take on discipline. 

4. Rewrite the following sentences using the instruction given in the brackets: 

- (a) She explained the matter. [correct the sentence] 

- (b) Between the mostly popular drinks are coffee and tea. [correct the sentence] 

- (c) I like (cook). [use the right form of the verb] 

- (d) He recommended that she (write) the letter. [use the right form of the verb in bracket] 

- (e) He is endowed talents. [Fill in the gap with a preposition] 

- (f) She reached just time. [Fill in the gap with a preposition] 

- (g) He made me do the work. [Make it passive] 

- (h) It is said that she is a spy. [Make it active] 

- (i) He said to me, "Please wait here till I return". [Turn it into indirect speech] 

- (j) She did not listen to me. [Rewrite by using the idiom "turn a deaf ear"] 

সাধারণ �ান 

িবষয় �কাড: ১০৪ 

মান: ৪০ 

১. ��ািবত �ােদিশক সরকার ব�ব�া বাংলােদেশর জন� কতটা বা�বস�ত? আপনার মতামত উপ�াপন ক�ন । 

২. বাংলােদেশ �রািহ�া উ�া�েদর �ত�াবসেন বাধাসমূহ কী কী? এসব বাধা কীভােব �র করা যায়? 

৩. মুসিলম �দশ�েলার সােথ স�ক� িবষেয় সংিবধােনর ২৫ (২) ধারা �কন সি�েবিশত হেয়িছল? প�দশ 

- সংেশাধনীেত �কান যুি�েত এ ধারা� বাদ �দয়া হয়? 

৪. রািশয়া ও ইউে�ন যুে�র মূল কারণ�েলা কী কী? ব�াখা ক�ন । 

৫. িপং পং �টনীিত (Ping Pong Diplomacy) কী? এর ফলাফল কী হেয়িছল? 

৬. SDG কী? এর কয়� ল��মা�া রেয়েছ? �য �কান ১০� ল��মা�ার নাম িলখুন । 

৭. শ� �ষণ কী? এর উৎস কী কী? শ� �ষণ কীভােব �রাধ করা যায়? 

৮. �বতার তর� কী? �রিডও, �টিলিভশন ও রাডাের এ তর� কীভােব ব�ব�ত হয়? 

- (1) Speed (ii) Noise and (iii) Power consumption. 

�টকিনক�াল 

িবষয় �কাড: ১০৫ 

মান: ৮০ 

1. (a) Consider the following logic circuit. 

- (i) Derive the boolean expression algebraically for T, through T4. Derive F₁ and F₂ as function the three inputs A, B and C. 

(ii) Use K-map to simplify these expressions F₁ and F2, and show that they are equivalent the ones obtained in (i). 

- (b) Represent - 25 in 8 bit binary using 2's complement. 

- (c) Compare TTL and CMOS logic family in terms of 

- (i) Speed (ii) Noise and (iii) Power consumption. 

2. (a) Design an ER diagram for a library management systems where 

- (i) A library has multiple books. 

- (ii) Each book can have multiple copies. 

(b) Consider the following database schema 

employee (employee_name, street, city) works (employee_name, company_name, salary) company (employee_name, city) **Write the SQL commands to perform the following operations:** (i) Find the names of all employees who live in the city 'Dhaka'. (ii) Find the names of all employees whose salary in greater than BDT 1,00,000. (iii) Find the names of all employees who live in 'Dhaka' and whose salary in less than 1,00,000. 

(c) Why normalization is required in Database? Write shortly about 3NF. 1+1 3. (a) Consider a computer system with the following specifications: Physical memory (RAM): 4 GB Page size: 4 KB Virtual address space: 32 bits Page table entry size: 8 bytes 

Answer the following: (i) How many pages are there in the virtual address space? Explain your answer. (ii) What is the size of the page table? Explain your answer. (b) What is process? Describe different states of a process. 

(c) Define context switch with proper example. 

(d) What is cache memory? Explain the concepts of 

(i) Cache hit and (ii) Cache miss. 4. (a) A network has been assigned the IP address 200.1.2.0/24 It has 3 subnets. Determine the following for each subnet: 

(i) Total number of IP addresses (ii) Range of usable IP addresses (iii) Network address (iv) Direct broadcast address 

(v) Limited broadcast address. 

(b) Draw the diagram of TCP/IP protocol suite and mention the name of (v) Limited broadcast address. 

(b) Draw the diagram of TCP/IP protocol suite and mention the name of protocols used in different layers of TCP/IP. 

(c) Compare circuit switching and packet switching. 

5. (a) Describe the following terms: (i) Supervised learning (ii) Unsupervised learning 

(iii) Reinforcement learning 

(b) Given following values: 

True Positive (TP) = 560 True Negative (TN) = 330 False Positive (FP) = 60 False Negative (FN) = 50 Calculate the following: (1) Accuracy (ii) Precision (iii) Recall 

(iv) F1 Score 

(c) What is activation function in Deep Neural Network? What is the usability of this? 

6. (a) Write down a program is any high level language to read an integer and display a pattern like below. For example, if the given integer number is 1234, then the following pattern will be printed. 1234 234 34 

(b) What is friend function? Given the following class, show how to add a friend function, named isneg() that takes one parameter of type myclass and return true if num is negative and false otherwise. 

class myclass { int num; public: myclass(int i) { num = i;} }; 

7. (a) Apply the Krushkal's algorithm for the following graph to find out the cost of the Minimum Spanning Tree (MST). 

8.(a) What is 2-factor authentication? Describe it with an example. 

(b) What is hash table? What are the advantages of using hash table. 

- (c) Explain the rule of BIOS (Basic Input Output System) in the boot process of a PC. 

(d) Describe the steps involved in booting a computer from power on to loading the operating system. 

|**1**<br>**Bangladesh Telecommunication Regulatory Commission**<br>**Post Name: Assistant Director (Technical)**<br>**Exam Date: April 05, 2019**||

|---|---|

|**SL**<br>**Question**<br><br><br>|**Solution**<br><br><br>|

|What is 3dB? How can you tom a converter into an inverter.<br>||

|Basic factions of &GM and SOM. Describe LTE radio technology.<br>||

|Possible threads to a computer system and how to provide security.<br><br>||

|Va321 is IC? Advantages of IC over discrete component circuit. Why do ICs<br>need small power for their operation?||

|What is an access network? briefly describe the available access network. 6.<br>What do you mean by two factor authentication. Explain with example.||

|Math:<br>1. If 67x=l/a—l/b, show. that (x-3a)(x-32)+(x+3b)/(x-3b)=2., a not equal to<br>b.<br>2. Find the interest rate where difference between the compound interest and<br>simple interest ova principle of Tk 20000 for a 2 year period is Tk 392.<br>3.Write an essay on 'The roles of ICT in creating a knowledge economy'.<br>4.Bangle to English translation||

|MCQ: 30<br>১. “�য সেব বে�েত জি� িহংেস ব�বাণী,�স সব কাহার জ� িনন�য় ন জািন। কিবতা�–কার রচনা?উ�রঃ<br>আব�ল হািকম<br>২.�ার ব� কের িদেয় �মটাের �িখ.সত� বেল,আিম তেব �কাথা িদেয় ঢুিক?উি�� কার �লখা?উ�রঃ<br>রবী�নাথ ঠা�র<br>৩. For goodএর অনুবাদ িক?উ�রঃ িচরতের<br>৪.দহরম মহরম এর িবপরীত বাগধারা িক?উ�রঃ অিহন�ল<br>৫.িল�া�র হয় না �কান শে�র?উ�রঃ কিবরাজ<br>৬. Our fates seemed intertwined. Which one is similar to the underlined word?<br>উ�রঃlinked<br>৭. Find the synonym of the word ‘morose’?উ�রঃgloomy<br>৮. The antonym of the word ‘terrible’?উ�রঃfrightening<br>৯. Find the correctly spelt word.উ�রঃAbeyance<br>১০. ‘A legal authorization to debtors to postpone payment’ is known as?উ�রঃ<br>Moratorium<br>১১.১০ � বইেয়র মেধ� ৪ � বই কত �কাের বাছাই করা যায়,যােত িনিদ�� �ই� বই সব�দা বাদ থােক?উ�রঃ<br>২৮<br>১২. DIGITALশ��র বণ**�**িলেক কত �কাের সাজােনা যায় যােত �রবণ**�** একে� থােক?উ�রঃ ৩৬০<br><br>ze oft<br>IT OF<br>walfree<br>shot<br>woas<br>BIT<br>alae TPA<br>6<br>«ws B<br>oF<br>AREER<br>adeT<br>Bere<br>wapaerre<br>8ater<br>RDaeCe<br>bwas||
