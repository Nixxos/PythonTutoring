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
<Details>
  <summary>Click to Expand! (Contains Hints)</summary> </br>
  <!-- <section> -->

  ##### 1. Get user input using the input() function
  <ul>
  <li> It takes a string as inputs (usually a prompt for the user to type something in) </li>
  <li> <details><summary>Example:</summary>

  ```python
  user_in = input("Please input a roll in the form NdM:\t")
  ```
  </details> </li>
  </ul>

  ***

  ##### 2. Make a variable to keep track of the sum of our rolls
  <ul>
  <li> An integer </li>
  <li> <details><summary>Example:</summary>

  ```python
  roll_sum = 0
  ```
  </details> </li>
  </ul>

  ***

  ##### 3. Split our string into a list of just the two numbers
  <ul>
  <li> This will take a string like "6d4" and return a list like ["6", "4"]. </li>
  <li> It uses the "d" we typed in for 6d4 as the delimeter, which is something that is used to divide the text </li>
  <li> <details><summary>Example:</summary>

  ```python
  str_n = user_in.split("d")
  ```
  </details> </li>
  </ul>

  ***

  ##### 4. Turning our list of strings into a list of integers
  <ul>
  <li> Run through all numbers (currently strings) in the list and convert them to integers </li>
  <li> <details><summary>Example:</summary>

  ```python
  nums = [int(n) for n in str_n]
  ```
  </details> </li>
  </ul>

  ***

  ##### 5. Make a for loop repeating N times, used to re-roll our dice
  <ul>
  <li> N being the first number in NdM </li>
  <li> N is also stored in nums[0] </li>
  <li> <details><summary>Example:</summary>

  ```python
  for i in range(nums[0]):
  ```
  </details> </li>
  </ul>

  ***

  ##### 6. "Roll" a random number from 1 to M and add it to the sum of the rolls
  <ul>
  <li> Usage of randint(a, b): "Return a random integer N such that a <= N <= b" </li>
  <li> <details><summary>Example:</summary>

  ```python
  roll_sum += randint(1, nums[1])
  ```
  </details> </li>
  </ul>

  ***

  ##### 7. Finally, print out the sum of the rolls
  <ul>
  <li> <details><summary>Example:</summary>

  ```python
  print('The sum of your rolls is %s!\n' % roll_sum)
  ```
  </details> </li>
  </ul>
  <!-- </section> -->
</details>

<!-- Extended Problem
------ -->
