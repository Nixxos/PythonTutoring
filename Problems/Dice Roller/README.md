# Python Tutoring - Dice Roller

###### Details

> Base Difficulty: Easy </br>
> Focus: Loops, Random </br>
> Packages Required: random </br>

Base Problem
------
- Input:
 - Your program will accept inputs in the form NdM
 - N is the number of rolls
 - M is the number of sides on the dice
- Outputs:
 - Sum of all the dice rolls
- Test Inputs:
 - 5d12, 6d4, 1d2, 1d8, 6d6, 7d20, 100d100

Walkthrough
------
<!-- <Details> -->
<!-- <summary>Click to Expand! (Contains Hints)</summary> </br> -->

##### 1. Get user input using the input() function
  - It takes a string as inputs (usually a prompt for the user to type something in)
  - <details><summary>Example:</summary>

    ```python
user_in = input("Please input a roll in the form NdM:\t")
    ```
  </details>

***

##### 2. Make a variable to keep track of the sum of our rolls
  - An integer
  - <details><summary>Example:</summary>

    ```python
roll_sum = 0
    ```
  </details>

***

##### 3. Split our string into a list of just the two numbers
  - This will take a string like "6d4" and return a list like ["6", "4"].
  - It uses the "d" we typed in for 6d4 as the delimeter, which is something that is used to divide the text
  - <details><summary>Example:</summary>

    ```python
str_n = user_in.split("d")
    ```
  </details>

***

##### 4. Turning our list of strings into a list of integers
  - Run through all numbers (currently strings) in the list and convert them to integers
  - <details><summary>Example:</summary>

    ```python
nums = [int(n) for n in str_n]
    ```
  </details>

***

##### 5. Make a for loop repeating N times, used to re-roll our dice
  - N being the first number in NdM
  - N is also stored in nums[0]
  - <details><summary>Example:</summary>

    ```python
for i in range(nums[0]):
    ```
  </details>

***

##### 6. "Roll" a random number from 1 to M and add it to the sum of the rolls
  - Usage of randint(a, b): "Return a random integer N such that a <= N <= b"
  - <details><summary>Example:</summary>

    ```python
roll_sum += randint(1, nums[1])
    ```
  </details>

***

##### 7. Finally, print out the sum of the rolls
  - <details><summary>Example:</summary>

    ```python
print('The sum of your rolls is %s!\n' % roll_sum)
    ```
  </details>


<!-- </details> -->

<!-- Extended Problem
------ -->
