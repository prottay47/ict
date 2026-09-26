# Financial Report Council Bangladesh, Assistant Programmer, 2024ok

- **Original URL:** [https://it.jobqns.com/financial-report-council-bangladesh-assistant-programmer-2024/](https://it.jobqns.com/financial-report-council-bangladesh-assistant-programmer-2024/)
- **Date:** 2026-03-05T18:35:31
- **Categories:** Job Solution 2024

---

#### Financial Report Council Bangladesh
Post: Assistant Programmer;  Date: 10 May, 2024 Exam Taker: FRCB; Marks: Non:60; Tech:40



1.What is polymorphism in the context of OOP? Explain with example.

**Polymorphism**  means “many forms”. In Object-Oriented Programming, it allows a single function, method, or object to behave differently depending on the object or input.

**Concept:**  Same interface but different implementation. This helps to write flexible and reusable code.

**Types:**

- **Compile-time Polymorphism:**  Achieved by  **method overloading**  where multiple methods have the same name but different parameters.
- **Run-time Polymorphism:**  Achieved by  **method overriding**  where a child class provides its own implementation of a method.

**Example:** A method  **draw()**  behaves differently for different objects:Circle → draw circleRectangle → draw rectangleTriangle → draw triangle

**Benefit:**  Improves code reusability, flexibility, and reduces complexity.

**Polymorphism**  শব্দের অর্থ “একাধিক রূপ”। OOP-এ এটি এমন একটি বৈশিষ্ট্য যেখানে একই function বা method বিভিন্ন object বা input অনুযায়ী ভিন্নভাবে কাজ করে।

**Concept:**  একই interface কিন্তু ভিন্ন implementation। এটি code-কে flexible এবং reusable করে।

**Types:**

- **Compile-time Polymorphism:**   **method overloading**  এর মাধ্যমে হয়, যেখানে একই নামের method ভিন্ন parameter নিয়ে কাজ করে।
- **Run-time Polymorphism:**   **method overriding**  এর মাধ্যমে হয়, যেখানে child class নিজস্ব method implementation দেয়।

**Example:** একটি  **draw()**  method বিভিন্ন object-এর জন্য ভিন্ন কাজ করে:Circle → circle আঁকেRectangle → rectangle আঁকেTriangle → triangle আঁকে

**Benefit:**  Code reuse বাড়ায়, flexibility দেয় এবং complexity কমায়।

2. See the following relation and answer the following question.
Servers (ID, DaysRunning, OsName, RamCapacity);
a) Create table name Servers with attributes ID, DaysRunning, OsName, RamCapacity.
b) Write SQL query to update the server to Unix where the RamCapacity than 16GB.
c) Write SQL query to select the OsName for which Servers are running more than 365 days.
```
#include <stdio.h>
#include <math.h>

// Function to calculate factorial
double factorial(int n) {
double result = 1.0;
for (int i = 1; i <= n; i++) {
result *= i;
}
return result;
}

// Function to calculate sine using the series expansion
double sine_series(double x, int terms) {
double sum = 0.0;
for (int n = 0; n < terms; n++) {
int sign = (n % 2 == 0) ? 1 : -1; // Alternating signs
double term = pow(x, 2 * n + 1) / factorial(2 * n + 1);
sum += sign * term;
}
return sum;
}

int main() {
double x;
int terms;

// Input angle in radians and number of terms
printf("Enter the value of x (in radians): ");
scanf("%lf", &x);
printf("Enter the number of terms: ");
scanf("%d", &terms);

// Calculate sine using the series expansion
double result = sine_series(x, terms);

// Output the result
printf("The sine of %.2lf using %d terms is: %.6lf\n", x, terms, result);

return 0;
}
```

3. Given an IP address: 212.15.180.0/24 and wants to divide into 16 subnet.
a) What will be the subnet mask and how many hosts belongs to every subnet.
b) What is the first and last address of first and last subnet address?

**Given:** IP address = 212.15.180.0/24Required subnets = 16

**a) Subnet mask and hosts per subnet** To make 16 subnets, we need 4 subnet bits because 24 = 16.So new prefix = /24 + 4 =  **/28** Subnet mask =  **255.255.255.240** Host bits = 32 – 28 = 4Total addresses per subnet = 24 = 16Usable hosts per subnet = 16 – 2 =  **14**

**b) First and last address of first and last subnet** Block size = 16, so subnet addresses increase by 16.

**First subnet:** Network address =  **212.15.180.0** First usable address =  **212.15.180.1** Last usable address =  **212.15.180.14** Broadcast address =  **212.15.180.15**

**Last subnet:** Network address =  **212.15.180.240** First usable address =  **212.15.180.241** Last usable address =  **212.15.180.254** Broadcast address =  **212.15.180.255**

4. What do you understand by database view? Write a simple example to create, update and drop a view.

**Database View:** A  **view**  is a virtual table created from a SQL query. It does not store data physically; instead, it displays data from one or more tables.

**Example:**

**1. Create View**

```
CREATE VIEW emp_view AS
SELECT id, name, salary
FROM employee;
```

**2. Update View**

```
UPDATE emp_view
SET salary = 50000
WHERE id = 1;
```

**3. Drop View**

```
DROP VIEW emp_view;
```

**Final Answer:** A view is a virtual table used to simplify queries and enhance security.
