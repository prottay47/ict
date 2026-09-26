# M4: Operating System (Memory Management: Memory Allocation)

- **Original URL:** [https://it.jobqns.com/m4-operating-system-memory-management-memory-allocation/](https://it.jobqns.com/m4-operating-system-memory-management-memory-allocation/)
- **Date:** 2026-09-13T22:56:38
- **Categories:** Uncategorized, IT Preparation Module

---

**Operating System:**  Memory Allocation (ET: 1.5 Hours)



**Video Tutorial:**  Memory Allocation



- **Watch Video:**   Memory management in operating system

- **Watch Video:**  Functions and goals of memory management

- **Watch Video:**  Swapping

- **Watch Video:**  Contiguous and Non Contiguous | Memory Allocation

- **Watch Video:**  Fixed Size Partition | Contiguous Memory Allocation

- **Watch Video:**  Internal & External Fragmentation

- **Watch Video:**  Variable Size Partition | Contiguous Memory Allocation

Memory Allocation

- 1

What is Memory Management? Write Functions and Goals of Memory Management.


Memory Management is an important function of an Operating System that manages the system's Primary Memory (Main Memory).
It manages the allocation and deallocation of memory for processes, keeps track of which memory locations are allocated and which are free, and manages the movement of data between Primary Memory and Secondary Memory when required.
Memory Management helps the Operating System achieve better  **concurrency, system performance, and memory utilization** .
**Functions of Memory Management**
**1. Memory Allocation and Deallocation:**  The Operating System allocates memory to processes when they need it and releases the memory when the processes finish or no longer need it.
**2. Tracking Memory Usage:**  The Operating System keeps track of the status of memory locations, identifying which parts of memory are allocated and which parts are free.
**3. Process Movement:**  Memory Management can move processes or data between Primary Memory and Secondary Memory when required, allowing the system to manage limited Main Memory efficiently.
**4. Memory Protection:**  The Operating System protects the memory allocated to one process from being improperly accessed or corrupted by another process. This helps prevent unexpected or faulty system behavior.
**5. Memory Sharing:**  Memory Management allows processes to share memory spaces when required. This can help multiple programs use shared memory resources efficiently.
**Goals of Memory Management**
**1. Efficient Memory Utilization:**  To use the available Primary Memory efficiently and reduce unnecessary memory wastage.
**2. Better Concurrency:**  To allow multiple processes to reside in memory and execute efficiently, improving the overall concurrency of the system.
**3. Better System Performance:**  To manage memory efficiently so that processes can execute smoothly and the system can provide better performance.
**4. Memory Protection:**  To prevent one process from interfering with or corrupting the memory allocated to another process.
**5. Support for Large Programs:**  To enable programs that require more memory than the currently available Primary Memory by moving data between Primary and Secondary Memory when necessary.
**6. Efficient Memory Sharing:**  To allow processes to share memory spaces when required while maintaining proper memory management.

Memory Management হলো Operating System-এর একটি গুরুত্বপূর্ণ Function, যার মাধ্যমে সিস্টেমের Primary Memory (Main Memory) পরিচালনা করা হয়।
এটি বিভিন্ন Process-এর জন্য Memory Allocation ও Deallocation পরিচালনা করে, কোন Memory Location ব্যবহৃত হচ্ছে এবং কোনটি Free আছে তা নির্ধারণ করে এবং প্রয়োজন অনুযায়ী Primary Memory ও Secondary Memory-এর মধ্যে Data বা Process স্থানান্তর করতে পারে।
Memory Management-এর মাধ্যমে Operating System উন্নত  **Concurrency, System Performance এবং Memory Utilization**  অর্জন করতে পারে।
**Memory Management-এর Functions**
**1. Memory Allocation ও Deallocation:**  কোনো Process-এর Memory প্রয়োজন হলে Operating System তাকে Memory Allocate করে এবং Process শেষ হলে বা Memory আর প্রয়োজন না হলে সেই Memory Release করে।
**2. Memory Usage Tracking:**  Operating System Memory-এর প্রতিটি অংশের অবস্থা পর্যবেক্ষণ করে এবং কোন অংশ Allocated ও কোন অংশ Free রয়েছে তা Track করে।
**3. Process Movement:**  প্রয়োজন অনুযায়ী Primary Memory এবং Secondary Memory-এর মধ্যে Process বা Data স্থানান্তর করা যায়। এর মাধ্যমে সীমিত Main Memory আরও কার্যকরভাবে ব্যবহৃত হয়।
**4. Memory Protection:**  একটি Process-এর জন্য বরাদ্দকৃত Memory অন্য কোনো Process যেন অনুপযুক্তভাবে Access বা Corrupt করতে না পারে, Operating System তা নিশ্চিত করে। এর ফলে Unexpected বা Faulty System Behavior প্রতিরোধ করা যায়।
**5. Memory Sharing:**  প্রয়োজন অনুযায়ী একাধিক Process-এর মধ্যে Memory Space Share করার ব্যবস্থা করা যায়। এর ফলে Shared Memory Resources আরও কার্যকরভাবে ব্যবহার করা সম্ভব হয়।
**Memory Management-এর Goals**
**1. Efficient Memory Utilization:**  Available Primary Memory কার্যকরভাবে ব্যবহার করা এবং অপ্রয়োজনীয় Memory Wastage কমানো।
**2. Better Concurrency:**  একাধিক Process-কে Memory-তে অবস্থান ও কার্যকরভাবে Execute করার সুযোগ দিয়ে System-এর Concurrency বৃদ্ধি করা।
**3. Better System Performance:**  Memory দক্ষতার সাথে পরিচালনা করে Process-এর Smooth Execution নিশ্চিত করা এবং System Performance উন্নত করা।
**4. Memory Protection:**  একটি Process যেন অন্য Process-এর জন্য Allocated Memory-তে অনুপযুক্তভাবে Access বা Interference করতে না পারে তা নিশ্চিত করা।
**5. Support for Large Programs:**  কোনো Program-এর প্রয়োজনীয় Memory Available Primary Memory-এর চেয়ে বেশি হলেও প্রয়োজন অনুযায়ী Primary Memory ও Secondary Memory-এর মধ্যে Data স্থানান্তরের মাধ্যমে সেই Program পরিচালনা করতে সহায়তা করা।
**6. Efficient Memory Sharing:**  প্রয়োজন অনুযায়ী একাধিক Process-এর মধ্যে Memory Space Share করার সুযোগ দেওয়া এবং একই সাথে সঠিক Memory Management নিশ্চিত করা।

2

Swapping in Operating System


**What is Swapping?**
Swapping is a Memory Management technique in an Operating System in which a Process is temporarily moved between  **Main Memory (RAM)**  and  **Secondary Memory (Hard Drive)**  to manage limited memory efficiently.
Suppose several Processes such as P1, P2, P3, and P4 are ready to be executed. If P1 and P2 consume a large amount of memory, there may not be enough Main Memory available for P3 and P4. In such a situation, the Operating System can temporarily move a suitable Process from Main Memory to Secondary Memory to make memory available for another Process.
The area of Secondary Memory where swapped-out Processes are stored is called  **Swap Space** .
When sufficient Main Memory becomes available, the swapped-out Process can be brought back into Main Memory and its execution can continue.
**Swap In**
Swap In is the process of bringing a Process from  **Secondary Memory (Hard Drive)**  into  **Main Memory (RAM)**  so that it can be executed or its execution can continue.
**Secondary Memory → Main Memory**
**Swap Out**
Swap Out is the process of moving a Process from  **Main Memory (RAM)**  to  **Secondary Memory (Hard Drive)**  to free Main Memory for another Process.
**Main Memory → Secondary Memory**
**Medium-Term Scheduler**
The  **Medium-Term Scheduler (MTS)**  manages the swapping of Processes between Main Memory and Secondary Memory.
**Advantages of Swapping**
**1. Maximum CPU Utilization:**  Swapping helps keep suitable Processes available for execution so that the CPU can remain busy as much as possible.
**2. Memory Availability:**  Swapping creates free space in Main Memory for Processes that need to be executed.
**3. Avoids Process Starvation:**  Swapping can help provide execution opportunities to waiting Processes by making the required memory available.
**4. Supports Multiple Processes:**  Swapping allows the Operating System to manage more Processes even when the available Main Memory is limited.
**5. Proper RAM Utilization:**  It helps the Operating System utilize Main Memory efficiently by temporarily moving Processes to Secondary Memory.
**6. Swap Space:**  Swapping uses a dedicated area of Secondary Memory, called  **Swap Space** , to store swapped-out Processes.
**7. Supports Priority-based Scheduling:**  In priority-based scheduling, a suitable Low-Priority Process may be swapped out so that a High-Priority Process can be brought into Main Memory for execution.
**8. Economical Memory Management:**  Swapping helps manage limited Main Memory by using available Secondary Memory when required.
**Disadvantage of Swapping:**  Swapping can affect system performance because transferring Processes between Main Memory and Secondary Memory requires additional time.

**Swapping কী?**
Swapping হলো Operating System-এর একটি Memory Management Technique, যেখানে সীমিত Memory কার্যকরভাবে ব্যবহারের জন্য একটি Process-কে সাময়িকভাবে  **Main Memory (RAM)**  এবং  **Secondary Memory (Hard Drive)** -এর মধ্যে স্থানান্তর করা হয়।
ধরা যাক, P1, P2, P3 এবং P4 নামে কয়েকটি Process Execution-এর জন্য Ready অবস্থায় রয়েছে। যদি P1 এবং P2 বেশি পরিমাণ Memory ব্যবহার করে, তাহলে P3 এবং P4-এর জন্য Main Memory-তে পর্যাপ্ত জায়গা নাও থাকতে পারে। এই অবস্থায় Operating System উপযুক্ত কোনো Process-কে সাময়িকভাবে Main Memory থেকে Secondary Memory-তে পাঠিয়ে অন্য Process-এর জন্য Memory Available করতে পারে।
Secondary Memory-এর যে অংশে Swapped-out Process সংরক্ষণ করা হয় তাকে  **Swap Space**  বলা হয়।
পরবর্তীতে Main Memory-তে পর্যাপ্ত জায়গা তৈরি হলে Swapped-out Process-কে আবার Main Memory-তে নিয়ে আসা হয় এবং তার Execution পুনরায় শুরু করা যায়।
**Swap In**
Swap In হলো কোনো Process-কে  **Secondary Memory (Hard Drive)**  থেকে  **Main Memory (RAM)** -তে নিয়ে আসার প্রক্রিয়া, যাতে Process-টির Execution শুরু বা পুনরায় চালু করা যায়।
**Secondary Memory → Main Memory**
**Swap Out**
Swap Out হলো কোনো Process-কে  **Main Memory (RAM)**  থেকে  **Secondary Memory (Hard Drive)** -তে স্থানান্তর করার প্রক্রিয়া, যাতে Main Memory-তে অন্য Process-এর জন্য জায়গা তৈরি হয়।
**Main Memory → Secondary Memory**
**Medium-Term Scheduler**
**Medium-Term Scheduler (MTS)**  Main Memory এবং Secondary Memory-এর মধ্যে Process Swapping পরিচালনা করে।
**Swapping-এর সুবিধা**
**1. Maximum CPU Utilization:**  Execution-এর জন্য উপযুক্ত Process Available রাখার মাধ্যমে CPU-কে যতটা সম্ভব ব্যস্ত রাখতে Swapping সাহায্য করে।
**2. Memory Availability:**  Main Memory থেকে কোনো Process সরিয়ে অন্য Process-এর Execution-এর জন্য খালি Memory তৈরি করা যায়।
**3. Process Starvation কমাতে সাহায্য করে:**  অপেক্ষমাণ Process-এর জন্য প্রয়োজনীয় Memory Available করে Execution-এর সুযোগ দিতে Swapping সাহায্য করতে পারে।
**4. Multiple Process Support:**  Main Memory সীমিত হলেও Swapping-এর মাধ্যমে অধিক সংখ্যক Process পরিচালনা করা সম্ভব হয়।
**5. Proper RAM Utilization:**  প্রয়োজন অনুযায়ী Process-কে Secondary Memory-তে সাময়িকভাবে স্থানান্তর করে Main Memory কার্যকরভাবে ব্যবহার করা যায়।
**6. Swap Space:**  Swapping-এর জন্য Secondary Memory-তে একটি নির্দিষ্ট স্থান ব্যবহার করা হয়, যাকে  **Swap Space**  বলা হয়। এখানে Swapped-out Process সংরক্ষণ করা হয়।
**7. Priority-based Scheduling Support:**  Priority-based Scheduling-এর ক্ষেত্রে উপযুক্ত কোনো Low-Priority Process-কে Swap Out করে High-Priority Process-কে Main Memory-তে এনে Execution করা যেতে পারে।
**8. Economical Memory Management:**  সীমিত Main Memory-এর পাশাপাশি Secondary Memory ব্যবহার করে Memory Management আরও কার্যকরভাবে করা যায়।
**Swapping-এর অসুবিধা:**  Swapping System Performance-এর উপর প্রভাব ফেলতে পারে, কারণ Main Memory এবং Secondary Memory-এর মধ্যে Process স্থানান্তর করতে অতিরিক্ত সময় লাগে।

3

Memory Allocation in Operating System: Contiguous & Non Contiguous


Memory Allocation is the process of assigning memory space to a process or program by the Operating System. There are two main types of memory allocation strategies:  **Contiguous Memory Allocation**  and  **Non-Contiguous Memory Allocation** .
**1. Contiguous Memory Allocation**
Contiguous Memory Allocation refers to assigning sequential physical memory blocks to a process or program. In this technique, a process is allocated a single continuous block of memory rather than scattered blocks.
When a process requests memory, the Operating System searches for a free continuous memory area large enough to hold the process. Since the allocated memory addresses are adjacent, memory addressing and access are relatively simple and fast.
**Important Points:**  Contiguous Memory Allocation makes memory addressing easier and can improve memory access speed. When processes are loaded and removed, small gaps may be created between allocated blocks. This causes  **External Fragmentation** . External Fragmentation may prevent a large process from being allocated even when the total amount of free memory is sufficient. The Operating System can use techniques such as  **Compaction**  to rearrange memory and reduce fragmentation.
**2. Non-Contiguous Memory Allocation**
Non-Contiguous Memory Allocation allows a process to be stored in multiple dispersed or non-adjacent memory regions. Unlike Contiguous Memory Allocation, the entire process does not need to occupy one continuous block of physical memory.
This technique is useful when memory has fragmented free spaces or when processes have variable memory requirements. The Operating System uses data structures such as tables or linked structures to keep track of available memory blocks.
**Important Points:**  Non-Contiguous Memory Allocation provides greater flexibility because a process can use scattered memory areas. It can help reduce  **External Fragmentation**  because available gaps can be used more flexibly. Memory management is more complex because the Operating System must track multiple memory locations. Allocation may be slower because the Operating System needs to search for suitable memory areas and manage additional information. This approach is commonly associated with systems having dynamic memory requirements.
**Difference Between Contiguous and Non-Contiguous Memory Allocation**

Aspect
Contiguous Memory Allocation
Non-Contiguous Memory Allocation

**Memory Layout**
Memory blocks are sequentially adjacent.
Memory blocks can be scattered throughout memory.

**Fragmentation**
External Fragmentation may occur due to changing block sizes.
Can reduce External Fragmentation by using available gaps more flexibly.

**Allocation**
Generally simpler and faster.
More complex because scattered memory areas must be managed.

**Memory Access**
Relatively simple and fast because addresses are contiguous.
More complex because memory locations may be scattered.

**Flexibility**
Less flexible because a continuous block is required.
More flexible because multiple memory areas can be used.

**Usage**
Suitable for systems with simpler or fixed memory requirements.
Suitable for systems with dynamic memory requirements.

Memory Allocation হলো Operating System কর্তৃক কোনো Process বা Program-এর জন্য Memory Space নির্ধারণ করার প্রক্রিয়া। Memory Management-এর ক্ষেত্রে প্রধানত দুই ধরনের Memory Allocation Strategy রয়েছে:  **Contiguous Memory Allocation**  এবং  **Non-Contiguous Memory Allocation** ।
**১. Contiguous Memory Allocation**
Contiguous Memory Allocation হলো কোনো Process বা Program-এর জন্য পরপর বা sequential physical memory blocks বরাদ্দ করার পদ্ধতি। এই পদ্ধতিতে একটি Process-কে একটি continuous memory block দেওয়া হয়, scattered memory block নয়।
কোনো Process Memory চাইলে Operating System এমন একটি free continuous memory area খুঁজে বের করে, যেখানে পুরো Process-টি রাখা যায়। যেহেতু Memory Address-গুলো পরপর থাকে, তাই Memory Addressing এবং Access তুলনামূলকভাবে সহজ ও দ্রুত হয়।
**গুরুত্বপূর্ণ বিষয়:**  Contiguous Memory Allocation Memory Addressing সহজ করে এবং Memory Access-এর speed বাড়াতে পারে। Process Memory-তে Load এবং Remove করার সময় allocated blocks-এর মাঝে ছোট ছোট free gaps তৈরি হতে পারে। একে  **External Fragmentation**  বলা হয়। External Fragmentation-এর কারণে পর্যাপ্ত মোট free memory থাকা সত্ত্বেও একটি বড় Process-এর জন্য প্রয়োজনীয় continuous memory block পাওয়া নাও যেতে পারে। Operating System  **Compaction** -এর মতো technique ব্যবহার করে Memory পুনর্বিন্যাস করে Fragmentation কমাতে পারে।
**২. Non-Contiguous Memory Allocation**
Non-Contiguous Memory Allocation হলো এমন একটি পদ্ধতি যেখানে একটি Process-কে একাধিক dispersed বা non-adjacent memory region-এ রাখা যায়। অর্থাৎ পুরো Process-টিকে একটি continuous memory block-এ রাখার প্রয়োজন হয় না।
Memory-তে fragmented free space থাকলে অথবা Process-এর Memory requirement পরিবর্তনশীল হলে এই পদ্ধতি বেশি flexible। Operating System বিভিন্ন available memory block-এর তথ্য সংরক্ষণ ও পরিচালনার জন্য table বা linked structure-এর মতো data structure ব্যবহার করে।
**গুরুত্বপূর্ণ বিষয়:**  Non-Contiguous Memory Allocation বেশি flexibility প্রদান করে, কারণ একটি Process-এর জন্য scattered memory area ব্যবহার করা যায়। Available memory gaps বিভিন্নভাবে ব্যবহার করা যায় বলে এটি  **External Fragmentation**  কমাতে সাহায্য করতে পারে। Memory Management তুলনামূলকভাবে বেশি complex, কারণ Operating System-কে একাধিক Memory Location track করতে হয়। Suitable memory area খুঁজে বের করা এবং অতিরিক্ত information manage করার কারণে Allocation তুলনামূলকভাবে ধীর হতে পারে। Dynamic Memory requirement থাকা system-এ এই পদ্ধতি বেশি উপযোগী।
**Contiguous এবং Non-Contiguous Memory Allocation-এর পার্থক্য**

বিষয়
Contiguous Memory Allocation
Non-Contiguous Memory Allocation

**Memory Layout**
Memory blocks পরপর বা adjacent থাকে।
Memory blocks বিভিন্ন জায়গায় scattered থাকতে পারে।

**Fragmentation**
Changing block size-এর কারণে External Fragmentation হতে পারে।
Available gaps flexibleভাবে ব্যবহার করে External Fragmentation কমাতে পারে।

**Allocation**
তুলনামূলকভাবে সহজ ও দ্রুত।
Scattered memory area manage করতে হয় বলে বেশি complex।

**Memory Access**
Contiguous address হওয়ায় তুলনামূলকভাবে সহজ ও দ্রুত।
Memory Location scattered হওয়ায় তুলনামূলকভাবে complex।

**Flexibility**
কম flexible, কারণ continuous block প্রয়োজন।
বেশি flexible, কারণ একাধিক memory area ব্যবহার করা যায়।

**ব্যবহার**
Simple বা fixed memory requirement-এর system-এর জন্য উপযোগী।
Dynamic memory requirement-এর system-এর জন্য উপযোগী।

4

Contiguous Memory Allocation Techniques : Fixed Size Partition Scheme


In Contiguous Memory Allocation, whenever a process needs memory space, the Operating System allocates a  **continuous empty block**  of memory to the process.
Contiguous Memory Allocation can be done in two ways:
**1. Fixed-size Partition Scheme**   **2. Variable-size Partition Scheme**
**Fixed-size Partition Scheme**
Fixed-size Partition Scheme is a Contiguous Memory Allocation technique in which  **each process is allocated a fixed-size continuous block**  in Main Memory.
In this method, the entire memory is divided into a number of  **continuous fixed-size partitions** . When a new process is loaded, each partition can hold  **exactly one process** .
Since the partition size is fixed, every process is allocated the same-size memory block regardless of the actual size of the process. Therefore, this technique is also called  **Fixed Partitioning**  or  **Static Partitioning** .
**Example:**  Suppose there are three processes of sizes  **3 MB, 1 MB, and 4 MB** , and each memory partition has a fixed size of  **5 MB** . The 3 MB process is allocated a 5 MB partition. The 1 MB process is allocated another 5 MB partition. The 4 MB process is also allocated another 5 MB partition. Thus, the actual process size does not determine the partition size; the  **partition size is fixed** .
**Degree of Multiprogramming**
The number of processes that can stay in Main Memory at the same time is called the  **Degree of Multiprogramming** .
In Fixed-size Partitioning, the degree of multiprogramming is determined by the  **number of partitions**  created in Main Memory.
**Advantages of Fixed-size Partition Scheme**  1. It is  **simple to implement**  because the memory is divided into fixed-size blocks and processes are assigned to those blocks. 2. It is easy to  **keep track of available memory blocks** , which determines how many more processes can be loaded into memory. 3. Multiple processes can remain in Main Memory at the same time, so it supports  **Multiprogramming** .
**Disadvantages of Fixed-size Partition Scheme**  1. A process whose size is  **greater than the partition size**  cannot be allocated to any partition. 2. The  **number of partitions**  determines the Degree of Multiprogramming, so only that many processes can remain in Main Memory at a time. 3. If a process is smaller than its allocated partition, the unused portion of that partition is wasted. This causes  **Internal Fragmentation** .

Contiguous Memory Allocation-এ কোনো Process-এর জন্য Memory Space প্রয়োজন হলে Operating System Process-টিকে একটি  **continuous empty memory block**  বরাদ্দ করে।
Contiguous Memory Allocation প্রধানত দুইভাবে করা যায়:
**১. Fixed-size Partition Scheme**   **২. Variable-size Partition Scheme**
**Fixed-size Partition Scheme**
Fixed-size Partition Scheme হলো একটি Contiguous Memory Allocation technique, যেখানে প্রতিটি Process-এর জন্য Main Memory-তে একটি  **fixed-size continuous memory block**  বরাদ্দ করা হয়।
এই পদ্ধতিতে সম্পূর্ণ Memory-কে কয়েকটি  **continuous fixed-size partition** -এ ভাগ করা হয়। কোনো নতুন Process Memory-তে Load হলে প্রতিটি Partition-এ  **একটি Process**  রাখা যায়।
Partition-এর Size fixed হওয়ায় Process-এর প্রকৃত Size যাই হোক না কেন, প্রতিটি Process-এর জন্য একই Size-এর Memory Block বরাদ্দ করা হয়। তাই এই technique-কে  **Fixed Partitioning**  বা  **Static Partitioning** ও বলা হয়।
**উদাহরণ:**  ধরা যাক, তিনটি Process-এর Size হলো  **3 MB, 1 MB এবং 4 MB**  এবং প্রতিটি Memory Partition-এর fixed Size হলো  **5 MB** । 3 MB-এর Process-কে একটি 5 MB Partition দেওয়া হবে। 1 MB-এর Process-কে আরেকটি 5 MB Partition দেওয়া হবে। 4 MB-এর Process-কেও আরেকটি 5 MB Partition দেওয়া হবে। অর্থাৎ Process-এর প্রকৃত Size Partition-এর Size নির্ধারণ করে না;  **Partition Size fixed**  থাকে।
**Degree of Multiprogramming**
একই সময়ে Main Memory-তে যতগুলো Process থাকতে পারে, তাকে  **Degree of Multiprogramming**  বলা হয়।
Fixed-size Partitioning-এ Main Memory-তে তৈরি করা  **Partition-এর সংখ্যা**  Degree of Multiprogramming নির্ধারণ করে।
**Fixed-size Partition Scheme-এর Advantages**  ১. এটি  **সহজে implement**  করা যায়, কারণ Memory-কে fixed-size block-এ ভাগ করে Process-গুলোকে সেই block-এ বরাদ্দ করা হয়। ২. কতগুলো Memory Block খালি আছে তা সহজে  **track**  করা যায়। এর মাধ্যমে আরও কতগুলো Process Memory-তে Load করা যাবে তা জানা যায়। ৩. একই সময়ে একাধিক Process Main Memory-তে রাখা যায়, তাই এটি  **Multiprogramming**  support করে।
**Fixed-size Partition Scheme-এর Disadvantages**  ১. কোনো Process-এর Size যদি  **Partition Size-এর চেয়ে বড়**  হয়, তাহলে সেই Process-কে কোনো Partition-এ বরাদ্দ করা যায় না। ২. Memory-তে তৈরি করা  **Partition-এর সংখ্যা**  Degree of Multiprogramming নির্ধারণ করে। তাই সর্বোচ্চ সেই সংখ্যক Process একই সময়ে Main Memory-তে থাকতে পারে। ৩. কোনো Process তার allocated Partition-এর চেয়ে ছোট হলে Partition-এর অব্যবহৃত অংশ নষ্ট হয়। এর ফলে  **Internal Fragmentation**  সৃষ্টি হয়।
**Quick Revision**  Fixed-size Partitioning → Memory fixed-size continuous Partition-এ ভাগ করা হয়। একটি Partition → একটি Process ধারণ করে। অন্য নাম → Fixed Partitioning / Static Partitioning। Partition Size → Fixed। Degree of Multiprogramming → Partition-এর সংখ্যার উপর নির্ভর করে। প্রধান সমস্যা → Internal Fragmentation। বড় Process → Process Size Partition Size-এর চেয়ে বড় হলে fit করতে পারে না।

5

Contiguous Memory Allocation Techniques : Variable-size Partition Scheme


In this type of contiguous memory allocation technique,  **no fixed blocks or partitions are made in the memory.**  Instead, each Process is allotted a variable-sized block depending upon its requirements. Whenever a new Process needs memory space, the required amount is assigned from the available free memory. Therefore, the size of each block depends on the size and requirements of the Process occupying it.

In this scheme, there are no fixed-size partitions. For example, if the first Process needs 3MB of memory space, it is allotted 3MB only. Similarly, other Processes are allotted only the amount of space required by them. As a result, the allocated memory blocks have different sizes.

As the block sizes are variable and are decided as Processes arrive, this scheme is also called  **Dynamic Partitioning** .
**Advantages**

1. As Processes are allotted memory space according to their requirements, there is  **no Internal Fragmentation** . Hence, there is no memory wastage due to Internal Fragmentation.

2. The number of Processes that can be present in memory at the same time depends on how many Processes are in memory and how much space they occupy. Therefore, it can be different for different cases and is dynamic.

3. As there are no fixed-size blocks, even a large Process can be allotted the required memory space if a sufficiently large contiguous space is available.
**Disadvantages**

1. Because this approach is dynamic, a Variable-size Partition Scheme is difficult to implement.

2. It is difficult to keep track of Processes and the remaining free space in memory. Dynamic Partitioning can suffer from  **External Fragmentation** , where free memory is split into small gaps between allocated blocks.

Even when there is enough total free memory, a large new Process may not fit unless the free spaces are compacted into one sufficiently large contiguous block.

এই ধরনের  **Contiguous Memory Allocation**  technique-এ Memory-তে কোনো fixed block বা fixed partition তৈরি করা হয় না। এর পরিবর্তে, প্রতিটি Process-এর requirement অনুযায়ী তাকে variable-sized memory block দেওয়া হয়। অর্থাৎ, কোনো নতুন Process-এর memory space প্রয়োজন হলে available free memory থেকে তার প্রয়োজন অনুযায়ী memory space দেওয়া হয়। তাই প্রতিটি block-এর size নির্ভর করে সেই block-এ থাকা Process-এর size ও requirement-এর উপর।
এই scheme-এ কোনো fixed-size partition থাকে না। উদাহরণস্বরূপ, প্রথম Process-এর যদি 3MB memory space প্রয়োজন হয়, তাহলে তাকে শুধুমাত্র 3MB memory দেওয়া হবে। একইভাবে, অন্যান্য Process-কেও তাদের প্রয়োজন অনুযায়ী memory space দেওয়া হবে। ফলে allocated memory block-গুলোর size ভিন্ন ভিন্ন হয়।
Process আসার সময় তার requirement অনুযায়ী block-এর size নির্ধারিত হয় বলে এই scheme-কে  **Dynamic Partitioning** ও বলা হয়।
**Advantages**
1. Process-এর requirement অনুযায়ী memory space দেওয়া হয় বলে  **Internal Fragmentation**  হয় না। ফলে Internal Fragmentation-এর কারণে memory wastage হয় না।
2. একই সময়ে Memory-তে কতগুলো Process থাকতে পারবে তা নির্ভর করে কতগুলো Process Memory-তে আছে এবং তারা কতটুকু memory space ব্যবহার করছে তার উপর। তাই বিভিন্ন ক্ষেত্রে এই সংখ্যা ভিন্ন হতে পারে এবং এটি dynamic হয়।
3. কোনো fixed-size block না থাকায়, পর্যাপ্ত বড় contiguous memory space available থাকলে বড় আকারের Process-কেও তার প্রয়োজনীয় memory space দেওয়া যায়।
**Disadvantages**
1. এই approach dynamic হওয়ায়  **Variable-size Partition Scheme**  implement করা তুলনামূলকভাবে difficult।
2. Process এবং Memory-তে থাকা remaining free space track করা difficult। Dynamic Partitioning-এ  **External Fragmentation**  হতে পারে, যেখানে allocated block-গুলোর মাঝখানে free memory ছোট ছোট gap হিসেবে বিভক্ত হয়ে যায়।
এমনকি মোট free memory পর্যাপ্ত থাকলেও, একটি বড় নতুন Process Memory-তে fit নাও করতে পারে, যদি না free space-গুলোকে  **Compaction**  করে একটি বড় contiguous block তৈরি করা হয়।

6

Fragmentation in Memory : Internal Fragmentation & External Fragmentation


**Fragmentation**  in memory is a condition where the available memory is divided into  **small**  and  **non-contiguous**  blocks after allocating and deallocating memory to various Processes. In simpler words, fragmentation means there are some gaps in memory after running multiple Processes at different memory locations.
Fragmentation can lead to  **wastage of memory** . Even though there is enough total memory available, it may not be possible to allocate memory to a new Process due to fragmentation.
**Types of Fragmentation**
Fragmentation can be classified into two types:  **1. Internal Fragmentation**   **2. External Fragmentation**
**Internal Fragmentation**
Internal Fragmentation occurs when a Process gets more memory than it actually needs. The Operating System allocates memory in fixed-size blocks or frames. If a Process uses only a part of the allocated memory, some memory will be wasted.
In the figure, Process  **P1**  is allocated  **F1, F2, and F3**  frames of memory. But it is only using  **F1 and F2**  frames. The  **F3**  frame is wasted because the Process does not need it. Similarly, the  **F6, F7, and F9**  frames are also wasted because Processes  **P2**  and  **P3**  are holding them.
**Causes of Internal Fragmentation**
**Fixed Size Memory Allocation:**  Some Operating Systems allocate memory in fixed-size blocks or frames. If a Process requires less memory than the allocated block size, the remaining memory will be wasted. For example, consider a system that allocates memory to all Processes in blocks of 4 KB. If a Process requires 6 KB of memory, the Operating System should allocate 8 KB of memory, which means two blocks. Therefore, 2 KB of memory will be wasted.
**Management Overheads:**  Some systems reserve a part of the allocated memory for purposes such as bookkeeping and management. Sometimes this reserved memory may not be used by the Process.
**Memory Alignment:**  Some systems require memory to be aligned to certain boundaries, such as 4-byte or 8-byte boundaries. This can lead to wastage of memory and Internal Fragmentation.
**External Fragmentation**
**External Fragmentation**  refers to gaps generated in memory when multiple Processes are loaded and unloaded from memory.
To understand this, suppose Process  **P1**  is allocated three frames of memory:  **F1, F2, and F3** . Process  **P2**  is allocated one frame  **F4**  and Process  **P3**  is allocated two frames  **F5 and F6** . Now, if  **P2**  is terminated, frame  **F4**  will be free. This introduces a gap in memory between the memory allocated to  **P1**  and  **P3** .
The gaps generated in memory will add up over time as more Processes are loaded and unloaded from memory. This can lead to a situation where, even though there is enough total memory available, the system will not be able to allocate memory to a new Process because the available memory is scattered in small non-contiguous blocks.
**Causes of External Fragmentation**
**Dynamic Memory Allocation:**  Some systems use Dynamic Memory Allocation. In such systems, memory is allocated to Processes when they request it and deallocated when they are done. This can cause fragmentation as there is no fixed rule to allocate memory.
**Process Termination:**  When a Process is completed, it is terminated from memory. This will create gaps in memory if the terminated Process was allocated memory between other Processes.
**Variable Size Memory Allocation:**  Some systems allocate memory to Processes in variable sizes. This can lead to fragmentation as there is no fixed rule to allocate memory.
**How to Reduce Fragmentation?**
**Compaction:**  Compaction is a technique where the Operating System rearranges the memory contents to place all free memory together in one large block. This removes the gaps in memory and reduces fragmentation.
**Paging:**  Paging is a memory management technique that uses virtual memory to store the Process and then maps it to frames of physical memory. This can eliminate External Fragmentation as the Process can be stored in non-contiguous frames of memory.
**Segmentation:**  Segmentation divides memory into variable-sized segments based on the logical structure of a program. This can reduce fragmentation as the segments can be allocated in non-contiguous memory locations.

Memory-তে  **Fragmentation**  হলো এমন একটি condition যেখানে বিভিন্ন Process-কে memory allocate এবং deallocate করার পর available memory ছোট ছোট এবং  **non-contiguous**  block-এ বিভক্ত হয়ে যায়। সহজভাবে বলা যায়, একাধিক Process বিভিন্ন memory location-এ run করার পর Memory-তে কিছু gap তৈরি হলে তাকে Fragmentation বলা হয়।
Fragmentation-এর কারণে  **memory wastage**  হতে পারে। এমনকি মোট available memory পর্যাপ্ত থাকলেও Fragmentation-এর কারণে নতুন কোনো Process-কে memory allocate করা সম্ভব নাও হতে পারে।
**Types of Fragmentation**
Fragmentation দুই ধরনের:  **1. Internal Fragmentation**   **2. External Fragmentation**
**Internal Fragmentation**
Internal Fragmentation তখন ঘটে যখন কোনো Process তার actual requirement-এর চেয়ে বেশি memory পায়। Operating System fixed-size block বা frame-এর মাধ্যমে memory allocate করে। কোনো Process যদি allocated memory-এর শুধুমাত্র একটি অংশ ব্যবহার করে, তাহলে বাকি memory waste হয়।
Figure-এ Process  **P1** -কে  **F1, F2 এবং F3**  frame allocate করা হয়েছে। কিন্তু এটি শুধুমাত্র  **F1 এবং F2**  frame ব্যবহার করছে। Process-এর প্রয়োজন না থাকায়  **F3**  frame-টি wasted হচ্ছে। একইভাবে  **F6, F7 এবং F9**  frame-ও wasted হচ্ছে, কারণ এগুলো Process  **P2**  এবং  **P3**  ধরে রেখেছে।
**Causes of Internal Fragmentation**
**Fixed Size Memory Allocation:**  কিছু Operating System fixed-size block বা frame-এর মাধ্যমে memory allocate করে। কোনো Process-এর requirement allocated block-এর চেয়ে কম হলে remaining memory waste হয়। উদাহরণস্বরূপ, কোনো system যদি সব Process-কে 4 KB block-এ memory allocate করে এবং কোনো Process-এর 6 KB memory প্রয়োজন হয়, তাহলে Operating System-কে 8 KB memory অর্থাৎ দুটি block allocate করতে হবে। ফলে 2 KB memory waste হবে।
**Management Overheads:**  কিছু system bookkeeping এবং management-এর মতো কাজের জন্য allocated memory-এর একটি অংশ reserve করে রাখে। কখনো কখনো এই reserved memory Process ব্যবহার করে না।
**Memory Alignment:**  কিছু system-এ memory-কে নির্দিষ্ট boundary অনুযায়ী align করতে হয়, যেমন 4-byte বা 8-byte boundary। এর ফলে memory wastage এবং Internal Fragmentation হতে পারে।
**External Fragmentation**
**External Fragmentation**  হলো একাধিক Process Memory-তে load এবং unload করার সময় Memory-তে তৈরি হওয়া gap।
এটি বোঝার জন্য ধরা যাক, Process  **P1** -কে memory-এর তিনটি frame  **F1, F2 এবং F3**  allocate করা হয়েছে। Process  **P2** -কে একটি frame  **F4**  এবং Process  **P3** -কে দুটি frame  **F5 এবং F6**  allocate করা হয়েছে। এখন  **P2**  terminate করলে  **F4**  frame-টি free হয়ে যাবে। ফলে  **P1**  এবং  **P3** -এর allocated memory-এর মাঝখানে একটি gap তৈরি হবে।
সময়ের সাথে আরও Process Memory-তে load এবং unload হওয়ার কারণে এই gap-গুলো জমা হতে থাকে। এর ফলে এমন situation তৈরি হতে পারে যেখানে মোট available memory পর্যাপ্ত থাকা সত্ত্বেও নতুন Process-কে memory allocate করা সম্ভব হয় না। কারণ available memory ছোট ছোট  **non-contiguous**  block-এ ছড়িয়ে থাকে।
**Causes of External Fragmentation**
**Dynamic Memory Allocation:**  কিছু system Dynamic Memory Allocation ব্যবহার করে। এসব system-এ Process memory চাইলে memory allocate করা হয় এবং কাজ শেষ হলে memory deallocate করা হয়। এর ফলে Fragmentation হতে পারে, কারণ memory allocation-এর জন্য কোনো fixed rule থাকে না।
**Process Termination:**  কোনো Process-এর কাজ শেষ হলে সেটি Memory থেকে terminate হয়। যদি terminated Process-এর memory অন্য Process-এর মাঝখানে থাকে, তাহলে সেখানে gap তৈরি হবে।
**Variable Size Memory Allocation:**  কিছু system Process-কে variable size অনুযায়ী memory allocate করে। এর ফলে Fragmentation হতে পারে, কারণ memory allocation-এর জন্য কোনো fixed rule থাকে না।
**How to Reduce Fragmentation?**
**Compaction:**  Compaction হলো এমন একটি technique যেখানে Operating System Memory-এর contents rearrange করে সব free memory-কে একটি বড় block-এর মধ্যে একত্র করে। এর ফলে Memory-র gap দূর হয় এবং Fragmentation কমে।
**Paging:**  Paging হলো একটি memory management technique যেখানে virtual memory ব্যবহার করে Process store করা হয় এবং পরে সেটিকে physical memory-এর frames-এর সাথে map করা হয়। Process non-contiguous frame-এ রাখা যায় বলে এটি External Fragmentation eliminate করতে পারে।
**Segmentation:**  Segmentation একটি program-এর logical structure-এর ভিত্তিতে Memory-কে variable-sized segment-এ ভাগ করে। এই segment-গুলো non-contiguous memory location-এ allocate করা যায় এবং এর ফলে Fragmentation কমানো যায়।

7

Placement Algorithm in Operating System: First Fit, Next Fit, Best Fit, Worst Fit (with Example)  Fixed Size Partition Scheme


**Watch Video:**   First Fit, Next Fit, Best Fit, Worst Fit | Fixed Size Partition Placement Algorithm in Operating System determines where a Process or Data should be placed in memory. It helps to use available memory efficiently, reduce memory fragmentation, and improve system performance.
**Types of Placement Algorithms**   **First Fit:**  Allocates the first available memory block that is large enough for the Process.  **Best Fit:**  Allocates the smallest available block that can accommodate the Process.  **Worst Fit:**  Allocates the largest available memory block, leaving larger free spaces for future allocations.  **Next Fit:**  Similar to First Fit, but the search starts from the last allocated position.
**Method to Solve Placement Problems**  Understand the memory layout and block sizes → identify Process sizes → select the required Placement Algorithm → allocate Processes step by step → consider Internal or External Fragmentation → evaluate memory efficiency.

**Advantages**  Efficient memory utilization, reduced idle memory slots, support for multitasking, improved system throughput, and adaptability to different memory demands.
**Disadvantages**  May cause External or Internal Fragmentation, can require memory compaction, and some algorithms may be computationally expensive or complex.

Placement Algorithm in Operating System নির্ধারণ করে কোনো Process বা Data-কে Memory-এর কোথায় রাখা হবে। এটি available memory-এর কার্যকর ব্যবহার, Memory Fragmentation কমানো এবং system performance উন্নত করতে সাহায্য করে।
**Placement Algorithm-এর ধরন**   **First Fit:**  Process-এর জন্য যথেষ্ট বড় প্রথম available memory block-এ Process-কে allocate করে।  **Best Fit:**  Process-এর জন্য যথেষ্ট এমন সবচেয়ে ছোট available block-এ Process-কে allocate করে।  **Worst Fit:**  সবচেয়ে বড় available memory block-এ Process-কে allocate করে, যাতে ভবিষ্যতের জন্য বড় free space থাকে।  **Next Fit:**  First Fit-এর মতো, তবে search শুরু হয় সর্বশেষ allocation position থেকে।
**Placement Problem সমাধানের পদ্ধতি**  Memory layout ও block size বুঝতে হবে → Process-এর size নির্ধারণ করতে হবে → উপযুক্ত Placement Algorithm নির্বাচন করতে হবে → step by step allocation করতে হবে → Internal বা External Fragmentation বিবেচনা করতে হবে → Memory efficiency মূল্যায়ন করতে হবে।
**Advantages**  Efficient memory utilization, idle memory slots কমানো, multitasking support, system throughput উন্নত করা এবং বিভিন্ন memory demand অনুযায়ী কাজ করতে পারে।
**Disadvantages**  External বা Internal Fragmentation হতে পারে, memory compaction প্রয়োজন হতে পারে এবং কিছু Algorithm computationally expensive বা complex হতে পারে।

8

Placement Algorithm in Operating System: First Fit, Next Fit, Best Fit, Worst Fit (with Example) Variable-size Partition Scheme


**Watch Video:**   First Fit, Next Fit, Best Fit, Worst Fit | Variable Size Partition|



**Previous Job Question:**  Memory Management



Topic Wise Question Bank

All Topics

- ☆

1

Microprocessor & Computer Architecture
Memory Management

A system has a very fast CPU but slow main memory, explain how memory hierarchy helps reduce the performance gap between CPU and memory.

Combined Bank, AE(IT)/AME, 26
| AME/ANE/AE

**Memory Hierarchy :**

Memory hierarchy is an arrangement of different types of memory (Cache, RAM, Secondary Storage) based on  **speed, cost, and size** .
Faster memory is placed closer to CPU and slower memory is placed farther away.

**How It Reduces CPU–Memory Gap:**

**Use of Cache Memory:**  Frequently used data is stored in  **Cache**  (very fast) → CPU accesses data quickly.
**Temporal Locality:**  Recently used data is likely to be used again → kept in cache.
**Spatial Locality:**  Nearby data is also loaded → reduces repeated memory access.
**Reduced Access Time:**  CPU mostly accesses cache instead of slow main memory.
**Layered Access:**  If data not in cache → check RAM → then secondary storage.
**Improved Performance:**  Overall system speed increases by minimizing slow memory access.

**Memory Hierarchy :**

Memory hierarchy হলো বিভিন্ন ধরনের memory (Cache, RAM, Secondary Storage)-এর একটি বিন্যাস, যা  **speed, cost এবং size**  অনুযায়ী সাজানো হয়।
দ্রুত memory CPU-এর কাছে থাকে এবং ধীর memory দূরে থাকে।

**কিভাবে CPU–Memory gap কমায়:**

**Cache Memory ব্যবহার:**  বেশি ব্যবহৃত data  **Cache** -এ রাখা হয় → CPU দ্রুত access করতে পারে।
**Temporal Locality:**  সম্প্রতি ব্যবহৃত data আবার ব্যবহার হওয়ার সম্ভাবনা বেশি → cache-এ রাখা হয়।
**Spatial Locality:**  কাছাকাছি data একসাথে load হয় → বারবার memory access কমে।
**Access Time কমে:**  CPU বেশি সময় cache ব্যবহার করে → slow RAM কম ব্যবহার হয়।
**Layer অনুযায়ী access:**  Cache → RAM → Secondary Storage এইভাবে খোঁজা হয়।
**Performance বৃদ্ধি:**  slow memory access কমিয়ে overall system দ্রুত হয়।

☆

2

Operating System
Memory Management

What is Swapping from virtual memory in the primary memory.

CB, AE(IT)/AHME/SO, 21
| AME/ANE/AE

**Swapping in Operating System**
**Swapping**  is a memory management technique used by an operating system to efficiently manage the limited  **primary memory (RAM)**  and the larger but slower  **secondary memory**  such as a hard disk or SSD.
**What is Swapping?**
Swapping is the process of moving entire processes between  **primary memory (RAM)**  and  **secondary memory** . When the RAM becomes full and the system needs memory to run active programs, the operating system moves some inactive or low-priority processes from RAM to secondary memory. This process is called  **swapping out** .
Later, when the swapped-out process is required again, the operating system brings the process back into RAM from secondary memory. This process is called  **swapping in** .
Through this back-and-forth movement of processes between RAM and secondary memory, the operating system can run more processes than the physical memory can normally support.

**Operating System-এ Swapping**
**Swapping**  হলো একটি memory management technique যা operating system ব্যবহার করে সীমিত  **primary memory (RAM)**  এবং তুলনামূলক বড় কিন্তু ধীর  **secondary memory**  (hard disk বা SSD) দক্ষভাবে পরিচালনা করতে।
**Swapping কী?**
Swapping হলো এমন একটি প্রক্রিয়া যেখানে সম্পূর্ণ process-কে  **primary memory (RAM)**  এবং  **secondary memory** -এর মধ্যে স্থানান্তর করা হয়। যখন RAM পূর্ণ হয়ে যায় এবং নতুন program চালানোর জন্য memory প্রয়োজন হয়, তখন operating system কিছু inactive বা কম গুরুত্বপূর্ণ process-কে RAM থেকে secondary memory-তে সরিয়ে দেয়। এই প্রক্রিয়াকে  **swapping out**  বলা হয়।
পরে যখন সেই process আবার প্রয়োজন হয়, তখন operating system সেটিকে secondary memory থেকে আবার RAM-এ নিয়ে আসে। এই প্রক্রিয়াকে  **swapping in**  বলা হয়।
এইভাবে RAM এবং secondary memory-এর মধ্যে process আদান-প্রদানের মাধ্যমে operating system একসাথে অনেকগুলো process পরিচালনা করতে পারে।



☆

3

Operating System
Memory Management

In the given example, let us assume the jobs and the memory requirements as the following: Job1 = 90k, Job2 = 20k, Job350k, Job4=200k. Let the free pace memory allocation blocks be: Block1= 50k, Block2= 100k, Block3=90k, Block4=200k, Block5 50k. Now show Best Fit Method and first fit method memory allocation. [Similar Question but value cannot exactly remember.]

Janata, ASA, 21
| AME/ANE/AE

**Given:** Jobs: J1 = 90K, J2 = 20K, J3 = 50K, J4 = 200K
Blocks: B1 = 50K, B2 = 100K, B3 = 90K, B4 = 200K, B5 = 50K
**1) First Fit Method**
In First Fit, each job is placed in the  **first block**  that is large enough.
**Step by step:**
J1 = 90K → first block that fits is B2 = 100K
Remaining in B2 = 10K
J2 = 20K → first block that fits is B1 = 50K
Remaining in B1 = 30K
J3 = 50K → first block that fits is B3 = 90K
Remaining in B3 = 40K
J4 = 200K → first block that fits is B4 = 200K
Remaining in B4 = 0K
**First Fit Allocation Table:**

Job
Size
Allocated Block
Block Size
Unused Space

J1
90K
B2
100K
10K

J2
20K
B1
50K
30K

J3
50K
B3
90K
40K

J4
200K
B4
200K
0K

**2) Best Fit Method**
In Best Fit, each job is placed in the  **smallest block**  that can hold it.
**Step by step:**
J1 = 90K → best block is B3 = 90K
Remaining in B3 = 0K
J2 = 20K → best block is B1 = 50K
Remaining in B1 = 30K
J3 = 50K → best block is B5 = 50K
Remaining in B5 = 0K
J4 = 200K → best block is B4 = 200K
Remaining in B4 = 0K
**Best Fit Allocation Table:**

Job
Size
Allocated Block
Block Size
Unused Space

J1
90K
B3
90K
0K

J2
20K
B1
50K
30K

J3
50K
B5
50K
0K

J4
200K
B4
200K
0K

**Final Answer:**
First Fit allocation:
J1 → B2, J2 → B1, J3 → B3, J4 → B4
Best Fit allocation:
J1 → B3, J2 → B1, J3 → B5, J4 → B4
