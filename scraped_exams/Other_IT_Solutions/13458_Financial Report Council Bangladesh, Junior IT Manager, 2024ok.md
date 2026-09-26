# Financial Report Council Bangladesh, Junior IT Manager, 2024ok

- **Original URL:** [https://it.jobqns.com/financial-report-council-bangladesh-junior-it-manager-2024/](https://it.jobqns.com/financial-report-council-bangladesh-junior-it-manager-2024/)
- **Date:** 2026-03-05T19:03:59
- **Categories:** Job Solution 2024

---

#### Financial Report Council Bangladesh
Post: Junior IT Manager;  Date: 10 May, 2024 Exam Taker: FRCB; Marks: Non:60; Tech:40



1. Write a program for sum of digits of a number. Without using library functions other than basic input output.
```
#include <stdio.h>

int main() {
int num, sum = 0;

printf("Enter a number: ");
scanf("%d", &num);

// Calculate sum of digits
while (num != 0) {
sum += num % 10;
num = num / 10;
}

printf("Sum of digits = %d\n", sum);

return 0;
}
```

2. a) Write full form: DHCP and ARP.
b) Answer the following question give IP 192.168.10.100/26
(i) Find Network address.
(ii) Maximum Number of Host.
(iii) Broadcast address of the IP address 9.1.5.31 and default subnet mask 250.0.0.0.

**a) Full form:** DHCP =  **Dynamic Host Configuration Protocol** ARP =  **Address Resolution Protocol**

**b) For IP 192.168.10.100/26**

**(i) Network address:** /26 subnet mask = 255.255.255.192Block size = 64Subnets are: 0, 64, 128, 192100 falls in 64–127So, Network address =  **192.168.10.64**

**(ii) Maximum number of hosts:** Host bits = 32 − 26 = 6Total IPs = 26 = 64Usable hosts = 64 − 2 =  **62**

**(iii) Broadcast address of IP 9.1.5.31 with default subnet mask 250.0.0.0:**  **250.0.0.0 is not a valid subnet mask** , so the broadcast address cannot be determined using that mask.

If the question intended the default Class A mask, then it should be  **255.0.0.0** .In that case:Network address = 9.0.0.0Broadcast address =  **9.255.255.255**

**Final answers:** DHCP =  **Dynamic Host Configuration Protocol** ARP =  **Address Resolution Protocol** Network address =  **192.168.10.64** Maximum number of hosts =  **62** Broadcast address for 9.1.5.31 with mask 250.0.0.0 =  **invalid question** If mask is 255.0.0.0, then broadcast =  **9.255.255.255**

3. Write a program for login using database in PHP. Use various parameters (username, hostname, database name and database user).
```
<?php
// Database connection parameters
$hostname = "localhost";
$db_username = "root";
$db_password = "";
$database = "test_db";

// Create connection
$conn = new mysqli($hostname, $db_username, $db_password, $database);

// Check connection
if ($conn->connect_error) {
die("Connection failed: " . $conn->connect_error);
}

// Get login data from form
$username = $_POST['username'];
$password = $_POST['password'];

// SQL query to check user
$sql = "SELECT * FROM users WHERE username='$username' AND password='$password'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
echo "Login Successful";
} else {
echo "Invalid Username or Password";
}

$conn->close();
?>
```

4. Write down the concept about inheritance with example.

**Inheritance**  is a feature of Object-Oriented Programming where one class (child/subclass) acquires the properties and behaviors of another class (parent/superclass).

**Concept:**  It allows code reuse by using existing class properties in a new class.

**Types:**  Single, Multiple, Multilevel, Hierarchical inheritance.

**Advantage:**  Reduces code duplication and improves maintainability.

**Example:** A class  **Animal**  has a method  **eat()** .A class  **Dog**  inherits from Animal and can use  **eat()**  and also have its own method  **bark()** .

**Inheritance**  হলো OOP-এর একটি বৈশিষ্ট্য যেখানে একটি class (child/subclass) অন্য একটি class (parent/superclass)-এর property এবং behavior গ্রহণ করে।

**Concept:**  এটি existing class-এর বৈশিষ্ট্য নতুন class-এ ব্যবহার করার মাধ্যমে code reuse করতে সাহায্য করে।

**Types:**  Single, Multiple, Multilevel, Hierarchical inheritance।

**Advantage:**  Code duplication কমায় এবং maintain করা সহজ হয়।

**Example:** একটি  **Animal**  class-এ  **eat()**  method আছে।একটি  **Dog**  class, Animal থেকে inherit করে এবং  **eat()**  ব্যবহার করতে পারে এবং নিজের  **bark()**  method থাকে।
