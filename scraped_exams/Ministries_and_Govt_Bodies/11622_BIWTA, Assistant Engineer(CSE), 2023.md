# BIWTA, Assistant Engineer(CSE), 2023

- **Original URL:** [https://it.jobqns.com/biwta-assistant-engineercse-2023/](https://it.jobqns.com/biwta-assistant-engineercse-2023/)
- **Date:** 2026-02-10T16:12:13
- **Categories:** Job Solution 2023, Other IT Job Solution, Other IT Job Solution 2023

---

#### Bangladesh Inland Water Transport Authority  Post: Assistant Engineer (CSE) Exam Date: 24-02-2023,  Exam Taker: BUET



1. Give IP 192.168.1.50 and subnet mask 255.255.255.240; Find valid host, Network address, and Broadcast address

**Convert Subnet Mask to Binary** : The subnet mask
```
255.255.255.240
```
can be written in binary as:

```
11111111.11111111.11111111.11110000
```

**Determine the Number of Hosts** : The number of host bits is  **4** , so we use the formula: 24 – 2 =14

Therefore, there are  **14 valid hosts**  in this subnet.

**Calculate the Network Address** : Perform a bitwise AND between the IP address and subnet mask:

**IP Address**  (
```
192.168.1.50
```
):
```
11000000.10101000.00000001.00110010
```

**Subnet Mask**  (
```
255.255.255.240
```
):
```
11111111.11111111.11111111.11110000
```

The result is the  **network address**  in binary:

```
11000000.10101000.00000001.00110000
```

When converted back to decimal, the network address is:  **192.168.1.48**

**Calculate the Broadcast Address** : The broadcast address is obtained by setting all host bits to 1 in the network address:

- Network Address:
```
11000000.10101000.00000001.00110000
```
- Host bits set to 1:
```
11000000.10101000.00000001.00111111
```

The result is the  **broadcast address** :  **192.168.1.63**

**Determine the Valid Host Range** : The valid host range is the IP addresses between the network address and the broadcast address, excluding those two addresses:

- The  **first valid host**  is  **192.168.1.49**  (Network Address + 1).
- The  **last valid host**  is  **192.168.1.62**  (Broadcast Address – 1).
- **Network Address** :
```
192.168.1.48
```
- **Broadcast Address** :
```
192.168.1.63
```
- **Valid Host Range** :
```
192.168.1.49
```
to
```
192.168.1.62
```
- **Number of Hosts** :
```
14
```

2. Consider the two schema employees (id, first_name, last_name, designation, oining_date, salary, dept_id) and department (dept_id, dept_name). Where detp_id is forgeign key. Find the first_name and department name whose salary is maximum.
```
SELECT e.first name, d.dept_name
FROM employees e
JOIN department d ON e.dept_id = d.dept_id
ORDER BY e.salary DESC
LIMIT 1;
```

3. Write a C program to print the following pattern:
0
010
01010
```
#include <stdio.h>

int main() {
int rows;

printf("Enter number of rows: ");
scanf("%d", &rows);

int maxWidth = 2 * rows - 1;

for (int i = 0; i < rows; i++) {
int numbers = 2 * i + 1;
int spaces = (maxWidth - numbers) / 2;

// print leading spaces
for (int s = 0; s < spaces; s++) {
printf(" ");
}

// print 0 and 1 pattern
for (int j = 0; j < numbers; j++) {
printf("%d", j % 2);
}

printf("\n");
}

return 0;
}
```

```
Sample I/O:
Enter number of rows: 5
0
010
01010
0101010
010101010

=== Code Execution Successful ===
```

🔗 Run Online: Print Pattern

4. Write PEAS for (a) Auto taxi (b) Automatic clinical test.

**PEAS for Auto Taxi**

**Performance Measure:**  Safe driving, minimum travel time, fuel efficiency, passenger comfort, obey traffic rules.

**Environment:**  Roads, traffic signals, pedestrians, other vehicles, weather conditions.

**Actuators:**  Steering, accelerator, brake, horn, display system.

**Sensors:**  Cameras, GPS, radar, lidar, speed sensors.

**PEAS for Automatic Clinical Test**

**Performance Measure:**  Accurate diagnosis, fast test result, minimum error, patient safety.

**Environment:**  Patient samples, laboratory conditions, medical database.

**Actuators:**  Display screen, report printer, robotic arms.

**Sensors:**  Blood sensors, chemical sensors, scanners, imaging devices.

**Auto Taxi-এর জন্য PEAS**

**Performance Measure:**  নিরাপদ ড্রাইভিং, কম সময়ে গন্তব্যে পৌঁছানো, জ্বালানি সাশ্রয়, যাত্রী স্বাচ্ছন্দ্য, ট্রাফিক নিয়ম মেনে চলা।

**Environment:**  রাস্তা, ট্রাফিক সিগন্যাল, পথচারী, অন্যান্য যানবাহন, আবহাওয়া।

**Actuators:**  স্টিয়ারিং, এক্সেলারেটর, ব্রেক, হর্ন, ডিসপ্লে সিস্টেম।

**Sensors:**  ক্যামেরা, GPS, রাডার, লিডার, স্পিড সেন্সর।

**Automatic Clinical Test-এর জন্য PEAS**

**Performance Measure:**  সঠিক রোগ নির্ণয়, দ্রুত ফলাফল, কম ত্রুটি, রোগীর নিরাপত্তা।

**Environment:**  রোগীর নমুনা, ল্যাবরেটরি পরিবেশ, মেডিক্যাল ডাটাবেস।

**Actuators:**  ডিসপ্লে স্ক্রিন, রিপোর্ট প্রিন্টার, রোবোটিক বাহু।

**Sensors:**  রক্ত সেন্সর, কেমিক্যাল সেন্সর, স্ক্যানার, ইমেজিং ডিভাইস।

5. Determine the root of the given equation x2 - 3 = 0 for x ∈ [1,2]

**Finding the Root of the Equation x² − 3 = 0 using Bisection Method**

Let f(x) = x² − 3. We are given the interval [1, 2].

f(1) = −2 and f(2) = 1, so f(1)·f(2) < 0. Hence, a root exists in the interval [1, 2].

**Iteration 1:**  a = 1, b = 2, c = (1 + 2)/2 = 1.5, f(c) = −0.75. Since f(c) and f(a) have the same sign, the new interval is [1.5, 2].

**Iteration 2:**  a = 1.5, b = 2, c = 1.75, f(c) = 0.0625. Since f(c) and f(a) have opposite signs, the new interval is [1.5, 1.75].

**Iteration 3:**  a = 1.5, b = 1.75, c = 1.625, f(c) = −0.359375. New interval is [1.625, 1.75].

**Iteration 4:**  a = 1.625, b = 1.75, c = 1.6875, f(c) = −0.15234375. New interval is [1.6875, 1.75].

**Conclusion:**  By continuing this process, the root converges to x = √3 ≈ 1.732.

**Bisection Method ব্যবহার করে x² − 3 = 0 সমীকরণের Root নির্ণয়**

ধরা যাক, f(x) = x² − 3 এবং দেওয়া interval হলো [1, 2]।

f(1) = −2 এবং f(2) = 1 হওয়ায় f(1)·f(2) < 0, অর্থাৎ interval-এর মধ্যে একটি root বিদ্যমান।

**Iteration 1:**  a = 1, b = 2, c = 1.5, f(c) = −0.75। যেহেতু f(c) ও f(a)-এর sign একই, নতুন interval হবে [1.5, 2]।

**Iteration 2:**  a = 1.5, b = 2, c = 1.75, f(c) = 0.0625। sign বিপরীত হওয়ায় নতুন interval হবে [1.5, 1.75]।

**Iteration 3:**  a = 1.5, b = 1.75, c = 1.625, f(c) = −0.359375। নতুন interval হবে [1.625, 1.75]।

**Iteration 4:**  a = 1.625, b = 1.75, c = 1.6875, f(c) = −0.15234375। নতুন interval হবে [1.6875, 1.75]।

**উপসংহার:**  Iteration চালিয়ে গেলে root-এর মান √3 ≈ 1.732-এর দিকে ধীরে ধীরে পৌঁছে যায়।

6. Sort the following data using merge sort. Also mention best and worst case of the algorithm.
A [8] = {11, 6, 3, 24, 46, 22, 7}

**Merge Sort Example: Sorting Array [11, 6, 3, 24, 46, 22, 7]**

**Step 1: Initial Array**

**A = [11, 6, 3, 24, 46, 22, 7]**

**Step 2: Divide the Array**

We divide the array into two halves:

**A1 = [11, 6, 3, 24]**  and  **A2 = [46, 22, 7]**

**Step 3: Recursively Divide Each Half**

For  **A1 = [11, 6, 3, 24]** , we divide it into:

**A1.1 = [11, 6]**  and  **A1.2 = [3, 24]**

For  **A1.1 = [11, 6]** , divide it into:

**A1.1.1 = [11]**  and  **A1.1.2 = [6]**

For  **A1.2 = [3, 24]** , divide it into:

**A1.2.1 = [3]**  and  **A1.2.2 = [24]**

For  **A2 = [46, 22, 7]** , we divide it into:

**A2.1 = [46, 22]**  and  **A2.2 = [7]**

For  **A2.1 = [46, 22]** , divide it into:

**A2.1.1 = [46]**  and  **A2.1.2 = [22]**

**Step 4: Merge Subarrays**

Now, we begin merging the subarrays:

Merge  **[11]**  and  **[6]**  →  **[6, 11]**

Merge  **[3]**  and  **[24]**  →  **[3, 24]**

Merge  **[46]**  and  **[22]**  →  **[22, 46]**

Merge  **[22, 46]**  and  **[7]**  →  **[7, 22, 46]**

**Step 5: Final Merge**

Finally, merge the two sorted halves:

**[6, 11, 3, 24]**  and  **[7, 22, 46]**

After merging, the sorted array is:

**[3, 6, 7, 11, 22, 24, 46]**

**Time Complexity**

**Best Case Time Complexity** :  **O(n log n)**

**Worst Case Time Complexity** :  **O(n log n)**

7. Your company earn a contract to develop a system for a government agency. The project team is considering whether to build the system from scratch, or reuse existing partial-experience components, or buy an available software product and modify it to meet the requirement. As analyst you have made a decision tree as a figure.........

**Decision Tree for Software Development Strategy**

For the government project, the analyst considers three possible options: building the system from scratch, reusing existing components, or buying and modifying an available software product. A decision tree helps evaluate these options based on cost, time, risk, and requirement fulfillment.

**Option 1: Build from Scratch**

This option provides full control over system design and functionality and ensures all requirements are met. However, it requires high development cost, longer time, and higher risk.

**Option 2: Reuse Existing Components**

Reusing partial-experience components reduces development time and cost. The risk is moderate, but compatibility and integration issues may arise if components do not perfectly match requirements.

**Option 3: Buy and Modify Software**

Buying an existing software product and customizing it is usually the fastest and lowest-cost option. However, it may not fully satisfy all requirements and may create dependency on the vendor.

**Conclusion:**

The decision tree helps compare these alternatives systematically. For a government project where reliability and compliance are critical, reuse or buy-and-modify may be preferred if requirements are mostly satisfied; otherwise, building from scratch is the safest choice.

**Software Development Strategy নির্ধারণে Decision Tree**

সরকারি সংস্থার জন্য system তৈরির ক্ষেত্রে analyst তিনটি বিকল্প বিবেচনা করে: নতুন করে system তৈরি করা, বিদ্যমান component পুনঃব্যবহার করা, অথবা প্রস্তুত software কিনে সেটি পরিবর্তন করা। Decision tree এই বিকল্পগুলোকে cost, time, risk এবং requirement অনুযায়ী বিশ্লেষণ করতে সাহায্য করে।

**Option 1: Build from Scratch**

এই পদ্ধতিতে system-এর উপর সম্পূর্ণ নিয়ন্ত্রণ থাকে এবং সব requirement পূরণ করা যায়। তবে এতে বেশি সময়, বেশি খরচ এবং বেশি ঝুঁকি থাকে।

**Option 2: Reuse Existing Components**

বিদ্যমান component ব্যবহার করলে সময় ও খরচ কম লাগে। তবে component compatibility এবং integration সমস্যা হতে পারে।

**Option 3: Buy and Modify Software**

প্রস্তুত software কিনে পরিবর্তন করলে দ্রুত কাজ শেষ হয় এবং খরচ কম হয়। কিন্তু সব requirement পূরণ নাও হতে পারে এবং vendor-এর উপর নির্ভরতা তৈরি হয়।

**উপসংহার:**

Decision tree ব্যবহার করে analyst সহজেই সেরা বিকল্প নির্বাচন করতে পারে। সরকারি project-এর ক্ষেত্রে যদি requirement আংশিকভাবে পূরণ হয়, তাহলে reuse বা buy-and-modify উপযুক্ত; নাহলে build from scratch সবচেয়ে নিরাপদ সিদ্ধান্ত।

8. Design 6×1 MUX by using 2×1 MUX

To design a 6-to-1 multiplexer (MUX) using 2-to-1 multiplexers, we can break it down into smaller parts. A 6-to-1 MUX has 6 data inputs, 1 output, and 3 selection bits (since 2^3 = 8 and we need 3 bits to select one of the 6 inputs). A 2-to-1 MUX has 2 inputs, 1 output, and 1 selection bit.

S2S1S0Output Y000I0001I1010I2011I3100I4101I511001010

**9. Consider the following six processes each having its own unique processing time and arrival time:**
**Process**   **Arrival Time**   **Processing Time**      A 0 8   B 0 4   C 0 5   D 1 9   E 1 7   F 0 1
Find average turnaround time using shortest job first scheduling algorithm.
