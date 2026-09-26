# CAAB, Assistant Programmer, 2022

- **Original URL:** [https://it.jobqns.com/caab-assistant-programmer-2022/](https://it.jobqns.com/caab-assistant-programmer-2022/)
- **Date:** 2026-02-19T12:18:21
- **Categories:** Job Solution 2022, Other IT Job Solution, Other IT Job Solution 2022

---

#### Civil Aviation Authority of Bangladesh
Post: Assistant ProgrammerExam Date: 2022, Exam Taker: CAAB



[Question Pattern: Bangla=15, English: 15; Math: 20; Technical: 30] Technical=30



1. Write a c/c++ program to find the sum of digits.
```
#include
using namespace std;

int main() {
int n, sum = 0, m;
cout << "Enter a Number= "; cin >> n;
while (n > 0) {
m = n % 10;
sum = sum + m;
n = n / 10;
}
cout << "Summation of Every Digit = " << sum << endl;
return 0;
}
```

input: Enter a Number= 1234output: Summation of Every Digit = 10

2.Draw A flowchart of the following series:
1+3+5+7+......+N

3. Write down the difference between Compiler and Interpreter.

4. Number Conversion:
i. (4673)8=()16
ii. (7491)10=()16

#### Conversion of (4673)8 to Base 16

#### Base 8 to Decimal Calculation:

(4673)8 = (4 × 83) + (6 × 82) + (7 × 81) + (3 × 80)= (2491)10

#### Decimal to Base 16 Calculation:

Divide the decimal number by 16 to get the digits from the remainders:

DivisionQuotientRemainderDigit2491 / 1615511B155 / 16911B9 / 16099

Thus, (4673)8 = (9BB)16.

#### Conversion of (7491)10 to Base 16

#### Decimal to Base 16 Calculation:

Divide the decimal number by 16 to get the digits from the remainders:

DivisionQuotientRemainderDigit7491 / 1646830468 / 16294129 / 16113D1 / 16011

Thus, (7491)10 = (1D43)16.



5. Write Short Answer on the following  (1*10=10)



(a) What is computer network?

A computer network is a system that connects two or more devices for transmitting and sharing information. These devices can communicate through physical wires or wirelessly.1

(b)What is Constructor?

A constructor in C++ is a special method that is automatically called when an object of a class is created. The constructor has the same name as the class and is followed by parentheses
```
()
```
.

```
class MyClass {
public:
MyClass() { // Constructor
cout << "Hello World!";
}
};

int main() {
MyClass myObj; // Object creation (constructor is called)
return 0;
}
```

(c) What is full meaning of SDLC?

Software Development Life Cycle.

(d)Write the HTML Code to add Google URL.
```
<a href="https://www.google.com/">Visit Google.com</a>;
```

(e) What is DDL and DML?
- **DDL (Data Definition Language):** Used to define data structures like creating or altering tables in SQL. **Example:**
```
CREATE TABLE
```
,
```
ALTER TABLE
```
.
- **DML (Data Manipulation Language):** Used to manipulate data itself like inserting, updating, or deleting data. **Example:**
```
INSERT
```
,
```
UPDATE
```
,
```
DELETE
```
.

(f)What is Trojan Horse Virus?

A Trojan Horse or Trojan is malicious software disguised as legitimate software. It is designed to harm, steal, or disrupt data and networks.

(g) Define Full duplex with an example.

Full-duplex communication allows simultaneous data transmission and reception between two devices. It is twice as fast as half-duplex communication. **Example:**  Communication over two separate wire pairs or channels like mobile call.

(h) h. X+X'Y=?
- X + X’Y
- = (X + X’) + X’Y
- = 1 + X’Y (Complement Law)
- = 1 (Final Answer)

(i) Write the syntax of while and do while loop.

```
while
```
loop syntax:

```
while (testExpression) {
// body of the loop
}
```

```
do-while
```
loop syntax:

```
do {
// body of the loop
} while (condition);
```

(j) How many specifiers are used in c++ programming?

C++ has three access specifiers:

- **Public:**  Members are accessible from outside the class.
- **Private:**  Members are accessible only within the class.
- **Protected:**  Members are not accessible outside the class but can be accessed in derived classes.
