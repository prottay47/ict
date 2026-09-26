# M1: Computer Network (Flow Control and Its Protocol)

- **Original URL:** [https://it.jobqns.com/m1-computer-network-flow-control-and-its-protocol/](https://it.jobqns.com/m1-computer-network-flow-control-and-its-protocol/)
- **Date:** 2026-08-26T23:13:38
- **Categories:** Uncategorized, IT Preparation Module

---

**Computer Network**  (Flow Control and Its Protocol) (ET: 2.5 Hours)



**Video Tutorial:**  (Flow Control and Its Protocol)



- **Watch Video:**  Flow Control Introduction

- **Watch Video:**  Stop and Wait Protocol

- **Watch Video:**  Stop and Wait ARQ Protocol

- **Watch Video:**   Sliding Window Protocol

- **Watch Video:**   Sliding Window Protocol (Solved Problem 1)

- **Watch Video:**   Sliding Window Protocol (Solved Problem 2)

- **Watch Video:**   Efficiency Analysis Stop and Wait Protocol

Flow Control and Its Protocol

- 1

Flow Control


**Flow Control**  is a speed-matching mechanism used in the  **Data Link Layer**  to control the rate of data transmission between a sender and a receiver. It ensures that a fast sender does not send data faster than the receiver can receive, store, and process it.
The receiver has a limited processing speed and limited memory (buffer) for storing incoming data. If data arrives faster than the receiver can process it, the buffer may become full and data may be lost. Therefore, the receiver can inform the sender to reduce or temporarily stop the transmission.
In simple terms,  **Flow Control coordinates the amount of data that can be sent before the sender needs to wait for an acknowledgment from the receiver.**  It mainly focuses on the receiver's ability to handle incoming data.
**Flow Control Protocols**
Flow control protocols are generally categorized according to the type of communication channel:
**1. Protocols for Noiseless Channel:**  These include  **Simplest Protocol**  and  **Stop-and-Wait Protocol** .
**2. Protocols for Noisy Channel:**  These include  **Stop-and-Wait ARQ, Go-Back-N ARQ**  and  **Selective Repeat ARQ** . Here,  **ARQ**  stands for  **Automatic Repeat reQuest** .
**Key Point:**  Flow control prevents data loss by matching the sender's transmission rate with the receiver's processing capacity.

**Flow Control**  হলো  **Data Link Layer** -এর একটি গুরুত্বপূর্ণ পদ্ধতি, যার মাধ্যমে Sender ও Receiver-এর মধ্যে Data Transmission-এর Speed নিয়ন্ত্রণ করা হয়। এটি নিশ্চিত করে যে Fast Sender যেন Receiver-এর Data Receive, Store এবং Process করার ক্ষমতার চেয়ে বেশি গতিতে Data পাঠাতে না পারে।
Receiver-এর Data Process করার Speed এবং Incoming Data সংরক্ষণের জন্য Memory (Buffer) সীমিত থাকে। যদি Data Receiver-এর Processing Speed-এর চেয়ে দ্রুত আসে, তাহলে Buffer পূর্ণ হয়ে Data Loss হতে পারে। তাই Receiver প্রয়োজনে Sender-কে Data পাঠানোর গতি কমাতে বা সাময়িকভাবে Transmission বন্ধ করতে নির্দেশ দিতে পারে।
সহজভাবে বলা যায়,  **Flow Control নির্ধারণ করে Receiver-এর কাছ থেকে Acknowledgment পাওয়ার আগে Sender কত পরিমাণ Data পাঠাতে পারবে।**  তাই Flow Control-এর ক্ষেত্রে মূলত Receiver-এর Data Handle করার ক্ষমতার ওপর গুরুত্ব দেওয়া হয়।
**Flow Control-এর Protocol**
Channel-এর ধরন অনুযায়ী Flow Control Protocol-গুলো সাধারণত দুই ভাগে বিভক্ত:
**১. Noiseless Channel-এর Protocol:**  এর মধ্যে রয়েছে  **Simplest Protocol**  এবং  **Stop-and-Wait Protocol** ।
**২. Noisy Channel-এর Protocol:**  এর মধ্যে রয়েছে  **Stop-and-Wait ARQ, Go-Back-N ARQ**  এবং  **Selective Repeat ARQ** । এখানে  **ARQ**  এর পূর্ণরূপ হলো  **Automatic Repeat reQuest** ।
**মূল কথা:**  Flow Control Sender-এর Transmission Rate এবং Receiver-এর Processing Capacity-এর মধ্যে সমন্বয় করে Data Loss প্রতিরোধ করে।

2

Stop-and-Wait Protocol


**Stop-and-Wait Protocol**  is a  **Data Link Layer**  flow control protocol used for transmitting frames over a  **noiseless channel** . It provides  **unidirectional data transmission**  with flow control but does not provide error control.
The basic idea is very simple: the  **sender sends only one frame at a time**  and waits for an  **acknowledgment (ACK)**  from the receiver before sending the next frame.
**Working of Stop-and-Wait Protocol:**

The sender sends one data frame to the receiver.
The sender waits for an acknowledgment before sending the next frame.
The receiver receives and consumes the frame.
After consuming the frame, the receiver sends an acknowledgment to the sender.
After receiving the acknowledgment, the sender sends the next frame.

**Example:**  Sender → Frame 1 → Receiver → ACK → Sender → Frame 2 → Receiver → ACK, and the process continues.
**Advantages:**

Very simple and easy to implement.
Provides basic flow control between sender and receiver.
Prevents the sender from overwhelming a slow receiver.

**Problems of Stop-and-Wait Protocol:**

**Lost Data:**  If the data frame is lost, the receiver cannot send an acknowledgment, and the sender may wait indefinitely.
**Lost Acknowledgment:**  If the receiver's acknowledgment is lost, the sender does not know that the frame was successfully received and waits for the ACK.
**Delayed Data or Acknowledgment:**  If an ACK is delayed beyond the sender's waiting period, the sender may incorrectly interpret the delayed ACK as belonging to another frame.

**Key Point:**  Stop-and-Wait is simple and reliable for flow control, but it is inefficient for large amounts of data because the sender must wait for an acknowledgment after every frame.

**Stop-and-Wait Protocol**  হলো একটি  **Data Link Layer** -এর Flow Control Protocol, যা  **Noiseless Channel** -এ Frame Transmission-এর জন্য ব্যবহৃত হয়। এটি  **Unidirectional Data Transmission**  এবং Flow Control প্রদান করে, তবে Error Control প্রদান করে না।
এর মূল ধারণা খুবই সহজ:  **Sender একবারে একটি Frame পাঠায়**  এবং পরবর্তী Frame পাঠানোর আগে Receiver-এর কাছ থেকে  **Acknowledgment (ACK)**  পাওয়ার জন্য অপেক্ষা করে।
**Stop-and-Wait Protocol-এর কার্যপ্রণালী:**

Sender একটি Data Frame Receiver-এর কাছে পাঠায়।
Sender পরবর্তী Frame পাঠানোর আগে ACK-এর জন্য অপেক্ষা করে।
Receiver Frame গ্রহণ ও Process করে।
Frame গ্রহণ করার পর Receiver Sender-কে ACK পাঠায়।
ACK পাওয়ার পর Sender পরবর্তী Frame পাঠায়।

**উদাহরণ:**  Sender → Frame 1 → Receiver → ACK → Sender → Frame 2 → Receiver → ACK—এভাবে প্রক্রিয়াটি চলতে থাকে।
**সুবিধাসমূহ:**

খুব সহজ এবং Implement করা সহজ।
Sender ও Receiver-এর মধ্যে Basic Flow Control প্রদান করে।
Slow Receiver-এর ওপর অতিরিক্ত Data-এর চাপ সৃষ্টি হতে দেয় না।

**Stop-and-Wait Protocol-এর সমস্যা:**

**Data Lost:**  Data Frame হারিয়ে গেলে Receiver ACK পাঠাতে পারে না এবং Sender দীর্ঘ সময় অপেক্ষা করতে পারে।
**ACK Lost:**  Receiver-এর পাঠানো ACK হারিয়ে গেলে Sender বুঝতে পারে না যে Frame সফলভাবে পৌঁছেছে এবং ACK-এর জন্য অপেক্ষা করতে থাকে।
**Delayed Data বা ACK:**  ACK Sender-এর নির্ধারিত অপেক্ষার সময়ের পরে পৌঁছালে Sender ভুলভাবে সেটিকে অন্য Frame-এর ACK হিসেবে বিবেচনা করতে পারে।

**মূল কথা:**  Stop-and-Wait Flow Control-এর জন্য সহজ ও কার্যকর হলেও বড় পরিমাণ Data Transmission-এর ক্ষেত্রে এটি কম Efficient, কারণ প্রতিটি Frame পাঠানোর পর Sender-কে ACK-এর জন্য অপেক্ষা করতে হয়।

3

Stop-and-Wait ARQ Protocol


**Stop-and-Wait ARQ (Automatic Repeat reQuest)**  is a Data Link Layer protocol used for  **flow control and error control**  over noisy channels. It is an improved version of the simple Stop-and-Wait protocol.
In Stop-and-Wait ARQ, the sender sends  **one frame at a time**  and waits for an  **acknowledgment (ACK)**  before sending the next frame. It additionally uses a  **timer**  and  **sequence numbers**  to handle lost or delayed frames and acknowledgments.
**Working:**  After sending a frame, the sender starts a timer. If the ACK arrives before the timer expires, the sender sends the next frame. If the ACK does not arrive within the specified time, the sender assumes that the frame or ACK may have been lost and  **automatically retransmits the frame** . This automatic retransmission is why it is called  **Automatic Repeat reQuest (ARQ)** .
**Important Components:**

**ACK:**  Confirms that the frame has been received successfully.
**Timer:**  Detects when an ACK has not arrived within the expected time.
**Sequence Number:**  Helps identify frames and detect duplicate frames caused by retransmission.
**Retransmission:**  The sender automatically sends the frame again when a timeout occurs.

**Important Scenarios:**

**ACK received before timeout:**  The frame and ACK are received successfully, so the sender sends the next frame.
**Frame lost:**  The receiver does not receive the frame and therefore does not send an ACK. After timeout, the sender retransmits the frame.
**ACK lost:**  The receiver receives the frame and sends an ACK, but the ACK is lost. After timeout, the sender retransmits the frame.
**Timeout occurs too soon:**  The frame and ACK are successfully delivered, but the ACK arrives after the timer expires. The sender retransmits the frame unnecessarily.

**Difference from Simple Stop-and-Wait:**  Simple Stop-and-Wait mainly provides flow control and may wait indefinitely if a frame or ACK is lost.  **Stop-and-Wait ARQ**  adds a  **timer, sequence numbers, error detection and automatic retransmission** , making it suitable for noisy channels.
**Key Point:**  Stop-and-Wait ARQ =  **Stop-and-Wait + Timer + Sequence Number + Automatic Retransmission** .

**Stop-and-Wait ARQ (Automatic Repeat reQuest)**  হলো একটি Data Link Layer Protocol, যা  **Noisy Channel** -এ Flow Control এবং Error Control-এর জন্য ব্যবহৃত হয়। এটি Simple Stop-and-Wait Protocol-এর একটি উন্নত সংস্করণ।
Stop-and-Wait ARQ-তে Sender একবারে  **একটি Frame পাঠায়**  এবং পরবর্তী Frame পাঠানোর আগে  **Acknowledgment (ACK)** -এর জন্য অপেক্ষা করে। এছাড়া Lost বা Delayed Frame এবং ACK মোকাবিলার জন্য এতে  **Timer**  এবং  **Sequence Number**  ব্যবহার করা হয়।
**কার্যপ্রণালী:**  Sender একটি Frame পাঠানোর পর একটি Timer চালু করে। Timer শেষ হওয়ার আগে ACK পাওয়া গেলে Sender পরবর্তী Frame পাঠায়। নির্দিষ্ট সময়ের মধ্যে ACK না এলে Sender ধরে নেয় যে Frame বা ACK হারিয়ে যেতে পারে এবং  **স্বয়ংক্রিয়ভাবে Frame-টি পুনরায় পাঠায়** । এই Automatic Retransmission-এর কারণেই এর নাম  **Automatic Repeat reQuest (ARQ)** ।
**গুরুত্বপূর্ণ উপাদান:**

**ACK:**  Frame সফলভাবে গ্রহণ করা হয়েছে তা নিশ্চিত করে।
**Timer:**  নির্দিষ্ট সময়ের মধ্যে ACK না এলে তা শনাক্ত করে।
**Sequence Number:**  Frame শনাক্ত করতে এবং Retransmission-এর কারণে Duplicate Frame চিহ্নিত করতে সাহায্য করে।
**Retransmission:**  Timeout হলে Sender স্বয়ংক্রিয়ভাবে Frame পুনরায় পাঠায়।

**গুরুত্বপূর্ণ পরিস্থিতি:**

**Timeout-এর আগে ACK পাওয়া:**  Frame ও ACK সফলভাবে পৌঁছালে Sender পরবর্তী Frame পাঠায়।
**Frame হারিয়ে গেলে:**  Receiver Frame না পাওয়ায় ACK পাঠায় না। Timeout হলে Sender Frame-টি পুনরায় পাঠায়।
**ACK হারিয়ে গেলে:**  Receiver Frame পেয়ে ACK পাঠায়, কিন্তু ACK হারিয়ে যায়। Timeout হলে Sender Frame-টি পুনরায় পাঠায়।
**Timeout খুব দ্রুত হলে:**  Frame ও ACK উভয়ই সফলভাবে পৌঁছালেও ACK Timer শেষ হওয়ার পরে পৌঁছায়। ফলে Sender অপ্রয়োজনীয়ভাবে Frame পুনরায় পাঠায়।

**Simple Stop-and-Wait-এর সাথে পার্থক্য:**  Simple Stop-and-Wait মূলত Flow Control প্রদান করে এবং Frame বা ACK হারিয়ে গেলে দীর্ঘ সময় অপেক্ষা করতে পারে। অন্যদিকে  **Stop-and-Wait ARQ** -তে  **Timer, Sequence Number, Error Control এবং Automatic Retransmission**  রয়েছে, তাই এটি Noisy Channel-এর জন্য উপযোগী।
**মূল কথা:**  Stop-and-Wait ARQ =  **Stop-and-Wait + Timer + Sequence Number + Automatic Retransmission** ।

4

Sliding Window Protocol


The  **Sliding Window Protocol**  is a flow control protocol used to transmit multiple frames before receiving acknowledgements. It improves the utilization of network bandwidth compared to the  **Stop-and-Wait ARQ**  protocol.
**Need for Sliding Window Protocol:**  In Stop-and-Wait ARQ, only one frame can be transmitted at a time, so a large amount of bandwidth may remain unused, especially in high-speed networks. This results in poor bandwidth utilization and lower performance.
**Working of Sliding Window Protocol:**  In this protocol, the sender and receiver use a parameter called  **Window Size** . The window size determines how many frames can be transmitted before the sender needs to wait for acknowledgements.
Each frame is assigned a unique  **Sequence Number** . As acknowledgements are received, the window moves or  **slides**  forward, allowing the sender to transmit new frames.
**Example:**  Suppose there are 11 frames numbered  **0 to 10**  and the window size is  **4** . The sender can initially send frames  **0, 1, 2, and 3**  without waiting for individual acknowledgements.
When the acknowledgement for frame  **0**  is received, the window slides forward and the sender can send frame  **4** . Similarly, when the acknowledgement for frame  **1**  is received, the sender can send frame  **5** . Thus, the window continuously moves forward as acknowledgements are received.
**Three Parts of the Sliding Window:**

**Sent and Acknowledged:**  Frames that have already been successfully transmitted and acknowledged.
**Sent but Not Acknowledged:**  Frames that have been transmitted but their acknowledgements have not yet been received.
**Not Yet Sent:**  Frames that are waiting to be transmitted.

**Advantages:**

Allows multiple frames to be transmitted at a time.
Provides better bandwidth utilization.
Improves network performance compared to Stop-and-Wait.
Reduces the waiting time between frame transmissions.

**Key Point:**  The number of frames that can be transmitted before waiting for acknowledgements is determined by the  **Window Size** . As acknowledgements arrive, the window slides forward and new frames are transmitted.

**Sliding Window Protocol**  হলো একটি Flow Control Protocol, যেখানে Acknowledgement পাওয়ার আগেই একাধিক Frame পাঠানো যায়। এটি  **Stop-and-Wait ARQ** -এর তুলনায় Network Bandwidth আরও ভালোভাবে ব্যবহার করতে সাহায্য করে।
**Sliding Window Protocol-এর প্রয়োজনীয়তা:**  Stop-and-Wait ARQ-এ এক সময়ে মাত্র একটি Frame পাঠানো যায়। ফলে বিশেষ করে High-Speed Network-এ অনেক Bandwidth অব্যবহৃত থাকে। এর ফলে Bandwidth Utilization এবং Network Performance কমে যায়।
**Sliding Window Protocol-এর কার্যপদ্ধতি:**  এই Protocol-এ Sender এবং Receiver একটি  **Window Size**  ব্যবহার করে। Window Size নির্ধারণ করে Acknowledgement পাওয়ার আগে সর্বোচ্চ কতগুলো Frame পাঠানো যাবে।
প্রতিটি Frame-এর একটি নির্দিষ্ট  **Sequence Number**  থাকে। Sender যখন বিভিন্ন Frame-এর Acknowledgement পেতে থাকে, তখন Window সামনে দিকে  **Slide**  করে এবং নতুন Frame পাঠানোর সুযোগ তৈরি হয়।
**উদাহরণ:**  ধরা যাক, মোট ১১টি Frame রয়েছে এবং Frame-গুলো  **0 থেকে 10**  পর্যন্ত Numbered। যদি Window Size  **4**  হয়, তাহলে Sender প্রথমে  **0, 1, 2 এবং 3**  নম্বর Frame একসাথে পাঠাতে পারবে।
যখন Frame  **0** -এর Acknowledgement পাওয়া যাবে, তখন Window সামনে Slide করবে এবং Sender Frame  **4**  পাঠাতে পারবে। একইভাবে Frame  **1** -এর Acknowledgement পাওয়ার পর Sender Frame  **5**  পাঠাতে পারবে। এভাবে Acknowledgement পাওয়ার সাথে সাথে Window সামনে এগিয়ে যায়।
**Sliding Window-এর তিনটি অংশ:**

**Sent and Acknowledged:**  যে Frameগুলো সফলভাবে পাঠানো হয়েছে এবং যেগুলোর Acknowledgement পাওয়া গেছে।
**Sent but Not Acknowledged:**  যে Frameগুলো পাঠানো হয়েছে কিন্তু এখনো Acknowledgement পাওয়া যায়নি।
**Not Yet Sent:**  যে Frameগুলো এখনো পাঠানো হয়নি এবং অপেক্ষায় রয়েছে।

**সুবিধাসমূহ:**

একসাথে একাধিক Frame পাঠানো যায়।
Bandwidth-এর ভালো ব্যবহার নিশ্চিত করে।
Stop-and-Wait-এর তুলনায় Network Performance বৃদ্ধি করে।
Frame পাঠানোর মধ্যবর্তী Waiting Time কমায়।

**গুরুত্বপূর্ণ বিষয়:**  Acknowledgement পাওয়ার আগে কতগুলো Frame পাঠানো যাবে তা  **Window Size**  দ্বারা নির্ধারিত হয়। Acknowledgement পাওয়ার সাথে সাথে Window সামনে Slide করে এবং নতুন Frame পাঠানো হয়।

5

Station A uses 32 byte packets to transmit message to Station B using a
sliding window protocol. The round trip delay between A and B is 80
milliseconds and the bottleneck bandwidth on the path between A and B is
128 kbps. What is the optimal window size that A should use?


**Given:**
Packet size = 32 bytes = 32 × 8 =  **256 bits**
RTT = 80 ms =  **0.08 s**
Bandwidth = 128 kbps =  **128,000 bps**
**Formula:**
Optimal Window Size = Bandwidth × RTT ÷ Packet Size
**Calculation:**
= (128,000 × 0.08) ÷ 256
= 10,240 ÷ 256
=  **40 packets**
**Answer: The optimal window size is 40 packets.**

6

The distance between two stations M and N is L kilometres. All frames are K
bits long. The propagation time per kilometer is t seconds. Let R bits/second
be the channel capacity. Assuming the processing delay is negligible, the
minimum number of bits for the sequence number field in a frame for
maximum utilization, when the sliding window protocol is used, is:


**Given:**

Distance = L km
Frame size = K bits
Propagation time per km = t seconds
Channel capacity = R bits/second
**Propagation delay:**  L × t seconds
**Round-trip propagation delay:**  2Lt seconds

For maximum utilization, the sender's window must be large enough to keep the channel busy:
**Window size**  ≥ 1 + (2LtR / K)

Let the sequence number field contain  **n bits** . Then the number of sequence numbers is 2n.

Therefore,

2n ≥ 1 + (2LRt / K)

Taking log2 on both sides:
**n ≥ log2[1 + (2LRt / K)]**

Hence, the minimum number of bits required for the sequence number field is:
**n = ⌈log2(1 + 2LRt/K)⌉ bits**

7

If the bandwidth of a line is 1.5 Mbps, RTT is 45 ms, and packet size is 1 KB, find the link utilization in Stop-and-Wait protocol.


Given: Bandwidth = 1.5 Mbps, RTT = 45 ms, Packet size = 1 KB.
**Formula:**  Transmission Delay, Tt = Packet Size / Bandwidth Propagation Delay, Tp = RTT / 2 a = Tp / Tt Stop-and-Wait Efficiency, η = 1 / (1 + 2a)
**Transmission Delay (Tt)**  = (1024 × 8) / (1.5 × 106) = 5.461 ms
**Propagation Delay (Tp)**  = 45 / 2 = 22.5 ms
**a**  = 22.5 / 5.461 ≈ 4.12
**Link Utilization (η)**  = 1 / (1 + 2 × 4.12) ≈ 0.108  **Therefore, Link Utilization ≈ 10.8%.**

8

A channel has a bit rate of 4 Kbps and one-way propagation delay of 20 ms. The channel uses Stop-and-Wait protocol. The transmission time of the acknowledgement frame is negligible. To get a channel efficiency of at least 50%, what should be the minimum frame size?


Let the frame size = L bits. **Formula:**  a = Tp / Tt η = 1 / (1 + 2a)
For η ≥ 50%:
1 / (1 + 2a) ≥ 1/2 Therefore, a ≤ 1/2
**Transmission Delay:**  Tt = L / 4 × 103
Therefore,
a = (20 × 10-3 × 4 × 103) / L = 80 / L
Therefore,
80 / L ≤ 1/2 L ≥ 160 bits
**Correct Answer: 160 bits**

9

What is the throughput achievable in Stop-and-Wait protocol for a maximum packet size of 1000 bytes and a network span of 10 km? Assume the speed of light in the cable is 70% of the speed of light in vacuum.


**Answer:**  Packet size, L = 1000 bytes Distance, d = 10 km = 104 m Propagation speed, v = 0.7 × 3 × 108 = 2.1 × 108 m/s
**Formula:**  Propagation Delay, Tp = Distance / Propagation Speed Round-Trip Propagation Delay = 2Tp For the simplified calculation used here: Throughput = Packet Size / Round-Trip Propagation Delay
**Round-Trip Propagation Delay**  = (2 × 104) / (2.1 × 108) ≈ 9.524 × 10-5 s
**Throughput**  = 1000 / (9.524 × 10-5) ≈ 1.05 × 107 bytes/s
**Therefore, Throughput ≈ 10.5 MBps.**

10

If the packet size is 1 KB, propagation time is 15 ms, and channel bandwidth is 109 bits/sec, find the transmission time and sender utilization in Stop-and-Wait protocol.


**Answer:**  Packet size = 1 KB = 1024 bytes = 8192 bits Bandwidth = 109 bits/s Propagation delay = 15 ms
**Formula:**  Transmission Time, Tt = Packet Size / Bandwidth a = Tp / Tt Sender Utilization, η = 1 / (1 + 2a)
**Transmission Time (Tt)**  = 8192 / 109 = 8.192 μs
**a**  = 15 ms / 8.192 μs ≈ 1831.05
**Sender Utilization (η)**  = 1 / (1 + 2 × 1831.05) ≈ 0.000273 ≈  **0.0273%** </p


11

Consider a MAN with an average source and destination distance of 20 km and a one-way propagation delay of 100 μs. At what data rate does the round-trip delay equal the transmission delay for a 1 KB packet?


**Answer:**  Propagation delay = 100 μs Packet size = 1 KB = 1024 bytes = 8192 bits
**Formula:**  Round-Trip Delay = 2 × Propagation Delay Transmission Delay, Tt = Packet Size / Bandwidth
Given,
Transmission Delay = Round-Trip Delay
2 × 100 μs = 200 μs
Therefore,
Bandwidth = 8192 / (200 × 10-6) = 40.96 × 106 bits/s
**Therefore, Required Data Rate = 40.96 Mbps.**

12

Two hosts X and Y are connected by a direct link of rate 106 bits/sec. The distance between them is 10,000 km and the propagation speed is 2 × 108 m/sec. Host X sends a file of 50,000 bytes as one large message to Y. Find the transmission delay and propagation delay.


**Answer:**  Bandwidth = 106 bits/s Distance = 10,000 km = 107 m File size = 50,000 bytes Propagation speed = 2 × 108 m/s
**Formula:**  Transmission Delay, Tt = Packet/File Size / Bandwidth Propagation Delay, Tp = Distance / Propagation Speed
**Transmission Delay**  = (50,000 × 8) / 106 = 0.4 s =  **400 ms**
**Propagation Delay**  = 107 / (2 × 108) = 0.05 s =  **50 ms**
**Correct Answer: — p = 400 ms and q = 50 ms.**

13

A sender uses Stop-and-Wait ARQ for reliable transmission. Frames are 1000 bytes and the sender transmission rate is 80 Kbps. The acknowledgement size is 100 bytes and the receiver transmission rate is 8 Kbps. The one-way propagation delay is 100 ms. Assuming no frame is lost, find the sender throughput in bytes/sec.


**Formula:**  Data Frame Transmission Time = Frame Size / Sender Rate ACK Transmission Time = ACK Size / Receiver Rate Total Time = Data Transmission Time + 2 × Propagation Delay + ACK Transmission Time Efficiency = Useful Time / Total Time Throughput = Efficiency × Sender Bandwidth
**Data Frame Transmission Time**  = (1000 × 8) / (80 × 103) = 100 ms
**ACK Transmission Time**  = (100 × 8) / (8 × 103) = 100 ms
**Total Time**  = 100 + 100 + 100 + 100 = 400 ms
**Efficiency**  = 100 / 400 = 0.25 = 25%
**Sender Throughput**  = 0.25 × 80 Kbps = 20 Kbps
Throughput in bytes/sec = (20 × 1000) / 8 =  **2500 bytes/sec**



**Previous Job Question:**  Flow Control & Its Protocol



Topic Wise Question Bank

All Topics

- ☆

1

Computer Network
Flow Control Protocol

A satellite link has a one way propagation delay of 250 ms and a transmission rate 1 Mbps. Frame size 1000 bytes , calculate utilization efficiency if stop-and-wait protocol is used what is minimum window size required to achieve 100% efficiency.

RAKUB, ANSE, 26
| AME/ANE/AE

Given:    One-way propagation delay (Tp) = 250 ms = 0.25 s    Transmission rate (Bandwidth) = 1 Mbps = 106 bits/s    Frame size = 1000 bytes = 1000 × 8 = 8000 bits    Protocol: Stop-and-WaitStep 1: Calculate Transmission Time (Tt)
Tt = Frame size ÷ Bandwidth Tt = 8000 bits ÷ 106 bits/s = 0.008 s = 8 ms
Step 2: Calculate Round Trip Time (RTT)
RTT = 2 × Tp = 2 × 250 ms = 500 ms
Step 3: Calculate Efficiency (Utilization) for Stop-and-Wait
Efficiency = Tt ÷ (Tt + RTT)
Efficiency = 8 ÷ (8 + 500) = 8 ÷ 508
= 0.0157 Efficiency = 1.57%
Step 4: Calculate Minimum Window Size for 100% Efficiency For 100% efficiency, the sender must keep the channel fully utilized. This means the window size must be large enough so that the total transmission time of all frames in the window equals or exceeds the RTT.
Window size (N) = RTT ÷ Tt N = 500 ÷ 8 = 62.5 N = 63 frames (rounded up to the nearest whole number)
Alternatively, using the formula: Efficiency = (N × Tt) ÷ (Tt + RTT)
For 100% efficiency: N × Tt ≥ Tt + RTT N ≥ (Tt + RTT) ÷ Tt = (8 + 500) ÷ 8 = 63.5 N = 63 or 64 framesReference:

☆

2

Computer Network
Flow Control Protocol

Using an explanation of the difference between flow-control and congestion  control, Discuss the impact of a stable end-to-end latency.

Combined Bank, O(IT), 24
| Officer (IT)

**Flow-Control vs Congestion Control**

**Flow-Control:**  Flow-control manages the rate of data transmission between a sender and receiver to prevent the receiver's buffer from overflowing. It ensures the sender does not overwhelm the receiver.
**Congestion Control:**  Congestion control manages the overall traffic in the network to prevent network congestion. It reduces the sending rate when the network is overloaded to avoid packet loss and high delays.

**Impact of Stable End-to-End Latency**
Stable latency ensures that the time taken for data to travel from source to destination remains consistent, even under varying network loads.

**Improved QoS:**  Real-time applications like VoIP and video conferencing rely on consistent latency for smooth performance.
**Reduced Jitter:**  Low variation in latency leads to smoother audio and video playback.
**Efficient Flow-Control:**  Predictable latency helps flow-control algorithms maintain optimal data rates without overwhelming the receiver.
**Effective Congestion Control:**  With stable latency, network devices can detect congestion accurately and react appropriately, preventing unnecessary packet drops or retransmissions.
**Reliable Real-Time Systems:**  Industrial automation and control systems benefit from predictable delays, ensuring timely and safe operations.

**Flow-Control বনাম Congestion Control**

**Flow-Control:**  Flow-control sender এবং receiver-এর মধ্যে data transmission rate নিয়ন্ত্রণ করে, যাতে receiver-এর buffer overflow না হয়। এটি নিশ্চিত করে যে sender receiver-কে overwhelm করবে না।
**Congestion Control:**  Congestion control পুরো network-এ traffic নিয়ন্ত্রণ করে, যাতে network congested না হয়। Network overload হলে এটি sending rate কমায়, packet loss এবং high delays এড়াতে।

**Stable End-to-End Latency-এর প্রভাব**
Stable latency নিশ্চিত করে যে source থেকে destination পর্যন্ত data travel time ধ্রুবক থাকে, এমনকি network load পরিবর্তিত হলেও।

**Improved QoS:**  VoIP এবং video conferencing-এর মতো real-time applications smooth performance পায় consistent latency-র মাধ্যমে।
**Reduced Jitter:**  Latency variation কমলে smoother audio এবং video playback হয়।
**Efficient Flow-Control:**  Predictable latency flow-control algorithm-কে সাহায্য করে optimal data rate maintain করতে এবং receiver overwhelm হওয়া রোধ করতে।
**Effective Congestion Control:**  Stable latency থাকলে network devices congestion সঠিকভাবে detect করে এবং উপযুক্তভাবে react করে, unnecessary packet drop বা retransmission এড়াতে।
**Reliable Real-Time Systems:**  Industrial automation এবং control systems predictable delay-এর সুবিধা পায়, timely এবং safe operation নিশ্চিত হয়।

**Assigment:**   Flow Control & Its Protocol

#### Q1. Flow Control

What is Flow Control? Explain its purpose in computer networks and discuss why flow control is necessary between a fast sender and a slow receiver.

#### Q2. Flow Control Protocols

What are the different flow control protocols used for  **noiseless and noisy channels** ? Explain the basic characteristics of each protocol.

#### Q3. Stop-and-Wait Protocol

Explain the working principle of the  **Stop-and-Wait Protocol**  with a suitable example. Discuss its advantages and limitations.

#### Practical Scenario

A high-speed network has a long propagation delay. Explain why  **Stop-and-Wait Protocol**  may result in poor bandwidth utilization and why a  **Sliding Window Protocol**  would be more suitable.

#### Q4. Stop-and-Wait ARQ

What is  **Stop-and-Wait ARQ** ? Explain how ACK, timer, sequence number, and retransmission are used to provide reliable communication over a noisy channel.

#### Q5. Stop-and-Wait vs Stop-and-Wait ARQ

Differentiate between  **Stop-and-Wait Protocol**  and  **Stop-and-Wait ARQ**  based on flow control, error control, timer, sequence number, and retransmission.

#### Q6. Sliding Window Protocol

What is the  **Sliding Window Protocol** ? Explain its working principle and discuss how it improves bandwidth utilization compared with Stop-and-Wait ARQ.

#### Q7. Sliding Window Components

Explain the three states of frames in a Sliding Window Protocol:

- Sent and acknowledged
- Sent but not acknowledged
- Not yet sent

#### Q8. Optimal Window Size

Station A uses  **32-byte packets**  to transmit data to Station B. The RTT between A and B is  **80 ms** , and the bottleneck bandwidth is  **128 kbps** . Calculate the  **optimal window size** .

#### Q9. Sequence Number Field

Two stations M and N are separated by  **L km** . Each frame contains  **K bits** , the propagation time per kilometer is  **t seconds** , and the channel capacity is  **R bits/second** .

Derive the minimum number of bits required in the  **sequence number field**  for maximum channel utilization using the Sliding Window Protocol.

#### Q10. Stop-and-Wait Link Utilization

A communication line has a bandwidth of  **1.5 Mbps** , RTT is  **45 ms** , and packet size is  **1 KB** . Calculate the  **link utilization**  using the Stop-and-Wait Protocol.

#### Q11. Minimum Frame Size

A channel has a bit rate of  **4 Kbps**  and a one-way propagation delay of  **20 ms** . The channel uses Stop-and-Wait Protocol, and the transmission time of the ACK is negligible.

What should be the  **minimum frame size**  to achieve a channel efficiency of at least  **50%** ?

#### Q12. Stop-and-Wait Throughput

What is the throughput achievable in a Stop-and-Wait Protocol for a maximum packet size of  **1000 bytes**  and a network span of  **10 km** ? Assume the propagation speed in the cable is  **70% of the speed of light in vacuum** .

#### Q13. Transmission Time and Sender Utilization

A packet size is  **1 KB** , the propagation time is  **15 ms** , and the channel bandwidth is  **10⁹ bits/sec** .

Calculate:a) Transmission timeb) Sender utilization using Stop-and-Wait Protocol.

#### Q14. Required Data Rate

A MAN has an average source-to-destination distance of  **20 km**  and a one-way propagation delay of  **100 μs** . At what data rate will the  **round-trip delay equal the transmission delay**  for a  **1 KB packet** ?

#### Q15. Transmission and Propagation Delay

Two hosts X and Y are connected by a direct link with a data rate of  **10⁶ bits/sec** . The distance between them is  **10,000 km** , and the propagation speed is  **2 × 10⁸ m/sec** . Host X sends a file of  **50,000 bytes**  as one large message.

Calculate:a) Transmission delayb) Propagation delay

#### Q16 Numerical Problem — Sliding Window

A sender transmits  **1000-bit frames**  over a  **1 Mbps**  link. The RTT is  **40 ms** .

Calculate the minimum window size required to keep the link fully utilized.

#### Q17. Numerical Problem — Stop-and-Wait

A packet is  **2000 bits**  long and the transmission rate is  **500 Kbps** . The one-way propagation delay is  **20 ms** .

Calculate the Stop-and-Wait efficiency, assuming the ACK transmission time is negligible.



📘 Flow Control and Its Protocol

#### 1. In the sliding window method of flow control, the receiver window size ______ when frames are received.

#### 2. In the sliding window method of flow control, the receiver window size ______ when an ACK is sent.

#### 3. A sender has a sliding window of size 15. The first 15 frames are sent. The first ACK received is ACK 15. What frames has the receiver accepted?

#### 4. A sender has a sliding window of size 15. The first 15 frames are sent. The first ACK received is ACK 15. What frame is the receiver expecting?

#### 5. A sender has a sliding window of size 15. The first 15 frames are sent. How many frames are in the window now?

#### 6. A sender has a sliding window of size 15. The first 10 frames are sent. How many frames can still be sent before the window is full?

#### 7. A sender has a sliding window of size 15. The first 15 frames are sent. The receiver receives 10 frames. How many frames can the receiver still receive?

#### 8. A sender has a sliding window of size 15. The first 15 frames are sent. The receiver sends ACK 10. How many spaces does the receiver window expand?

#### 9. A sender has a sliding window of size 15. The first 15 frames are sent. The receiver sends ACK 10 and expands its window. What is the size of the receiver window now?

#### 10. The receiver's window in a sliding window protocol expands when ______.

#### 11. The sender's window in a sliding window protocol expands when ______.

#### 12. The stop-and-wait flow control method is the same as the sliding window method with a window size of ______.

#### 13. Flow control is mainly a function of the ______ layer.

#### 14. ______ is the regulation of the amount of data that can be sent.

#### 15. Which Data Link Layer function answers the question: How much data may be sent?

#### 16. Stop-and-wait is a ______ technique.

#### 17. Sliding window is a ______ technique.

#### 18. In the stop-and-wait method of flow control, the sender sends ______ at a time.

#### 19. In the sliding window method of flow control, the sender may send ______ at a time.

#### 20. In the stop-and-wait method of flow control, after the receiver receives a data frame, ______ frame can be sent.

#### 21. What is the main disadvantage of stop-and-wait flow control?

#### 22. In the stop-and-wait method of flow control, if 100 good data frames are sent and received, how many ACK frames have been sent by the receiver?

#### 23. In the sliding window method of flow control, if 100 good data frames are sent and received, how many ACK frames may be sent by the receiver?

#### 24. In the sliding window method of flow control, if the frame numbers range from 0 to 31, the size of the window is ______ frames.

#### 25. In the sliding window method of flow control, if the frame numbers range from 0 to 63, the size of the window is ______ frames.

#### 26. In the sliding window method of flow control, the sender window ______ size when frames are sent.

#### 27. In the sliding window method of flow control, the sender window ______ size when an ACK is received.
