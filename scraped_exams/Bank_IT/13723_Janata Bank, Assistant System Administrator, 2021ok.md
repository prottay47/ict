# Janata Bank, Assistant System Administrator, 2021ok

- **Original URL:** [https://it.jobqns.com/janata-bank-assistant-system-administrator-2021/](https://it.jobqns.com/janata-bank-assistant-system-administrator-2021/)
- **Date:** 2026-03-09T00:42:13
- **Categories:** Bank IT Job Solution 2021, Job Solution 2021

---

AME/ANE/AE • Year 2021

Janata Bank

💼Post Name: Assistant System Administrator

🏛Exam Taker: CTI

📅Exam Date: 20-Dec-2021

- ☆

1

Linux Command

(a)Write Shell command which make a folder name 'A' with read permission access only.

```
mkdir A
chmod 400 A
```


☆

2

Linux Command

(b)Write Shell command which copy folder 'A' all information into folder 'P'. Folder 'A' and folder 'P's parent folder is same.

```
cp -r A P
```


☆

3

Theory of Computation

Give regular expressions that generate, The language {w|w contains at least two a's, or exactly two b's}.

The language is:
**{ w | w contains at least two a's, OR exactly two b's }**
**Regular Expressions:**
**Strings with at least two a's:**
(b|a)* a (b|a)* a (b|a)*
**Strings with exactly two b's:**
a* b a* b a*
**Combined Regular Expression (Union):**
((a|b)*a(a|b)*a(a|b)*) | (a*b a*b a*)

☆

4

Microprocessor & Computer Architecture

Consider a hard disk with: 4 surfaces, 64 tracks/surface, 128 sectors/track, 256 ytes/sector, what is the capacity of the hard disk?

**Given:**
Surfaces = 4
Tracks per surface = 64
Sectors per track = 128
Bytes per sector = 256 bytes
**Disk Capacity Formula:**
Capacity = Surfaces × Tracks per surface × Sectors per track × Bytes per sector
Total sectors = 4 × 64 × 128
= 256 × 128
= 32,768 sectors
Total capacity = 32,768 × 256 bytes
=  **8,388,608 bytes**
**Convert to MB:**
1 MB = 1,048,576 bytes
8,388,608 ÷ 1,048,576 =  **8 MB**
**Answer:**
Disk Capacity ≈  **8 MB**

☆

5

Object Oriented Programming

An Abstract class Player with two sub class Bowler and Batsman, Abstract class have me abstract method average, also have constructor and a string function that display ame bowler or batsman. Batsman class implement abstract function average and isplay result, Batsman class have run and number match data. Now write a Java rogram and show Batsman average run.

```
abstract class Player {
String name;

// Constructor
Player(String name) {
this.name = name;
}

// Abstract method
abstract double average();

// Display player type
String displayType(String type) {
return "Player Type: " + type;
}
}

// Batsman class
class Batsman extends Player {
int runs;
int matches;

// Constructor
Batsman(String name, int runs, int matches) {
super(name);
this.runs = runs;
this.matches = matches;
}

// Implement abstract method
@Override
double average() {
return (double) runs / matches;
}

// Display Batsman result
void displayResult() {
System.out.println(displayType("Batsman"));
System.out.println("Name: " + name);
System.out.println("Total Runs: " + runs);
System.out.println("Number of Matches: " + matches);
System.out.println("Batting Average: " + average());
}
}

// Bowler class
class Bowler extends Player {

Bowler(String name) {
super(name);
}

// Implement abstract method
@Override
double average() {
return 0;
}

// Display Bowler result
void displayResult() {
System.out.println(displayType("Bowler"));
System.out.println("Name: " + name);
System.out.println("Bowler average is not calculated here.");
}
}

// Main class
public class Main {
public static void main(String[] args) {

// Create Batsman object
Batsman batsman = new Batsman("Rahim", 500, 10);

// Display batsman information
batsman.displayResult();
}
}
```

```
Player Type: Batsman
Name: Rahim
Total Runs: 500
Number of Matches: 10
Batting Average: 50.0
```

- ☆

6

Operating System
Deadlock

What is Deadlock? Explain two situations where deadlock condition occurs.

**Deadlock**  is a situation in an Operating System where two or more processes are unable to continue execution because each process is waiting for a resource that is held by another process.
**Two Situations Where Deadlock Occurs**

**Mutual Exclusion:**  A resource can be used by only one process at a time. If another process requests the same resource, it must wait until the resource is released.
**Circular Wait:**  Deadlock occurs when a group of processes form a circular chain where each process is waiting for a resource held by the next process in the chain.

- ☆

7

Computer Network
Subnetting

Consider the IP address 10.20.30.0/25 now answer the below question: a. What is the subnet mask of the above IP address? b. How many host per subnet have? c. What is the Broadcast address of this 10.20.30.0/3 IP address?

**Given:**
IP Address = 10.20.30.0/25
**a) Subnet Mask**
A  **/25**  prefix means 25 bits are used for the network.
Subnet Mask =  **255.255.255.128**
Binary form:
11111111.11111111.11111111.10000000
**b) Number of hosts per subnet**
Host bits = 32 − 25 =  **7 bits**
Total IP addresses per subnet = 27 =  **128**
Usable hosts = 128 − 2 =  **126 hosts**
(2 addresses are reserved for network and broadcast)
**c) Broadcast address**
With /25, each subnet block size =  **128** .
Subnet range:
10.20.30.0 → 10.20.30.127
Network address =  **10.20.30.0**
Broadcast address =  **10.20.30.127**
Usable host range:
10.20.30.1 – 10.20.30.126
**Final Answers:**

Question
Answer

Subnet Mask
255.255.255.128

Hosts per subnet
126 usable hosts

Broadcast Address
10.20.30.127

- ☆

8

Database Management System
ER Diagram

Given a scenario about football Game (Game_no, game time, game_name), Team (team-id, coach_id, team-name), Coach (Coach-id, Coach-name) Player (player-id, palyer- name, player-position), Stadium information (stadium-id, stadium-name, stadium-loc) Match (match_id, match date, match_result). i. Draw ER diagram

- ☆

9

Operating System
Memory Management

In the given example, let us assume the jobs and the memory requirements as the following: Job1 = 90k, Job2 = 20k, Job350k, Job4=200k. Let the free pace memory allocation blocks be: Block1= 50k, Block2= 100k, Block3=90k, Block4=200k, Block5 50k. Now show Best Fit Method and first fit method memory allocation. [Similar Question but value cannot exactly remember.]

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

- ☆

10

Operating System
Process Scheduling Algorithm

Calculate The Average Waiting Time of  SJF scheduling algorithm.    Process Burst Time Arrival Time   P1 10 3   P2 1 1   P3 2 3   P4 1 4   P5 5 2    (i) Average waiting time for FCFS (ii) Preemptive SJF(iii) Round Robin (Quantum time: 3) scheduling algorithm

- ☆

11

Design Analysis of Algorithm
Shortest Path

Shortest Path Algorithm.

```
Dijkstra(G, s)
for each vertex v in G
dist[v] = infinity
visited[v] = false

dist[s] = 0

for i = 1 to number of vertices
u = vertex with minimum dist[u] among unvisited vertices
visited[u] = true

for each neighbor v of u
if visited[v] == false and dist[u] + w(u,v) < dist[v]
dist[v] = dist[u] + w(u,v)

return dist
```

- ☆

12

Non Technical Question
Non Tech

Non-Dept (5*10-50)1.  **রচনাঃ সামাজিক মূল্যবোধ বৃদ্ধিতে দেশীয় সংস্কৃতির গুরুত্ব ব্যাখ্যা কর।**
2.  **Write an Essay: climate change impact in Bangladesh.**
3.  **Bangla to English Translation:**
4.  **English to Bangla Translation::**
**5.Short Question [5*2-10]**
a.SWIFT full form.
b.Which international organization help Rohingya?
c. Where "Golden Gate" Situated?
