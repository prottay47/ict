# NPCBL, Executive Trainee, 2022ok

- **Original URL:** [https://it.jobqns.com/npcbl-executive-trainee-2022/](https://it.jobqns.com/npcbl-executive-trainee-2022/)
- **Date:** 2026-03-09T00:12:14
- **Categories:** Job Solution 2022, Power Sector IT Job Solution 2022

---

#### Nuclear Powerplant Company Bangladesh Limited (NPCBL)
Post: Executive Trainee (IT)Exam Date: 2022 (BUET)



1. Difference between RISC and CISC.

2. Huffman encoding draw huffman tree. Given word "CONNECTION"

**Huffman encoding for the word:**  CONNECTION

**Step 1: Count frequency of each character**

C O N N E C T I O N

CharacterFrequencyN3C2O2E1T1I1

**Step 2: Build Huffman tree**

One valid construction is:E(1) + I(1) = 2T(1) + C(2) = 3O(2) + (E,I)(2) = 4N(3) + (T,C)(3) = 64 + 6 = 10

**Huffman tree:**

```
[10]
/    \
[4]    [6]
/  \    /  \
O(2) [2] N(3) [3]
/ \       / \
E(1) I(1) T(1) C(2)
```

**Assign 0 to left branch and 1 to right branch**

CharacterCodeO00E010I011N10T110C111

**Encode CONNECTION**

C = 111O = 00N = 10N = 10E = 010C = 111T = 110I = 011O = 00N = 10

**Encoded bit string:** 1110010100101111100110010

3. For BST of 1D which represented by an array, insert a data by using int insertData (const int *arr, int x); Write a function insert node in bst.
```
#include <iostream>
using namespace std;
#define SIZE 100
int bst[SIZE];

// Initialize BST array
void initBST() {
for(int i = 0; i < SIZE; i++)
bst[i] = -1;
}

// Insert node in BST represented by array
int insertData(const int *arr, int x) {
int index = 0;

while(index < SIZE) {

// If empty position found
if(bst[index] == -1) {
bst[index] = x;
return index;
}

// Go to left child
if(x < bst[index])
index = 2 * index + 1;

// Go to right child
else
index = 2 * index + 2;
}

return -1; // Tree full
}

int main() {
initBST();

insertData(bst, 50);
insertData(bst, 30);
insertData(bst, 70);
insertData(bst, 20);
insertData(bst, 40);

cout << "BST array representation:\n";
for(int i = 0; i < 15; i++) {
if(bst[i] != -1)
cout << "Index " << i << " : " << bst[i] << endl;
}

return 0;
}
```

4. Amplitude Modulation related problem. (Approximate)

Not fully Collected

5. Draw Delta modulation figure and math. (Approximate)


[৫ টা written question । ৫*১০=৫০। MCQ General- ২০ টা , Technical- ৩০ টা ৫০*১=৫০ Time –  ১ ঘন্টা।]
