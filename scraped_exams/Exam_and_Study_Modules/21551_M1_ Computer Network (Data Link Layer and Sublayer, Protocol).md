# M1: Computer Network (Data Link Layer and Sublayer, Protocol)

- **Original URL:** [https://it.jobqns.com/computer-network-datalink-layer-sublayer-protocol/](https://it.jobqns.com/computer-network-datalink-layer-sublayer-protocol/)
- **Date:** 2026-08-22T17:38:14
- **Categories:** Uncategorized, IT Preparation Module

---

Data Link Layer and Sub-layer, Protocol (ET: 1.5 hours)



**Video Tutorial:**  Data Link Layer and Sublayer, Protocol



- **Watch Video:**  Link Layer Services

- **Watch Video:**   Sublayer of Data Link Layer (LLC & MAC)

- **Watch Video:**  Data Link Control Protocol : HDLC

- **Watch Video:**  Bit Stuffing

Topic Wise Question Bank


Data Link Layer


- 1

Data Link Layer

Data link Layer Services

Introduction to Data Link Layer Services


Data Link Layer

**Data Link Layer:**  The Data Link Layer is the  **2nd layer**  of the OSI Model. It is also called the  **Link Layer** . It receives a packet from the Network Layer and adds a header and trailer to create a  **Frame** . Its main responsibility is to provide reliable  **node-to-node communication** .
**Five Main Services of the Data Link Layer:**

**Framing**
**Physical Addressing**
**Flow Control**
**Error Control**
**Access Control**

**1. Framing:**  Framing is the process of dividing the stream of bits received from the Network Layer into manageable units called  **Frames** . It helps the receiver distinguish one frame from another. The Data Link Layer adds a header and trailer to the Network Layer packet to form a frame.
**Example:**  Just as an envelope separates one letter from another, framing separates one data unit from another.
**2. Physical Addressing:**  The Data Link Layer adds the  **Source MAC Address**  and  **Destination MAC Address**  to the frame. MAC addresses are physical addresses used for communication between devices on the same network or link.
**3. Flow Control:**  Flow control is a  **speed-matching mechanism**  between a sender and a receiver. It prevents a fast sender from overwhelming a slow receiver. The sender controls the amount of data it sends based on the receiver's ability to process the data.
**Example:**  If a receiver can handle only 10 packets at a time, the sender should not continuously send 100 packets without allowing the receiver to process them.
**4. Error Control:**  Error control deals with errors that may occur while a frame is being transmitted. The Data Link Layer can use  **Error Detection**  and, in some systems,  **Error Correction**  mechanisms. If an error is detected, the frame may be discarded or retransmitted depending on the protocol.
**5. Access Control:**  Access control determines which device can use a  **shared communication medium**  at a particular time. It helps prevent or manage collisions when multiple devices want to transmit data through the same medium. This is commonly associated with  **Media Access Control (MAC)** .

**Data Link Layer:**  Data Link Layer হলো OSI Model-এর  **2nd Layer** । একে  **Link Layer** -ও বলা হয়। এটি Network Layer থেকে একটি Packet গ্রহণ করে এবং এর সাথে Header ও Trailer যুক্ত করে একটি  **Frame**  তৈরি করে। Data Link Layer-এর প্রধান দায়িত্ব হলো নির্ভরযোগ্য  **Node-to-Node Communication**  প্রদান করা।
**Data Link Layer-এর পাঁচটি প্রধান Service:**
**1. Framing**
**2. Physical Addressing**
**3. Flow Control**
**4. Error Control**
**5. Access Control**
**1. Framing:**  Framing হলো Network Layer থেকে প্রাপ্ত Bit Stream-কে ছোট ও পরিচালনাযোগ্য Unit বা  **Frame** -এ ভাগ করার প্রক্রিয়া। এর মাধ্যমে Receiver একটি Frame থেকে অন্য Frame-কে আলাদা করে শনাক্ত করতে পারে। Data Link Layer Network Layer-এর Packet-এর সাথে Header এবং Trailer যুক্ত করে একটি Frame তৈরি করে।
**Example:**  যেমন একটি Envelope একটি চিঠিকে অন্য চিঠি থেকে আলাদা করে রাখে, তেমনি Framing একটি Data Unit-কে অন্য Data Unit থেকে আলাদা করতে সাহায্য করে।
**2. Physical Addressing:**  Data Link Layer Frame-এর মধ্যে  **Source MAC Address**  এবং  **Destination MAC Address**  যুক্ত করে। MAC Address হলো একটি Physical Address, যা একই Network বা Link-এর মধ্যে Device-গুলোর মধ্যে Communication-এর জন্য ব্যবহৃত হয়।
**3. Flow Control:**  Flow Control হলো Sender এবং Receiver-এর মধ্যে একটি  **Speed-Matching Mechanism** । এটি দ্রুতগতির Sender যেন ধীরগতির Receiver-কে অতিরিক্ত Data দিয়ে Overwhelm করতে না পারে তা নিশ্চিত করে। Receiver কতটুকু Data Process করতে সক্ষম, তার ওপর ভিত্তি করে Sender তার Data Transmission-এর পরিমাণ নিয়ন্ত্রণ করে।
**Example:**  যদি একটি Receiver একসাথে সর্বোচ্চ 10টি Packet Process করতে পারে, তাহলে Sender-এর উচিত নয় Receiver-কে Process করার সুযোগ না দিয়ে ক্রমাগত 100টি Packet পাঠানো।
**4. Error Control:**  Error Control হলো Frame Transmission-এর সময় যে Error হতে পারে তা নিয়ন্ত্রণ করার ব্যবস্থা। Data Link Layer-এ  **Error Detection**  এবং কিছু System-এ  **Error Correction**  Mechanism ব্যবহার করা হয়। কোনো Error শনাক্ত হলে Protocol অনুযায়ী Frame-টি Discard করা হতে পারে অথবা পুনরায় Transmit করা হতে পারে।
**5. Access Control:**  Access Control নির্ধারণ করে একটি  **Shared Communication Medium**  কোনো নির্দিষ্ট সময়ে কোন Device ব্যবহার করতে পারবে। একই Medium-এর মাধ্যমে একাধিক Device Data Transmit করতে চাইলে Collision হতে পারে। Access Control এই ধরনের Collision প্রতিরোধ বা নিয়ন্ত্রণ করতে সাহায্য করে। এটি সাধারণত  **Media Access Control (MAC)** -এর সাথে সম্পর্কিত।

- 2

Data Link Layer

Data link SubLayer Services

Sublayer of Data Link Layer ( Logical Link Control, MAC Sublayer)


Data Link Layer

**Data Link Layer**  is the  **Layer 2**  of the OSI Reference Model. The Data Link Layer is divided into two sublayers:

**Logical Link Control (LLC) Sublayer**
**Media Access Control (MAC) Sublayer**

The two sublayers work together to provide services such as flow control, framing, physical addressing, error control, and media access control.
**Data Link Layer Structure**

**1. Logical Link Control (LLC) Sublayer**
The  **Logical Link Control (LLC)**  is the upper sublayer of the Data Link Layer. It provides communication between the Network Layer and the lower Data Link Layer functions.
The LLC sublayer receives the  **Network Layer PDU (Packet)**  and adds necessary control information to support reliable communication and Data Link Layer services.
**Major Responsibility of LLC**

Provides an interface between the Network Layer and Data Link Layer.
Handles  **Flow Control** .
Adds necessary control information to the data received from the Network Layer.
Helps coordinate communication between upper-layer protocols and Data Link Layer functions.

**Important Point:**  Among the five commonly discussed Data Link Layer services,  **Flow Control**  is associated with the LLC/DLC sublayer in this model.
**2. Media Access Control (MAC) Sublayer**
The  **Media Access Control (MAC)**  is the lower sublayer of the Data Link Layer. It is located directly above the Physical Layer and interacts directly with the physical transmission medium.
The MAC sublayer is commonly implemented in hardware, particularly as part of the  **Network Interface Card (NIC)** .
The MAC sublayer has two major responsibilities:

**Data Encapsulation**
**Media Access Control**

**2.1 Data Encapsulation**
Data encapsulation is the process of preparing the Network Layer packet for transmission over the physical medium.
The MAC sublayer adds a  **Header**  and a  **Trailer**  to the Network Layer PDU. As a result, the Data Link Layer PDU becomes a  **Frame** .
**Packet + MAC Header + MAC Trailer = Frame**
The MAC sublayer performs two important operations:

**Frame Assembly:**  At the sender side, the MAC sublayer constructs a frame by adding the required header and trailer.
**Frame Disassembly:**  At the receiver side, the MAC sublayer receives the frame and removes the Data Link Layer header and trailer to extract the packet.

**2.2 Primary Functions of MAC Sublayer**
The MAC sublayer performs the following important Data Link Layer functions:

**Framing**  — Converts the Network Layer packet into a Data Link Layer frame by adding a header and trailer.
**Physical Addressing / MAC Addressing**  — Uses MAC addresses to identify devices on the local network.
**Error Control**  — Provides mechanisms for detecting transmission errors, commonly using techniques such as FCS/CRC in many frame formats.
**Media Access Control**  — Determines how devices access and use a shared transmission medium.

**Responsibilities of LLC and MAC Sublayers**

Data Link Layer Service
Responsible Sublayer
Short Explanation

Flow Control
**LLC**
Controls the rate of data transmission between sender and receiver.

Framing
**MAC**
Creates frames from Network Layer packets.

Physical Addressing
**MAC**
Uses source and destination MAC addresses.

Error Control
**MAC**
Helps detect transmission errors in frames.

Access Control
**MAC**
Controls access to the shared transmission medium.

**LLC vs MAC Sublayer**

Feature
LLC Sublayer
MAC Sublayer

Full Form
Logical Link Control
Media Access Control

Position
Upper sublayer
Lower sublayer

Located Above
Network Layer functions
LLC

Located Below
MAC
Physical Layer

Main Responsibility
Flow Control
Framing, Physical Addressing, Error Control and Media Access Control

Physical Layer Interaction
Indirect
Direct

Hardware Implementation
Generally associated with logical functions
Commonly implemented in NIC hardware

**How Data Moves Through the Data Link Sublayers**
When a packet comes from the Network Layer, it first reaches the Data Link Layer. The  **LLC sublayer**  handles the logical link-control functions and flow-control aspects. The data then reaches the  **MAC sublayer** , where the packet is encapsulated into a frame by adding the required header and trailer.
The MAC sublayer also handles MAC addressing, error detection, and access to the physical medium. Finally, the frame is passed to the  **Physical Layer**  for transmission as signals over the communication medium.
At the receiving side, the Physical Layer receives the signal and passes the received frame to the MAC sublayer. The MAC sublayer processes the frame and removes the Data Link Layer encapsulation. The resulting packet is then passed upward toward the Network Layer.
**Simple Flow:**
Network Layer →  **LLC**  →  **MAC**  → Physical Layer → Transmission Medium
**Receiver Side:**
Transmission Medium → Physical Layer →  **MAC**  →  **LLC**  → Network Layer

**Data Link Layer**  হলো OSI Reference Model-এর  **Layer 2** । Data Link Layer দুটি Sublayer-এ বিভক্ত:
**1. Logical Link Control (LLC) Sublayer**
**2. Media Access Control (MAC) Sublayer**
এই দুটি Sublayer একসাথে Flow Control, Framing, Physical Addressing, Error Control এবং Media Access Control-এর মতো গুরুত্বপূর্ণ Service প্রদান করে।
**Data Link Layer Structure**
**1. Logical Link Control (LLC) Sublayer**
**Logical Link Control (LLC)**  হলো Data Link Layer-এর Upper Sublayer। এটি Network Layer এবং Data Link Layer-এর Lower Functions-এর মধ্যে Communication Interface হিসেবে কাজ করে।
LLC Sublayer Network Layer থেকে  **Network Layer PDU (Packet)**  গ্রহণ করে এবং Reliable Communication ও Data Link Layer-এর বিভিন্ন Service পরিচালনার জন্য প্রয়োজনীয় Control Information যুক্ত করে।
**LLC-এর প্রধান দায়িত্ব:**
Network Layer এবং Data Link Layer-এর মধ্যে একটি Interface প্রদান করা।
**Flow Control**  পরিচালনা করা।
Network Layer থেকে প্রাপ্ত Data-এর সাথে প্রয়োজনীয় Control Information যুক্ত করা।
Upper-Layer Protocol এবং Data Link Layer-এর Function-এর মধ্যে Communication Coordinate করতে সাহায্য করা।
**গুরুত্বপূর্ণ বিষয়:**  Data Link Layer-এর সাধারণভাবে আলোচিত পাঁচটি Service-এর মধ্যে এই Model-এ  **Flow Control**  মূলত LLC/DLC Sublayer-এর সাথে সম্পর্কিত।
**2. Media Access Control (MAC) Sublayer**
**Media Access Control (MAC)**  হলো Data Link Layer-এর Lower Sublayer। এটি সরাসরি Physical Layer-এর উপরে অবস্থান করে এবং Physical Transmission Medium-এর সাথে সরাসরি Interaction করে।
MAC Sublayer সাধারণত Hardware-এর মাধ্যমে Implement করা হয় এবং বিশেষ করে  **Network Interface Card (NIC)** -এর একটি অংশ হিসেবে এটি Implement হতে পারে।
MAC Sublayer-এর দুটি প্রধান দায়িত্ব হলো:
**1. Data Encapsulation**
**2. Media Access Control**
**2.1 Data Encapsulation**
Data Encapsulation হলো Network Layer-এর Packet-কে Physical Medium-এর মাধ্যমে Transmission-এর উপযোগী করার প্রক্রিয়া। MAC Sublayer Network Layer PDU-এর সাথে একটি  **Header**  এবং একটি  **Trailer**  যুক্ত করে। এর ফলে Data Link Layer PDU একটি  **Frame** -এ পরিণত হয়।
**Packet + MAC Header + MAC Trailer = Frame**
MAC Sublayer Data Encapsulation-এর সময় দুটি গুরুত্বপূর্ণ Operation সম্পন্ন করে।
**Frame Assembly:**  Sender Side-এ MAC Sublayer প্রয়োজনীয় Header এবং Trailer যুক্ত করে একটি Frame তৈরি করে।
**Frame Disassembly:**  Receiver Side-এ MAC Sublayer Frame গ্রহণ করে এবং Data Link Layer-এর Header ও Trailer সরিয়ে মূল Packet বের করে।
**2.2 MAC Sublayer-এর প্রধান Function**
**Framing:**  Header এবং Trailer যুক্ত করে Network Layer Packet-কে Data Link Layer Frame-এ রূপান্তর করে।
**Physical Addressing / MAC Addressing:**  Local Network-এর Device শনাক্ত করার জন্য Source এবং Destination MAC Address ব্যবহার করে।
**Error Control:**  Transmission-এর সময় Frame-এ সংঘটিত Error শনাক্ত করার ব্যবস্থা প্রদান করে। অনেক Frame Format-এ Error Detection-এর জন্য  **FCS**  এবং  **CRC** -এর মতো Technique ব্যবহার করা হয়।
**Media Access Control:**  Shared Transmission Medium-এ বিভিন্ন Device কীভাবে Access করবে এবং Medium ব্যবহার করবে তা নির্ধারণ ও নিয়ন্ত্রণ করে।
**LLC এবং MAC Sublayer-এর দায়িত্ব**

**Data Link Layer Service**
**Responsible Sublayer**
**সংক্ষিপ্ত ব্যাখ্যা**

Flow Control
**LLC**
Sender এবং Receiver-এর মধ্যে Data Transmission-এর Rate নিয়ন্ত্রণ করে।

Framing
**MAC**
Network Layer Packet থেকে Frame তৈরি করে।

Physical Addressing
**MAC**
Source এবং Destination MAC Address ব্যবহার করে।

Error Control
**MAC**
Frame-এর Transmission Error শনাক্ত করতে সাহায্য করে।

Access Control
**MAC**
Shared Transmission Medium-এ Access নিয়ন্ত্রণ করে।

**LLC বনাম MAC Sublayer**

**Feature**
**LLC Sublayer**
**MAC Sublayer**

Full Form
Logical Link Control
Media Access Control

Position
Upper Sublayer
Lower Sublayer

Located Above
Network Layer Functions
LLC

Located Below
MAC
Physical Layer

Main Responsibility
Flow Control
Framing, Physical Addressing, Error Control এবং Media Access Control

Physical Layer Interaction
Indirect
Direct

Hardware Implementation
সাধারণত Logical Function-এর সাথে সম্পর্কিত
সাধারণত NIC Hardware-এ Implement করা হয়

**Data Link Sublayer-এর মধ্য দিয়ে Data কীভাবে প্রবাহিত হয়**
Network Layer থেকে একটি Packet এলে এটি প্রথমে Data Link Layer-এ প্রবেশ করে। এরপর  **LLC Sublayer**  Logical Link-Control Function এবং Flow Control-এর দিকগুলো পরিচালনা করে। তারপর Data  **MAC Sublayer** -এ যায়, যেখানে প্রয়োজনীয় Header এবং Trailer যুক্ত করে Packet-কে একটি Frame-এ Encapsulate করা হয়।
MAC Sublayer MAC Addressing, Error Detection এবং Physical Medium-এ Access-এর কাজও পরিচালনা করে। এরপর Frame-টি Signal হিসেবে Communication Medium-এর মাধ্যমে Transmission-এর জন্য  **Physical Layer** -এ পাঠানো হয়।
Receiver Side-এ Physical Layer Signal গ্রহণ করে এবং প্রাপ্ত Frame-টি MAC Sublayer-এ পাঠায়। MAC Sublayer Frame-টি Process করে এবং Data Link Layer-এর Encapsulation সরিয়ে দেয়। এরপর প্রাপ্ত Packet LLC-এর মাধ্যমে উপরের দিকে Network Layer-এর কাছে পাঠানো হয়।
**Simple Flow:**
Network Layer →  **LLC**  →  **MAC**  → Physical Layer → Transmission Medium
**Receiver Side:**
Transmission Medium → Physical Layer →  **MAC**  →  **LLC**  → Network Layer

- 3

Data Link Layer

DLL Protocol

HDLC (High-Level Data Link Control), Bit Stuffing


Data Link Layer

**HDLC (High-Level Data Link Control)**
HDLC is a  **bit-oriented Data Link Layer protocol**  used for reliable communication over data links. It was standardized by ISO and was based on IBM's SDLC (Synchronous Data Link Control).
**Bit-Oriented Protocol:**  In a bit-oriented protocol, a frame is treated as a sequence or collection of bits rather than a collection of characters.
**HDLC Frame Format:**
**Flag | Address | Control | Information | FCS/CRC | Flag**

Field
Purpose

**Flag**
Marks the beginning and end of a frame. The standard flag pattern is  **01111110** .

**Address**
Identifies the station involved in the communication.

**Control**
Controls the type and operation of the HDLC frame.

**Information**
Carries data received from the Network Layer. Its size is variable.

**FCS/CRC**
Used for error detection.

**HDLC Frame Types**

**I-Frame (Information Frame)**  — Carries user data and supports sequencing and acknowledgments.
**S-Frame (Supervisory Frame)**  — Used mainly for flow and error control.
**U-Frame (Unnumbered Frame)**  — Used for link management and other control functions.

**Control Field Identification:**

Control Field Starting Bits
Frame Type

**0**
I-Frame

**10**
S-Frame

**11**
U-Frame

**Bit Stuffing in HDLC**
**Bit Stuffing**  is a technique used in HDLC to prevent the data from being confused with the special  **Flag pattern 01111110** .
**Problem:**  The Flag pattern contains  **six consecutive 1s** . If a similar pattern occurs inside the actual data, the receiver might incorrectly interpret it as the end of the frame.
**Solution:**  The sender inserts a  **0 after every sequence of five consecutive 1s**  in the data.
**Example:**
Original data:  **01111110**
After bit stuffing:  **011111010**
Here, a  **0**  is inserted after the fifth consecutive  **1** .
**At the Receiver:**  The receiver removes the inserted  **0**  whenever it detects a zero following five consecutive 1s. This process is called  **bit destuffing** .

**HDLC (High-Level Data Link Control)**
HDLC হলো একটি  **bit-oriented Data Link Layer protocol** , যা Data Link-এর মাধ্যমে নির্ভরযোগ্য Communication-এর জন্য ব্যবহৃত হয়। এটি ISO দ্বারা Standardized এবং IBM-এর  **SDLC (Synchronous Data Link Control)** -এর উপর ভিত্তি করে তৈরি করা হয়েছিল।  **Bit-Oriented Protocol:**  Bit-oriented Protocol-এ একটি Frame-কে Character-এর সমষ্টি হিসেবে নয়, বরং ধারাবাহিকভাবে সাজানো একটি Sequence বা Collection of Bits হিসেবে বিবেচনা করা হয়।  **HDLC Frame Format:**   **Flag | Address | Control | Information | FCS/CRC | Flag**

Field
উদ্দেশ্য

**Flag**
Frame-এর শুরু এবং শেষ নির্দেশ করে। Standard Flag Pattern হলো  **01111110** ।

**Address**
Communication-এ অংশগ্রহণকারী Station-কে শনাক্ত করে।

**Control**
HDLC Frame-এর Type এবং Operation নিয়ন্ত্রণ করে।

**Information**
Network Layer থেকে প্রাপ্ত Data বহন করে। এর Size পরিবর্তনশীল।

**FCS/CRC**
Transmission-এর সময় Error Detection-এর জন্য ব্যবহৃত হয়।

**HDLC Frame Types**
**1. I-Frame (Information Frame)**  — User Data বহন করে এবং Sequencing ও Acknowledgment-এর মতো কার্যক্রম Support করে।
**2. S-Frame (Supervisory Frame)**  — প্রধানত Flow Control এবং Error Control-এর জন্য ব্যবহৃত হয়।
**3. U-Frame (Unnumbered Frame)**  — Link Management এবং অন্যান্য Control Function-এর জন্য ব্যবহৃত হয়।
**Control Field Identification:**

Control Field Starting Bits
Frame Type

**0**
I-Frame

**10**
S-Frame

**11**
U-Frame

**Bit Stuffing in HDLC**
**Bit Stuffing**  হলো HDLC-এর একটি গুরুত্বপূর্ণ Technique, যার মাধ্যমে Data-এর মধ্যে থাকা Bit Pattern যেন বিশেষ  **Flag Pattern 01111110** -এর সাথে ভুলভাবে মিলে না যায় তা নিশ্চিত করা হয়।
**সমস্যা:**  HDLC-এর Flag Pattern  **01111110** -এ পরপর ছয়টি  **1**  রয়েছে। যদি একই ধরনের Bit Pattern প্রকৃত Data-এর মধ্যেও থাকে, তাহলে Receiver সেটিকে ভুলভাবে Frame-এর শেষ বা Flag হিসেবে শনাক্ত করতে পারে।
**সমাধান:**  Sender Data-এর মধ্যে পরপর পাঁচটি  **1**  পাওয়ার পর একটি  **0**  Insert করে। অর্থাৎ, Data-এর মধ্যে যখনই পরপর পাঁচটি  **1**  থাকে, তার পরে একটি অতিরিক্ত  **0**  যুক্ত করা হয়।
**Example:**
Original Data:  **01111110**
After Bit Stuffing:  **011111010**
এখানে পরপর পাঁচটি  **1** -এর পরে একটি অতিরিক্ত  **0**  Insert করা হয়েছে। এর ফলে Data-এর Bit Pattern-কে HDLC-এর Flag Pattern থেকে আলাদা রাখা যায়।
**At the Receiver:**  Receiver যখন পরপর পাঁচটি  **1** -এর পরে একটি  **0**  শনাক্ত করে, তখন সেই  **0** -কে Inserted Bit হিসেবে Remove করে। এই প্রক্রিয়াকে  **Bit Destuffing**  বলা হয়।



**Assigment:**  Data Link Layer Services and Protocol



- Explain briefly about the Services of  Data Link Layer.
- Explain LLC Layer and MAC Layer
- What is HDLC?
- Find The bit sequence after bit stuffing: 110101111101011111101011111110
