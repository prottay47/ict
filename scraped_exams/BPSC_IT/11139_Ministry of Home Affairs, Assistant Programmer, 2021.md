# Ministry of Home Affairs, Assistant Programmer, 2021

- **Original URL:** [https://it.jobqns.com/ministry-of-home-affairs-assistant-programmer-2021/](https://it.jobqns.com/ministry-of-home-affairs-assistant-programmer-2021/)
- **Date:** 2026-02-04T20:07:05
- **Categories:** BPSC IT Job Solution, BPSC IT Job Solution 2021, Job Solution 2021

---

#### Ministry of Home Affairs
Post:  Assistant ProgarmmerExam Date:  19.12.2021, Exam Taker: BPSC



1. (a) Write down a function in C programming language that will take an n*n matrix as parameter and the dimension n as another parameter, then compute the sum of main diagonal elements of the matrix.

**C Function to Find Sum of Main Diagonal Elements** The function takes an  **n×n matrix**  and its dimension  **n**  as parameters and returns the sum of the main diagonal elements.

```
int diagonalSum(int matrix[][10], int n)
{
int i,sum=0;
for(i=0;i<n;i++)
{sum+=matrix[i][i];
}return sum;
}
```

1. (b) Differentiate between Heap Sort and Merge Sort with necessary examples.

**Difference between Heap Sort and Merge Sort**  **Heap Sort** • Based on  **Binary Heap**  data structure• Sorting is done in-place• Time Complexity: O(n log n) in all cases• Space Complexity: O(1) (in-place)• Not stable sorting algorithm **Example:**  Array: [4,10,3,5,1] → Build Max-Heap → Extract max repeatedly → Sorted array: [1,3,4,5,10]

**Merge Sort** • Based on  **Divide and Conquer**  approach• Array is divided into subarrays and merged• Time Complexity: O(n log n) in all cases• Space Complexity: O(n) (extra memory needed)• Stable sorting algorithm **Example:**  Array: [4,10,3,5,1] → Divide into halves → Merge sorted halves → Sorted array: [1,3,4,5,10]

**Heap Sort এবং Merge Sort এর মধ্যে পার্থক্য**  **Heap Sort** •  **Binary Heap**  ব্যবহার করে কাজ করে• In-place sorting করা হয়• Time Complexity: সব ক্ষেত্রে O(n log n)• Space Complexity: O(1)• Stable নয় **উদাহরণ:**  Array: [4,10,3,5,1] → Max-Heap তৈরি → বারবার max বাদ → Sorted: [1,3,4,5,10]

**Merge Sort** •  **Divide and Conquer**  পদ্ধতিতে কাজ করে• Array ভাগ করে আবার merge করা হয়• Time Complexity: সব ক্ষেত্রে O(n log n)• Space Complexity: O(n)• Stable sorting algorithm **উদাহরণ:**  Array: [4,10,3,5,1] → ছোট ভাগ → merge → Sorted: [1,3,4,5,10]

1. (c) Explain the difference between Stateless and Stateful protocols. Which type of protocol is HTTP?

**Stateless Protocol** A stateless protocol does  **not remember previous interactions**  between the client and server. Each request is treated independently and must contain all the required information to be processed. **Example:**  HTTP, UDP

**Stateful Protocol** A stateful protocol  **maintains session information**  about previous interactions. The server remembers the client’s state and uses it to process future requests. **Example:**  FTP, TCP

**Which Type of Protocol is HTTP?** HTTP is a  **stateless protocol** . Each HTTP request is independent, and the server does not store client information between requests. State management is achieved using cookies and sessions.

**Stateless Protocol** Stateless protocol পূর্ববর্তী client-server যোগাযোগ  **মনে রাখে না** । প্রতিটি request আলাদা ভাবে process হয় এবং প্রয়োজনীয় সব তথ্য একসাথে পাঠাতে হয়। **উদাহরণ:**  HTTP, UDP

**Stateful Protocol** Stateful protocol আগের interaction এর তথ্য  **সংরক্ষণ করে** । Server client এর state মনে রাখে এবং পরবর্তী request এ তা ব্যবহার করে। **উদাহরণ:**  FTP, TCP

**HTTP কোন ধরনের Protocol?** HTTP হলো একটি  **stateless protocol** । প্রতিটি HTTP request স্বাধীন এবং server কোনো client state সংরক্ষণ করে না। Cookie এবং session ব্যবহার করে state বজায় রাখা হয়।

2. (a) What is the subnet mask of 10.2.1.3 /26? What is the usable number of IP addresses on a network that has a /26 mask?

**Subnet Mask of 10.2.1.3/26** /26 means 26 bits are used for the network part.Subnet Mask =  **255.255.255.192**

**Usable Number of IP Addresses** Host bits = 32 − 26 = 6Total IP addresses = 26 = 64Usable IP addresses = 64 − 2 (Network + Broadcast) =  **62**

**10.2.1.3/26 এর Subnet Mask** /26 মানে network অংশে 26 bit ব্যবহার করা হয়েছে।Subnet Mask =  **255.255.255.192**

**Usable IP Address এর সংখ্যা** Host bit = 32 − 26 = 6মোট IP address = 26 = 64Usable IP address = 64 − 2 (Network ও Broadcast বাদ) =  **62**

2. (b) Distinguish between TCP and UDP protocols. **Difference between TCP and UDP**
**TCP এবং UDP এর মধ্যে পার্থক্য**

2. (c) What is the purpose of routers? How does congestion control work in the TCP protocol?

**Purpose of Routers** Routers are network devices used to  **connect multiple networks**  and  **forward data packets**  between them based on IP addresses. They select the best path for data using routing tables and protocols, helping reduce traffic and improve network efficiency.

**Congestion Control in TCP** TCP congestion control prevents network overload by adjusting the data transmission rate. It uses mechanisms such as  **Slow Start**  (gradually increases sending rate),  **Congestion Avoidance**  (careful growth of data rate),  **Fast Retransmit** , and  **Fast Recovery** . TCP detects congestion through packet loss or delay and reduces the sending rate to maintain reliable communication.

**Router এর উদ্দেশ্য** Router হলো এমন একটি নেটওয়ার্ক ডিভাইস যা  **একাধিক নেটওয়ার্ককে সংযুক্ত করে**  এবং IP address অনুযায়ী  **ডাটা প্যাকেট ফরওয়ার্ড**  করে। এটি routing table ও protocol ব্যবহার করে ডাটার জন্য সঠিক পথ নির্বাচন করে এবং নেটওয়ার্কের কার্যকারিতা বাড়ায়।

**TCP তে Congestion Control** TCP congestion control নেটওয়ার্কে অতিরিক্ত চাপ এড়াতে ডাটা পাঠানোর গতি নিয়ন্ত্রণ করে। এতে  **Slow Start** ,  **Congestion Avoidance** ,  **Fast Retransmit**  এবং  **Fast Recovery**  ব্যবহৃত হয়। Packet loss বা delay শনাক্ত হলে TCP ডাটা পাঠানোর হার কমিয়ে নেটওয়ার্ককে স্থিতিশীল রাখে।

3. (a) What is the purpose of database triggers? Explain with an example.

Purpose of Database TriggersA database trigger is a special stored program that automatically executes when an INSERT, UPDATE, or DELETE operation occurs on a table. Triggers are used to maintain data integrity, enforce business rules, and perform automatic actions without user intervention.

**Example** Automatically log salary changes of employees.

```
CREATE TRIGGER salary_update_trigger
AFTER UPDATE ON employee
FOR EACH ROW BEGIN
INSERT INTO salary_log(emp_id, old_salary, new_salary)
VALUES (OLD.emp_id, OLD.salary, NEW.salary);
END;
```

Database Trigger এর উদ্দেশ্যDatabase trigger হলো একটি স্বয়ংক্রিয় program যা কোনো table এ INSERT, UPDATE বা DELETE ঘটলে নিজে থেকেই execute হয়। এটি data integrity বজায় রাখা, business rule প্রয়োগ এবং স্বয়ংক্রিয় কাজ সম্পাদনের জন্য ব্যবহৃত হয়।

**উদাহরণ** Employee এর salary পরিবর্তন হলে তা স্বয়ংক্রিয়ভাবে log table এ সংরক্ষণ করা।

```
CREATE TRIGGER salary_update_trigger
AFTER UPDATE ON employee
FOR EACH ROW BEGIN
INSERT INTO salary_log(emp_id, old_salary, new_salary)
VALUES (OLD.emp_id, OLD.salary, NEW.salary);
END;
```

3. (b) Explain the different types of database keys with examples.

**Types of Database Keys**  **Primary Key** : A key that uniquely identifies each record in a table and cannot be NULL. **Example:**  Student(student_id, name) → student_id

**Foreign Key** : A key that references the primary key of another table to maintain relationships. **Example:**  Order(customer_id) references Customer(customer_id)

**Candidate Key** : All possible keys that can uniquely identify records; one is chosen as primary key. **Example:**  Employee(emp_id, email) → emp_id, email

**Super Key** : A set of one or more attributes that uniquely identify records (may contain extra attributes). **Example:**  (emp_id, name)

**Composite Key** : A key formed by combining two or more attributes. **Example:**  Enrollment(student_id, course_id)

**Database Key এর প্রকারভেদ**  **Primary Key** : একটি table এর প্রতিটি record কে আলাদা করে শনাক্ত করে এবং NULL হতে পারে না। **উদাহরণ:**  Student(student_id, name) → student_id

**Foreign Key** : অন্য table এর primary key কে reference করে সম্পর্ক তৈরি করে। **উদাহরণ:**  Order(customer_id) → Customer(customer_id)

**Candidate Key** : যেসব key দিয়ে uniquely record শনাক্ত করা যায়; এর মধ্যে একটি primary key হয়। **উদাহরণ:**  Employee(emp_id, email)

**Super Key** : এক বা একাধিক attribute এর সমষ্টি যা record uniquely চিহ্নিত করে। **উদাহরণ:**  (emp_id, name)

**Composite Key** : দুই বা ততোধিক attribute মিলিয়ে তৈরি key। **উদাহরণ:**  Enrollment(student_id, course_id)

3. (c) Between Depth First Search (DFS) and Breadth First Search (BFS), which one is faster? Which one requires more memory?

**DFS vs BFS: Speed and Memory**  **Which is faster?**  It depends on the problem.  **BFS**  is faster for finding the  **shortest path**  (in unweighted graphs) because it explores level by level.  **DFS**  may be faster when the solution is deep and not necessarily the shortest.

**Which uses more memory?**   **BFS**  requires  **more memory**  because it stores all nodes at the current level (queue).  **DFS**  uses  **less memory**  as it stores only the path being explored (stack/recursion).

**DFS ও BFS: গতি ও মেমরি**  **কোনটি দ্রুত?**  সমস্যা অনুযায়ী ভিন্ন।  **BFS**  unweighted graph এ  **shortest path**  খুঁজতে দ্রুত, কারণ এটি level-by-level খোঁজে।  **DFS**  গভীর কোনো সমাধান থাকলে তুলনামূলক দ্রুত হতে পারে।

**কোনটি বেশি মেমরি লাগে?**   **BFS**  এ  **বেশি মেমরি**  লাগে (queue তে একই level এর সব node রাখতে হয়)।  **DFS**  এ  **কম মেমরি**  লাগে (শুধু বর্তমান path/stack রাখা হয়)।

4. (a) What are the differences between a linked list and a stack data structure?

**Difference between Linked List and Stack**  **Linked List** • A dynamic data structure consisting of nodes linked by pointers• Insertion and deletion can be done at any position• No restriction on access order• Can be singly, doubly, or circular linked list• Used to implement dynamic memory structures

**Stack** • A linear data structure following  **LIFO (Last In First Out)**  principle• Insertion (push) and deletion (pop) occur only at one end (top)• Restricted access to elements• Can be implemented using array or linked list• Used in function calls, expression evaluation, undo operations

**Linked List এবং Stack এর মধ্যে পার্থক্য**  **Linked List** • Pointer দ্বারা সংযুক্ত node নিয়ে গঠিত dynamic data structure• যেকোনো position এ insertion ও deletion করা যায়• Access করার ক্ষেত্রে কোনো নির্দিষ্ট নিয়ম নেই• Singly, doubly ও circular linked list হতে পারে• Dynamic memory ব্যবস্থাপনায় ব্যবহৃত হয়

**Stack** •  **LIFO (Last In First Out)**  নীতির উপর ভিত্তি করে কাজ করে• শুধুমাত্র top position এ insertion ও deletion হয়• Access সীমাবদ্ধ থাকে• Array বা linked list দিয়ে implement করা যায়• Function call, expression evaluation ও undo operation এ ব্যবহৃত হয়

4. (b) What are the differences between supervised and unsupervised learning? Explain with examples.

**Difference between Supervised and Unsupervised Learning**  **Supervised Learning** • Uses  **labeled data**  (input with known output)• Learns by mapping inputs to correct outputs• Used for prediction and classification tasks• Requires training data with labels **Example:**  Email spam detection, house price prediction, student result prediction

**Unsupervised Learning** • Uses  **unlabeled data**  (no predefined output)• Finds hidden patterns or groupings in data• Used for clustering and association analysis• Does not require labeled data **Example:**  Customer segmentation, market basket analysis, grouping similar images

**Supervised এবং Unsupervised Learning এর মধ্যে পার্থক্য**  **Supervised Learning** •  **Labeled data**  ব্যবহার করে (input ও output জানা থাকে)• Input থেকে সঠিক output শেখে• Prediction ও classification কাজে ব্যবহৃত হয়• Training data তে label থাকতে হয় **উদাহরণ:**  Email spam শনাক্তকরণ, বাড়ির দাম নির্ণয়, পরীক্ষার ফলাফল পূর্বাভাস

**Unsupervised Learning** •  **Unlabeled data**  ব্যবহার করে• Data এর ভেতরের লুকানো pattern খুঁজে বের করে• Clustering ও association কাজে ব্যবহৃত হয়• Label প্রয়োজন হয় না **উদাহরণ:**  Customer segmentation, market basket analysis, একই ধরনের ছবি grouping

4. (c) What are the three types of services provided by the cloud?

**Three Types of Cloud Services**  **1) IaaS (Infrastructure as a Service):**  Provides virtualized hardware resources like servers, storage, and networks. **Example:**  Amazon EC2, Google Compute Engine

**2) PaaS (Platform as a Service):**  Provides a platform to develop, test, and deploy applications without managing infrastructure. **Example:**  Google App Engine, Heroku

**3) SaaS (Software as a Service):**  Provides ready-to-use software applications over the internet. **Example:**  Gmail, Microsoft Office 365

**Cloud এর তিনটি Service টাইপ**  **১) IaaS (Infrastructure as a Service):**  Server, storage ও network এর মতো virtual hardware প্রদান করে। **উদাহরণ:**  Amazon EC2, Google Compute Engine

**২) PaaS (Platform as a Service):**  Application তৈরি, test ও deploy করার জন্য platform দেয়। **উদাহরণ:**  Google App Engine, Heroku

**৩) SaaS (Software as a Service):**  Internet এর মাধ্যমে প্রস্তুত software ব্যবহার করার সুযোগ দেয়। **উদাহরণ:**  Gmail, Microsoft Office 365

5. (a) Distinguish between Frequency Division Multiplexing (FDM) and Time Division Multiplexing (TDM).

**Difference between FDM and TDM**  **Frequency Division Multiplexing (FDM)** • Divides the available bandwidth into multiple frequency bands• Each signal is transmitted simultaneously on different frequencies• Requires guard bands to avoid interference• Used mainly in analog communication **Example:**  Radio and cable TV transmission

**Time Division Multiplexing (TDM)** • Divides the channel into different time slots• Each signal uses the full bandwidth but at different times• No guard band is required• Used mainly in digital communication **Example:**  Digital telephony, GSM

**FDM এবং TDM এর মধ্যে পার্থক্য**  **Frequency Division Multiplexing (FDM)** • Bandwidth কে একাধিক frequency band এ ভাগ করা হয়• সব signal একই সময়ে ভিন্ন frequency তে পাঠানো হয়• Interference এড়াতে guard band প্রয়োজন হয়• প্রধানত analog communication এ ব্যবহৃত হয় **উদাহরণ:**  Radio ও cable TV transmission

**Time Division Multiplexing (TDM)** • Channel কে বিভিন্ন time slot এ ভাগ করা হয়• প্রতিটি signal আলাদা সময়ে পুরো bandwidth ব্যবহার করে• Guard band প্রয়োজন হয় না• প্রধানত digital communication এ ব্যবহৃত হয় **উদাহরণ:**  Digital telephony, GSM

5. (b) Differentiate between vector and raster graphics. What are the applications of computer graphics?

**Difference between Vector and Raster Graphics**  **Vector Graphics** • Based on mathematical paths (lines, curves, shapes)• Resolution-independent; no quality loss on scaling• Smaller file size for simple images• Easy to edit shapes and colors **Examples:**  SVG, AI, EPS

**Raster Graphics** • Made of pixels arranged in a grid• Resolution-dependent; quality degrades when scaled up• Larger file size for high resolution• Best for complex images and photos **Examples:**  JPEG, PNG, BMP

**Applications of Computer Graphics** • User interfaces and web design• Animation, movies, and games• Medical imaging and visualization• CAD/CAM and engineering design• Education, simulations, and data visualization

**Vector ও Raster Graphics এর পার্থক্য**  **Vector Graphics** • Mathematical path (line, curve, shape) দিয়ে তৈরি• Resolution-independent; zoom করলে quality নষ্ট হয় না• Simple image এ file size ছোট• Shape ও color সহজে edit করা যায় **উদাহরণ:**  SVG, AI, EPS

**Raster Graphics** • Pixel দিয়ে তৈরি grid-based image• Resolution-dependent; বড় করলে quality কমে• High resolution এ file size বড়• Photo ও complex image এর জন্য উপযুক্ত **উদাহরণ:**  JPEG, PNG, BMP

**Computer Graphics এর ব্যবহার** • UI ও web design• Animation, movie ও game• Medical imaging ও visualization• CAD/CAM ও engineering design• Education, simulation ও data visualization

5. (c) What is a thread? Give some benefits of multi-threaded programming.

**Thread** A thread is the  **smallest unit of execution**  within a process. Multiple threads can exist inside a single process and  **share the same memory and resources**  while executing independently.

**Benefits of Multithreaded Programming** • Better CPU utilization by running tasks in parallel• Faster execution and improved application performance• Efficient resource sharing (shared memory)• Improved responsiveness (e.g., UI remains active)• Lower overhead compared to multiple processes

**Thread** Thread হলো একটি process এর ভেতরের  **সবচেয়ে ছোট execution unit** । একটি process এর মধ্যে একাধিক thread থাকতে পারে এবং তারা  **একই memory ও resource share করে**  আলাদাভাবে কাজ করতে পারে।

**Multithreaded Programming এর সুবিধা** • CPU এর ভাল ব্যবহার (parallel execution)• দ্রুত execution ও ভাল performance• Resource sharing সহজ (shared memory)• Application এর responsiveness বৃদ্ধি পায়• Multiple process এর তুলনায় কম overhead

6. (a) What is Artificial Intelligence (AI)? What are the necessary conditions for a deadlock in an operating system?

**Artificial Intelligence (AI)** Artificial Intelligence (AI) is a branch of computer science that focuses on creating systems capable of  **performing tasks that normally require human intelligence** , such as learning, reasoning, problem-solving, decision-making, and understanding natural language.

**Necessary Conditions for Deadlock in an Operating System** A deadlock occurs when a set of processes are blocked forever because each process is holding a resource and waiting for another. For a deadlock to occur, the following  **four conditions must hold simultaneously** :•  **Mutual Exclusion:**  At least one resource must be held in a non-shareable mode.•  **Hold and Wait:**  A process holds one or more resources while waiting for additional resources.•  **No Preemption:**  Resources cannot be forcibly taken from a process; they must be released voluntarily.•  **Circular Wait:**  A circular chain of processes exists where each process waits for a resource held by the next process.

**Artificial Intelligence (AI)** Artificial Intelligence (AI) হলো computer science এর একটি শাখা, যেখানে এমন system তৈরি করা হয় যা  **মানুষের মতো বুদ্ধিমত্তা ব্যবহার করে কাজ করতে পারে** , যেমন শেখা, চিন্তা করা, সমস্যা সমাধান, সিদ্ধান্ত নেওয়া এবং ভাষা বোঝা।

**Operating System এ Deadlock হওয়ার শর্তসমূহ** Deadlock ঘটে যখন কিছু process একে অপরের resource এর জন্য অনির্দিষ্ট সময় অপেক্ষা করে থাকে। Deadlock হওয়ার জন্য নিচের  **চারটি শর্ত একসাথে পূরণ হতে হয়** :•  **Mutual Exclusion:**  অন্তত একটি resource এক সময়ে একটি process ব্যবহার করতে পারে।•  **Hold and Wait:**  একটি process কিছু resource ধরে রেখে অন্য resource এর জন্য অপেক্ষা করে।•  **No Preemption:**  Resource জোর করে কেড়ে নেওয়া যায় না।•  **Circular Wait:**  Process গুলোর মধ্যে একটি বৃত্তাকার অপেক্ষার অবস্থা তৈরি হয়।

6. (b) Simplify the following expression using Boolean Algebra, x'y'z + x'yz + x'yz + x'y

**Given Expression** x’y’z + x’yz + x’yz + x’y **=** x’y’z + x’yz + x’y      [a+a=a]=x'(y’z + yz + y)=x'(y + z)        [y’z + yz = z(y’ + y) = z] **x'(y + z)**

6. (c) Using a truth table, find which of the following implications are equivalent to p → q i.  q → p  ii. ¬ q → ¬ p

p
q
p → q
q → p
¬q → ¬p

T
T
T
T
T

T
F
F
T
F

F
T
T
F
T

F
F
T
T
T

• The truth values of  **p → q**  and  **¬q → ¬p**  are identical in all cases.

• The truth values of  **q → p**  differ from  **p → q** .

**Therefore:**

**¬q → ¬p**  is equivalent to  **p → q** , but  **q → p**  is not.
