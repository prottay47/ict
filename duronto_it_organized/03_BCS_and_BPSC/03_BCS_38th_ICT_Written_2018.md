# 38th BCS (ICT) Written Exam - 2018

| Field | Details |
| :--- | :--- |
| **Organization** | BPSC |
| **Post Name** | BCS (ICT Cadre / Lecturer) |
| **Exam Date** | 2018 |
| **Exam Taker** | BPSC |
| **Marks / Format** | 200 Marks (3 Hours) |
| **Source** | Duronto IT Academy / Smart IT Job Solution |

---

**Bangladesh Civil Service – 38**<sup>**th**</sup> **(ICT) Date : 2018  Time :  3 Hours. Full marks : 200** 

###### **4.(a)Consider the following algebraic equation : Y = AB’CD’ +ABC’+A’BD+AB’CD. Draw** **the truth table that satisfies the above-mentioned equation .** 

|**ABCD**|**Y**|

|---|---|

|**0000**|**0**|

|**0001**|**0**|

|**0010**|**0**|

|**0011**|**0**|

|**0100**|**0**|

|**0101**|**1**|

|**0110**|**0**|

|**0111**|**1**|

|**1000**|**0**|

|**1001**|**0**|

|**1010**|**1**|

|**1011**|**1**|

|**1100**|**1**|

|**1101**|**1**|

|**1110**|**0**|

|**1111**|**0**|

**(b) Simplify the equation using K-map .** 

||**CD(00)**|**01**|**11**|**10**|

|---|---|---|---|---|

|**AB(00)**|0|1|3|2|

|**01**|4|**5**|**7**|6|

|**11**|**12**|**13**|15|14|

|**10**|8|9|**11**|**10**|

Y = ABC’ + A’BD+AB’C 

**(c) Draw the circuit diagram for the simplified equation by using basic gates. Calculate the number of basic gates required for implementing the simplified circuit .** 

**Page 1** 

###### **(d)Draw the circuit for simplified equation by using only NOR gate .** 

**5. (a) Determine the nyquist sampling rate and the nyquist sampling interval for the signal X(t) = sin(2100pit)** 

Signal Frequency fm = 2100Pi/2Pi =  1050Hz Nyquist Sampling Rate = 2fm = 2100Hz Nyquist sampling interval Ts = 1/fs = 0.476 ms. 

**(b) What is modulation ? Describe the pulse code modulation technique.State the advantage and disadvantage of PCM .** 

Modulation is the process of converting data into radio waves by adding information to an electronic or optical carrier signal. A carrier signal is one with a steady waveform -- constant height, or amplitude, and frequency **.** 

In Pulse Code Modulation, the message signal is represented by a sequence of coded pulses. This message signal is achieved by representing the signal in discrete form in both time and amplitude. 

**Basic Elements of PCM** 

**Page 2** 

The transmitter section of a Pulse Code Modulator circuit consists of Sampling, Quantizing and Encoding, which are performed in the analog-to-digital converter section. The low pass filter prior to sampling prevents aliasing of the message signal. 

The basic operations in the receiver section are regeneration of impaired signals, decoding, and reconstruction of the quantized pulse train. Following is the block diagram of PCM which represents the basic elements of both the transmitter and the receiver sections. 

###### **Low Pass Filter** 

This filter eliminates the high frequency components present in the input analog signal which is greater than the highest frequency of the message signal, to avoid aliasing of the message signal. 

###### **Sampler** 

This is the technique which helps to collect the sample data at instantaneous values of message signal, so as to reconstruct the original signal. The sampling rate must be greater than twice the highest frequency component W of the message signal, in accordance with the sampling theorem. 

###### **Quantizer** 

Quantizing is a process of reducing the excessive bits and confining the data. The sampled output when given to Quantizer, reduces the redundant bits and compresses the value. 

###### **Encoder** 

The digitization of analog signal is done by the encoder. It designates each quantized level by a binary code. The sampling done here is the sample-and-hold process. These three 

**Page 3** 

sections LPF,Sampler,andQuantizer LPF,Sampler,andQuantizer will act as an analog to digital converter. Encoding minimizes the bandwidth used. 

###### **Regenerative Repeater** 

This section increases the signal strength. The output of the channel also has one regenerative repeater circuit, to compensate the signal loss and reconstruct the signal, and also to increase its strength. 

###### **Decoder** 

The decoder circuit decodes the pulse coded waveform to reproduce the original signal. This circuit acts as the demodulator. 

###### **Reconstruction Filter** 

After the digital-to-analog conversion is done by the regenerative circuit and the decoder, a lowpass filter is employed, called as the reconstruction filter to get back the original signal. 

Hence, the Pulse Code Modulator circuit digitizes the given analog signal, codes it and samples it, and then transmits it in an analog form. This whole process is repeated in a reverse pattern to obtain the original signal. 

**There are some important advantages of PCM(pulse code modulation) which are given below,** The PCM (pulse code modulation) convenient for long distance communication. It has a higher transmitter efficiency. 

It has a higher noise immunity. 

**There are some disadvantages of PCM (pulse code modulation) which are given below,** The PCM (pulse code modulation) requires large bandwidth as compared to analog system. Encoding, decoding and quantizing circuit of PCM is very complex. 

###### **6.(a) What is the block diagram of digital computer .describe each unit briefly.** 

**Computer Block Diagram System** : Mainly computer system consists of three parts, that are central processing unit (CPU), Input Devices, and Output Devices. The Central Processing Unit (CPU) is divided into two parts again: arithmetic logic unit (ALU) and the control unit (CU). The set of instruction is in the form of raw data. 

A large amount of data is stored in the computer memory with the help of primary and secondary storage devices. The CPU is like the heart/brain of the computer. The user does not get the desired output, without the necessary option taken by the CPU.  The Central processing unit (CPU) is responsible for the processing of all the instructions which are given by the user to the computer system. 

**Page 4** 

Fig: Block Diagram of the computer. 

The data is entered through input devices such as the keyboard, mouse, etc. This set of instruction is processed by the CPU after getting the input by the user, and then the computer system produces the output. The computer can show the output with the help of output devices to the user, such as  monitor, printer, etc. 

- CPU (Central Processing Unit) 

- Storage Unit 

- ALU(Arithmetic Logic Unit) 

- Control Unit 

###### **Central Processing Unit (CPU)** 

The computer system is nothing without the Central processing Unit so, it is also known as the brain or heat of computer. The CPU is an electronic hardware device which can perform different types of operations such as arithmetic and logical operation. 

**Page 5** 

The CPU contains two parts: the arithmetic logic unit and control unit. We have discussed briefly the arithmetic unit, logical unit, and control unit which are given below: 

###### **Control Unit** 

The control unit (CU) controls all the activities or operations which are performed inside the computer system. It receives instructions or information directly from the main memory of the computer. 

When the control unit receives an instruction set or information, it converts the instruction set to control signals then; these signals are sent to the central processor for further processing. The control unit understands which operation to execute, accurately, and in which order. 

###### **Arithmetic and Logical Unit** 

The arithmetic and logical unit is the combinational digital electronic circuit that can perform arithmetic operations on integer binary numbers.It presents the arithmetic and logical operation. The outputs of ALU will change asynchronously in response to the input. The basic arithmetic and bitwise logic functions are supported by ALU. 

###### **Storage Unit** 

The information or set of guidelines are stored in the storage unit of the computer system. The storage unit provides the space to store the data or instruction of processed data. The information or data is saved or hold in computer memory or storage device. The data storage is the core function and fundamental of the computer components. 

###### **(b) What is pipelining? How does pipeline implementation make faster instruction execution? Solution :** 

Pipelining is a technique used to improve the execution throughput of a CPU by using the processor resources in a more efficient manner. 

The basic idea is to split the processor instructions into a series of small independent stages. Each stage is designed to perform a certain part of the instruction. At a very basic level, these stages can be broken down into: 

- **Fetch Unit** Fetch an instruction from memory 

- **Decode Unit** Decode the instruction be executed 

- **Execute Unit** Execute the instruction 

- **Write Unit** Write the result back to register or memory 

**Page 6** 

There will be a dedicated CPU module for each of the stages mentioned above. 

On a non-pipelined CPU, when a instruction is being processed at a particular stage, the other stages are at an idle state – which is very inefficient. If you look at the diagram, when the 1st instruction is being decoded, the Fetch, Execute and Write Units of the CPU are not being used and it takes 8 clock cycles to execute the 2 instructions. 

On the other hand, on a pipelined CPU, all the stages work in parallel. When the 1st instruction is being decoded by the Decoder Unit, the 2nd instruction is being fetched by the Fetch Unit. It only takes 5 clock cycles to execute 2 instructions on a pipelined CPU. 

Note that increasing the number of stages in the pipeline will not always result in an increase of the execution throughput. On a non-pipelined CPU, an instruction could only take 3 cycles, but on a pipelined CPU it could take 4 cycles because of the different stages involved. Therefore, a single instruction might require more clock cycles to execute on a pipelined CPU. But the time taken to complete the execution of multiple instructions gets faster in pipelined CPUs. So there needs to a balance in between. 

One of the major complications with deep pipelining (eg, 31-stage pipelining used in some of the Intel Pentium 4 processors) is when a conditional branch instruction is being executed – due to the fact that the processor will not be able to determine the location of the next instruction, therefore it has to wait for the branch instruction to finish and the whole pipeline may need to be flushed as a result. If a program has many conditional branch instructions, pipelining could have a negative effect on the overall perfomance. To alleviate this problem, branch prediction can be used, but this too can have a negative effect if the branches are predicted wrongly. 

Due to the different ways AMD and Intel implement pipelining in their CPUs, comparing their CPUs purely based on the clock speed is never accurate. (c) How does an interrupt can be enabled ? 

###### **6(c )What are the steps that occur when an interrupt is processed . Solution:** 

An interrupt is like a **shopkeeper** . If one needs a service or product, he goes to him and apprises him of his needs. In case of interrupts, wh 

The sequence of steps that occurs during interrupt processing are: 

**Page 7** 

- The contents of flag register the CS and IP are pushed on to the stack. 

- To disable single steps and INTR interupts the TF and IF are cleared. 

- The program then jumps to the beginning or starting adsress of ISS. 

- When the IRET executes last line that are also ISS last line the CS and IP flag contents are popped from stack and placed in appropriate registers. 

- Once the flags are restored then Tf and IF values are also restored to their previos values. 

- Then it continues the process which was doing before interrupt 

   - **7.A host IP address in a network is written as both 192.68.25.16/28 and 3FFE:85B:IFIF::A9:1234.** 

(a) **Which one is IPV4 address ? How many bits are used for IPV6 address ? How does the above IPV6 address completely with the addressing scheme . Solution:** 

192.68.25.16/28 is ipv4 address and 3FFE:85B:IFIF::A9:1234 is ipv6 address .128 bits are used in ipv6 address . 

**Solution :** The IPv4 address is a 32-bit number that uniquely identifies a network interface on a machine. An IPv4 address is typically written in decimal digits, formatted as four 8-bit fields that are separated by periods..128 bits 

**(b) How many subnets and hosts are to be supported by the above mentioned IPV4  address ?** (c) Classify IPV4 address and IPV6 address . 

Class A Address 

The first bit of the first octet is always set to 0 (zero). Thus the first octet ranges from 1 – 127, i.e. 

Class A addresses only include IP starting from 1.x.x.x to 126.x.x.x only. The IP range 127.x.x.x is reserved for loopback IP addresses. 

The default subnet mask for Class A IP address is 255.0.0.0 which implies that Class A addressing can have 126 networks (2<sup>7</sup> -2) and 16777214 hosts (2<sup>24</sup> -2). 

Class A IP address format is thus: **0NNNNNNN** .HHHHHHHH.HHHHHHHH.HHHHHHHH 

Class B Address 

An IP address which belongs to class B has the first two bits in the first octet set to 10, i.e. 

**Page 8** 

Class B IP Addresses range from 128.0.x.x to 191.255.x.x. The default subnet mask for Class B is 255.255.x.x. 

Class B has 16384 (2<sup>14</sup> ) Network addresses and 65534 (2<sup>16</sup> -2) Host addresses. 

Class B IP address format is: **10NNNNNN.NNNNNNNN** .HHHHHHHH.HHHHHHHH 

Class C Address 

The first octet of Class C IP address has its first 3 bits set to 110, that is − 

Class C IP addresses range from 192.0.0.x to 223.255.255.x. The default subnet mask for Class C is 255.255.255.x. 

Class C gives 2097152 (2<sup>21</sup> ) Network addresses and 254 (2<sup>8</sup> -2) Host addresses. 

Class C IP address format is: **110NNNNN.NNNNNNNN.NNNNNNNN** .HHHHHHHH 

Class D Address 

Very first four bits of the first octet in Class D IP addresses are set to 1110, giving a range of − 

Class D has IP address range from 224.0.0.0 to 239.255.255.255. Class D is reserved for Multicasting. In multicasting data is not destined for a particular host, that is why there is no need to extract host address from the IP address, and Class D does not have any subnet mask. 

Class E Address 

This IP Class is reserved for experimental purposes only for R&D or Study. IP addresses in this class ranges from 240.0.0.0 to 255.255.255.254. Like Class D, this class too is not equipped with any subnet mask. 

- **Unicast** 

A unicast address specifies an identifier for a single interface to which packets are delivered. Under IPv6, the vast majority of Internet traffic is foreseen to be unicast, and it is for this reason that the largest assigned block of the IPv6 address space is dedicated to unicast addressing. Unicast addresses include all addresses other than loopback, multicast, link-local-unicast, and unspecified. 

**Page 9** 

For SRX Series devices, the flow module supports the following kinds of IPv6 unicast packets: 

- Pass-through unicast traffic, including traffic from and to virtual routers. The device transmits pass-through traffic according to its routing table. 

- Host-inbound traffic from and to devices directly connected to SRX Series interfaces. For example, host-inbound traffic includes logging, routing protocol, and management types of traffic. The flow module sends these unicast packets to the Routing Engine and receives them from it. Traffic is processed by the Routing Engine instead of by the flow module, based on routing protocols defined for the Routing Engine. 

The flow module supports all routing and management protocols that run on the Routing Engine. Some examples are OSPFv3, RIPng, TELNET, and SSH. 

- **Multicast** 

A multicast address specifies an identifier for a set of interfaces that typically belong to different nodes. It is identified by a value of 0xFF. IPv6 multicast addresses are distinguished from unicast addresses by the value of the high-order octet of the addresses. The devices support only host-inbound and host-outbound multicast traffic. Host inbound traffic includes logging, routing protocols, management traffic, and so on. 

- **Anycast** An anycast address specifies an identifier for a set of interfaces that typically belong to different nodes. A packet with an anycast address is delivered to the nearest node, according to routing protocol rules. 

There is no difference between anycast addresses and unicast addresses except for the subnet-router address. For an anycast subnet-router address, the low order bits, typically 64 or more, are zero. Anycast addresses are taken from the unicast address space. The flow module treats anycast packets in the same way as it handles unicast packets. If an anycast packet is intended for the device, it is treated as host-inbound traffic, and it delivers it to the protocol stack which continues processing it. 

###### **8.(a)What is structured programming ? with example .** 

**Structured programming is a program written with only the structured programming constructions: (1) sequence, (2) repetition, and (3) selection.** 

1. **Sequence.** Lines or blocks of code are written and executed in sequential order. 

Example: 

**x = 5 y = 11 z = x + y WriteLine(z)** 

2. **Repetition.** Repeat a block of code (Action) while a condition is true. There is no limit to the number of times that the block can be executed. 

**Page 10** 

**While condition action End While** Example: **x = 2 While x < 100 WriteLine(x) x = x * x End** 

3. **Selection.** Execute a block of code (Action) if a condition is true. The block of code is executed at most once. 

**If condition Then action End If** 

Example:` 

**x = ReadLine() If x Mod 2 = 0 WriteLine("The number is even.")** 

(b)Write a C program to store information using structures with dynamically memory allocation? Solution: 

#include <stdio.h> #include <stdlib.h> struct course { int marks; char subject[30]; }; 

int main() { struct course *ptr; int i, noOfRecords; printf("Enter the number of records: "); scanf("%d", &noOfRecords); 

// Memory allocation for noOfRecords structures ptr = (struct course *)malloc(noOfRecords * sizeof(struct course)); for (i = 0; i < noOfRecords; ++i) { 

printf("Enter the name of the subject and marks respectively:\n"); 

**Page 11** 

scanf("%s %d", (ptr + i)->subject, &(ptr + i)->marks); } 

printf("Displaying Information:\n"); for (i = 0; i < noOfRecords; ++i) printf("%s\t%d\n", (ptr + i)->subject, (ptr + i)->marks); 

return 0; } 

**(c)State the advantages of object oriented programming (OOP) over structured programming. Solution :** Advantages of Object-Oriented Programming 

Modularity for easier troubleshooting. Something has gone wrong, and you have no idea where to look. ... 

Reuse of code through inheritance. ... Flexibility through polymorphism. ... 

Effective problem solving. 

###### **(d)Explain encapsulation and inheritance in details .** 

**Encapsulation** is one of the four fundamental OOP concepts. The other three are inheritance, polymorphism, and abstraction. 

Encapsulation in Java is a mechanism of wrapping the data (variables) and code acting on the data (methods) together as a single unit. In encapsulation, the variables of a class will be hidden from other classes, and can be accessed only through the methods of their current class. Therefore, it is also known as **data hiding** . 

Inheritance can be defined as the process where one class acquires the properties (methods and fields) of another. With the use of inheritance the information is made manageable in a hierarchical order. 

The class which inherits the properties of other is known as subclass (derived class, child class) and the class whose properties are inherited is known as superclass (base class, parent class). 

**9.(a) A list of numbers 3,5,7,11,13,17 is stored in sequence. Which of the following data structure will have the least data movement when the number 11 is removed from the list ? FIFO,QUEUE,HEAP ,Linked list and stack, justify your answer .** 

**10.Suppose a circular array QUEUE has 6 memory locations.what are the values of front and REAR after the following operation ? (i) Initially QUEUE  is empty .** 

**Page 12** 

###### **(ii) A, C and D are added to the queue ; (iii) F is inserted.** 

###### **(iv) Two letters are deleted; (v) K, L and M are added to the queue; (vi) Two letters are deleted and (vii) R is added to the queue.** 

|**Solution:**<br>Initially front<br>A<br><br>|and rear=0<br>C<br>|D<br>|||

|---|---|---|---|---|

|A<br><br>|C<br><br>|D<br><br>|F<br>||

|A<br>|C<br>|||<br>|

|A<br>|C<br>|K<br>|L<br>|M<br>|

|A<br><br>|C<br><br><br>|K<br><br><br>|||

|A<br>|C|K|R||

###### **(b) What is operating system? Why do we need operating system?** 

An **operating system** is the most important software that runs on a computer. It manages the computer's memory and processes, as well as all of its software and hardware. It also allows **you** to communicate with the computer without knowing how to speak the computer's language. 

a modern OS provides a litany of services that makes it far preferable for app developers to target an OS instead of handling its own bootstrapping, along with all the other crap that goes along with supporting J. Random Hardware Configuration. Sure, some graphics drivers require a bit of tweaking for certain games, but it’s still better than the alternative. You think nVidia’s gonna provide specs for their hardware so random app developers can program their graphics cards down to the hardware? Nope. Not gonna happen. A modern computer really only works anywhere near its potential if you abstract away the necessity to understand every piece of hardware so that there can be a common base, with common services and access models, and developers don’t need to reinvent the wheel every time they write a new piece of software. 

**(c) What is deadlock? Describe the way of detecting and protecting deadlock.** Solution : 

A **deadlock** occurs when a process or thread enters a waiting state because a requested system resource is held by another waiting process, which in turn is waiting for another resource held by another waiting process. 

In the previous post, we have discussed Deadlock Prevention and Avoidance. In this post, Deadlock Detection and Recovery technique to handle deadlock is discussed. **Deadlock Detection** 

**Page 13** 

1. If resources have single instance: 

In this case for Deadlock detection we can run an algorithm to check for cycle in the Resource Allocation Graph. Presence of cycle in the graph is the sufficient condition for deadlock. 

In the above diagram, resource 1 and resource 2 have single instances. There is a cycle R1 → P1 → R2 → P2. So, Deadlock is Confirmed. 

2. If there are multiple instances of resources: Detection of the cycle is necessary but not sufficient condition for deadlock detection, in this case, the system may or may not be in deadlock varies according to different situations. 

**Deadlock Recovery** 

A traditional operating system such as Windows doesn’t deal with deadlock recovery as it is time and space consuming process. Real-time operating systems use Deadlock recovery. **Recovery method** 

1. **Killing the process:** killing all the process involved in the deadlock. Killing process one by one. After killing each process check for deadlock again keep repeating the process till system recover from deadlock. 

2. **Resource Preemption:** Resources are preempted from the processes involved in the deadlock, preempted resources are allocated to other processes so that there is a possibility of recovering the system from deadlock. In this case, the system goes into starvation. 

**11.A full joint probability distribution for the Toothache, Cavity and catch world is given below.** 

**Page 14** 

**Page 15** 

###### **13.(a) Describe different techniques use the risk analysis of software development explanation.** 

- Discuss security issues surrounding the software (substeps include arguing about how the product works and determining areas of disagreement; identifying possible vulnerabilities, sometimes by using tools or lists of common vulnerabilities; mapping out exploits and discussing possible fixes; and gaining an understanding of current and planned security controls). 

- Determine the probability of compromise (substeps include mapping out attack scenarios for vulnerability exploitation and balancing controls against threat capacity to determine likelihood). 

- Perform impact analysis (substeps include determining the impact on asset and business goals and considering the impact on security). 

- Rank risks. 

- Develop a mitigation strategy (a substep is recommending countermeasures to mitigate risks). 

- Report findings (substeps include carefully describing major and minor risks while paying close attention to impact, and providing basic information about where to spend limited mitigation resources) 

###### **(b)  Why are the following two overloaded functions inherently ambiguous? int f(int a,int b= 5) int f(int &a)** 

two functions cannot be overloaded when the only difference is that one takes a reference parameter and the other takes a normal, call-by-value parameter. 

**(c) What is database security? Describe different approaches to ensure database security.** Solution: 

Database security encompasses a range of security controls designed to protect the Database Management System (DBMS). The types of database security measures your business should use include protecting the underlying infrastructure that houses the database such as the network and servers), securely configuring the DBMS, and the access to the data itself. 

Database security refers to the collective measures used to protect and secure a database or database management software from illegitimate use and malicious threats and attacks. 

**Page 16** 

It is a broad term that includes a multitude of processes, tools and methodologies that ensure security within a database environment. 

###### **Database security controls** 

Database security encompasses multiple controls, including system hardening, access, DBMS configuration, and security monitoring. These different security controls help to manage the circumventing of security protocols. 

###### **System hardening and monitoring** 

The underlying architecture provides additional access to the DBMS. It is vital that all systems are patched consistently, hardened using known security configuration standards, and monitored for access, including insider threats. 

###### **DBMS configuration** 

It is critical that the DBMS be properly configured and hardened to take advantage of security features and limit privileged access that may cause a misconfiguration of expected security settings. Monitoring the DBMS configuration and ensuring proper change control processes helps ensure that the configuration stays consistent. 

###### **Authentication** 

Database security measures include authentication, the process of verifying if a user’s credentials match those stored in your database, and permitting only authenticated users access to your data, networks, and database platform. 

###### **Access** 

A primary outcome of database security is the effective limitation of access to your data. Access controls authenticate legitimate users and applications, limiting what they can access in your database. Access includes designing and granting appropriate user attributes and roles and limiting administrative privileges. 

###### **Database auditing** 

Monitoring (or auditing) actions as part of a database security protocol delivers centralized oversight of your database. Auditing helps to detect, deter, and reduce the overall impact of unauthorized access to your DBMS. 

###### **Backups** 

**Page 17** 

A data backup, as part of your database security protocol, makes a copy of your data and stores it on a separate system. This backup allows you to recover lost data that may result from hardware failures, data corruption, theft, hacking, or natural disasters. 

###### **Encryption** 

Database security can include the secure management of encryption keys, protection of the encryption system, management of a secure, off-site encryption backup, and access restriction protocols. 

###### **Application security** 

Database and application security framework measures can help protect against common known attacker exploits that can circumvent access controls, including SQL injection. 

**Page 18** 

- `৩৬ তম বিবিএি হতত ৩৮ তম বিবিএি পরীক্ষার বিবিএি িাধারণ (বিক্ষা) ক্যাডাতরর িরক্াবর ক্তেতের প্রভাষক্ আইবিবি(ক্বিউিার িাতেন্স অথিা িমমাতের িািতেক্ট) এর প্রশ্নঃ` 

**Data Structure and Algorithm Analysis** 

1. A list of numbers 3,5,7,11,13,17 is stored in sequence. Which of the following data structure will have the least data movement when the number 11 is removed from the list 

   - ? FIFO,QUEUE,HEAP ,Linked list and stack, justify your answer . **[BCS – 38**<sup>**th**</sup> **(ICT)]** 

2. Suppose a circular array QUEUE has 6 memory locations. What are the values of front and REAR after the following operation ? **[BCS – 38**<sup>**th**</sup> **(ICT)]** 

      - a. Initially QUEUE  is empty . 

      - b. A, C and D are added to the queue ; 

      - c. F is inserted. 

      - d. Two letters are deleted; 

      - e. K, L and M are added to the queue; 

      - f. Two letters are deleted and 

      - g. R is added to the queue. 

3. How does dynamic memory allocation help in managing data . **[BCS – 37**<sup>**th**</sup> **(ICT)]** 

4. What is linear data structure ? Why we use stack ? Difference between array and linked list ?What is merge sort and how it works ? **[BCS – 37**<sup>**th**</sup> **(ICT)]** 

5. Write a Sorting Algorithm to sort “n” number always in O(nlogn) time. **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

6. What are the main functionality of “prority Queue”? How to implement these functions by using heap ? **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

7. Describe “Huffman’s” Algorithm. **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

8. What are the differences between Graph & Tree ? What is Hamiltonian Graph ? **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

9. What is Big-O ,Big-Omega ,Big theta ? **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

10. Explain NP-hard and NP complete with example. **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

11. What is minimum spanning tree ? **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

12. Write down about Divide and conquer algorithm. What are the differences between divide and conquer and dynamic programming. **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

13. Explain how to Bellman Ford Algorithm can identify a negative  cycle of a graph. **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

14. Make a binary search tree using following numbers :28/25/30/15/100/105 **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

###### **Computer Architecture** 

Govt CSE or IT JOB : OUR GOAL™ [Largest IT Job group of Bangladesh ] ☑ ️ 

1. What is the block diagram of digital computer. Describe each unit briefly. **[BCS – 38**<sup>**th**</sup> **(ICT)]** 

2. What are the differences between CISC and RISC architecture ? **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

3. How can a optical mouse work ? **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

4. How does protected memory Management work ? **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

5. Explain Swapping & Memory protection system. **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

6. (b) What is pipelining? How does pipeline implementation make faster instruction execution? 

7. (c) How does an interrupt can be enabled ? 

###### **Database :** 

1. What is database security? Describe different approaches to ensure database security. **[BCS – 38**<sup>**th**</sup> **(ICT)]** 

2. Explain primary key and Foreign key. **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

3. What are the DDL and DML? **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

4. What is database normalization? Why 1NF,2NF,3NF and BCNF. **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

5. How hash indexing & B+ Tree indexing? **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

6. What is SQL? Write down two example of SQL. **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

###### **Digital Logic Design** 

1. Consider the following algebraic equation : Y = AB’CD’ +ABC’+A’BD+AB’CD **[BCS – 38**<sup>**th**</sup> **(ICT)]** 

   - a. Draw the truth table that satisfies the above-mentioned equation 

   - b. Simplify the equation using k-map 

   - c. Draw the circuit diagram for the simplified equation by using basic gates. Calculate the number of basic gates required for implementing the simplified circuit. 

   - d. Draw the circuit for simplified equation by using only NOR gate 

2. How to convert a J-K Flip Flop to a T Flip Flop ? **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

3. Design a 4 bit binary adder using 1-Bit full adder circuit. **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

###### **Discrete Math** 

1. Write down the differences between propositional logic and Predicative logic? **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

2. Explain the functionality of a push down automata. **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

3. How many permutations are possible from 26 Alphabet letters but they don’t have match with car, dog and byte? **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

Govt CSE or IT JOB : OUR GOAL™ [Largest IT Job group of Bangladesh ] ☑ ️ 

###### **Microprocessor:** 

1. Describe the architecture of Intel 8086 Micrprocessor. **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

###### **Machine Learning:** 

1. Explain Naïve Bayesian Model with example. **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

**2.** Describe the procedure of Genetic Algorithm. **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

###### **Networking:** 

1. Host IP address in a network is written as both 192.68.25.16/28 and 

   - 3FFE:85B:IFIF::A9:1234. **[BCS – 38**<sup>**th**</sup> **(ICT)]** 

      - a. Which one is IPV4 address ? How many bits are used for IPV6 address ? How does the above IPV6 address completely with the addressing scheme . 

      - b. How many subnets and hosts are to be supported by the above mentioned IPV4 address ? 

2. Distinguish between TCP and UDP . **[BCS – 37**<sup>**th**</sup> **(ICT)]** 

3. What is OSI model ? Draw the diagram of OSI model . State the protocol of each layer . **[BCS – 37**<sup>**th**</sup> **(ICT)]** 

4. **[BCS – 37**<sup>**th**</sup> **(ICT)]** 

      - a. What is static IP ? 

      - b. (b)Why do we need static private ip address and advantages of it . 

5. How DNS does work ? **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

###### **Object Oriented Programming:** 

1. State the advantages of object oriented programming (OOP) over structured programming. **[BCS – 38**<sup>**th**</sup> **(ICT)]** 

2. Explain encapsulation and inheritance in details . **[BCS – 38**<sup>**th**</sup> **(ICT)]** 

3. Why are the following two overloaded functions inherently ambiguous? int f(int a,int b= 5) and int f(int &a) **[BCS – 38**<sup>**th**</sup> **(ICT)]** 

4. **[BCS – 37**<sup>**th**</sup> **(ICT)]** 

   - a. What is object oriented programming? 

   - b. What are the main features of OOP? 

   - c. How can we solve problem using abstraction? 

   - d. How is a member function of a class ? 

Govt CSE or IT JOB : OUR GOAL™ [Largest IT Job group of Bangladesh ] ☑ ️ 

5. What are objects in C ++? How is a member function of a class ? **[BCS – 37**<sup>**th**</sup> **(ICT)]** 

6. Explain Early Binding and Late Binding with example ? **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

7. Explain Method overloading and Method overriding with example . **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

8. What is Encapsulation, inheritance and Polymorphism ? **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

###### **Operating system:** 

1. What is pipelining? How does pipeline implementation make faster instruction execution? **[BCS – 38**<sup>**th**</sup> **(ICT)]** 

2. What are the steps that occur when an interrupt is processed . **[BCS – 38**<sup>**th**</sup> **(ICT)]** 

3. What is operating system? Why do we need operating system? **[BCS – 38**<sup>**th**</sup> **(ICT)]** 

4. What is deadlock? Describe the way of detecting and protecting deadlock. **[BCS – 38**<sup>**th**</sup> **(ICT)]** 

5. (a)What is the difference between preemptive and non preemptive scheduling (b) What is aging ? Why it is used in OS ? **[BCS – 37**<sup>**th**</sup> **(ICT)]** 

6. What is Race Condition ? How to remove this ? **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

7. Explain how Parallel Processing does work? **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

8. What is interrupt Controller? **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

9. Explain Banker’s Algorithm for Deadlock handling. **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

10. Distinguish between paging & Segmentation. **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

###### **Security:** 

1. What is cryptography and public key infrastructure are important? **[BCS – 37**<sup>**th**</sup> **(ICT)]** 

2. What is Digital Signature ? How public key and private key encryption does? **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

3. Describe DoS and Brute Force attack. **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

###### **Software Engineering** 

1. Describe different techniques use the risk analysis of software development explanation. **[BCS – 38**<sup>**th**</sup> **(ICT)]** 

2. Describe agile Model. **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

3. Explain each component of Unit testing Environment. **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

4. Describe the disadvantages of prototype technique **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

###### **Structured Programming:** 

Govt CSE or IT JOB : OUR GOAL™ [Largest IT Job group of Bangladesh ] ☑ ️ 

1. What is structured programming ? with example . **[BCS – 38**<sup>**th**</sup> **(ICT)]** 

2. Write Pseudocode to implement Enqueue and Dequeue operation array of C. **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

3. Write a Program of basic calculator operation function using switch statement (+.-,*,/) using any language C/C++ **[BCS – 36**<sup>**th**</sup> **(ICT)]** 

4. (b)Write a C program to store information using structures with dynamically memory allocation? 

###### **Communication:** 

1. (a) Determine the nyquist sampling rate and the nyquist sampling interval for the signal X(t) = sin(2100pit) 

(b) What is modulation ? Describe the pulse code modulation technique.State the advantage and disadvantage of PCM . 

2.(a) What is the block diagram of digital computer .describe each unit briefly. 

(b) What is pipelining? How does pipeline implementation make faster instruction execution? 

###### **Probability Distribution** 

11.A full joint probability distribution for the Toothache, Cavity and catch world is given below. 

Ecommerce : 

- 2.(a)Difference between E-Commerce and M-commerce 

- (b) What are barriers of E-Commerce ? 

- (c) What is cryptography and public key infrastructure are important? 

```

১(ক) Problem solving technique এর িংজ্ঞা বেন। Structured programming এিং object-

oriented programming এর পাথ্ণকযগুযলা বলিুন। ৫

```

```

(ি) 1-D array কীভাযি initialize করা  াে? একো ফাংিন-এ কীভাযি array আমরা pass করযত পাবর?৫

```

```

(গ) একবে C program বলিুন  া একবে 5-digit িংিযার িকল digit-এর য াগফল বনরূপণ করযত পাযর। এই program

এর flowchart আঁকুন। ১০

```

```

(ঘ) Assembly language কী? এর বিবিষ্ট্যগুযলা বলিুন। একবে Assembly language program বলিুন  া দুবে

িংিযার য াগফল ও গুণফল বনরূপণ করযত পাযর। ৫

```

```

২. (ক) (E)16 িংিযার decimal, octal এিং binary রূপ বলিুন। বনম্নবলবিত Hexadecimal sequence এর পরিতণী

৪বে িংিযা কী হযি বলিুন। 6FC, 6FE,------, --------, --------, -------- ৫

```

`(ি) Boolean function কী? বনযের Boolean function-যক কীভাযি িহজীকরণ করা য যত পাযর? F = A` ’ `B' C + A' BC + AB' ৫` 

```

(গ) (+55)10 এর 2's complement বলিুন। J-K flip-flop এিং clocked D-flip-flop এি পাথ্ণকযগুযলা যেিান। ৫

(ঘ) (A+B) V(not A) V (notC) এর truth table বনণণে করুন। ৫

```

```

(ঙ) Two input multiplexer এর logic circuit অঙ্কন করুন। Multiplexer এিং demultiplexer এর

তুলনা করুন। ৫

```

`৩. (ক) Breadth-first search (BFS) এিং Depth-first search (DFS) এর পাথ্ণকযগুযলা বলিুন। কী কী ধরযনর problems এর জন্য BFS DFS এর যথ্যক ভাযলা? ৫` 

```

(ি) Array এর পবরিযতণ linked list িযিহাযরর সুবিধাগুযলা ও অসুবিধাগুযলা বলিুন। ৫

```

```

(গ) একবে algorithm এর time complexity এর িংজ্ঞা বেন। যকন Quicksort এর worst-case complexity Q(n

^ 2) িংবক্ষপ্তভাযি বলিুন। ৫

```

```

(ঘ) Sorted linked list এ কী Binary search apply করা িম্ভি বকনা? আপনার উত্তযরর িপযক্ষ উোহরণিহ  ুবি

যেিান। ৫

```

```

(ঙ) মযন করুন য  একবে Binary tree এর preorder traversal post order traversal এর মান  থ্াক্রযম deafg

এিং abdecfg যেওো আযে। ঐ Binary tree এর postorder traversal কী হযি? ৫

```

```

৪.(ক) Intel 8086 microprocessor এর block diagram আঁকুন। 8086 microprocessor এর বিবিষ্ট্যগুযলা

বলিুন। ৫

```

```

(ি) বনম্নবলবিত 8086 program status word এর অথ্ণ বলিুন। ৫

```

|`S`|`Z`|`AC`|`P`<br>`CY`|

|---|---|---|---|

|`0`|`0`|`1`|`1`<br>`0`|

Govt CSE or IT JOB : OUR GOAL™ [Largest IT Job group of Bangladesh ] ☑ ️ 

```

(ঙ) Interrupt এর উোহরণিহ িংজ্ঞা বেন।  বে processor এর গবত ১-৮ GHz হে তযি এর time period কত হচে ?

৪

```

```

পােণ- ২

(বনযম্নর িকল প্রযশ্নর উত্তর বেন)

 মান-২৫×৪=১০০

```

```

৫। (ক) n-িংিযক উপাত্তযক িাজাযনার জন্য divide and conquer strategy িযিহার কযর Merge sort Algorithm

বলিুন। ৫

```

```

(ি) Feasible solution এিং Optimal solution এর িংজ্ঞা বেন। একবে graph এর single-source

shortest path বতবর করার জন্য greedy algorithm-বে বলিুন। ৬

(গ) ধরুন একবে sum of subset problem এ n = 4 ,w=(w 1 ,w 2 , 3, 4) = (11, 13, 24, 6) এিং

m = 30 যেওো আযে। w এর িকল িম্ভািয subset গুযলা যির করুন  ার য াগফল এর িমান। এই

problem এর িম্ভািয solution space tree যির করুন এিং answer mode গুযলা বেবিত করুন।৬ \

(ঘ) বনম্নবলবিত term গুযলার িংজ্ঞা বেন:

```

```

Backtracking, NP, NP-Hard and NP complete problem. ৪

```

```

(ঙ) অপাযরবেং বিযেম এ Deadlock এর িংজ্ঞা বেন। একবে Deadlock situation যেিাযনার জন্য একবে িবিক

diagram অংকন করুন ও িংবক্ষপ্তভাযি আযলােনা করুন। ৪

```

```

(খ) Functional dependency এর িংজ্ঞা বেন। ইহার Armstrong's axioms property গুযলা বলিুন। ৫

(গ)বনম্নবলবিত Transaction হযত inconsistency state িযািযা করুন( বেথ্াযক)। ৫

```

Govt CSE or IT JOB : OUR GOAL™ [Largest IT Job group 

of Bangladesh ] ☑ ️ 

```

(ঘ) একজন software প্রযকৌিলীর একবে software design করার োবেত্বগুযলা বলিুন। ৫

```

```

(ঙ) Software testing কী? বনযম্নর term গুযলার পাথ্ণকযগুযলা বলিুন: ৫

```

```

(i) Blackbox testing ও Whitebox testing

```

```

(ii) Verification ও Validation

```

```

৭। (ক) HTTP এিং DNS এর িংজ্ঞা বেন। ধরুন য  mygov.bd একবে যডাযমইন যনম। এিাযন DNS কীভাযি কাজ

কযর? ৫

```

```

(ি) TCP ও UDP হযলা Transport layer protocol এর উোহরণ। এই protocol দুবের পাথ্ণকযগুযলা বলিুন।৩

```

```

(গ) বেত্রিহ circuit switching এিং packet switching এর পদ্ধবত আযলােনা করুন। ৭

```

```

(ঘ) Network এর topology এর িংজ্ঞা বেন। একবে কবিউোর লযাি স্থাপযনর জন্য BUS topology

  দ্বারা LAN এর বেত্র অঙ্কন করুন।৫

```

```

(ঙ) Virus, worms এিং trojan horse এর মযধয পাথ্ণকযগুযলা বলিুন। ৫

```

```

৮।(ক) Al এর Agent কত প্রকার ও কী কী এিং তাযের কাজগুযলা বলিুন।৫

```

```

(ি) Al এর Adversarial search উোহরণিহ িযািযা করুন। ৫

```

```

গ) Machine learning এ overfitting কী? কীভাযি আমরা Machine learning এ overfitting  এড়াযত পাবর? ৫

```

```

(ঘ) Supervised learning, unsupervised learning Supervised learning,  এেং reinforcement learning

এর িংজ্ঞা বেন। এগুযলা িযিহাযরর উযেশ্যগুযলা কী? ৫

```

```

(ঙ) Data communication এ Multiplexing কী? TDM এিং FDM এর মযধয পাথ্ণকযগুযলা বলিুন। ৫

```

Govt CSE or IT JOB : OUR GOAL™ [Largest IT Job group 

of Bangladesh ] ☑ ️ 

**Dutch Bangla Bank | Exam Taker :BUET Post : Assistant Network/Hardware Engineer Time :1:30 Hours | Date :05/03/19. Marks distribution :20(non_dept) +65(dept.) = 85** 

###### **1. What is state full and stateless firewall :** 

###### **Solution:** 

**Stateless Firewall** works by treating each packet as an isolated unit, Stateless Firewall filters based on header information in packet like Source IP, Destination IP, port number etc. 

**Stateful firewalls** works by maintaining context about active sessions and use “state information” to speed packet processing. Infact Stateful Firewalls use the concept of state table where it Stores the state of legitimate connections. Stateful Firewalls filter packets by matching to valid states in the state table 2. What is RAID and RAID level ? raid0, raid1 , raid5 

3.Write 3 private ip address range: 

a)10.0.0.0---10.255.255.255 b)172.16.0.0---172.31.255.255c)192.168.0.0-----192.168.255.255 

######  **2. Write down the online and offline Ups .**  

###### **Solution:** 

|Online UPS|Offline UPS|

|---|---|

|An online UPS is one which supplies the AC<br>power<br>through<br>rectifier<br>and<br>inverter<br>combination circuit in case of power availability<br>as well as in power outage|An offline UPS is one which supplies the AC<br>mains power directly to the load in case of<br>power availability and whenever there is power<br>outage it supplies power to load through backup<br>battery.|

|Heat dissipation is more in comparison to<br>offline ups because online ups is ON<br>continuously.|Heat dissipation is low because offline ups is<br>switched ON only in case of power outage.|

|Time required to switch the path during power<br>outage is termed as transfer time. As the transfer<br>switch in case of online ups is always ON thus,<br>transfer time is zero.|Transfer time is about5ms|

|Online UPS is immune to external distortions<br>such as surges, spikes and power failure.|Offline UPS is not immune to external<br>distortion.|

|It require more components and thus it is<br>complex to design.|It require less components and thus simpler in<br>design.|

|**5.**<br>**Difference between TCP and UDP**||

|---|---|

|TCP|UDP|

|TCP establishes connection between computers|UDP sends the data directly to the destination|

|before transmission of data .|computer without checking whether the system<br>is ready or not .|

|TCP is connection oriented|Connection less|

|Slower|Faster|

**Page | 1** 

|Heavy weight|Light weight|

|---|---|

|UseFTP,HTTP,SMTP,BGPetc|UseDNS,DHCP,TFTP,SNMPetc.|

###### **6. Find subnet and host number of 255.255.240.0**  

###### **Solution:** 

Here class C .we know that 240 = 11110000 So the subnet mask = 255.255.11110000.00000000 Total 1 = 4 total 0 = 12 So subnet = 2^4 ,host = 2^12 -2; 

 **7.output of the following code.**  `#include<stdio.h> int main() { int a =3 , b= 10 ; if(a>b) printf("A"); else printf("B"); return 0; }output : B` 

######  **9 Write down the following blanks** 

###### **Solution:** 

a) Ip address converted into physical address ARP . 

b) Names are converted into domain name DNS . 

c)Mail transferred between SMTCP protocol . 

d) Data link layer is responsible for convert ip address into mac address. e) HTTP SERVICE PROVIDES USING WHICH PROTOCOL tcp PROTOCOL ? 

###### **10 SQL query to find avg salary of all is greater than the salary of each department .Employee**  **(emp_id,emp_name,salary,city,dept_name) with some condition** 

###### **Solution:** 

Select avg(salary) from Employee where avg(salary)>salary group by Dept_name ; 

**Page | 2** 

১৫ তম শিক ্ষ ক শিবন ্ধ ি শিশিত 

১৫ তম শিক ্ষ ক শিবন ্ধ ি শিশিত 

|||অথিা,||

|---|---|---|---|

||(ক)|কাউন্টার বক? একটি 3 bit-Ripple Counter এর গঠন ির্ণনা করুন।|১+৪ = ৫|

||(ি)|ইনস্ট্রাকেন কফ্স সাইদক  ও এবিবকউেন সাইদক  এর কাদির ধারা ির্ণনা করুন।|৬|

||(গ)|RAM ও ROM এর পাথণকয ব খুন।|৪|

|৪।|(ক)|বরদ েনা  ডাটাদিি ম্যাদনিদমন্ট বসদস্ট্ম বক? ডাটাদিদির বিবভন্ন প্রকার বরদ েনেীপ<br>ির্ণনা করুন।|১+৬ = ৭|

||(ি)|GRANT ও REVOKE এর কাি ির্ণনা করুন।|৪|

||(গ)|DDL ও DML সিদকণ ব খুন।|৪|

|||অথিা,||

||(ক)|প্যারা া  প্রদসবসং বক? পাইপ াইন প্রদসবসং পদ্ধবত উোহরর্সহ ির্ণনা করুন।|১+৪ = ৫|

||(ি)|Indexing ও Hashing কী? Dense index ও Sparse index<br>ির্ণনা করুন।|২+৩ = ৫|

||(গ)|Flip-flop কী? একটি S-R Flip-flop এর গঠন সতযক সারবর্সহ ির্ণনা করুন।|১+৪ = ৫|

|৫।|(ক)|কনটওয়াকণ টদপা বি বক? বিবভন্ন প্রকার কনটওয়াকণ টদপা বির বিত্রসহ ির্ণনা ব খুন।|১+৬ = ৭|

||(ি)|Class ও Object ি দত বক বুঝায়? Class ও Object বডক্লায়ার করার বনয়ম ব খু|ু    ্ল    ুন। ২+৩ = ৫|

||(গ)|FOR. Loop এর গঠন ব্যাখ্যা করুন।|৩|

|||অথিা,||

||(ক)|কপ্রাগ্রাম উন্নয়দনর ধাপসমূদহর ির্ণনা ব খুন।|৫|

||(ি)|1<sup>2</sup>+ 2<sup>2</sup>+ 3<sup>2</sup>+ ............. + N<sup>2</sup>ধারাটির ক াগফ্  কির করার কপ্রাগ্রাম|৫|

|||ব খুন (User defined function ব্যিহার কদর)।||

||(গ)|Data abstraction কী? Data abstraction এর ক দভ গুদ া ির্ণনা করুন।|ু  ্ণ ু  ১ + ৪ = ৫|

|৬।|ফ্াংে ্র    ্    ু|্ন কপ্রদটাটাইপ ও ওভারদ াড ফ্াংেন ি দত বক বুঝায়?|৫|

|||অথিা,||

||ই-কমণ     ণ  ু ণ ণ  ু|াসণ ও ই-বিিদনস এর মদে পাথণকয ব খুন। ই-গভদনণস সিদকণ ব খুন।|৩ +২ = ৫|

|৭।|Cod<br>প্রধান ু|e generation ও Code optimization কী? Code generation এর<br>্র কািগুদ া কী কী?|১+৩+১=৫|

অথিা, 

১৫ তম শিক ্ষ ক শিবন ্ধ ি শিশিত 

১৭ তম বিকক বনিন ্ষ ্ধ ন লিলিত 

|||বিষয়: কবিউটার বিক্ষা|

|---|---|---|

|||বিষয় ককাড :<br>৩<br>১<br>৩|

|||পদের নাম: সহকারী বিক্ষক (তথ্যও ক াগাদ াগ প্রযুবি)<br> ্ট|

|||সময়- ৩ ঘন্টা<br>পূর্ণমান-১০০<br>(দ্রষ্টব্য: ডান পাদি উবিবিত সংখ্যা প্রদের পূর্ণমান জ্ঞাপক।)<br>ক বিভাগ|

|||নম্বর|

|১।|(ক)|গঠন ও বিয়ানীবত অনুসাদর কবিউটাদরর কেবর্বিভাগ আদ াচনা করুন।<br>১০|

||(ি)|২য় প্রজদের কবিউটাদরর বিবিষ্টযগুদ া ব খুন।<br>৫|

|||অথিা,|

||(ক)|সুপার কবিউটার ও কমইনদেম কবিউটার সিদকণ আদ াচনা করুন।<br>১০|

||(ি)|অযানা গ ও বডবজটা  কবিউটাদরর মদে পাথণকয ব খুন।<br>৫|

|২।|(ক)|বসবপইউ কী? বসবপইউ এর সংগঠন ির্ণনা করুন।<br>২+৮= ১০|

||(ি)|কবিউটার কীভাদি কাজ কদর? ব্যাখ্যা করুন।<br>৫|

|||অথিা,|

||(ক)|কবিউটার স্মৃবত ি দত কী কিাঝায়? কবিউটার স্মৃবতর কেবর্বিভাগ আদ াচনা করুন।<br>১০|

||(ি)|আধুবনক জীিদন ইন্টারদনদটর প্রদয়াগ আদ াচনা করুন।<br>৫|

|৩।|(ক)|বসদেম সফটওয়যার কী? বিবভন্ন প্রকার বসদেম সফটওয়যার সিদকণ আদ াচনা করুন।<br>২+৮= ১০|

||(ি)|বচত্রবভবিক অপাদরটং বসদেদমর গুরুত্বপূর্ণ কাজসমূহ ব খুন।<br>৫|

|||অথিা,|

||(ক)|মাবিপ্রদসবসং অপাদরটং বসদেম কাদক িদ ? বচত্রসহ মাবিপ্রদসবসং আপাদরটং বসদেদমর কা ণপদ্ধবত ১০<br>আদ াচনা করুন।|

||(ি)|অনুিােক কপ্রাগ্রাম কী? এর কাজসমূহ উদিি করুন।<br>৫|

|৪।|(ক)|সংখ্যা পদ্ধবতর বভবি ি দত কী কিাঝায়? পবজিনা  ও নন-পবজিনা  সংখ্যা পদ্ধবত উোহরর্সহ ২+৮= ১০<br>আদ াচনা করুন।|

||(ি)|(৫৩.৬২)১০সংখ্যাদক অক্টাদ  প্রকাি করুন।<br>৫|

||(ক)<br>২-এর পবরপূরক পদ্ধবত কী? ২-এর পবরপূরক পদ্ধবত ব্যিহার কদর (-১৩)১০ কথদক|২+৮= ১০|

|---|---|---|

||(৯)১০ বিদয়াগ করুন।||

||(ি)<br>িাইনাবর সংখ্যা পদ্ধবত ও বিবসবড ককাদডর তু নামূ ক আদ াচনা করুন।|৫|

|৫।|(ক)<br>কমৌব ক  বজক কগইটসমূহ সতযক সারর্ীসহ ির্ণনা করুন।|১০|

||(ি)<br>সতযক সারর্ী কী? উোহরর্সহ ব খুন।|৫|

||অথিা,||

||(ক)<br>NOR কগইদটর সাহাদে নট, অর এিং অযান্ড কগইদটর িাস্তিায়ন কেিান।|১০|

||(ি)<br>বে F = X Y + XY Z হয়, তদি প্রমার্ করুন ক , F. F = 0 .|৫|

||ি বিভাগ||

|৬।|কডটা প্রদসবসং পদ্ধবত আদ াচনা করুন।<br>অথিা,|৫|

||কপ্রাগ্রাম কলাচাদটণর প্রতীকগুদ া অথণসহ ব খুন।|৫|

|৭।|দুট সংখ্যার গ.সা.গু বনর্ণদয়র জন্য অযা গবরেম ব খুন।|৫|

||অথিা,||

||আয়তদক্ষদত্**র**কক্ষত্রফ  বনর্ণদয়র জন্য কলাচাটণ অঙ্কন করুন।|৫|

|৮।|ককাড কী? ASCII ককাদডর বিবিষ্টযগুদ া ব খুন।<br>অথিা,|১+৪ = ৫|

||ই-কমই  কী? ই-কমই  অযাদেদসর গঠন সিদকণ ব খুন।|৫|

|৯।|(BF)১৬এিং (৫৫)৮সংখ্যা দুট ক াগ করুন এিং ফ াফ  কহক্সাদডবসদমদ  প্রকাি করুন।|৫|

||অথিা,||

||ককান যুবিদত ১ + ১ = ১ এিং ১ + ১ = ১০ হয়? ব্যাখ্যা করুন।|৫|

|১০।|(A+C)(B+D)সমীকরর্ট সর  করুন এিং যুবি িতণনী অঙ্কন করুন।<br>অথিা,|৫|

||অযা গবরেম কী? অযা গবরেদমর বিবিষ্টযগুদ া ব খুন।|১+৪=৫|

১৭ তম শিকক শিবন ্ষ ্ধ ি শিশিত 

বিষয়: তথ ্য ও য োগোয োগ পয ্র বি ু 

বিষয় য োড : ৪৫২ পযের নোম: পভোষ ্র সময়- ৩ ঘন ্ট ো 

পর ূ ্ ণমোন-১০০ (দষ ্র ব ্ট : ডোন পোযে উবিবিত সংখ ্য ্য ো প ্র যের পর ূ ্ ণমোন জোপ । য  য োযনো েেট ্ঞ প ি ্র যের উতর বেযত হযি।) ্ত বিভোগ 

(ক) C প্রোগ্রোশমিং ল্োিংগুয়েয়ে user defined function এবিং library function এর পোর্থকয শিখুি। ৪ (ি) এমি একটি C program শিখুি যো একটি array ততশর কয়র কতগুয়িো প্েটো রোিয়ব, তোরপর ফিোফি শিয়েয়ব প্েটোগুয়িোয়ক শবপরীত শিক প্র্য়ক print করয়ব।                                                                                     ৬ 

অর্বো, 

(ক) Pointer কী? Pointer ব্যবিোয়রর সুশবধোগুয়িো শিখুি। ৪ (ি) রর্ম িিটি Fibonacci number রিিথয়ির েন্য একটি C program শিখুি। ৬ 

২। (ক) Local variable এবিং Global variable এর ময়ে পোর্থকয শিখুি। ৫ (ি) কী কী ধোরণোর উপর শিশি কয়র OOP রশতশিত? ধোরণোগুয়িো ব্যোখ্যো করুি।  ৫ 

অর্বো, 

(ক) উিোিরণেি Class এবিং Object এর ময়ে পোর্থকয ব্যোখ্যো করুি। ৪ 

- (ি) Inheritance কী? উিোিরণেি ব্যোখ্যো করুি। ৬ 

৩।( ) Modularization কী? উিোর সুশবধো েম্পয়কথ শিখুি। ৫ (ি) Software Engineering এর প্ক্ষয়ে Waterfall Model বণথিো করুি। ৫ 

অর্বো, 

১৭ তম শিকক শিবন ্ষ ্ধ ি শিশিত 

(ক) Software testing কী? উিোর গুরুত্ব আয়িোচিো করুি। ৬ 

(ি) Software maintenance এর েোয়র্ কী কী শবষে েশিত, তো আয়িোচিো করুি। ৪ ৪। ( ) B-tree data structure কী? এর রয়েোগ ব্যোখ্যো করুি। ৫ (ি) BFS ও DFS এর পোর্থকয শিখুি। ৫ 

- অর্বো, (ক) Linked List কী? উিোিরণেি বণথিো করুি। ৬ 

- (ি) Binary Search tree উিোর অপোয়রিিগুয়িো বণথিো করুি। ৪ 

৫। (ক) Decision Tree কী? উিোিরণেি বণথিো করুি। ৬ (ি) Linear Search এবিং Binary Search এর ময়ে পোর্থকয শিখুি। ৪ অর্বো, ( ) Heap data structure কী? প্কোি প্ক্ষয়ে Heap ব্যবিোর করো িে? ৪ (ি) অযোিগশরিয়মর complexity বিয়ত কী প্বোঝোে? কয়েকটি sorting algorithin এর complexity উয়েি করুি।                                                                                                                                   ৬ ৬। ( ) HTML Element  ী? উেোহরর্সহ ির্ণনো  রুন। ৬ (ি) Static ও Dynamic ওযয়িসোইযের মযে পোর্ণ য বিখুন। ৪ অর্িো, ( ) উেোহরর্সহ HTML webpage এর গঠন ব্যোখ্যো  রুন। ৫ (ি) বনযের বিস্ **ট** ততবর  রোর জন্য HTML য োড বিখুন: ৫ 1. Fruits (a) Mango (b) Orange 2. Vegetables `o` Green capsicum `o` Yellow capsicum `o` Red capsicum 

১৭ তম শিকক শিবন ্ষ ্ধ ি শিশিত 

|৭।|( )|Paging এিং Sigmentation এর পোর্ণ য বিখুন।|৪|

|---|---|---|---|

||(ি)|Unix file system এর প্র োরযভে ির্ণনো  রুন।<br>অর্িো,|৬|

||( )|Blocking এিং Buffering OS এর পোর্ণ য বিখুন।|৪|

||(ি)|Operating System-এর Memory hierarchy সবেত্র ির্ণনো  রুন।||

|৮।|( )|DDL এিং DML এর মযে পোর্ণ য বিখুন।|৪|

||(ি)|Centralized System ও  Client-Server System সম্পয ণ সবেত্র ির্ণনো  রুন।|্প ণ ্র ্ণ  ু    ৬|

|||অর্িো,||

||( )|Indexing এিং Hashing এর পদ্ধবতগুযিো ির্ণনো  রুন।|৬|

||(ি)|Speedup এিং Scaleup বেত্রসহ ব্যোখ্যো  রুন।|৪|

|৯।|( )|Data Fragmentation  ী? ব্যোখ্যো  রুন।|৬|

||(ি)|One-to-one এিং One-to-many বরযিেন উেোহরর্সহ ব্যোখ্যো  রুন।<br>অর্িো,|৪|

||( )|Private key এিং Public key উেোহরর্সহ ব্যোখ্যো  রুন।||

||(ি)|Plaintext ও Cipher text এর পোর্ণ য বিখুন।||

|১০।|( )|ফোইিোর অপটি   যোিযির গঠন ও তিবেষ্টয ব্যোখ্যো  রুন।|৬|

||(ি)|FDM এিং TDM এর পোর্ণ য বিখুন।|৪|

|||অর্িো,||

||( )|যডেো ট্রোন্সবমেযন Router ও Gateway এর মযে য োনটি অবি তর সুবিিোজন --|৪|

|||মতোমত ব্যি  রুন।||

||(ি)|Cloud computing  ী? উহোর তিবেষ্টয ও সুবিিো ির্ণনো  রুন।||

১৭ তম শিক ্ষ ক শিবন ্ধ ি শিশিত 

###### বিষয়: কবিউটার বিজ ্ঞ ান 

বিষয় ককাড : ৪৩১ 

পদের নাম: পভাষক ্র 

সময়- ৩ ঘন ্ট া 

(দষ ্র ব ্ট : ডান পাদে উবিবিত সংখ ্য ্য া প ্র দের পর ূ ্ ণমান জাপক। কে ককাদনা েেট ্ঞ প ি ্র দের উতর বেদত হদি।) ্ত 

###### ক বিভাগ 

নম্বর 

- ১। (ক) কবিউটার কী? বিত্রসহ একটি মাইদরা কবিউটাদরর প্রধান সাংগঠবনক অংেগুদ া ৬ ব্যাখ্যা করুন। 

- (ি) ন্যাদনাদটকদনা জী কী? এর প্রদয়াগ ও ব্যিহার সিদকণ আদ ািনা করুন। ৪ 

- ২। (ক) উোহরর্সহ কুইক সটণ অযা গবরেম ব খুন। ৫ (ি) কডটা স্ট্রাকিার ি দত কী বুদেন? স্ট্যাক ও বকউ কডটা স্ট্রাকিার ির্ণনা করুন। ৫ 

- ৩ (ক) কী ওয়াডণ কাদক িদ ? ১+৩+৫+.............+১০০ পেণন্ত সক  বিদজাড় পূর্ণ সংখ্যার কোগফ  কির ৬ করার জন্য বস ভাষায় একটি কপ্রাগ্রাম ব খুন। 

- (ি) ি ক কী? স্থানীয় ি ক ও সািণজনীন ি দকর মদে পার্ণকয ব খুন। ৪ 

- ৪। (ক) বনদে িবর্ণত Adjacency ম্যাবিক্স A এিং B এর জন্য ক িবিত্র অংকন করুন। ৫ 

   - 0     1      0      1      0 1     0      0      1      0 

   - (i) A =                                                       (ii) B = 0     0      0      1      1 1     1      1      0      1 0     1      1      1      0 

- (ি) f(x) = x<sup>2</sup> + x - 6 এিং g(x) = x<sup>3</sup> - 3x<sup>2</sup> - x + 3 এর ক িবিত্র অংকন করুন। ৫ 

- ৫। (ক) অনুিােক কপ্রাগ্রাম ি দত কী বুদেন? কিাই ার ও ইন্টারদপ্রটাদরর পার্ণকয ব খুন। ৫ (ি) সফটওয়যার কটবস্ট্ং ি দত কী বুদেন? White box কটবস্ট্ং ও black box ৫ কটবস্ট্ং আদ ািনা করুন। 

- ৬। (ক) (৯০ – ৭৫)১০ সংখ্যাটিদক িাইনাবর ও কহক্সাদডবসদমদ  রূপান্তর করুন। ২+২ = ৪ (ি) সর  করুন: A  B   C +  A  B  C  +   ABC ৩ (গ) EX - OR কগইট সতযক সারবর্সহ ির্ণনা করুন। ৩ 

১৭ তম শিক ্ষ ক শিবন ্ধ ি শিশিত 

|৮।|(ক)<br>(ি)|অপাদরটিং বসদস্ট্ম কাদক িদ ? অপাদরটিং বসদস্ট্দমর কােণািব  আদ ািনা করুন।<br>ফাই  বসদস্ট্ম কী? তা কত প্রকার ও কী কী?<br>ু   ণু     ু|৪<br>৩|

|---|---|---|---|

||(গ)|কডড ক ি দত কী বুোয়? কডড দকর েতণগুদ া সংদেদপ আদ ািনা করুন।<br>[ পর পৃষ্ঠা ্র্ট্য|৩<br>ৃ্ঠ দ্রষ্টব্য ]|

|৯।|(ক)|ই-কমাসণ কী? বিরয়দকন্দ্র ও ক নদেদনর প্রকৃবত অনুোয়ী ই-কমাদসণর কেবর্বিভাগ আদ ািনা করুন।|৬|

||(ি)|কডটার কগাপনীয়তা রোয় কডটা এনবরপেদনর ভূবমকা আদ ািনা করুন।|৪|

|১০।|(ক)|বরদ েনেীপ কী? দুটি কটবিদ র মদে বরদ েন ততবরর পদ্ধবত আদ ািনা করুন।|৬|

||(ি)|কী বফল্ড কী? প্রাইমাবর ও ফদরন কী ি দত কী বুোয়? ব্যাখ্যা করুন।|৪|

|১১।|(ক)|OSI মদড  কী? OSI মদডদ র ক য়ারসমূহ আদ ািনা করুন।|৫|

||(ি)|কনটওয়াকণ টদপা বজ কী? স্ট্ার ও িাস টদপা বজ আদ ািনা করুন।|৫|

|১২।|(ক)|কমবেন  াবনণং এিং কৃবত্রম বুবদ্ধসত্তার পার্ণকয ব খুন।|৪|

||(ি)|ANN এিং BNN এর তু না করুন।|৩|

||(গ)|Perception learning অযা গবরেম ব খুন।|৩|

|১৩।|<br>(ক)|সুদডাদকাড কী? বতনটি সংখ্যার মদে িড় সংখ্যা বনর্ণদয়র কলািাটণ অংকন করুন।|৫|

||(ি)|Class ও Object কী? Constructors ও Destructors ফাংেদনর মদে<br>পার্ণকয ব খুন।|৫|

১৬তম শিক ্ষ ক শিবন ্ধ ি শিশিত 

শবষয়: তথ ্য ও য োগোয োগ প ্র য ু শি 

শবষয় যকোড : ৪৫২ 

পযের িোম: পভোষক ্র 

সময়- ৩ ঘন ্ট ো 

পর ূ ্ ণমোি-১০০ 

(দষ ্র ব ্ট : ডোি পোযি উশিশিত সংখ ্য ্য ো প ্র যের পর ূ ্ ণমোি জোপক।) ্ঞ 

১। ক) একটি Array-তত পাঁচটি সংখ্যা ইিপুট শিসসসব শিসে তাসের গড় তবর করার জন্য C তরাগাশমং ল্যাঙ্গুসেসজ তকাড শিখুি।৬ (ি) C তরাগ্রাশমং ল্যাঙ্গুসেসজ Structure এবং Union এর মসে পার্থকয কী? উোিরণসি শিখুি।৪ 

অর্বা, 

(ক) লুপ কী? রবািশচত্রসি do-while এবং while এর গঠি ব্যাখ্যা করুি। ১+৪=৫ 

(ি) a * x ^ 2 + bx + c = 0 সমীকরণটির x চিসকর মাি শিণথসের জন্য C তরাগ্রাশমং ল্যাঙ্গুসেসজ একটি তকাড শিখুি। ৫ 

২। (ক) Object কী? কীভাসব Object ততশর করসত িে উোিরণসি ব্যাখ্যা করুি। ১+৩=৪ 

(ি) Friend function কী? উিার সুশবধা এবং' অসুশবধাগুসিা শিখুি। ১+৫=৬ 

অর্বা, 

- (ক) Object Oriented Programming-এর শতিটি রধাি মূিিীশত ব্যাখ্যা করুি। ৩ 

- (ি) Object Oriented Programming-এ Interface কী কাসজ িাসগ? ৩ 

(গ) Object Oriented Programming-এ method কী? Method কীভাসব ব্যবহৃত িে আসিাচিা করুি।৪ 

৩। (ক) Software Development Life Cycle (SDLC) এর শবশভন্ন ধাপগুসিা উসেি করুি ও সংসক্ষসপ বণথিা করুি। ৫ 

(ি) Software Development এর তক্ষসত্র Agile মসডি সম্পসকথ শিখুি। অন্যান্য মসডসির তুিিাে Agile মসডসির সুশবধা কী? ৫ 

অর্বা, 

(ক) Feasibility Test কী? সফটওেযার উন্নেসি উিার রসোজিীেতা বণথিা করুি। ১+৩=৪ 

(ি) Feasibility analysis এর শবশভন্ন ধাপসমূসির সংশক্ষপ্ত শববরণ শেি। ৬ 

৪। (ক) শিসি সংখ্যাগুসিাসক উৎশিমানুসাসর সাজাসিার জন্য Bubble sort শকভাসব কাজ করসব তা ধাসপ ধাসপ রেিথি করুণ। 

5,8,3,6,2      ৬ 

(ি) Binary Search (বাইিাশর সাচথ) শকভাসব করা িে? উোিরণসি তেিাি। ৪ 

অথবো 

(ক) শসসিকিি সটথ পদ্ধশতর অযািগশরেম শিখুি। ৪ 

১৬তম শিক ্ষ ক শিবন ্ধ ি শিশিত 

(ি) ৭ জি ছাসত্ **র** পরীক্ষাে রাপ্ত মাকথস তেো আসছ। ৪৫, ৭২, ৮০, ৬৫, ৮৪, ৫২, ৩৭ শসসিকিি সটথ ব্যবিার কসর িম্বরগুসিা শিম্ন িমানুযােী সাজাসিার রশিো ধাসপ ধাসপ শিখুি। ৬ 

৫। (ক) Heap শকভাসব ক কাজ কসর? উোিরণসি তেিাি। 

(ি) Greedy Algorithmm কাসক বসি? দুটি এমি সমস্যা বণথিা করুি যা Greedy Algorithm শেসে সমাধাি করা যাে। 

অর্বা, 

(ক) শিশিোর সাশচথং কী? উিার সুশবধা ও অসুশবধা ব্যাখ্যা করুি। 

(ি) Divide and Conquer technique কী? দুটি এমি সমস্যা বণথিা করুি Divide and Conquer technique এ সমাধাি করা যাে। 

৬। ক) ওসেব তপাটথাি ও ওসেব তিাশটং কী? ওসেব তিাশটং এর রসোজিীেতা ব্যাখ্যা করুি। ২+৩=৫ 

(ি) Cross-site Scripting বিসত কী তবাঝাে? এর িাত তর্সক রক্ষা পাওোর পদ্ধশতগুসিা শিখুি। ২+৩=৫ 

অর্বা, 

(ক) ওসেবসাইট কী? শিশিোর শসকুসেন্স ওসেব স্ট্রাকচার এবং শি ওসেব ১+২+২=৫ স্ট্রাকচার সশচত্র বণথিা করুি। ১+২+২ = ৫ (ি) শিসচর তটশবিটি ততশর করার জন্য HTML তকাড শিখুি: ৫ 

|Customer Name|P|roduct Nam|e|Product Manufacturer|

|---|---|---|---|---|

|Mr. John|Computer|Printer|Modem|HP|

|||||HP|

|||||ASUS|

৭। (ক) মাশি তরাগ্রাশমং অপাসরটিং শসসটম কী? সশচত্র বণথিা করুি। ৫ 

(ি) Virtual Memory বিসত কী তবাঝাে? এর কাযথ পদ্ধশত সংসক্ষসপ বণথিা করুি।৫ 

অর্বা, 

(ক) অপাসরটিং শসসটম এর তক্ষসত্র Swapping কী? তকাি তক্ষসত্র এটি ব্যবহৃত িে শিখুি। ১+২=৩ 

(ি) Distributed রসসশসং কী? উিার তবশিষ্ট্য ও সুশবধাগুসিা শিখুি। ১+৩+৩ = ৭ 

৮। (ক) Database এর তক্ষসত্র E-R Diagram বিসত কী তবাঝাে? একটি উোিরসণর মােসম ব্যাখ্যা করুি।৫ 

[(ি) Relational database model কী? অন্যান্য মসডসির তুিিাে এর সুশবধা-অসুশবধাগুসিা উসেি করুি। ৫ 

অর্বা, 

- (ক) তডটা এিশিপিি বিসত কী তবাঝাে? বহুি ব্যবহৃত কসেকটি এিশিপিি পদ্ধশতর িাম শিখুি। ২+২=৪ 

- (ি) Direct বা Random Access ফাইি রশিোকরণ শচত্রসি বণথিা করুি। ৬ 

৯। (ক) Data mining এবং Data warehousing বিসত কী তবাঝাে? এসের মসে সম্পকথ কী? এসের উপকাশরতা কী? ৬ 

- (ি) Database এর তক্ষসত্র indexing এর কাযথকাশরতা বণথিা করুি। ৪ 

১৬তম শিক ্ষ ক শিবন ্ধ ি শিশিত 

অর্বা, 

(ক) সটিং এবং ইসেশসং এর মসে পার্থকয শিখুি।৩<sup>থ</sup> 

(ি) SQL ব্যবিার কসর Student িাসম একটি তটশবি ততশর করুি। তটশবসি std-id, std-name, std-address এবং GPA িাসম চারটি field র্াকসব। Student তটশবি িসত তয সকি ছাসত্ **র** ফিাফি GPA-5 তাসের সকি তরকডথ তেিাসিার জন্য SQL query শিখুি।৪+৩ = ৭ 

১০। (ক) OSI model এর সাতটি স্তর (layer) কী কী? রর্ম দুটি স্তর সংসক্ষসপ বণথিা করুি। ৫ (ি) TCP/IP তরাসটাকি কী কাজ কসর তা বণথিা করুি। ৫ 

```

পাওয়ার সেক্টর

```

```

পাওয়ার সেক্টর

```

###### **Non Technical Part for Engineering Job** facebook group 

|**SL**<br>|**Questions**<br>|**Solution**|

|---|---|---|

|**1**<br><br>|`সেশের কত েতাাংে বিদ্যুৎ গ্ুাে সেশক উৎপােন হয় ?`<br><br>|`৪৭ (প্রায়), ৪৬.৫৩%`|

|**2**<br><br>|`িাাংলাশেশে বিদ্যুৎ বিতরণ োংস্থা কয়বি ?`<br><br>|`০৬ বি`|

|**3**<br><br>|`িাাংলাশেশে েশিবাচ্চ কত সকবি ওিারশহড লাইন আশে ?`<br><br>|`৪০০ সকবি`<br>|

|**4**<br>|`বনশের সকান বিদ্যুৎ বিতরণ োংস্থা েিবশেষ প্রবতবিত হশয়শে ?`<br>|NESCO<br>|

|**5**<br><br>|`িতবমাশন বিদ্যুৎ উৎপােন ক্ষমতা কত ?`<br><br>|29152MW<br><br>|

|**6**<br>|`রুপপুর পারমাণবিক বিদ্যুৎ সকশের লাইফ িাইম কত িের ?`<br>|`পাওয়ার ইউবনি ৫০ িের এিাং`<br>`বরয়াক্টরইউবনি ৬০িের।`<br>|

|**7**<br><br>|`নপনেনবর সেয়ারমযাি েহ সবােত সমম্বার কত জি ?`<br><br>|`্ট`<br>`৭ জি`<br><br>|

|**8**<br><br>|`রুপপুর পারমাণনবক নবদ্`**`য`**`ৎ সককে নিকে কত স াল্ট েরবরাহ ককর?`<br><br>|`৪০০ সকন`<br><br>|

|9<br>|Which is the latest Electricity Distribution Company of Bangladesh<br>|NESCO<br>|

|10<br><br>|Which area is the last national grd failure in Bangladesh ?<br><br>|Eastern<br><br>|

|12<br><br>|Install capacity of EGCB around ?<br><br>|987MW<br><br>|

|13<br><br>|Life time of Power unit in NPP in Rup pur ?<br><br>|50 yr<br><br>|

|14<br><br>|Which power plant is under the EGCB in Bangladesh<br><br>|Horipur<br><br>|

|15<br><br>|What type of Company EGCB ?<br><br>|Public<br><br>|

|16<br><br>|When occur the pick hour of power at present ?<br><br>|7 PM<br><br>|

|17<br><br>|Which turbine is as used in combined cycle power plant ?<br><br>|Gas turbine<br><br>|

|18<br><br>|Highest Voltage is --- for power transmission in Nuclear Power Plant<br><br>|400<br><br>|

|19<br><br>|`বিদ্যুশতর িবধবত োম কশি সেশক কার্বকর করা হয় ?`<br><br>|`০১ মােব, ২০২৩`<br><br>|

|20<br><br>|What is the name of hydroelectric power plant in Bangladesh<br><br>|Karnafuli<br><br>|

|21<br><br>|How many Board Member are there in BPDB ?<br><br>|06<br><br>|

|22<br><br>|Wapda is converted to BPDB on 1972---<br><br>|1 May<br><br>|

|23<br><br>|Where is the birth place of Indian billionaire Gautam Adani ?<br><br>|**Gujrat**<br><br>|

|24<br>|`রামপাল বিদ্যুৎ সকশে িারশতর সকান িুাাংক িাকা ইনশিস্ট কশরশে?`<br>|`এবিম িুাাংক `<br>|

|25<br><br>|`ইবিবেবি সকান ধরশণর সকাম্পাবন ?`<br><br>|`পািবলক বলবমশিড`<br>|

|26<br><br>|`প্রােবমক জ্বালানী বহশেশি িাাংলাশেশে বনশের সকানবি িুিহৃত হয় না ?`<br><br>|Urenium|

`প ্র ককৌশলী সমাো ঃ মানিক উনিি` [164] 

```

পাওয়ার সেক্টর

```

||What type of CPGCBL ?<br>|Ultra Super Critical Coal<br>Based Power Plant|

|---|---|---|

|<br>|What is the generation Capacity of CPGCBL ?<br><br>|**2*600 MW**|

||When The matarbari project is established ?<br>|**28 January 2018.**|

||Which turbine use in Rooppur<br>|Gas turbine|

||Current Power System total installed capacity<br>|29152MW<br>|

||Which generator used in matarbari to step up voltage<br>|Unit<br>|

||Maximum electricity generation in Bangladesh<br><br>|28562MW<br><br>|

||Highest Power demand in Bangladesh<br><br>|15648MW<br><br>|

||Life time of Reactor unit in NPP in Rooppur ?<br><br>|60 years<br><br>|

||How many pole used in Karnophuli Hydro Power plant ?<br><br>|None<br><br>|

||`িাাংলাশেশে বিদ্যুশতর েশিবাচ্চ ট্রান্সবমেন সিাশেি কত ?`<br><br>|400 KV<br><br>|

||`বিদ্যুৎ উৎপােশন সকান সমবেন িুিহৃত হয় ?`<br><br>|Synchronous Generator<br><br>|

||`বেবপবিবেবিএল সর্ মন্ত্রণালশয়র অধীন তার মন্ত্রীর নাম বক ?`<br><br>|Sheikh Hasina<br><br>|

||`সকান পাওয়ার প্লাশটির জ্বালানী খরে েিশেশয় কম ?`<br><br>|Hydroelectric<br><br>|

||`রামপাল মমত্রী োমবাল বিদ্যুৎ সকশের ক্ষমতা কত ?`<br><br>|1320MW<br><br>|

||`রুপপুর পারমাণবিক বিদ্যুৎ সকশের বরয়াক্টশরর আয়ুস্কাল কত ?`<br><br>|60 yr<br><br>|

||`িাাংলাশেশে বিদ্যুৎ বিতরণ োংস্থা কয়বি ?`<br><br>|6<br><br>|

||`িতবমাশন িাাংলাশেে বিদ্যুৎ উৎপােন ক্ষমতা কত ?`<br><br>|29152MW<br><br>|

||`বিদ্যুৎ সকশে বনিস্ব িুিহাশরর িন্য সকান ধরশণর ট্রান্সফরমার িুিহার করা হয় ?`<br><br>|Auxiliary<br><br>|

||How many pole used in Karnophuli Hydro Power plant ?<br><br>|None<br><br>|

||Which one is the largest power plant in Bangladesh ?<br><br>|Payra 1320<br><br>|

||Maximum install capacity of Electricity of Bangladesh ?<br><br>|29152MW<br><br>|

||Highest electricity generation in Bangladesh ?<br><br>|15648MW 15 April,2023<br><br>|

||Which type of power plant of “Nuclear power plant”<br><br>|Base Load<br><br>|

||Which basic design is used for Nuclear power plant in Bangladesh.<br><br><br>|VVER<br><br><br>|

||India Supplies how many power to Bangladesh ?<br><br>|2656MW<br><br>|

||What is the transformer called when it steps up ?<br>|Unit<br>|

||Install Capacity of Matarbari<br><br>|1200MW<br><br>|

||Install capacity of Payra<br><br>|1320MW<br><br>|

||Which is not transmission voltage of PGCB ?<br><br>|66KV<br><br>|

||What is the per capita electricity generation at present in Bangladesh ?<br><br>|602KW<br><br>|

`প ্র ককৌশলী সমাো ঃ মানিক উনিি` _________ 

```

পাওয়ার সেক্টর

```

||What will be the generation capacity target by 2041 in Bangladesh ?<br>|60000MW|

|---|---|---|

||Which organization deals with both distribution and generation<br><br>|BPDB|

|<br>|`DPDC এর আওতাধীন এবরয়া কত বকশলাবমিার ?`<br><br><br>|`২৫০`|

||`PGCB এর ৪০০ সকবি লাইশনর মের্ঘবু কত ?`<br><br>|`২১৬২ নেককনট`|

||`NESCO এর সেয়ারমুান সক ?`<br><br>|`ে. সেয়ে মাসুম আহকমে সেৌধুরী`|

||`WZPDCL সকান সিলায় ?`<br>|`খুলিা`|

||`EGCB স্থাপন ক্ষমতা কত ?`<br><br>|`৯৮৭`|

||`২০২১-২০২২ োশল DPDC এর প্রবফট কত সকাবি িাকা ?`<br><br>|`২১-২২ ১৬৬.৩৬ সকানট টাকা`|

|<br>|`NESCO এর িুিস্থাপনা পবরোলশকর নাম বক ?`<br><br><br>|`জানকউল ইেলাম`|

|<br>|`NESCO এর ৩৩/১১ সকবি োি সস্টেন কয়বি ?`<br><br><br>|`৮৩ নট`|

||`২০২২-২০২৩ োশল NESCO এর গ্রাহক িৃবির হার কত ?`<br><br>|`৫.৬৬%(২০২২-২০২৩)`|

||`রুপ পুর পারমাণবিক বিদ্যুৎ সকশের বরফুশয়বলাং েময় কত ?`<br><br>|`১২ মাে`|

||`কয়নট সজলায় সিেককা নবদ্`**`য`**`ৎ েরবরাহ ককর ?`<br><br>|`১৬ নট`<br>|

|27<br>|Transmission loss of DPDC ?<br>|**৬.০৬ %**<br>|

|2<br><br>|Total distribution transformer of NESCO ?<br><br>|১২১১০<br>|

|3<br><br>|Capacity of 400Kv HVDC substation is<br><br>|1000MW|

|4<br><br>|Number of customers of NESCO ?<br><br>|১৯,১৫,৯৯৬|

|5<br><br>|NESCOকয়টি জেলায় নিয়য় নিদুৎ সরিরাহ কয়র<br><br>|16|

|6<br><br>|NESCOএরconsumerকত েি?<br><br>|১৯,১৫,৯৯৬<br>|

|7<br>|WZPDCL system loss-<br>|৭.৩২%<br>|

|8<br><br>|NESCO consumer increase in<br><br>|৫.৬৬%<br><br>|

|9<br><br>|Maximum demand of NESCO<br><br>|896 MW<br><br>|

|10<br>|Member of DESCO panel-<br>|12<br>|

|11<br><br>|DPDC maximum demand which month and year<br><br>|**1806MW**<br>**10/09/2023**<br>**মেগাওযাট**<br><br>|

|12<br>|APSCL install capacity<br>|1647 MW|

|13<br><br>|Ruppur thermal output<br><br>|3212 MW|

|14<br><br>|What is the name of state minister of power ?<br><br>|িসরুল হানিদ|

|15<br><br>|Which year DESCO started its commercial works ?<br><br>|24 Sep 1998|

|16<br><br>|What is the system loss of DPDC ?<br><br>|6.06%|

|17<br><br>|Which voltage isn’t transmitted by PGCB ?<br><br>|66KV|

|18<br><br>|What is the number of PBS ?<br><br>|80|

`প ্র ককৌশলী সমাো ঃ মানিক উনিি` [166] 

```

পাওয়ার সেক্টর

```

|19<br>|Bangladesh import power from which state of India ?<br>|Tripura<br>|

|---|---|---|

|20<br><br>|The first unit will be launced in which year  NPCBL?<br><br>|2023<br><br>|

|21<br><br>|What is the number of power plant under BPDB ?<br><br>|39<br><br>|

|22<br><br>|PGCB which power company distribute their power ?<br><br>|None<br><br>|

|23<br><br>|According to PGCB the demand of power in month August ?<br><br>|13271MW<br><br>|

|24<br><br>|ওজ োপোডিজ ো এর শেয়োর  ত শ োটি টো োর ?<br>(a) 0.5 b) 1 c) 2.7 d)2.5<br><br>|2.5 Crore<br><br>|

|25<br><br>|ডপড ডিডির ৪০০ শ ডি লোইন  ত ড ডি ?<br>(a) 300 b)150  c) 200 d) 950 Circuit km<br><br>|2162<br><br>|

|26<br>|স্বোধীন িোাংলোজেজে িঙ্গিন্ধু  ত শিেঃ ওয়োট পোরিোনডি  ডিদ্যুৎ শ ন্দ্র স্থোপন  রজত<br>শেজয়ডিজলন?<br>(a) 50 b) 100 c) 200 d) 300<br>|200MW<br>|

|27<br><br>|স্বোধীন িোাংলোজেজে ডিডপডিডি  ত শিেঃওয়োট ডিদ্যুৎ প্রথি েোলু  জরডিল ?<br>a) 300MW b) 400MW c) 500MW d) 600MW<br><br>|600MW<br><br>|

|28<br><br>|`আহোন মবিশল সকান োশল প্রেম সুইে বিশপ বিদ্যুৎ োলু করা হয় ?`<br>(a) 1900 b) 1901 c) 1902 d) 1904<br><br>|1901<br><br>|

|29<br>|DESCO`কত োশল সেয়ার িািাশরর অন্তিুবক্ত হয় ?`<br>|২০০৬<br>|

|30<br><br>|DPDCএর িোি শেেন ৩৩/১১ শ ডি পর্যোজর়্ে ক্ষিতো শিোট  ত  MVA?<br><br>|4361MVA<br><br>|

|31<br><br>|REB  Pre Paid Meterব্যব্হার করলে কত পিলব্ট দেয়?<br><br>|০১%<br><br>|

|32<br><br>|পব্দ্**য**ৎ সুপব্ধা প্রাপ্ত জনসংখ্যা কত?<br><br>|১০০%<br><br>|

|33<br><br>|SREDAকত সালে প্রপতপিত হয়?<br><br>|২০১২<br><br>|

|34<br><br>|Which country generates highest power by using hydro fuel ?<br>Nuclear=USA<br><br>|China<br><br>|

|35<br><br>|What is the generation capacity of REB ?<br><br>|225.55MW<br><br>|

|36<br><br>|Which year WZPDCL established ?<br><br>|2002<br><br>|

|37<br><br>|What is the number of transformer of PGCB ?<br><br>||

|38<br><br><br>|DPDC substation number  ?<br><br><br>|73<br><br><br>|

|39<br><br>|Sreda Energy Efficiency and Conservation Promotion Financing<br>Project Which year duration ?<br>(a) 2019-2023 (b) 2021-2025  (c) 2022-2029 (d)2025-2030<br><br>||

|40<br><br>|Which year nawab ahsanullah house was established a generator ?<br><br>|1901<br><br>|

|41<br><br>|How much electricity is generated from Hydro ?<br><br>|1%<br><br>|

|42<br>|What is the total power plant of Bangladesh ?-<br>|151<br>|

|43<br><br>|<br>What is the dispatch capacity of REB ?<br><br>|17535 MVA<br><br>|

|44<br><br>|What is the capacity of DPDC distribution transformer?<br><br>|4361 MVA<br><br>|

|45<br>|Whatis thenumberof DESCOPrepaidMeter?<br>|671781<br>|

`প ্র ককৌশলী সমাো ঃ মানিক উনিি` [167]  

```

পাওয়ার সেক্টর

```

|46<br>|The second unit of NPCBL project will be completed within how many<br>weeks ?<br>|98 months<br>|

|---|---|---|

|47<br><br>|DESCO get registration from BERC:<br><br>|2007<br><br><br>|

|48<br><br>|Total length of Transmission and Distribution line under DPDC:<br><br>|5916 km<br><br><br>|

|49<br>|BREB system loss in Nov 2023:<br>|8.56%<br><br>|

|50<br><br>|PDB owned % of shares of PGCB:<br><br>|84.64%<br><br>|

|51<br>|According to SREDA Wind shared power<br>on grid:<br>|0.9MW<br>|

|52<br>|Total cost (Taka) of Rampal Power plant:<br>|16000 Crore<br>|

|53<br>|Bangladesh receives imported power from Tripura:<br>|160MW<br>|

|54<br>|Utilization factor of Rooppur Nuclear<br>Power plant:<br>|92%<br>|

|55<br><br>|Public owned Power Plants must be share % of generation in<br>Bangladesh:<br><br>|55%<br>|

|56<br><br><br>|দকানcompany power distributeকলর?<br>(i) PDB ii) NESCO iii) DPDC iv) all of the above<br><br><br>|NESCO<br>|

|57<br><br>|According to SREDA, what is the percentage of wind power<br>connected on grid?<br><br>|0.9 MW|

|58<br><br>|`রামপাল নবদ্`**`য`**`ৎককে এর নিমতাি বযায় কত সকানট টাকা?`<br><br>|১৬০০০ দকাটি টাকা<br>|

|59<br>|What percent of share from BPDB  to PGCB ?<br>(a) 85.6% (b) 84.64% (c) 86.9% (d) 90.1%<br>|84.64%<br>|

|60<br>|M¨v‡mi GKKNm<sup>-3</sup>ej‡Z †evSvq-<br>K.Newton Cubic Meter<br>L.Normal Cubic Meter<br>M.Natural Cubic Meter<br>N.Non-pressurized Cubic Meter<br>|DËi t L<br>|

|61<br><br>|evsjv‡`‡ki we`y¨r mieivnFrequencyn‡”Q<br>K.60 Hertz<br>L.50 Hertz<br>M.51 Hertz<br>N.49 Hertz<br><br>|DËi t L<br><br><br>|

|62<br>|evsjv‡`‡ki †Kvb AÂ‡j eZ©gv‡b m‡e©v”P we`y¨r Drcv`b nq?<br>K. c~e©vÂ‡j<br>L. DËivÂ‡j<br>M. `wÿYvÂ‡j<br>N. cwðgvÂ‡j<br>|DËi t K<br><br><br>|

|63<br>|evsjv‡`‡ki †Kvb AÂ‡j eZ©gv‡b m‡e©v”P we`y¨r Drcv`b nq?<br>K. c~e©vÂ‡j<br>L. DËivÂ‡j<br>M. `wÿYvÂ‡j<br>N. cwðgvÂ‡j<br>|DËi t K<br><br><br>|

|64<br><br>|evsjv‡`‡k wMÖ‡W eZ©gvb e¨envi‡hvM¨ we`y¨r Drcv`b ÿgZv cÖvq-<br>K.16000 MW<br>L.12 GW<br>M.30 GW<br>N.16000 KW<br><br>|DËi t K<br><br><br>|

|65<br><br>|†KvbwUSubstation?<br>K.33/11 KV<br>L.11/132 KV<br>M.132/11 KV<br>N.11/0.4 KV<br><br>|DËi t M<br><br>|

|66<br>a|BPDP†_‡K †K we`y¨r wK‡b bv?<br>K.NESCO<br>L.PGCB|DËi t L|

`প ্র ককৌশলী সমাো ঃ মানিক উনিি` ______=ZFfj 

```

পাওয়ার সেক্টর

```

||M.BREB<br>N.DPDC<br>||

|---|---|---|

|67<br><br>|ev®ú we`y¨r †K‡›`ª cÖvBg gyfvi wnmv‡e e¨eüZ nq-<br>K. óxg BwÄb, M¨vm UvievBb<br>L. óxg UvievBb, M¨vm UvievBb<br>M. óxg BwÄb,AvBwm BwÄb<br>N. óxg BwÄb,óxg UvievBb<br><br>|DËi t N<br> <br><br><br><br>|

|68<br>|PGCBn‡jv-<br>K. ¯^vaxb ms¯’v<br>L.BPDBGi wbqš¿Yvaxb GKwU †Kv¤úvbx<br>M. ¯^vqZ¡kvwmZ ms¯’v<br>N. AvavmiKvwi †Kv¤úvbx<br>|DËi t M<br><br><br>|

|69<br>|jvB‡b D”P †fv‡ëR cÖ‡qvM nq †Kb?<br>K. A_© mvkÖvqv‡_©<br>L. jvB‡b we`y¨r AcPq Kgv‡bvi Rb¨<br>M. UvIqv‡ii RvqMv Kgv‡bvi Rb¨<br>N. UvIqv‡ii msL¨v Kgv‡bvi Rb¨<br>|DËi t L<br><br><br>|

|70<br>|‡eBR †jvW cvIqvi cøv›U wn‡m‡e e¨eüZ nq-<br>K. óxg UvievBb cvIqvi cøv›U<br>L. DBÛ wgj cvIqvi cøv›U<br>M. M¨vm UvievBb cvIqvi cøv›U<br>N. wW‡Rj cvIqvi cøv›U<br>|DËi t K<br><br><br>|

|71<br><br><br>|What is the single phase voltage in Bangladesh?<br>K.230 V<br>L.250 V<br>M.400 V<br>N.440 V<br><br><br>|DËi t K<br> <br><br><br><br><br><br>|

|72<br><br>|Which has highest value of calorific?<br>K.LPG<br>L.CNG<br>M.Hydrogen<br>N.Petrol<br><br>|DËi t M<br><br><br><br>|

|73<br><br>|evsjv‡`k †Kvb R¦vjvwb Avg`vwb K‡i gRy` ivL‡e?<br>Ans :LNG<br><br>||

|74<br>|The highest transmission voltage used in Bangladesh-<br>K.400 KV<br>L.765 KV<br>M.230 KV<br>N.132 KV<br>|DËi t K<br> <br><br>|

|75<br>|A steam power station requires space-<br>K.equal to diesel power station<br>L.more than diesel power station<br>M.less than diesel power station<br>N.none of the above<br>|DËi t K<br>|

|76|K·evRv‡ii g‡nkLvjx gvZvievwo‡Z wK ai‡bi we`y¨r †K›`ª ¯’vwcZ n‡e?<br>K. Kqjv wfwËK Zvc we`y¨r †K›`ª<br>L. cvigvYweK we`y¨r †K›`ª<br>M.HFOcvIqvi cøv›U<br>N. †KvbwUB bq|DËi t K<br>|

|77<br>|gvZvievwo Zvc we`y¨r †K›`ª KZ †gMvIqv‡Ui?<br>K.1200 MW<br>L.600 MW<br>M.1320 MW<br>N.650 MW<br>|DËi t K<br><br>|

|78<br>|we‡k^i e„nËg fvmgvb †mŠiwe`y¨r Drcv`b †K›`ª ˆZwi K‡i‡Q †Kvb †`k?<br>K. ivwkqv<br>L. Pxb<br>M. fviZ<br>N. hy³ivóª<br>|DËi t L<br><br><br>|

|79<br><br><br>|evsjv‡`‡k wbg©vYvaxb GKgvÎ cvigvYweK we`y¨r †K›`ª †Kvb †Rjvq Aew¯’Z?<br>K. Kzwóqv<br>L. ewikvj<br>M. cvebv<br>N. ivRkvnx<br><br><br>|DËi t M<br><br><br><br>|

|80<br><br><br>|iƒccyi cvigvYweK we`y¨r †K‡›`ªi Drcv`b ÿgZv KZ?<br>K.1200 MW<br>L.2400 GW<br>M.1200 GW<br>N.2400 MW<br>©   y<br><br><br>|DËi t N<br><br><br><br>|

|81<br>|evsjv‡`‡k m‡e©v”P KZ †gMvIqvU we`y¨r Drcv`b nq?<br>|DËi t29251MW<br>|

80 iƒccyi cvigvYweK we`y¨r †K‡›`ªi Drcv`b ÿgZv KZ? K. 1200 MW L. 2400 GW M. 1200 GW N. 2400 MW 81 evsjv‡`‡k m‡e©v”P KZ †gMvIqvU we`y¨r Drcv`b nq? `প ্র ককৌশলী সমাো ঃ মানিক উনিি` ee  | 

```

পাওয়ার সেক্টর

```

||K.1100 MW<br>L.10000 MW||

|---|---|---|

||M.12893 MW<br>N.9000 MW||

|82|evsjv‡`k KZ †gMvIqvU we`y¨r fviZ †_‡K Avg`vbx K‡i?<br>K.1160 MW<br>L.500 MW<br>M.660 MW<br>N.1000 MW|DËi t2656MW<br>2656-1160 = 1496 MW<br>from Adani|

|83|cvqiv Zvc we`y¨r †K›`ª KZ †gMvIqvU ÿgZv m¤úbœ?<br>K. 1200 †gMvIqvU<br>L. 1320 †gMvIqvU<br>M. 660 †gMvIqvU<br>N. 1160 †gMvIqvU|DËi t L|

|84|wb‡Pi †KvbwU †Kej we`y¨r Drcv`‡bi D‡Ï‡k¨?<br>K.BPDP<br>L.NWPGCL<br>M.PGCB<br>N.BREB|DËi t L|

|85|iƒccyi wbDwK¬qvi cvIqvi cøv›U K‡e Drcv`‡b hv‡e? (m~ÎNPCBL Website)<br>K.2023<br>L.2022<br>M.2024<br>N.2025|DËi t2023|

|86|iƒccyi cvigvYweK we`y¨r †K›`ª KZ †gMvIqvU we`y¨r Drcbœ Ki‡e?<br>K.1320 MW<br>L.2400 MW<br>M.1200 MW<br>N.1160 MW|DËi t L|

|87|Transmission linewK‡mi ˆZwi nq?<br>K.Aluminium<br>L.Copper<br>M.Silver<br>N.Iron<br>|DËi t K<br>|

|88|Black outK‡e msMwVZ n‡qwQj?<br>K. 2014<br>L. 2015|DËi t K|

||M. 2017<br>N. 2016||

|89|What is system loss?<br>K.Power used in power plant<br>L.Power that does not include in billing<br>M.All of this<br>N.None of this|DËi t L|

|90|What is the unit of electricity bill?<br>K.KW<br>L.Kwh<br>M.KV<br>N.KVA|DËi t L|

|91|২০২২mv‡jDESCOGjvKv‡Zpick demandwQj AvbygvwbK-<br>K.1700 MW<br>L.500 MW<br>M.1500 MW<br>N.1000 MW|DËi t১৪৭৫|

|92|jvBd jvBb we`y¨Zvqb †h †ÿ‡Î cÖ‡hvR¨?<br>K.1-50 unitGi MÖvnK L.1-75 unitGi MÖvnK<br>M.50 unitGi Dc‡ii MÖvnK<br>N. ‡h †Kvb we`y¨r MÖvnK|DËi t K|

|93|Avcbvi evmv‡Z GK‡dR †fvë n‡”Q-<br>K.400 volts<br>L.430 volts<br>M.230 volts<br>N.250 volts|DËi t M|

|94|Avgv‡`i †`‡k we`y¨r Drcv`‡b cÖavb †h R¦vjvwb e¨envi nq?<br>K.Nuclear<br>L.Coal<br>M.Gas<br>N.None|DËi t M|

`প ্র ককৌশলী সমাো ঃ মানিক উনিি` ee | 

```

পাওয়ার সেক্টর

```

|95|we`y¨r weZiY †cvj hv w`‡q ˆZwi nq bv|DËi t N|

|---|---|---|

||K.Steel<br>L.Wood<br>M.Concrete<br>N.Cast Iron(XvjvB<br>†jvnv)||

|96|Avgv‡`i †`‡k we`y¨r GiFrequency-<br>K.50 Hz<br>L.60 Hz<br>M.45 Hz<br>N.55 Hz|DËi t K|

|97|DESCOhvi †_‡K wey`¨r wK‡b?<br>K.BPDB<br>L.PGCB<br>M.REB<br>N.Ghorasal Power Plant|DËi t K|

|98|‡KvbwUDESCOGjvKv‡Z bq?<br>K.Nikunja<br>L.Kallyanpur<br>M.Purbachal<br>N.Tejgaon|DËi t N|

|99|‡KvbwU D”P †jvW †bq?<br>K.AC<br>L.Computer<br>M.LED lamp<br>N.Calculator|DËi t N|

|100|‰e`y¨wZK kw³i GKK wK?|DËi t L|

||K.Kw<br>L.Kwh<br>M.Kva<br>N.Kv||

|101|evsjv‡`‡ki we`y¨r weZiYKvix cÖwZôv‡bi †gvU msL¨v?<br>K. 4<br>L. 5<br>M. 6<br>N. 2|DËi t M|

|102|Which one of the following is not situated in a substation?<br>K.Generator<br>L.Transformer<br>M.High Voltage Cable<br>N.Switch Gear|DËi t K|

|103|evsjv‡`‡k GKgvÎ cvigvYweK we`y¨r †K›`ª †Kv_vq?<br>K.Bheramara<br>L.Payra|DËi t M|

||M.Ruppur<br>N.Baghaban||

|104|evsjv‡`‡ki GKgvÎ Rj we`y¨r †K‡›`ªi †gvU Drcv`b ÿgZv-<br>K.2×50 MW<br>L.180 MW<br>M.230 MW<br>N.250 MW|DËi t M|

|105|gvZvievwo we`y¨r †K‡›`ª †h R¦vjvwb e¨envi n‡e?<br>K.LNG<br>L.Diesel<br>M.HFO<br>N.Coal|DËi t N|

|106|‡Kvb we`y¨r †K‡›`ª Avg`vwbK…Z Kqjv e¨eüZ n‡e bv?<br>K.Barapukuria<br>L.Meghnaghat<br>M.Rampal<br>N.Matarbari|DËi t K|

|107|TransformerGi KvR wK?<br>K. we`y¨r Drcv`b<br>L. Kv‡i›U evov‡bv<br>M. †fv‡ë‡Ri cwieZ©b Kiv N. ˆe`y¨wZK kw³i cwieZ©b|DËi t M|

|108|KLb cy‡iv wm‡÷g e¨vcxLoad shedKivi cÖ‡qvRb nq bv?<br>K. we`y¨r Drcv`b Pvwn`vi Zzjbvq †eknx n‡j<br>L. weZiY jvBb ÎæwU n‡j<br>M. †fv‡ëR †ewk K‡g †M‡j N. †KvbwU bq|DËi t K|

`প ্র ককৌশলী সমাো ঃ মানিক উনিি` ee | 

```

পাওয়ার সেক্টর

```

|109|GKwU56BwÂcelling fanAvbygvwbK †h cwigvY we`y¨r e¨q K‡i?<br>K.75 W<br>L.60W<br>M.56 W<br>N.130 W|DËi t K|

|---|---|---|

|110|Avgv‡`i †`‡k kni GjvKv‡ZRoof top photo voltaic system<br>K. mivmwi e¨vUvwi‡Z<br>L. fe‡bi we`y¨r evmev‡i M. wbKU¯’ UªvÝdg©v‡i<br>N. †KvbwU bq|DËi t K|

|111|evsjv‡`‡k wbg©vYvaxb cvigvYweK we`y¨r †K‡›`ªi †gvU Drcv`b ÿgZv n‡e?<br>K.1200 MW<br>L.2×1200 MW<br>M.2200 MW<br>N.1000 MW|DËi t L|

|112|DESCO has no-<br>K.Power plant<br>L.Distribution Zone<br>M.Substation<br>N.Distribute Power in Dhaka Zone|DËi t K|

|113|Which one is not a protection device?<br>K.Isolator<br>L.Distribution<br>M.Switch<br>N.Relay|DËi t L|

|114|Which one is the primary fuel of Duel-fuel power plant?<br>K.Gas<br>L.Steam<br>M.Diesel<br>N.Coal|DËi t K|

|115|evsjv‡`‡k me‡P‡q eo we`y¨r †K›`ª †KvbwU?<br>K.NWPGCL<br>L.APSCL<br>M.RPCL<br>N.EGCB|DËi t L|

|116|Load-shedding is done in-<br>K.Nearest Pole<br>L.Substation end<br>M.Consumer end<br>N.None|DËi t L|

|117|Which one is prime mover of generator?<br>K.Engine<br>L.Steam turbine<br>M.Gas turbine<br>N.All of these|DËi t N|

|118|‡KvbwU Zvi wn‡m‡e e¨eüZ nq bv?<br>K.Copper<br>L.Aluminium<br>M.Steel<br>N.Aluminium Alloy|DËi t M|

|119|Which type of Meter is not used in Bangladesh.<br>K.Digital Meter<br>L.Prepaid Meter<br>M.Post-Paid Meter<br>N.Dies Type Meter|DËi t N|

|120|Transformer-G †Zj †Kb e¨envi Kiv nq?<br>K. VvÛv Kivi Rb¨<br>L. Zvc Kgv‡bvi Rb¨<br>M. Bbmy‡jkb wn‡m‡e KvR K‡i<br>N. me KqwU|DËi t N|

|121|Duralumin is an alloy of copper and...<br>K.Steel<br>L.Iron|DËi t M|

||M.Aluminium<br>N.Cast Iron||

|122|‡KvbwU Rxevk¥ R¦vjvwb bq?<br>K. †mvjvi GbvwR©<br>L. wRI-_vg©vj GbvwR©<br>M. I‡qf GbvwR©<br>N. me KqwU|DËi t N|

|123|msKi avZz Kvmvi Dcv`vb wK wK?<br>K. Zvgv I ‡jvnv<br>L. Zvgv I wUb|DËi t L|

`প ্র ককৌশলী সমাো ঃ মানিক উনিি` ee | 

```

পাওয়ার সেক্টর

```

||M. Zvgv I `¯Ív<br>N. Zvgv I wb‡Kj<br>||

|---|---|---|

|124<br><br><br>|iƒccyi cvigvYweK we`y¨r †K›`ª †Kvb wefv‡M?<br>K. XvKv<br>L. ivRkvnx<br>M. Lyjbv<br>N. ewikvj<br><br><br>|DËi t L<br> <br><br><br><br>|

|125<br>|Duralumin is an alloy of copper and ...<br>K.Steel<br>L.Iron<br>M.Cast Iron<br>N.Aluminium<br>|DËi t N<br><br><br>|

|126<br>|DPDCGjvKvi evwn‡i †KvbwU?<br>K. avbgwÛ<br>L. dZzjøv<br>~©<br>|DËi t N<br><br><br>|

||M. bvivqbMÄ<br>N. c~e©vPj<br>||

|127<br>|evsjv‡`‡ki ¯^vqZ¡kvwmZ we`y¨r weZiY ms¯’v †gvU KqwU?<br>K. 2wU<br>L. 6wU<br>M. 3 wU<br>N. 5 wU<br>|DËi t N<br><br><br><br>|

|128<br><br>|gvwmK KZ GKK (Kwh)ch©šÍ we`y¨r LiP Ki‡jLife LineMÖvnK wnmv‡e ejv nq?<br>K. 10<br>L. 30<br>M. 50<br>N. 75<br><br>|DËi t M<br><br><br><br>|

|129<br><br>|Life LineMÖvn‡Ki Rb¨ GKK cÖwZ we`y¨‡Zi bZzb †iU n‡”Q KZ UvKv?<br>K. 3.50 UvKv<br>L. 3.57 UvKv<br>M. 4.35 UvKv<br>N. 3.75 UvKv<br>m~Î : LyPiv bZzb we`y¨r g~j¨nvi cÖKvwkZ 1 gvP© 2020 wLª.<br><br>|DËi t N<br><br><br><br>|

|130<br>|DPDC†gvU MÖvnK msL¨v cÖvq KZ?<br>K. 11 jvL<br>L. 13 jvL<br>M. 15 jvL<br>N. 10.5 jvL<br>|DËi t**১৭,০৮৯৫৯**<br><br><br>|

|131<br>|evsjv‡`‡kiSupply Frequencyn‡”Q-<br>K.550 Hz<br>L.60 Hz<br>M.55 Hz<br>N.50 Hz<br>|DËi t N<br><br><br>|

|132<br>|AvevwmK d¨vb, evwZ BZ¨vw`‡Z KZ †fvë e¨envi Kiv nq?<br>K. 230 †fvë<br>L. 400 †fvë<br>M. 415 †fvë<br>N. 110 †fvë<br>|DËi t K<br><br><br>|

|133<br>|Over head lineGConductorwnmv‡e e¨envi Kiv nq?<br>K.Aluminium<br>L.Copper<br>M.Steel<br>N.Brass<br>|DËi t K<br><br><br>|

|134<br><br>|1wU 1 UbAC1 N›Uv Pvjy _vK‡j KZ we`y¨r LiP n‡e?<br>K.1 Khw<br>L.1.5 Khw<br>M.2 Khw<br>N.3 Khw<br><br>|DËi t N<br><br><br><br>|

|135<br>|DPDCGjvKvqPeak demandcÖvq<br>K.1600 MW<br>L.1000 MW<br>M.2000 MW<br>N.1400 MW<br>|DËi t K<br>**১৮০৬ মেগাওযাট**<br><br>|

|136<br>|DPDC has no-<br>K.Power plant<br>L.Substation<br>M.Distribution<br>N.Distribution zone in Dhaka and Narayanganj.<br>|DËi t K<br>|

|137<br><br><br>|‡KvbwU wWwcwWwm GjvKvi evwn‡i?<br>K. avbgwÛ<br>L. †ZRMuvI<br>M. igbv<br>N. c~e©vPj<br><br><br>|DËi t N<br><br><br>|

|138<br>|wWwcwWwmi m‡e©v”P wMÖW mve‡÷kb n‡jv-<br>|DËi t K<br>|

||K. 132/33/11 †K.wf<br>L. 132/11 †K.wf<br>||

`প ্র ককৌশলী সমাো ঃ মানিক উনিি`  | 

```

পাওয়ার সেক্টর

```

||M. 33/11 †K.wf<br>N. 66/11 †K.wf||

|---|---|---|

|139|‡jvW †kwWs †Kv_vq nq?||

||K. MÖvnK cÖv‡šÍ<br>L. †cv‡ji Kv‡Q<br>M. mve‡÷kb cÖv‡šÍ<br>N. †KvbwU bq<br>DËi t M||

|140|evsjv‡`‡ki KZ kZvsk gvbyl we`y¨r myweav cv‡”Q?<br>K. 95%<br>L. 96%<br>M. 97%<br>N. 98%|DËi t**১০০%**|

|141|‡mvjvi c¨v‡bj †mŠi †_‡K †Kvb kw³ MÖnY K‡i?<br>K. B‡jKUªb<br>L. †cÖvUb<br>M. wbDUb<br>N. †dvUb|DËi t N|

|142|wb‡Pi †KvbwU Rxevk¥ R¦vjvwb bq?<br>K. †mvjvi GbvwR©<br>L. wRI-_vg©vj GbvwR©<br>M. I‡qf GbvwR©<br>N. me KqwU|DËi t L|

|143|msKi avZz Kvmvi Dcv`vb Kx?<br>K. Zvgv I wUb<br>L. Zvgv I `¯Ív<br>M. Zvgv I †jvnv<br>N. Zvgv I wb‡Kj|DËi t K|

|144|iƒccyi cvigvYweK we`y¨r †K›`ª †Kv_vq Aew¯’Z?<br>K. cvebv<br>L. Kzwóqv<br>M. ivRkvnx<br>N. PÆMÖvg|DËi t K|

|145|The Gas usually Filled in the electric bulb is-<br>K.Hydrogen<br>L.Oxygen<br>M.Nitrogen<br>N.Carbondioxide|DËi t M|

|146|The hydroelectric power plant in kaptai was established in the year?<br>K.1962<br>L.1972<br>M.1961<br>N.1964|DËi t K|

|147|The largest hydroelectric power station in the world is-<br>K.Three georges<br>L.Kaptai<br>M.Ashwan<br>N.Niagara fall|DËi t K|

|148|The annual rate of increase of electricity price is 10%, if the rate of the<br>2020 is 10/kwh, what was the rate of 2018?<br>K.TK 8/kwh<br>L.TK 8.2644/kwh<br>M.TK 8.6745/kwh|DËi t L|

|149|The present distribution loss is 8%. The distribution loss will be<br>decreased.<br>K. If the diameter of the distribution conductor is increased.<br>L.If the diameter of the distribution conductor is decreased.<br>M.If the capacitor is added to the distribution system.<br>e¨vL¨v tPower Factor improvementKivi Rb¨ Avgiv jvB‡b K¨vcvwmUi<br>ev K¨vcvwUi e¨vswKs e¨envi Kwi| d‡j wm‡÷g DbœZ nq| ZvB mwVK DËi(M)||DËi t M|

|150|The largest power plant of Bangladesh?<br>K.Shiddhirganj<br>L.Ashuganj<br>M.Ghorashal|DËi t L|

|151|The peak demand of Bangladesh for the year২০২২/২৩-<br>K.12893 mw<br>ঘ.15648 MW<br>L.10563 mw<br>M.90825 MW|DËi t১৫৬৪৮|

`প ্র ককৌশলী সমাো ঃ মানিক উনিি` ee | 

```

পাওয়ার সেক্টর

```

|152|Which fuel is used most for generating electricity in BD?<br>K.Furnace oil<br>L.Coal<br>M.Natural Gas<br>N.Diesel|DËi t M|

|---|---|---|

|153|Suppose a man uses a water heater that consumes 600 W electricity. If<br>he utilizes it for 10 minutes daily. Find out the monthly electricity<br>consumption for the water heater.<br>K.30 Units<br>L.60 Units<br>M.3 Units<br>N.300 Units<br>e¨vL¨vtEnergy for one month𝐸[NESCO AE 18 ] =<br>𝑃×𝑡×30<br>1000<br>𝑘𝑤ℎ=<br>600×<sup>10</sup><br>60<br>30<br>1000<br>= 3 𝑘𝑤ℎ<br>1 Kwh = 1 Unit so 3 Kwh = 3 Units.|DËi t M|

|154<br>|The total length of electricity distribution line controlled by NESCO is<br>approximately.<br>K.10500 km<br>L.19131 km<br>M.19882 km<br>N.1050 km<br>e¨vL¨v t G mKj Z_¨ cwieZ©bkxj| ZvB Avc‡WU †R‡b ivLvi Rb¨ cixÿvi Av‡M<br>NESCO Website‡`‡L ivL‡Z n‡e| †mB mgq DËiwU wQj19131 kmGLb<br>Zv cwieZ©b n‡Z cv‡i|<br>|DËi t26402.00 Km<br>|

|155<br>|Which countries contribution the most to green house gas emission?<br>K.China and United States<br>L.India and China<br>M.China and RussiaN.USA and UK<br>|DËi t K<br>|

|156<br>|The important Condition of the parallel operation transformer is<br>K.Polarity must be same<br>L.Polarity must be opposite<br>M.The load must be higher than the capacity of the existing<br>transformer<br>|DËi t K<br>|

|157<br><br>|With the increase of temperature, the resistance of the semiconductor.<br>K.Increase<br>L.Decreases<br>M.REmains constant<br><br>|DËi t L<br><br><br>|

|158<br><br>|evsjv‡`‡ki m‡e©v”P UªvÝwgkb jvBb KZ †fv‡ëR?<br>K.765 /KV<br>L.400KV<br>M.232 KV<br>N.132 KV<br><br>|DËi t L<br><br><br><br>|

|159<br><br>|BPDBK‡e MwVZ nq?<br>K.1972<br>L.1973<br>M.1974<br>N.1977<br><br>|DËi t K<br><br><br><br><br>|

|160<br><br>|The largest coal power plant of Bangladesh.<br><br>|Ans: Payra 1320 MW<br>Thermal Power Plant.<br><br><br><br>|

|161<br><br>|eZ©gv‡b evsjv‡`‡k gv_vwcQz we`y¨r Drcv`b-<br>K.512 Kwh<br>L.550 Kwh<br>M.510 Kwh<br>N.560 Kwh<br><br>|DËi t**৬০২ kwh**<br><br><br>|

|162<br><br>|iƒccyi cvigvYweK we`y¨r †K›`ªwU Aew¯’Z?<br>K. cvebv<br>L. Ck^i`x<br>M. cvKkx<br>N. Pinvmvbcyi<br><br>|DËi t L<br><br>|

`প ্র ককৌশলী সমাো ঃ মানিক উনিি` [175]  

```

পাওয়ার সেক্টর

```

|163<br><br>|wb‡Pi †KvbwU bevqb‡hvM¨ kw³i Drm bs?<br>K. evqykw³<br>L. †mŠikw³<br>M. cÖvK…wZK M¨vm<br>N. †Rvqvi fvUv<br>e¨vL¨v t bevqb‡hvM¨ R¦vjvwbt †h mKj R¦vjvwb cÖK…wZ‡Z †kl nq bv Zv‡K<br>bevqb‡hvM¨ R¦vjvwb e‡j| †hgb- evqykw³,†mŠikw³,†Rvqvi fvUv|<br>Ö…  Ö<br><br>|DËi t M<br> <br><br>|

|---|---|---|

|164<br><br>|cÖvK…wZK M¨v‡mi cÖavb Dcv`vb wK?<br>K. A¨v‡gvwbqv<br>L. B‡_b<br>M. nvB‡Wªv‡Rb<br>N. wg‡_b<br>‘ ’’<br><br>|DËi t N<br> <br><br>|

|165<br>|‡Kvb e¯‘wUi w¯’wZ¯’vcKZv Kg?<br>K. †mvbv<br>L. Zvgv<br>M. ivevi<br>N. A¨vjywgwbqvg<br>|DËi t M<br>|

|166<br><br>|‡Kvb e¯‘wUi w¯’wZ¯’vcKZv †ekx?<br>K. ivevi<br>L. KbwµU<br>M. B¯úvZ<br>N. †jvnv<br><br>|DËi t M<br><br>|

|167<br><br>|evsjv‡`k fviZ †hŠ_ we`y¨r mÂvjb †K‡›`ªi gva¨‡g †h cwigvY we`y¨r evsjv‡`‡kInput<br>nq-<br>K.500 MW<br>L.1160 MW<br>M.1000 MW<br>N.660 MW<br>y  Ö ¦<br><br>|DËi t 2656<br>MW<br><br>|

|168<br>|evsjv‡`‡ki we`y¨r Drcv`‡bi cÖavb R¦vjvwb-<br>K. †Zj<br>L. M¨vm<br>M. Kqjv<br>N. †mŠikw³<br>|DËi t L<br>|

|169<br>|KvßvB W¨vg †Kvb †Rjvq Aew¯’Z?<br>K. PÆMÖvg<br>L. K·evRvi<br>M. iv½vgvwU<br>N. ev›`ievb<br>|DËi t M<br>|

|170<br><br>|M¨vjfvbvBwRs Gi Kv‡R e¨eüZ nq †Kvb avZz?<br>K. Kcvi<br>L. wRsK<br>M. A¨vjywgwbqvg<br>N. wmjfvi<br><br>|DËi t L<br><br>|

|171<br><br>|cÙv †mZz cÖK‡í g~j †mZz wbg©v‡Yi Kvh©v‡`k cÖvß †Kv¤úvbx †KvbwU?<br>K. Pvqbv †gRi BwÄwbqvwis L. Gm.Gb.wR jvfvwjb<br>M. û›`vB<br>N. Rvcvb Bbd«v÷ªvKPvi †W‡fjc‡g›U †Kvt<br><br>|DËi t K<br><br>|

|172<br>|cvIqvi d¨v±i wK?<br>|DËi t N<br>|

||K.𝐶𝑜𝑠𝜃=<br>𝑅<br>𝑍<br>L.𝑆𝑖𝑛𝜃=<br>𝑅<br>𝑍<br>||

||M.𝐶𝑜𝑠𝜃=<br>𝐾𝑊<br>𝐾𝑉𝐴<br>N. K I L DfqB<br>||

|173<br><br>|miKvwi we`y¨r †K›`ª-<br>K. †Nvovkvj Zvc we`y¨r †K›`ª<br>L. eocyKzwiqv Zvc we`y¨r †K›`ª<br>M. KvßvB cvwb we`y¨r †K›`ª N. †fovgviv I ivDRvb Zvc we`y¨r †K›`ª<br>O. Dc‡ii me KqwU<br><br>|DËi t O<br><br>|

|174<br><br>|evsjv‡`‡ki cvigvYweK we`y¨r †K›`ª †Kv_vq Aew¯’Z?<br>K. iƒccyi, cvebv<br>L. Kjvcvov, cUzqvLvjx<br>M. †fovgviv,Kzwóqv   N. gvZvievwo,K·evRvi<br><br>|DËi t K<br><br>|

|175<br><br>|eZ©gv‡b †`‡ki we`y¨r myweav cÖvß Rb‡Mvôx KZ kZvsk? (Avc‡WU-08 A‡±vei 2020 Bs)<br>K. 96<br>L. 97<br>M. 98<br>N. 99<br><br>|DËi t১০০%<br><br>|

||e¨vL¨v t Gme Z_¨ cwieZ©bkxj cixÿvi Av‡M Aek¨BPowercellGi I‡qemvBU †`Lv<br>DwPZ|www.powercell.gov.bd/†mB mgq cvIqvi †m±‡ii cÖkœ Kg nZ|<br>||

```

পাওয়ার সেক্টর

```

|176<br>|WZPDCLGKwU-<br>K. weZiY †Kv¤úvwb L.Transmission Company<br>M. †Rbv‡ikb †Kv¤úvbx<br>N. me¸‡jv<br>|DËi t K<br><br>|

|---|---|---|

|177<br><br>|‡`‡ki cÖ_g †emiKvwi we`y¨r †K›`ª †Kv_vq Aew¯’Z?<br>K. Lyjbv<br>L. PÆMÖvg<br>M. Kzwóqv<br>N. XvKv<br>© Ö<br><br>|DËi t K<br><br><br>|

|178<br>|WZPDCLGi eZ©gvb MÖvnK msL¨v-<br>K. 8 jÿ<br>L. 9 jÿ<br>M. 10 jÿ<br>N. cÖvq 11 jÿ<br>|DËi t**জন **<br><br>|

|179<br><br>|evsjv‡`‡ki GKgvÎ Rjwe`y¨r †K›`ª †Kv_vq Aew¯’Z?<br>K. ev›`ievb<br>L. iv½vgvwU<br>M. PÆMÖvg<br>N. K·evRvi<br><br>|DËi t ১৪ েক্ষ ৫৭ হাজার ৩৬৮<br>জন<br><br>|

|180<br>|‰e`y¨wZK ev‡j¦i wdjv‡g›U wK w`‡q ˆZwi nq?<br>K. U¨vs‡÷b<br>L. Kcvi<br>M. A¨vjywgwbqvg<br>N. K¨vWwgqvg<br>|DËi t K<br><br>|

|181<br><br>|evsjv‡`‡k e¨eüZFrequency-<br>K.50 Hz<br>L.55 Hz<br>M.45 Hz<br>N.52 Hz<br><br>|DËi t K<br><br><br><br>|

|182<br><br>|GKwU 100 †K.wf.G 5% weq¨vKU¨vÝ wewkó cvIqviTransformerGi2000†K.wf.G<br>†em| wiq¨vKU¨vÝ KZ?<br>K.10%<br>L.20%<br>M.8%N.5%<br><br>|<br><br>|

|183<br>|evsjv‡`‡ki gv_vwcQz we`y¨r Drcv`b-<br>K.500 Kwh<br>L.512 Kwh<br>M.490 Kwh<br>N.520 Kwh<br>|DËi t৬০২<br><br><br>|

|184<br>|we`y¨‡Zi me©‡kl gvóvicø¨vb Kiv nq-<br>K. 2016<br>L. 2014<br>M. 2017<br>N. 2015<br>Ö   y<br>|DËi t K<br><br><br>|

|185<br><br>|‡Kvb cÖwZôvb GKB mv‡_ we`y¨r Drcv`b I weZiY K‡i?<br>K.NWPGCL<br>L.BPDP<br>M.BREB<br>N.WZPDCL<br><br>|DËi t L<br><br><br><br>|

|186<br><br>|2021 mv‡j KZ †gMvIqvU we`y¨r Drcv`b n‡e?<br>K.2000 MW<br>L.24000 MW<br>M.22000 MW<br>N.25000 MW<br><br>|DËi t L<br><br><br>|

|187<br>|Power TransmissionK‡i †Kvb cÖwZôvb?<br>K.PGCB<br>L.BPDC<br>M.NESCO<br>N.WZPDCL<br>|DËi t K<br>|

|188<br><br>|DESCOGiFull meaningKx?<br><br>|DËi tDhaka Electric<br>Supply Company<br>Limited<br><br>|

|189<br><br>|we`y¨r kw³‡K hvwš¿K kw³‡Z iƒcvšÍi Kiv‡K Kx ejv nq?<br><br>|DËi t kw³i iƒcvšÍi<br><br>|

|190<br><br><br>|DPDCGi c~Y©iƒc †jL?<br><br><br>|DËi tDhaka Power<br>Distribution Company<br>Ltd<br><br><br>|

|191<br><br>|‡`‡ki me©cÖ_g Kqjv wfwËK Zvc we`y¨r †K›`ª †Kvb †Rjvq Aew¯’Z?<br>K. w`bvRcyi<br>L. iscyi<br><br>|DËi t K<br><br>|

190 DPDC Gi c~Y©iƒc †jL? 191 ‡`‡ki me©cÖ_g Kqjv wfwËK Zvc we`y¨r †K›`ª †Kvb †Rjvq Aew¯’Z? K. w`bvRcyi L. iscyi `প ্র ককৌশলী সমাো ঃ মানিক উনিি`  | 

```

পাওয়ার সেক্টর

```

||M. PÆMÖvg<br>N. XvKv||

|---|---|---|

|192|‡`‡ki me©cÖ_g Kqjv wfwËK Zvc we`y¨r †K‡›`ªi bvg Kx?<br>K. †Nvovkvj Zvc we`y¨r †K›`ª<br>L. eocyKzwiqv Zvc we`y¨r †K›`ª<br>M. cvqiv Zvc we`y¨r †K›`ª N. ivgcvj Zvc we`y¨r †K›`ª|DËi t L|

|193|eocyKzwiqv Zvc we`y¨r †K‡›`ªi Drcv`b ÿgZv-<br>K.250 MW<br>L.500 MW<br>M.525 MW<br>N.225 MW|DËi t M|

|194|What is the Capacity of EGCB?<br>K.987 MW<br>L.1500 MW<br>M.500 MW<br>N.1200 MW|DËi t K|

|195|What is the base load Power plant?<br>K.Nuclear<br>L.HFO Power plant<br>M.Coal<br>N. K I M|DËi t N|

|196|What is non renewable Source of Energy?<br>K.Sun<br>L.Wind<br>M.Nuclear<br>N.Biothermal|DËi t M|

|197|What is the Capacity of Kaptai Hydroelectric plant-<br>K.230 MW<br>L.250 MW<br>M.110 MW<br>N.130 MW|DËi t K|

|198|Which is the demand of electricity during winter season?<br>K.50-60%<br>L.60-70%<br>M.70-80%<br>N.40-50%|DËi t K|

|199|Which is involved electricity in system loss-<br>K.Distribution<br>L.Generation<br>M.Transmission<br>N.None|DËi t M|

|200|Nuclear Power plant is Similar to operation with-<br>K.Steam<br>L.Gas<br>M.HFO<br>N.Hydroelectricpower|DËi t K|

|201|Nuclear Power plant cycle is-<br>K.Brayton Cycle<br>L.Otto Cycle<br>M.Diesel Cycle<br>N.Rankine Cycle|DËi t N|

|202|What type of is used as base load power plant?<br>K.Steam Turbine Power plant<br>L.Gas Turbine Power plant<br>M.Waster Turbine Power plant<br>N.None|DËi t K|

|203|EGCB sell electricity to-<br>K.BPDP<br>L.BERC<br>M.DPDC<br>N.DESCO|DËi t K|

|204|evsjv‡`‡ki evqy we`y¨r cÖKí †Kvb ¯’v‡b Aew¯’Z?<br>K. †dbx †Rjvi †mvbvMvRx Dc‡Rjv<br>L. K·evRv‡ii KzZzew`qv|DËi t K|

|205|evsjv‡`‡ki m‡e©v”P UªvÝwgkb †fv‡ëR KZ?<br>K.400 KV<br>L.230 KV<br>M.700 KV<br>N.132 KV|DËi t K|

`প ্র ককৌশলী সমাো ঃ মানিক উনিি` ee | 

```

পাওয়ার সেক্টর

```

|206|evsjv‡`‡ki we`y¨r I R¦vjvwbপ্রডতgš¿xi bvg Kx?<br>K. †Mvjvg wKewiqv<br>L. Avn‡¤§` KvDQvi<br>M. bmiæj nvwg`<br>N. kvnwiqvi Kwei|DËi t M|

|---|---|---|

|207|What time is called as a off pick hour in.|DËi :11 PM to 5 PM|

|208|B-R Powergen‡Kvb ai‡bi cÖwZôvb?|DËi tBPDPGi GKwU A½<br>cÖwZôvb we`y¨r †Rbv‡ikb K‡i<br>_v‡K||

|209|24000 Generation Capacity target for Bangladesh when year?<br>K.2021<br>L.2024<br>M.2022<br>N.2023|DËi t K|

|210|What kind of work PGCB done?<br>K.Transmission<br>L.Distribution<br>M.Generation<br>N.None|DËi t K|

|211|Solar Panel Set-up is which direction in BD-<br>K.North<br>L.South<br>M.West<br>N.East|DËi t L|

|212|Bangladesh will be import hydro electric Power form which Country?|DËi tIndia-Nepal|

|213|Which is first nuclear Power plant in our country?|DËi tRuppur Nuclear<br>Power pant iswardi Pabna<br>2400 MW|

|214|RPCLK‡e MwVZ nq?<br>K.1994<br>L.1995<br>M.1997<br>N.1996|DËi t K|

|215|gvwmK KZ GKK(Kwh)ch©šÍ we`y¨r LiP Ki‡jLife lineMÖvnK wn‡m‡e aiv nq?<br>K.1-50 Unit<br>L.1-75 Unit<br>M.1-100 Unit<br>N.1-80 Unit||

|216|Which of the following generation station has the minimum running<br>cost?<br>K.Nuclear power station<br>L.Thermal Power station<br>M.Diesel power station<br>N.Hydroelectricpower station|DËi t N|

|217|What is the full name of ACST<br>K.Alloy carbon stell reinforcement<br>L.Alloy Conductor stell reinforcement<br>M.Alloy Conductor supper<br>N.Aluminium conductor steel reinforced Cable|DËi t N|

|218|A transformer transforms-<br>K.Voltage<br>L.Current<br>M.Voltage & CurrentN.Power|DËi t M|

|219|1 GW equal-<br>K.10<sup>3</sup>W<br>L.10<sup>6</sup>W<br>M.10<sup>9</sup>W<br>N.10<sup>12</sup>W|DËi t M|

`প ্র ককৌশলী সমাো ঃ মানিক উনিি` ee | 

```

পাওয়ার সেক্টর

```

|220|HRSG is used in power plant of-<br>K.Single cycle<br>L.Combined cycle<br>M.Both<br>N.None|DËi t L|

|---|---|---|

|221|In a power plant high rate indicates-<br>K.High efficiency<br>L.High calorific valveM.Low efficiency<br>N.None|<br>DËi t M|

|222|Which power plant of 50 MW Capacity will have more poles for 50<br>HZ<br>K.Wind<br>L.Nuclear|DËi t L|

||M.Thermal<br>N.Hydro||

|223|What is the present per capita electricity generation (Kwh) in<br>Bangladesh<br>K.560<br>L.500<br>M.602<br>N.1000|DËi t M**602 Kwh**|

|224|Bangladesh power Grid stability by PGCB is controlled by<br>K.Voltage<br>L.Current<br>M.Voltage & CurrentN.None|DËi t K|

|225|Total Connected Consumers is for BREB is approximates<br>K.2.70 crore<br>L.2.50 crore<br>M.3 crore<br>N.3,53,944|DËi tঘ|

|226|A de generation generate.<br>K.De voltage<br>L.Ac voltage|DËi t L|

|227|The transmission lines generally use-<br>K.Copper<br>L.All aluminium<br>M.ACSR ConductorN.None|DËi t M|

|228|The line voltage on the L.T side of a distribution-<br>K.400 V<br>L.230 V<br>M.11 KV<br>N.33 KV|DËi t L|

|229|The highest transmission voltage used in Bangladesh is-<br>K.132 KV<br>L.230 KV<br>M.400 KV<br>N.765 KV|DËi t M|

|230|Which of the following poorest Conductor of electricity-<br>K.Aluminium<br>L.Copper<br>M.Carbon<br>N.Iron|DËi t M|

|231|Steam turbines may be classified according to<br>K.Direction of steam flow<br>L.Number of stages<br>M.Mode of steam action<br>N.All of these|DËi t N|

|232|‡KvbwU‡KFossil Fuelejv nq? (Rxevk¥ R¦vjvwb)<br>K. Kqjv<br>L. LwbR †Zj<br>M. cÖvK…wZK M¨vm<br>N. me¸wj mwVK|DËi t N<br>e¨vL¨v t Rxevk¥ R¦vjvwb nj GK<br>cÖKvi<br>R¦vjvwb<br>hv<br>evqyi<br>Abycw¯’wZ‡Z AevZ cPb cÖwµqvq<br>ˆZwi nq| hv ˆZwi n‡Z wgwjqb<br>eQi jv‡M||

|233|One KWH is equal to-<br>K.360×10<sup>3</sup>J<br>L.10<sup>3</sup>J|DËi t M|

`প ্র ককৌশলী সমাো ঃ মানিক উনিি` _______ lf 

```

পাওয়ার সেক্টর

```

||M.3.6×10<sup>6</sup>J<br>N.10<sup>6</sup>J<br>||

|---|---|---|

|234<br><br><br>|AwaK `~i‡Z¡ we`y¨r †cÖi‡Yi †ÿ‡Î †fv‡ëR evov‡bv nq| G‡Z wK jvf nq?<br>K. we`y¨‡Zi jm Kg nq<br>L. `ªæZ we`y¨r †cŠuQvq<br>M. Zv‡ii evav Kg nq<br>N. †KvbwUB mwVK bq<br><br><br>|<br>DËi t K<br><br><br><br>|

|235<br><br>|Which distribution voltage is not used in BREB distribution network.<br>K.230 V<br>L.11 KV<br>M.33 KV<br>N.66 KV<br><br>|DËi t N<br><br><br>|

|236<br>|It the length of the transmission line in 300 to 400 km, the suitable<br>transmission network.<br>K.11 KV<br>L.33 KV<br>M.66 KV<br>N.400 KV<br>|DËi t N<br><br><br>|

|237<br>|BPDPK‡e cÖwZwl|VZ nq?<br>K. 1959<br>L. 1972<br>M. 1962<br>N. 1973<br>|DËi t L<br><br><br><br>|

|238<br><br>|we`y¨r µq I weµq K‡i †Kvb cÖwZôvb?<br>K.PGCB<br>L.BPDP<br>M.BREB<br>N.NWPGCL<br><br>|DËi t L<br><br><br><br>|

|239<br>|KZ mv‡j XvKvq cÖ_g we`y¨r mieivn †Rbv‡iUi ¯’vcb Kiv nq?<br>K. 1902<br>L. 1901<br>M. 1912<br>N. 1919<br>|DËi t L<br><br><br>|

|240<br>|evsjv‡`‡k KZ †gMvIqvU we`y¨rImportedK‡i?<br>K. 1160 †gMvIqvU<br>L. 560 †gMvIqvU<br>M. 1000 †gMvIqvU<br>N. 500 †gMvIqvU<br>|DËi t2656 MW<br><br><br>|

|241<br>|eZ©gv‡b we`y¨‡Zi GKK †µZv<br>K.PGCB<br>L.BPDP<br>M.BREB<br>N.DPDC<br>|DËi t L<br><br><br><br>|

|242<br>|Presently BPDP’S distribution network is comprising of<br>|Ans. 33 kv, 11 kv and<br>11/0.4 kv lines<br><br><br>|

|243<br><br>|BPDBGi eZ©gvb MÖvnK msL¨v?<br>K. 25 jÿ<br>L. 27 jÿ<br>M. 30 jÿ<br>N. cÖvq 35 jÿ<br><br>|DËi t N<br><br><br>|

|244<br><br><br>|BPDBGi wfkb nj t<br>DËi t mK‡ji wbKU wbiwew”Qbœ gvbm¤§Z we`y¨r †cŠu‡Q †`qv|<br><br><br>||

|245<br><br>|evsjv‡`‡ki we`y¨r Drcv`b ÿgZv †gMvIqvU -<br><br>|29152 MW<br><br><br>|

|246<br>|‡KvbwU wMÖW mve‡÷kb?<br>K.132/33 kv<br>L.11/132 kv<br>M.33/11 kv<br>N.66/11 kv<br>|DËi t K<br><br><br>|

|247<br><br>|BPDB†_‡K †K we`y¨r wK‡b bv?<br>K.NESCO<br>L.PGCB<br>M.REB<br>N.DPDC<br><br>|DËi t L<br><br><br><br>|

|248<br>|PGCB-<br>K. we`y¨r mÂvjb K‡i<br>L. we`y¨r Drcv`b K‡i<br>M. we`y¨r weZiY K‡i<br>N. me KqwU<br>|DËi t K<br><br><br>|

`প ্র ককৌশলী সমাো ঃ মানিক উনিি` ee | 

```

পাওয়ার সেক্টর

```

|249|Transmission lineG D”P †fv‡ëR Gi myweav-<br>K. A_© mvkÖqv‡_©<br>L. we`y¨r AcPq Kgv‡bvi Rb¨<br>M.TowerGi RvqMv Kgv‡bvi Rb¨<br>N.TowerGi msL¨v Kgv‡bvi Rb¨|DËi t L|

|---|---|---|

|250<br>|wcwRwmwe m‡e©v”P UªvÝwgkb †fv‡ëR KZ?<br>K. 765 †K wf<br>L. 400 †K wf<br>M. 230 †K wf<br>N. 132 †K wf<br>|DËi t L<br>|

|251<br><br>|wcwRwmwei †gvUTransmission lineKZ wK.wg. mvwK©U?<br>(www.powerdivision.gov.bd)<br>K.12379 Circuit KmL.10000 Circuit Km<br>M.15000 Circuit KmN.16000 Circuit Km<br><br>|DËi t K<br>**14948 Ckt**<br><br>|

|252<br><br>|wMÖ‡W e¨envi‡hvM¨ we`y¨r Drcv`b ÿgZv cÖvq-<br>K.16000 MW<br>L.12 GW<br>M.16000 KW<br>N.30 GW<br><br>|DËi t K<br><br>|

|253<br><br>|DPDCGjvKvqpeak demandcÖvq-<br>K.16000 MW<br>L.1000 MW<br>M.2000 MW<br>N.1400 MW<br><br>|DËi t1806 MW <br><br>|

|254<br>|DPDC†gvU MÖvnK msL¨v cÖvq-<br>K. 11 jvL<br>L.17,08,959<br>|DËi t L1708959<br>|

||M. 15 jvL<br>N. 10.5 jvL<br>||

|255<br><br>|wWwcwWwm GjvKvi evwn‡i †KvbwU?<br>K. avbgwÛ<br>L. dZzjøv<br>M. bvivqbMÄ<br>N. c~e©vPj<br><br>|DËi t N<br><br>|

|256<br>|Life lineMÖvn‡Ki Rb¨ GKK cÖwZ we`y¨‡Zi bZzb †iU n‡”Q-<br>K. 3.50 UvKv<br>L. 3.57 UvKv<br>M. 4.35 UvKv<br>N. 3.75 UvKv<br>|DËi t N<br>|

|257<br>|bZzb ms‡hv‡Mi †ÿ‡Î KZ wK‡jvIqvU Aby‡gvw`Z †jvW ch©šÍ wb¤œPvc(LT)MÖvnK wn‡m‡e<br>we‡ewPZ nq-<br>K.100 KW<br>L.80 KW<br>M.70 KW<br>N.90 KW<br>|DËi t L<br>|

|258<br>|‡Kvb GjvKvwU wWwcwWwmi †fZ‡i-<br>K. †ZRMuvI<br>L. DËiv<br>~©<br>|DËi t K<br>|

||M. Avãyjøvcyi<br>N. c~e©vPj<br>||

|259<br>|DESCO has no-<br>K.Power Plant<br>L.Distribution Zone<br>M.Sub Station<br>|DËi t K<br>|

||N.Distributepower in Dhaka Zone<br>||

|260<br><br>|‡KvbwUDESCOGjvKv‡Z bq?<br>K. wbKzÄ<br>L. Kj¨vYcyi<br>L. c~e©vPj<br>N. †ZRMuvI<br><br>|DËi t N<br><br>|

|261<br><br><br>|jvBd jvBb we`y¨Zvqb †h †ÿ‡Î cÖ‡hvR¨?<br>K.1-5 UnitGi MÖvnK<br>L.1-75 UnitGi MÖvnK<br>M.50- UnitGi Dc‡ii MÖvnK<br>N. †h †Kv‡bv we`y¨r MÖvn‡Ki Rb¨<br><br><br>|DËi t K<br><br>|

|262<br>|20২১mv‡jDESCOGjvKv‡ZPick demandwQj AvbygvwbK-<br>K.1700 MW<br>L.500 MW<br>|DËi t N১৪৭৫ MW|

262 20 ২১ mv‡j DESCO GjvKv‡Z Pick demand wQj AvbygvwbKK. 1700 MW L. 500 MW `প ্র ককৌশলী সমাো ঃ মানিক উনিি` [182]  

```

পাওয়ার সেক্টর

```

||M.1500 MW<br>N.1000 MW||

|---|---|---|

|263|DESCOhvi †_‡K we`y¨r wK‡b?<br>K.BPDB<br>L.PGCB<br>M.REBN.Ghorasal Power Plant|DËi t K|

|264|DESCOcÖ_g Ae¯’vq †Kvb GjvKvq Kvh©µg ïiæ K‡i?<br>K. DËiv<br>L. †ZRMuvI<br>M. Kgjvcyi<br>N. wgicyi|DËi t N|

|265|DESCOGi eZ©gvb MÖvnK msL¨v cÖvq-<br>K. 9 jÿ<br>L.১২,৪০,১৪০  ন<br>M. 11 jÿ<br>N. 8 jÿ|DËi t L১২,৪০,১৪০  ন|

|266|‡Kvb cÖwZôvb n‡ZDESCO15 b‡f¤^i 2007 Zvwi‡L jvB‡mÝ cÖvß nq?<br>K.BERC<br>L.BPDB<br>M.BREB<br>N.PGCB|DËi t K|

|267|‡Kvb we`y¨r weZiY cÖwZôvb me©cÖ_g AbjvB‡b we`y¨r wej cwi‡kva c×wZ Pvjy K‡i?<br>K.DESCO<br>L.DPDC<br>M.BPDB<br>N.NESCO|DËi t K|

|268|NESCOK‡e cÖwZôv jvf K‡i?<br>K. 2016 mv‡j<br>L. 1996 mv‡j<br>M. 2008 mv‡j<br>N. 2014 mv‡j|DËi t K|

|269|NESCOGKwU-<br>K. we`y¨r weZiYKvix cÖwZôvb<br>L. we`y¨r Drcv`b K‡i<br>M. mÂvjb K‡i<br>N. †KvbwU bq|DËi t K|

|270|NESCOGi eZ©gvb MÖvnK msL¨v-<br>K. cÖvq 14 jÿ<br>L.১৯, ১৫, ৯৯৬ জন<br>M. cÖvq 16 jÿ<br>N. cÖvq 13 jÿ|DËi t<br>১৯, ১৫, ৯৯৬ জন|

|271|NESCOKZwU †Rjv‡Z we`y¨r †mev w`‡q _v‡K?<br>K. 16wU<br>L. 10 wU<br>M. 15 wU<br>N. 17 wU|DËi t KTotal 16 Districts<br>and 26 Upazilas|

|272|NESCOGi m‡e©v”P we`y¨r Pvwn`v KZ-<br>K.760 MW<br>L.1000 MW<br>M.500 MW<br>N.1200 MW|DËi t896 MW|

|273|NESCOGi MÖvnK e„w×i nvi-<br>K. 7.20%<br>L. 8%<br>M. 6.20%<br>N. 7.80%|DËi t5.66 %|

|274|evsjv‡`‡ki me©e„nr we`y¨r †K›`ª †Kv_vq Aew¯’Z?<br>K. g‡nkLvjx<br>L. cUzqvLvjx<br>M. iƒccyi<br>N. AvïMÄ|DËi t N|

|275|AvïMÄ Zvc we`y¨r †K›`ª †Kvb b`xi Zx‡i Aew¯’Z?<br>K. ‡gNbv<br>L. cÙv<br>M. KY©dzjx<br>N. iƒcmv|DËi t K|

|276|‡`‡ki me©e„nr we`y¨r †K›`ª-<br>K. AvïMÄ Zvc we`y¨r †K›`ª L. †Nvovkvj Zvc we`y¨r †K›`ª<br>M. eocyKzwiqv Zvc we`y¨r †K›`ª<br>N. cvqiv Zvc we`y¨r †K›`ª|DËi t K|

`প ্র ককৌশলী সমাো ঃ মানিক উনিি` ee | 

```

পাওয়ার সেক্টর

```

|277<br>|AvïMÄ Zvc we`y¨r †K‡›`ªi Drcv`<br>K. 1690 †gMvIqvU<br>M. 1600 †gMvIqvU<br>|y ª b ÿgZv KZ?<br>L. 1876 †gMvIqvU<br>N. 1620 †gMvIqvU<br>|DËi t1571.03 দেগাওয়াট পব্দ্**য**ৎ<br>উৎিােন ক্ষেতা<br><br>|

|---|---|---|---|

|278<br>|ASPCLGi ¯’vcb ÿgZv KZ †<br>K. 1690 †gMvIqvU<br>M. 1876 †gMvIqvU<br>|’   gMvIqvU?<br>L. 2400 †gvMIqvU<br>N. 1620 †gMvIqvU<br>|DËi t**1647 মেগাওযাট** <br><br>|

|279<br>|BREBMwVZ nq-<br>K. 1977<br>M. 1972<br>|L. 1978<br>N. 1975<br>|DËi t K<br><br>|

|280<br>|BREBeZ©gvb MÖvnK msL¨v-<br>K. 2 †KvwU 90 jÿ (A<br>L. 2 †KvwU 80 jÿ<br>M. 3 †KvwU<br>|vc‡WU- 25/08/2020)<br>N. 2 †KvwU 70 jÿ<br>|DËi tব্ততোলন**৩৫,৩৯৯,০৪৭ টি**<br>|

|281<br>|BREBGi m‡e©v”P Pvwn`v KZ †<br>K.7100 MW<br>M.4500 MW<br>**বর্তোনন ৮৬০৬ মেগাও**<br>|©   gMvIqvU-<br>L.5000 MW<br>N.6000 MW<br>**্ত  যাট**<br>|DËi t K**বর্তোনন ৯৮০১**<br>**মেগাওযাট**<br><br>|

|282<br>|BREBKvi †_‡K we`y¨r µq K‡<br>K.BPDB<br>|y  i-<br>L.PGCB<br>|DËi t K<br><br>|

||M.EGCB<br>y y y   ©<br><br>|N.NWPGCL<br>y y y   ©<br><br>|**্ত**<br><br><br>|

|283<br>|evsjv‡`‡ki KZ kZvsk gvbyl we`y y   ©<br>K. 96%<br>M. 98%<br>ব্ততোলন ১০০%<br>|y y¨r myweav cv‡”Q? (Z_¨ cwieZ©bkxj)<br>L. 97%<br>N. 99%<br>|DËi t**বর্তোনন ১০০%**<br><br>|

|284<br><br>|cjøx we`y¨r mwgwZ KZwU?<br>K. 77wU<br>M. 85 wU<br><br>|L. 80 wU<br>N. 50 wU<br><br>|DËi t L<br>**্ত  ি**<br><br>|

|285<br>|kZfvM we`y¨Zvqb Dc‡Rjv-<br>K. 461 wU<br>M. 451 wU<br>|L. 492 wU<br>N. 392 wU<br>|**বর্তোনন ৪৬২ টি**<br>|

|286<br><br>|What is the name of a<br>generation.**?**<br><br>|transformer which is step up for power|Unit|

|287<br>|How much voltage from P<br>|ayra-Gopalgonj-Aminbazar Line ?|400KV|

|288<br><br><br>|What is the name of hydr<br><br><br>|o power plant of Bangladesh  ?<br>|Karnophuli|

|289<br><br>|What is the generation ca<br><br>|pacity of Payra Power plant ?<br>|1320 MW|

|290<br>|Rooppur Reactor Unit Lif<br>|e span ?<br>|60 yrs|

|291<br>|What type of transformer<br>|does the power plant use for its own use? <br>|Auxiliary|

|292<br><br>|What kind of plant is R**oo**<br><br>|ppur? <br><br>|Base-load <br>|

|293<br>|Rooppur power unit life s<br>|pan how many years? <br>|50 years<br>|

|294<br><br>|How much electricity is c<br><br>|urrently being generated from gas? <br><br>|45% (According to BPDB<br>its is 44%)<br><br><br>|

|295<br><br>|How much generation cap<br><br>|acity of NWPGCL have? <br><br>|Answer:<br>3000MW<br>(according to NWPGCL<br>3063MW)<br><br><br>|

`প ্র ককৌশলী সমাো ঃ মানিক উনিি` ee | 

```

পাওয়ার সেক্টর

```

 296 No of pole in kornofuli water plant? None of the mentiond 

> <sup>an)@</sup> 

`প ্র ককৌশলী সমাো ঃ মানিক উনিি` _______=Zf
