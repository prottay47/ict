# Combined Bank, Assistant Database Administrator, 2026 (Based year 2023)

- **Original URL:** [https://it.jobqns.com/combined-bank-assistant-database-administrator-2026-based-year-2023/](https://it.jobqns.com/combined-bank-assistant-database-administrator-2026-based-year-2023/)
- **Date:** 2026-06-06T17:34:31
- **Categories:** Bank IT Job Solution 2026, Field-Based Job Solution (MCQ+Written), Latest Post

---

#### Combined Bank Post: Assistant Database Administrator(Based Year 2023)  Exam:  08-May-2026



All questions are scenario-based and assumed.

Collected question

a) Hard Drive need RAID-5

b) Preventive and Corrective Maintenance - Data Center

c) Routing Table - supernet - CIDR nation
d) SQL Querry- top 5 hospitals name from accident treatment

e) SQL Querry error - salary

f) Given Table - Super Key + primary key

g) Http code- mobile phone upload not affirmation

h) Why not use nosql(mongoDB) why use RDBMS in Banking?

i) R1 R2 lossless Join- decomposition database

k) Cloud Vendor or bank fault; legally vs technically

l) Half duplex and full duplex- example with network topology/hardware
m) API Gateway? Backened

n) RISC ARM processor vs CISC- x86 processor -RISC design philosophy-which setup will be better cloud infrastructure environment?

o) An app- weekly changing user feedback - government tight policies regarding user information- which SDLC(Waterfall,Agile/scrum or spiral)-uncertaintiy vs Rigidity- trade off

1. A bank plans to upgrade its storage system for transaction processing. The system must continue operating even if a single hard drive fails while efficiently utilizing available storage capacity. Which RAID level would you recommend, how does it work, and why is it suitable for this scenario?

**Recommendation: RAID 5**

For a bank’s transaction processing system that must survive a single drive failure while using storage efficiently,  **RAID 5**  is the ideal choice. It balances fault tolerance, performance, and capacity utilization better than other levels for this specific need.

**How RAID 5 Works**

RAID 5 uses  **block-level striping with distributed parity** . Data and parity information are spread across all drives in the array.

- **Striping:**  Data is split into blocks and written across multiple drives simultaneously, improving read and write speed.
- **Distributed parity:**  Parity (error-checking) data is calculated and stored across all drives, not on a single dedicated drive. If one drive fails, the missing data can be reconstructed from the remaining drives and parity.
- **Minimum drives:**  Requires at least 3 drives.

**Why RAID 5 is Suitable for Bank Transaction Processing**

RequirementRAID 5 FulfillmentSurvive single drive failureYes, parity allows full reconstructionEfficient storage useOnly 1 drive worth of space lost for parityRead performanceFast, data striped across all drivesWrite performanceGood for transactional workloadsCost efficiencyLower than RAID 1 or RAID 10

**Capacity Example:** With 4 drives of 2 TB each in RAID 5:Total raw space = 8 TBParity overhead = 2 TB (one drive) **Usable space = 6 TB**

**Bank Transaction Processing-এর জন্য Recommended RAID Level**

**Recommendation: RAID 5**

Bank-এর transaction processing system-এর জন্য যা single drive failure survive করবে এবং storage efficiently utilize করবে,  **RAID 5**  ideal choice। এটি fault tolerance, performance এবং capacity utilization-এর মধ্যে এই specific need-এর জন্য best balance করে।<

**RAID 5 কীভাবে কাজ করে**

RAID 5  **block-level striping with distributed parity**  ব্যবহার করে। Data এবং parity information array-এর সব drives জুড়ে spread করা হয়।<

- **Striping:**  Data blocks-এ split হয়ে একসাথে multiple drives-এ write করা হয়, read এবং write speed improve করে।
- **Distributed parity:**  Parity (error-checking) data calculate করে সব drives-এ store করা হয়, single dedicated drive-এ নয়। একটি drive fail হলে missing data বাকি drives এবং parity থেকে reconstruct করা যায়।
- **Minimum drives:**  কমপক্ষে 3 drives প্রয়োজন।

**RAID 5 Bank Transaction Processing-এর জন্য Suitable কেন**

RequirementRAID 5 FulfillmentSingle drive failure surviveহ্যাঁ, parity full reconstruction allow করেEfficient storage useParity-এর জন্য শুধু 1 drive-এর সমান space lossRead performanceFast, data সব drives জুড়ে stripedWrite performanceTransactional workloads-এর জন্য goodCost efficiencyRAID 1 বা RAID 10-এর চেয়ে lower

**Capacity Example:** 4টি 2 TB drive RAID 5-এ:Total raw space = 8 TBParity overhead = 2 TB (একটি drive) **Usable space = 6 TB** <

2. A data center supporting 24/7 online banking services experiences occasional hardware failures and service interruptions. Explain how preventive maintenance and corrective maintenance differ, and discuss how each contributes to maintaining service availability.

A data center running 24/7 online banking services cannot afford downtime. Both preventive and corrective maintenance play essential but different roles in keeping systems running smoothly. **1. Preventive Maintenance** Preventive maintenance is scheduled, proactive work done to avoid failures before they happen. It aims to keep hardware and software in optimal condition.

- **Regular inspections:**  Checking server health, temperature, fan speed, and power supply status on a fixed schedule.
- **Component replacement:**  Swapping out aging hard drives, batteries, or cooling units before they fail.
- **Software updates:**  Applying security patches, firmware upgrades, and OS updates during planned windows.
- **Load testing:**  Simulating peak traffic to identify bottlenecks before real customers are affected.
- **Cleaning and cooling:**  Dust removal and HVAC checks to prevent overheating.

**Contribution to availability:** By catching problems early, preventive maintenance reduces the frequency of unexpected outages. For a bank, this means customers can transfer money and check balances at any time without surprise service interruptions.

**2. Corrective Maintenance**

Corrective maintenance is reactive work done after a failure has already occurred. It restores the system to working condition.

- **Fault diagnosis:**  Identifying which server, disk, or network link has failed.
- **Component repair or replacement:**  Fixing or swapping the broken part.
- **Data recovery:**  Restoring lost or corrupted data from backups.
- **Bug fixes:**  Patching code defects that caused application crashes.
- **Incident response:**  Escalating and documenting the issue for future prevention.

**Contribution to availability:** When preventive measures fail, corrective maintenance minimizes downtime. Fast response teams, spare parts inventory, and automated failover systems ensure that even after a hardware failure, banking services resume quickly.

**How Both Work Together for Banking Availability**

- **Preventive maintenance**  lowers the chance of failures during high-traffic periods like salary days or holidays.
- **Corrective maintenance**  ensures that if a failure still happens, the Mean Time To Repair (MTTR) is as short as possible.
- **Combined strategy:**  A bank that invests heavily in prevention but also maintains a skilled on-call team and hot-swappable spare parts achieves the highest possible uptime for its 24/7 services.

24/7 online banking services run করা data center downtime afford করতে পারে না। Preventive এবং corrective maintenance উভয়ই systems smoothly চলতে রাখতে essential কিন্তু ভিন্ন ভূমিকা পালন করে।

**1. Preventive Maintenance** Preventive maintenance হলো scheduled, proactive work যা failure হওয়ার আগেই করা হয়। এটি hardware এবং software optimal condition-এ রাখতে aim করে।

- **Regular inspections:**  Fixed schedule-এ server health, temperature, fan speed এবং power supply status check করা।
- **Component replacement:**  Fail করার আগেই aging hard drives, batteries বা cooling units swap করা।
- **Software updates:**  Planned windows-এ security patches, firmware upgrades এবং OS updates apply করা।
- **Load testing:**  Real customers affect হওয়ার আগে peak traffic simulate করে bottlenecks identify করা।
- **Cleaning and cooling:**  Overheating prevent করতে dust removal এবং HVAC checks করা।

**Availability-তে অবদান:** Problems early catch করলে preventive maintenance unexpected outages-এর frequency কমায়। Bank-এর জন্য এর মানে customers যেকোনো সময় money transfer এবং balance check করতে পারে surprise service interruptions ছাড়াই।<

**2. Corrective Maintenance**

Corrective maintenance হলো reactive work যা failure occur করার পরে করা হয়। এটি system working condition-এ ফিরিয়ে আনে।

- **Fault diagnosis:**  কোন server, disk বা network link fail করেছে তা identify করা।
- **Component repair or replacement:**  ভাঙা part fix বা swap করা।
- **Data recovery:**  Backups থেকে lost বা corrupted data restore করা।
- **Bug fixes:**  Application crashes cause করা code defects patch করা।
- **Incident response:**  Future prevention-এর জন্য issue escalate এবং document করা।

**Availability-তে অবদান:** Preventive measures fail হলে corrective maintenance downtime minimize করে। Fast response teams, spare parts inventory এবং automated failover systems ensure করে যে hardware failure-এর পরেও banking services দ্রুত resume হয়।

**Banking Availability-এর জন্য উভয় কীভাবে একসাথে কাজ করে**

- **Preventive maintenance**  high-traffic periods যেমন salary days বা holidays-এ failure হওয়ার chance কমায়।
- **Corrective maintenance**  failure হলেও Mean Time To Repair (MTTR) যতটা সম্ভব কম নিশ্চিত করে।
- **Combined strategy:**  যে bank prevention-এ heavily invest করে এবং skilled on-call team এবং hot-swappable spare parts maintain করে, সে তার 24/7 services-এর জন্য সর্বোচ্চ possible uptime achieve করে।

3. An ISP has been assigned the networks 192.168.0.0/24, 192.168.1.0/24, 192.168.2.0/24, and 192.168.3.0/24. To reduce routing table entries, the network engineer decides to use CIDR-based route aggregation. Determine the supernet address and explain how supernetting improves routing efficiency.

**Given Networks:**

- 192.168.0.0/24
- 192.168.1.0/24
- 192.168.2.0/24
- 192.168.3.0/24

**Step 1: Convert to Binary**

NetworkBinary (last octet)192.168.0.00000 0000192.168.1.00000 0001192.168.2.00000 0010192.168.3.00000 0011

**Step 2: Find Common Prefix** Looking at the last octet in binary:– 0 =  **00** 00 0000– 1 =  **00** 00 0001– 2 =  **00** 00 0010– 3 =  **00** 00 0011

The first  **22 bits**  are identical across all four networks. The last 2 bits vary (00, 01, 10, 11).

**Step 3: Determine Supernet Address**

Supernet address =  **192.168.0.0/22**

Mask: 255.255.252.0Range: 192.168.0.0 to 192.168.3.255Total hosts: 1024 (4 × 256)

**How Supernetting Improves Routing Efficiency**

- **Reduced table size:**  Instead of 4 separate /24 entries, the router stores 1 /22 entry. This saves memory and lookup time.
- **Faster lookups:**  Smaller routing tables mean faster longest-prefix-match searches, reducing packet forwarding delay.
- **Less update traffic:**  If one subnet changes, the aggregated route does not need to be re-advertised. BGP and OSPF updates are smaller.
- **Hierarchical routing:**  ISPs can advertise a single supernet to upstream providers instead of listing every customer subnet, keeping the global internet routing table manageable.

**Given Networks:**

- 192.168.0.0/24
- 192.168.1.0/24
- 192.168.2.0/24
- 192.168.3.0/24

**Step 1: Binary-তে Convert করা**

NetworkBinary (last octet)192.168.0.00000 0000192.168.1.00000 0001192.168.2.00000 0010192.168.3.00000 0011

**Step 2: Common Prefix খোঁজা**

Last octet binary-তে দেখলে:– 0 =  **00** 00 0000– 1 =  **00** 00 0001– 2 =  **00** 00 0010– 3 =  **00** 00 0011

চারটা network-এর প্রথম  **22 bits**  identical। শেষ 2 bits vary করে (00, 01, 10, 11)।

**Step 3: Supernet Address নির্ধারণ**

Supernet address =  **192.168.0.0/22**

Mask: 255.255.252.0Range: 192.168.0.0 থেকে 192.168.3.255Total hosts: 1024 (4 × 256)

**Supernetting Routing Efficiency কীভাবে Improve করে**

- **Reduced table size:**  4টা আলাদা /24 entry-এর পরিবর্তে router 1টা /22 entry store করে। এতে memory এবং lookup time বাঁচে।
- **Faster lookups:**  ছোট routing tables মানে দ্রুত longest-prefix-match search, packet forwarding delay কমে।
- **Less update traffic:**  একটা subnet change হলে aggregated route re-advertise করার প্রয়োজন হয় না। BGP এবং OSPF updates ছোট হয়।
- **Hierarchical routing:**  ISPs single supernet advertise করতে পারে upstream providers-এর কাছে, প্রতিটি customer subnet list না করেই, global internet routing table manageable রাখে।

4. A database contains a table named Hospital(HospitalID, HospitalName, Specialization, PatientCount). Write an SQL query to display the names of the five hospitals that specialize in accident treatment and have treated the highest number of patients.
```
SELECT HospitalName
FROM Hospital
WHERE Specialization = 'Accident Treatment'
ORDER BY PatientCount DESC
LIMIT 5;
```

**Explanation:**

- **WHERE**  filters hospitals specializing in accident treatment.

- **ORDER BY PatientCount DESC**  sorts hospitals from highest to lowest patient count.

- **LIMIT 5**  returns the top five hospitals.

5. A developer writes the SQL statement SELECT EmployeeName, Salary FROM Employees WHERE Salary > AVG(Salary);, but the query generates an error. Identify the problem and write a corrected SQL query. **Problem Identification:** The query is incorrect because  **AVG(Salary)**  is an aggregate function and cannot be used directly in the WHERE clause.

6.Given the relation Employee(EmployeeID, NationalID, Email, Name, Department), where EmployeeID, NationalID, and Email are unique, identify the super keys, candidate keys, and the most appropriate primary key with justification.

**Given Relation:** Employee(EmployeeID, NationalID, Email, Name, Department)

**Functional Understanding:** EmployeeID, NationalID, and Email are unique attributes (each can uniquely identify an employee).

**Candidate Keys:** Minimal attributes that can uniquely identify a tuple.

- EmployeeID
- NationalID
- Email

**Super Keys:** Any combination of attributes that can uniquely identify a tuple (including candidate keys and their supersets). Examples include:

- EmployeeID
- NationalID
- Email
- (EmployeeID, Name)
- (EmployeeID, Department)
- (Email, Department)
- (NationalID, Name, Department)
- and any superset containing at least one candidate key

**Primary Key (Most Appropriate Choice):**  **EmployeeID**

**Justification:**

- It is unique for every employee.
- It is stable (does not change over time).
- It is short and efficient for indexing and joins.
- Compared to NationalID or Email, it is less likely to change.

7. A mobile banking application successfully connects to a server and attempts to upload a customer document, but the server rejects the request because the uploaded file format is not supported. Which HTTP status code should be returned and why?

**Crrect Status Code: 415 Unsupported Media Type**

The server should return  **415 Unsupported Media Type**  because the uploaded file format violates the server’s accepted content types.

**Why 415 is the Right Choice**

- **Client error category:**  4xx codes indicate the problem is on the client side. The request was understood but cannot be processed due to invalid content.
- **Specific to content type:**  415 explicitly signals that the server refuses to accept the payload because its media type is not supported, unlike generic 400 which covers all bad requests.
- **Content-Type header mismatch:**  The client likely sent a Content-Type header (e.g.,
```
image/heic
```
or
```
application/x-bittorrent
```
) that the server does not allow for document uploads.

**Response Example:**

HTTP/1.1 415 Unsupported Media TypeContent-Type: application/json{  “error”: “Unsupported file format”,  “message”: “Only PDF, JPG, and PNG files are accepted”,  “received”: “image/webp”,  “allowed_types”: [“application/pdf”, “image/jpeg”, “image/png”]}

**Why Not Other Codes?**

CodeWhy Incorrect **400 Bad Request** Too generic; does not specifically identify the media type problem **403 Forbidden** Implies authentication or permission issue, not format rejection **406 Not Acceptable** Used when server cannot provide a response in client’s accepted format, not for uploaded content **500 Internal Server Error** Wrong category; the server is working correctly by rejecting the format

**Client Action:** The mobile app should read the 415 response, display the allowed formats to the user, and prompt them to select a supported file type before retrying the upload.

**Correct Status Code: 415 Unsupported Media Type**

Server  **415 Unsupported Media Type**  return করবে কারণ uploaded file format server-এর accepted content types violate করে।

**415 কেন Right Choice**

- **Client error category:**  4xx codes indicate করে problem client side-এ। Request understood হয়েছে কিন্তু invalid content-এর কারণে process করা যাচ্ছে না।
- **Specific to content type:**  415 explicitly signal করে যে server payload accept করছে না কারণ এর media type supported নয়, generic 400-এর বিপরীতে যা সব bad requests cover করে।
- **Content-Type header mismatch:**  Client সম্ভবত এমন Content-Type header পাঠিয়েছে (যেমন
```
image/heic
```
বা
```
application/x-bittorrent
```
) যা server document uploads-এর জন্য allow করে না।

**Response Example:**

HTTP/1.1 415 Unsupported Media TypeContent-Type: application/json{  “error”: “Unsupported file format”,  “message”: “Only PDF, JPG, and PNG files are accepted”,  “received”: “image/webp”,  “allowed_types”: [“application/pdf”, “image/jpeg”, “image/png”]}

**অন্যান্য Codes কেন নয়?**

CodeWhy Incorrect **400 Bad Request** Too generic; media type problem specifically identify করে না **403 Forbidden** Authentication বা permission issue imply করে, format rejection নয় **406 Not Acceptable** Server client-এর accepted format-এ response দিতে না পারলে ব্যবহার হয়, uploaded content-এর জন্য নয় **500 Internal Server Error** Wrong category; server correctly format reject করছে

**Client Action:** Mobile app 415 response পড়বে, user-কে allowed formats দেখাবে, এবং retry করার আগে supported file type select করতে prompt করবে।

8. A bank is considering replacing its relational database system with MongoDB for its core banking application. Discuss whether this is an appropriate decision and justify why an RDBMS or NoSQL database would be more suitable.

Replacing a relational database with MongoDB for core banking is generally  **not an appropriate decision** . Core banking applications have strict requirements that align better with RDBMS strengths than NoSQL flexibility. **Why RDBMS is More Suitable for Core Banking**

- **ACID compliance:**  Banking transactions require Atomicity, Consistency, Isolation, and Durability. RDBMS guarantees these natively. MongoDB supports multi-document ACID only from version 4.0, and it is less mature than decades-proven RDBMS implementations.
- **Complex joins and relationships:**  Accounts, customers, transactions, loans, and branches have deeply interconnected data. RDBMS handles complex joins efficiently. MongoDB’s document model forces denormalization or application-level joins, increasing complexity.
- **Data integrity constraints:**  Foreign keys, check constraints, and unique indexes ensure no orphaned records or invalid states. MongoDB lacks native foreign key enforcement.
- **Regulatory compliance:**  Banks must maintain audit trails, data lineage, and strict schema control. RDBMS schemas enforce structure. MongoDB’s schema-less design risks data inconsistency over time.
- **Mature tooling:**  RDBMS has decades of backup, replication, monitoring, and reporting tools designed for financial workloads.

**When MongoDB Could Be Appropriate**

MongoDB fits specific banking use cases but not core transactional systems:

- **Customer-facing mobile apps:**  Session data, preferences, and activity logs where flexibility and speed matter more than strict consistency.
- **Real-time analytics:**  Aggregating transaction patterns for fraud detection dashboards.
- **Document storage:**  KYC documents, scanned checks, and unstructured compliance paperwork.
- **Catalogs and product data:**  Bank product descriptions, interest rate tables, and marketing content.

**Recommended Architecture:** Use  **RDBMS (Oracle, PostgreSQL, or DB2)**  for core banking transactions. Complement with  **MongoDB**  only for peripheral services like mobile app caching, document storage, or analytics where its strengths apply.

**Core Banking-এ RDBMS-কে MongoDB দিয়ে Replace করা: Analysis**

Core banking-এর জন্য relational database-কে MongoDB দিয়ে replace করা সাধারণত  **appropriate decision নয়** । Core banking applications-এর strict requirements RDBMS strengths-এর সাথে better align করে NoSQL flexibility-এর চেয়ে।

**Core Banking-এ RDBMS কেন More Suitable**

- **ACID compliance:**  Banking transactions-এর জন্য Atomicity, Consistency, Isolation, এবং Durability প্রয়োজন। RDBMS এগুলো natively guarantee করে। MongoDB multi-document ACID শুধু version 4.0 থেকে support করে, এবং এটি decades-proven RDBMS implementations-এর চেয়ে less mature।
- **Complex joins এবং relationships:**  Accounts, customers, transactions, loans, এবং branches-এর deeply interconnected data থাকে। RDBMS complex joins efficiently handle করে। MongoDB-এর document model denormalization বা application-level joins force করে, complexity বাড়ায়।
- **Data integrity constraints:**  Foreign keys, check constraints, এবং unique indexes ensure করে যে orphaned records বা invalid states তৈরি হয় না। MongoDB-এ native foreign key enforcement নেই।
- **Regulatory compliance:**  Banks-কে audit trails, data lineage, এবং strict schema control maintain করতে হয়। RDBMS schemas structure enforce করে। MongoDB-এর schema-less design সময়ের সাথে data inconsistency risk তৈরি করে।
- **Mature tooling:**  RDBMS-এর decades of backup, replication, monitoring, এবং reporting tools আছে যা financial workloads-এর জন্য designed।

**MongoDB কখন Appropriate হতে পারে**

MongoDB specific banking use cases-এ fit করে কিন্তু core transactional systems-এ নয়:

- **Customer-facing mobile apps:**  Session data, preferences, এবং activity logs যেখানে flexibility এবং speed strict consistency-এর চেয়ে বেশি matter করে।
- **Real-time analytics:**  Fraud detection dashboards-এর জন্য transaction patterns aggregate করা।
- **Document storage:**  KYC documents, scanned checks, এবং unstructured compliance paperwork।
- **Catalogs এবং product data:**  Bank product descriptions, interest rate tables, এবং marketing content।

**Recommended Architecture:** Core banking transactions-এর জন্য  **RDBMS (Oracle, PostgreSQL, বা DB2)**  ব্যবহার করুন।  **MongoDB**  শুধু peripheral services যেমন mobile app caching, document storage, বা analytics-এর জন্য complement হিসেবে ব্যবহার করুন যেখানে এর strengths apply করে।

9. A relation R(A, B, C) is decomposed into R1(A, B) and R2(B, C). Explain whether the decomposition is lossless and describe the conditions required for a lossless join decomposition. **Given:**
Relation R(A, B, C) is decomposed into:
R1(A, B) and R2(B, C)

**Is the decomposition lossless?**

Yes, this decomposition is  **lossless join**  if attribute  **B**  is a key (or common key condition holds).

**Explanation:** The common attribute between R1 and R2 is  **B** .When joining R1 and R2 on B, we can perfectly reconstruct the original relation R(A, B, C) without losing or adding extra tuples, provided B functionally determines either R1 or R2.

**Lossless Join Condition:** A decomposition of R into R1 and R2 is lossless if:

**(R1 ∩ R2) → R1**  OR  **(R1 ∩ R2) → R2**

For this case:R1 ∩ R2 = {B}

So the condition becomes:

- B → A (then lossless), OR
- B → C (then lossless)

10. A bank hosts its online banking platform on a public cloud infrastructure. Due to a cloud service outage, customers are unable to access services for several hours. Discuss the technical and legal responsibilities of both the cloud service provider and the bank.

When a cloud service outage disrupts online banking, both the cloud provider and the bank share responsibilities, but in different domains. Their obligations are typically defined in a Service Level Agreement (SLA).

**1. Cloud Service Provider Responsibilities**

**Technical:**

**Infrastructure uptime:**  Maintain data center power, cooling, networking, and hardware to meet SLA guarantees (often 99.9% to 99.99%).

- **Redundancy and failover:**  Provide multi-zone or multi-region replication so a single point of failure does not cause total outage.
- **Incident response:**  Detect failures quickly, communicate status transparently, and restore services within agreed Recovery Time Objective (RTO).
- **Backup integrity:**  Ensure customer data backups are consistent and recoverable.

**Legal:**

- **SLA credits:**  Pay financial penalties or service credits if uptime falls below the guaranteed threshold.
- **Notification duty:**  Inform affected customers promptly about the outage cause, scope, and estimated resolution time.
- **Data protection:**  Comply with data residency and encryption standards even during failure events.
- **Liability cap:**  Most SLAs limit provider liability to monthly fees paid, excluding consequential damages like lost bank revenue.

**2. Bank Responsibilities**

**Technical:**

- **Architecture resilience:**  Design systems with multi-cloud or hybrid-cloud failover, not relying on a single provider or region.
- **Disaster recovery planning:**  Maintain active-active or warm standby systems that can switch over automatically.
- **Monitoring and alerting:**  Detect outages independently and trigger customer communication channels.
- **Data backups:**  Keep independent encrypted backups outside the primary cloud environment.

**Legal:**

- **Regulatory compliance:**  Banking regulators hold the bank accountable for service availability, regardless of cloud provider failures.
- **Customer duty:**  The bank must compensate customers for failed transactions, unauthorized access during recovery, or missed payments.
- **Contract management:**  The bank is responsible for negotiating SLAs, understanding liability limits, and demanding higher availability tiers.
- **Transparency to customers:**  The bank must explain outages to customers and regulators, not shift blame to the cloud provider.

Cloud service outage online banking disrupt করলে cloud provider এবং bank উভয়েরই responsibilities থাকে, কিন্তু ভিন্ন domains-এ। তাদের obligations সাধারণত Service Level Agreement (SLA)-এ define করা থাকে।

**1. Cloud Service Provider Responsibilities**

**Technical:**

- **Infrastructure uptime:**  Data center power, cooling, networking এবং hardware maintain করা SLA guarantees (প্রায়শই 99.9% থেকে 99.99%) meet করতে।
- **Redundancy এবং failover:**  Multi-zone বা multi-region replication provide করা যাতে single point of failure total outage cause না করে।
- **Incident response:**  দ্রুত failures detect করা, status transparently communicate করা, এবং agreed Recovery Time Objective (RTO)-এর মধ্যে services restore করা।
- **Backup integrity:**  Customer data backups consistent এবং recoverable কিনা নিশ্চিত করা।

**Legal:**

- **SLA credits:**  Uptime guaranteed threshold-এর নিচে নামলে financial penalties বা service credits pay করা।
- **Notification duty:**  Affected customers-কে promptly outage cause, scope এবং estimated resolution time সম্পর্কে inform করা।
- **Data protection:**  Failure events-এর সময়ও data residency এবং encryption standards comply করা।
- **Liability cap:**  Most SLAs provider liability monthly fees paid-এর মধ্যে limit করে, lost bank revenue এর মতো consequential damages বাদ দিয়ে।

**2. Bank Responsibilities**

**Technical:**

- **Architecture resilience:**  Multi-cloud বা hybrid-cloud failover সহ systems design করা, single provider বা region-এর উপর নির্ভর না করে।
- **Disaster recovery planning:**  Active-active বা warm standby systems maintain করা যা automatically switch over করতে পারে।
- **Monitoring এবং alerting:**  Independently outages detect করা এবং customer communication channels trigger করা।
- **Data backups:**  Primary cloud environment-এর বাইরে independent encrypted backups রাখা।

**Legal:**

- **Regulatory compliance:**  Banking regulators bank-কেই service availability-এর জন্য accountable ধরে, cloud provider failures যাই হোক না কেন।
- **Customer duty:**  Bank-কে failed transactions, recovery-এর সময় unauthorized access, বা missed payments-এর জন্য customers-কে compensate করতে হয়।
- **Contract management:**  Bank SLA negotiate, liability limits বোঝা, এবং higher availability tiers demand করার দায়িত্বে।
- **Transparency to customers:**  Bank-কে customers এবং regulators-কে outages explain করতে হবে, cloud provider-এর দোষ shift না করে।

11. A network administrator is replacing a hub-based LAN with a switch-based LAN. Explain the differences between half-duplex and full-duplex communication and discuss how the change affects network performance.

**Half-Duplex:** In half-duplex communication, data can flow in both directions, but not at the same time.Devices must take turns sending and receiving data.

**Full-Duplex:** In full-duplex communication, data can flow in both directions simultaneously.Devices can send and receive data at the same time.

**Key Differences:**

- **Data Flow:**  Half-duplex = one direction at a time, Full-duplex = both directions simultaneously
- **Efficiency:**  Full-duplex is more efficient
- **Collisions:**  Half-duplex has collisions, full-duplex eliminates collisions
- **Performance:**  Full-duplex provides higher throughput

**Impact of Replacing Hub with Switch**

**Hub-based LAN:** – Operates in half-duplex mode– All devices share bandwidth– High collisions and congestion

**Switch-based LAN:** – Supports full-duplex communication– Dedicated bandwidth per port– No collisions (due to separate collision domains)

**Performance Improvement:**

- Higher network speed and throughput
- Reduced collisions and retransmissions
- Better bandwidth utilization
- Improved overall LAN efficiency

**Conclusion:** Switching from hub to switch enables full-duplex communication, eliminates collisions, and significantly improves network performance and scalability.

**Half-Duplex vs Full-Duplex Communication**

**Half-Duplex:** Half-duplex communication-এ data দুই দিকেই যেতে পারে, কিন্তু একসাথে নয়।ডিভাইসগুলোকে একে অপরের সাথে পালাক্রমে send এবং receive করতে হয়।

**Full-Duplex:** Full-duplex communication-এ data একই সময়ে দুই দিকেই যেতে পারে।একই সাথে send এবং receive করা যায়।

**মূল পার্থক্য:**

- **Data Flow:**  Half-duplex = এক সময়ে এক দিক, Full-duplex = একসাথে দুই দিক
- **Efficiency:**  Full-duplex বেশি efficient
- **Collision:**  Half-duplex-এ collision হয়, Full-duplex-এ হয় না
- **Performance:**  Full-duplex বেশি speed দেয়

**Hub থেকে Switch-এ পরিবর্তনের প্রভাব:**

**Hub-based LAN:** – Half-duplex mode-এ কাজ করে– সব device একই bandwidth share করে– বেশি collision এবং congestion হয়

**Switch-based LAN:** – Full-duplex support করে– প্রতিটি port আলাদা bandwidth পায়– collision হয় না (separate collision domain)

**Performance improvement:**

- Network speed এবং throughput বাড়ে
- Collision এবং retransmission কমে
- Bandwidth utilization ভালো হয়
- Overall network efficiency বাড়ে

**উপসংহার:** Hub থেকে switch-এ পরিবর্তন করলে full-duplex communication সম্ভব হয়, collision দূর হয় এবং network performance অনেক উন্নত হয়।

12. A bank is migrating from a monolithic application to a microservices architecture and plans to deploy an API Gateway. Explain the role of an API Gateway and how it interacts with backend services in such an environment.

When a bank migrates from a monolithic application to microservices, the system breaks into many small, independent services. An  **API Gateway**  acts as the single entry point for all client requests, managing how they reach the correct backend services.

**1. Core Role of the API Gateway**

- **Single entry point:**  Instead of clients calling dozens of microservices directly, they send all requests to one gateway URL. The gateway routes each request to the right service.
- **Request routing:**  A request to
```
/api/accounts
```
goes to the account service, while
```
/api/transactions
```
goes to the transaction service.
- **Protocol translation:**  Converts external protocols (HTTPS/REST) to internal protocols (gRPC, message queues) that microservices use.
- **Load balancing:**  Distributes incoming traffic across multiple instances of the same microservice to prevent overload.

**2. How It Interacts with Backend Services**

StepAction1Client sends request to API Gateway2Gateway authenticates and validates the request3Gateway looks up routing rules for the endpoint4Gateway forwards request to the correct microservice5Microservice processes and returns response6Gateway may transform response format before sending to client

**3. Additional Responsibilities in Banking**

- **Authentication and authorization:**  Verifies JWT tokens or API keys before any request reaches backend services, protecting sensitive banking data.
- **Rate limiting:**  Prevents DDoS attacks by capping requests per client, ensuring services stay available.
- **SSL termination:**  Handles encryption/decryption at the edge so microservices focus on business logic.
- **Request aggregation:**  A single client request (like “show dashboard”) may need data from 5 services. The gateway calls all 5 in parallel and returns one combined response.
- **Circuit breaker:**  If a microservice fails, the gateway stops sending requests to it and returns a fallback response, preventing cascade failures.

**4. Why Banks Need It After Monolith Migration**

In a monolith, one codebase handled everything. In microservices, there may be 50+ services. Without a gateway, clients would need to know every service address, handle failures themselves, and manage multiple authentication points. The API Gateway hides this complexity.

**Microservices Architecture-এ API Gateway-এর Role**

Bank monolithic application থেকে microservices-এ migrate করলে system অনেক ছোট, independent services-এ ভাগ হয়ে যায়।  **API Gateway**  সব client requests-এর জন্য single entry point হিসেবে কাজ করে, কীভাবে সেগুলো সঠিক backend services-এ পৌঁছায় তা manage করে।

**1. API Gateway-এর Core Role**

- **Single entry point:**  Clients directly dozens of microservices call না করে সব requests একটা gateway URL-এ পাঠায়। Gateway প্রতিটি request সঠিক service-এ route করে।
- **Request routing:**
```
/api/accounts
```
request account service-এ যায়, আর
```
/api/transactions
```
transaction service-এ যায়।
- **Protocol translation:**  External protocols (HTTPS/REST)-কে internal protocols (gRPC, message queues)-এ convert করে যা microservices ব্যবহার করে।
- **Load balancing:**  Incoming traffic একই microservice-এর multiple instances-এর মধ্যে distribute করে overload prevent করে।

**2. Backend Services-এর সাথে কীভাবে Interact করে**

StepAction1Client API Gateway-তে request পাঠায়2Gateway request authenticate এবং validate করে3Gateway endpoint-এর জন্য routing rules look up করে4Gateway request সঠিক microservice-এ forward করে5Microservice process করে response return করে6Gateway response format transform করে client-এ পাঠাতে পারে

**3. Banking-এ Additional Responsibilities**

- **Authentication and authorization:**  Backend services-এর আগে JWT tokens বা API keys verify করে, sensitive banking data protect করে।
- **Rate limiting:**  প্রতি client-এর request cap করে DDoS attacks prevent করে, services available রাখে।
- **SSL termination:**  Edge-এ encryption/decryption handle করে যাতে microservices business logic-এ focus করতে পারে।
- **Request aggregation:**  একটা client request (যেমন “show dashboard”) 5টা service-এর data প্রয়োজন হতে পারে। Gateway parallel-এ সব 5টা call করে একটা combined response return করে।
- **Circuit breaker:**  কোনো microservice fail হলে gateway এতে request পাঠানো বন্ধ করে fallback response return করে, cascade failures prevent করে।

**4. Monolith Migration-এর পর Bank-এর কেন প্রয়োজন**

Monolith-এ একটা codebase everything handle করত। Microservices-এ 50+ services থাকতে পারে। Gateway ছাড়া clients প্রতিটি service address জানতে হবে, failures নিজেরা handle করতে হবে, এবং multiple authentication points manage করতে হবে। API Gateway এই complexity hide করে

13. A cloud service provider must choose between ARM-based processors and x86 processors for a new data center deployment. Compare the RISC and CISC architectures and recommend the most suitable option for large-scale cloud infrastructure.

Cloud providers must balance performance, power efficiency, cost, and scalability when choosing between ARM-based processors (RISC architecture) and x86 processors (CISC architecture) for data center deployment.

**1. RISC (ARM) Architecture**

RISC (Reduced Instruction Set Computer) uses a small, highly optimized set of simple instructions. Each instruction executes in one clock cycle. ARM processors are the dominant RISC implementation in mobile and increasingly in servers.

- **Simple instructions:**  Fewer instruction types, each completing in a single cycle.
- **More registers:**  ARM uses more general-purpose registers to reduce memory access.
- **Power efficiency:**  Lower power consumption per instruction, generating less heat.
- **Pipelining friendly:**  Uniform instruction size makes prediction and parallel execution easier.

**2. CISC (x86) Architecture**

CISC (Complex Instruction Set Computer) uses a large set of complex instructions. A single instruction can perform multi-step operations. Intel and AMD processors use x86, the dominant CISC architecture in desktops and traditional servers.

- **Complex instructions:**  One instruction can handle multiple low-level operations.
- **Fewer registers:**  More work is done through memory access and complex addressing modes.
- **Backward compatibility:**  Decades of software, especially legacy enterprise applications, are built for x86.
- **High single-thread performance:**  Complex instructions reduce instruction count for certain workloads.

**Recommendation for Large-Scale Cloud Infrastructure**

**ARM-based processors are the most suitable choice**  for modern large-scale cloud deployments, with specific exceptions.

**Justification:**

- **Power efficiency at scale:**  Data centers spend more on electricity and cooling than hardware. ARM cores deliver more performance per watt, directly reducing operational costs for thousands of servers.
- **High core density:**  ARM chips pack more cores per socket. Cloud workloads (microservices, containers, serverless functions) scale horizontally across many lightweight threads rather than relying on single-thread speed.
- **Cost per compute unit:**  ARM servers cost less to purchase and operate, improving margins for cloud providers who resell compute capacity.
- **Modern software alignment:**  Cloud-native stacks (Kubernetes, Docker, Linux, Python, Go, Java) are already ported to ARM. Legacy dependency is shrinking.
- **Real-world validation:**  AWS Graviton, Ampere Altra, and Apple Silicon have proven ARM’s viability in production cloud and edge environments.

**When x86 Remains Necessary:** Legacy Windows Server or proprietary enterprise software with no ARM port.

- High-frequency trading or scientific computing where single-thread performance dominates.
- Workloads heavily optimized for x86-specific vector instructions (AVX-512).

Cloud providers data center deployment-এর জন্য ARM-based processors (RISC architecture) এবং x86 processors (CISC architecture)-এর মধ্যে choose করার সময় performance, power efficiency, cost, এবং scalability balance করতে হয়।

**1. RISC (ARM) Architecture**

RISC (Reduced Instruction Set Computer) ছোট, highly optimized simple instructions-এর set ব্যবহার করে। প্রতিটি instruction একটা clock cycle-এ execute হয়। ARM processors mobile-এ dominant এবং increasingly servers-এও ব্যবহৃত হচ্ছে।

- **Simple instructions:**  কম instruction types, প্রতিটি single cycle-এ complete হয়।
- **More registers:**  ARM memory access কমাতে বেশি general-purpose registers ব্যবহার করে।
- **Power efficiency:**  প্রতি instruction-এ কম power consumption, কম heat generate করে।
- **Pipelining friendly:**  Uniform instruction size prediction এবং parallel execution সহজ করে।

**2. CISC (x86) Architecture**

CISC (Complex Instruction Set Computer) বড় set of complex instructions ব্যবহার করে। একটা instruction multi-step operations perform করতে পারে। Intel এবং AMD processors x86 ব্যবহার করে, যা desktops এবং traditional servers-এ dominant CISC architecture।

- **Complex instructions:**  একটা instruction multiple low-level operations handle করতে পারে।
- **Fewer registers:**  বেশি কাজ memory access এবং complex addressing modes-এর মাধ্যমে হয়।
- **Backward compatibility:**  Decades of software, বিশেষ করে legacy enterprise applications, x86-এর জন্য built।
- **High single-thread performance:**  Certain workloads-এর জন্য complex instructions instruction count কমায়।

**Large-Scale Cloud Infrastructure-এর জন্য Recommendation**

**ARM-based processors সবচেয়ে suitable choice**  modern large-scale cloud deployments-এর জন্য, specific exceptions সহ।

**Justification:**

- **Scale-এ power efficiency:**  Data centers hardware-এর চেয়ে electricity এবং cooling-এ বেশি খরচ করে। ARM cores প্রতি watt-এ বেশি performance deliver করে, হাজার হাজার servers-এর operational costs সরাসরি কমায়।
- **High core density:**  ARM chips প্রতি socket-এ বেশি cores pack করে। Cloud workloads (microservices, containers, serverless functions) horizontally scale করে অনেক lightweight threads জুড়ে, single-thread speed-এর উপর নির্ভর না করে।
- **Cost per compute unit:**  ARM servers purchase এবং operate করতে কম খরচ হয়, cloud providers-এর margins improve করে যারা compute capacity resell করে।
- **Modern software alignment:**  Cloud-native stacks (Kubernetes, Docker, Linux, Python, Go, Java) already ARM-এ port করা। Legacy dependency কমছে।
- **Real-world validation:**  AWS Graviton, Ampere Altra, এবং Apple Silicon production cloud এবং edge environments-এ ARM-এর viability prove করেছে।

**x86 কখনো Necessary থাকে:**

- Legacy Windows Server বা proprietary enterprise software যার ARM port নেই।
- High-frequency trading বা scientific computing যেখানে single-thread performance dominate করে।
- Workloads যা heavily x86-specific vector instructions (AVX-512)-এর জন্য optimized।

**Summary:**  Modern, horizontally-scalable workloads serve করা greenfield cloud data center-এর জন্য ARM-এর power efficiency, density, এবং cost advantage superior architectural choice করে। x86 শুধু specific legacy বা compute-bound workloads-এর জন্য retain করা উচিত।

14. A government mobile application receives frequent user feedback that requires weekly feature updates, while strict regulatory policies demand extensive documentation, compliance checks, and security reviews. Which SDLC model would be most appropriate for this project and why?

For a government mobile app that needs  **frequent updates**  but also faces  **strict regulatory requirements** , neither pure Agile nor pure Waterfall alone is sufficient. A  **hybrid model**  that combines Agile sprints for development with Waterfall gates for compliance is the best fit. **Why Pure Models Fail Here**

ModelWhy It Fails **Pure Waterfall** Too rigid for weekly feature updates; cannot adapt to user feedback quickly **Pure Agile** Lacks formal documentation and compliance checkpoints required by regulators

**How the Hybrid Model Works**

- **Agile sprints for development:**  Two-week sprints deliver working features based on user feedback. Daily standups, sprint reviews, and retrospectives keep the team responsive.
- **Waterfall gates for compliance:**  Before any release, the code must pass fixed checkpoints: security audit, documentation review, legal sign-off, and penetration testing.
- **Regulatory buffer sprint:**  Every fourth sprint is dedicated solely to compliance tasks — filling documentation gaps, updating security certificates, and preparing audit reports.
- **Versioned releases:**  Instead of continuous deployment, the team batches sprints into quarterly versioned releases that regulators can review as complete packages.

**Why This Model is Most Appropriate**

RequirementHybrid Model SolutionWeekly feature updatesShort Agile sprints deliver incremental valueStrict documentationWaterfall gates enforce formal records before releaseCompliance checksDedicated compliance sprints and pre-release auditsSecurity reviewsMandatory security gate before every production pushRegulatory audit trailVersioned releases with complete change logs

**Example Workflow:**

Week 1-2: Sprint 1 — Develop feedback feature (Agile)Week 3-4: Sprint 2 — Develop notification improvement (Agile)Week 5-6: Sprint 3 — Develop UI enhancement (Agile)Week 7-8: Sprint 4 —  **Compliance sprint**  — Document, audit, secure (Waterfall gate)Week 9: Release version 2.1 with full regulatory package

Government mobile app-এর জন্য যা  **frequent updates**  প্রয়োজন কিন্তু  **strict regulatory requirements** -এর মুখোমুখি, শুধু pure Agile বা pure Waterfall কোনোটাই যথেষ্ট নয়।  **Hybrid model**  যা development-এর জন্য Agile sprints এবং compliance-এর জন্য Waterfall gates combine করে, সবচেয়ে best fit। **কেন Pure Models এখানে Fail করে**

ModelWhy It Fails **Pure Waterfall** Weekly feature updates-এর জন্য too rigid; user feedback-এ দ্রুত adapt করতে পারে না **Pure Agile** Regulators-এর প্রয়োজনীয় formal documentation এবং compliance checkpoints অনুপস্থিত

**Hybrid Model কীভাবে কাজ করে**

- **Development-এর জন্য Agile sprints:**  Two-week sprints user feedback-এর উপর ভিত্তি করে working features deliver করে। Daily standups, sprint reviews, এবং retrospectives team-কে responsive রাখে।
- **Compliance-এর জন্য Waterfall gates:**  যেকোনো release-এর আগে code fixed checkpoints pass করতে হবে: security audit, documentation review, legal sign-off, এবং penetration testing।
- **Regulatory buffer sprint:**  প্রতি চতুর্থ sprint শুধু compliance tasks-এর জন্য dedicated — documentation gaps fill করা, security certificates update করা, এবং audit reports prepare করা।
- **Versioned releases:**  Continuous deployment-এর পরিবর্তে team sprints-কে quarterly versioned releases-এ batch করে যা regulators complete packages হিসেবে review করতে পারে।

**এই Model কেন Most Appropriate**

RequirementHybrid Model SolutionWeekly feature updatesShort Agile sprints incremental value deliver করেStrict documentationWaterfall gates release-এর আগে formal records enforce করেCompliance checksDedicated compliance sprints এবং pre-release auditsSecurity reviewsপ্রতিটি production push-এর আগে mandatory security gateRegulatory audit trailComplete change logs সহ versioned releases

**Example Workflow:**

Week 1-2: Sprint 1 — Feedback feature develop করা (Agile)Week 3-4: Sprint 2 — Notification improvement develop করা (Agile)Week 5-6: Sprint 3 — UI enhancement develop করা (Agile)Week 7-8: Sprint 4 —  **Compliance sprint**  — Document, audit, secure (Waterfall gate)Week 9: Full regulatory package সহ version 2.1 release
