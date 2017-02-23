# Elementary

This section is for absolute beginners

## List of exercises

### 1. Hello World!
  - Print ‘Hello World!’ to the screen.
    ```
    output: Hello World!
    ```
### 2. Greetings!
- Ask the user for his name and then greet him using his name.

    ```
    output: What's your name?
    input: Gregory
    output: Hi, Gregory!
    ```
- Modify the program such that only the user Admin is greeted with his name.  

    ```
    output: What's your name?
    input: Gregory
    output: Bye
    ```
### 3. Sum
- Write a program that asks the user for a number n and prints the sum of the numbers 1 to n
    ```
    output: Enter a number: 
    input: 10
    output: 55
    ```
- Modify the program such that only positive numbers are accepted as input
    ```
    output: Enter a number: 
    input: -5
    output: ValueError: Input value must be > 0 
    ```
- Modify the program such that sum output is human readable
    ```
    output: Enter a number: 
    input: 6
    output: 1 + ... + 6 = 21
    ```
- Modify the program such that only multiples of three or five are considered in the sum  
  + easy  
    ```
    output: Enter a number: 
    input: 11
    output: 33
    ```
  + medium
    ```
    output: Enter a number: 
    input: 11
    output: 3 + 5 + 6 + 9 + 10 = 33
    ```
  + hard
    ```
    output: Enter a number: 
    input: 11
    output: (3 + ... + 9) + (5 + ... + 10) = 33
    ```
- Modify the program to use builtin sum() function
    ```
    output: Enter a number: 
    input: 11
    output: (3 + ... + 9) + (5 + ... + 10) = 33
    ```


12. Write a function to print such sums '(3 + ... + 9)'
 6. Write a program that asks the user for a number n and gives him the possibility to choose between computing the sum and computing the product of 1,…,n.
 7. Write a program that prints a multiplication table for numbers up to 12.
 8. Write a program that prints all prime numbers. (Note: if your programming language does not support arbitrary size numbers, printing all primes up to the largest number you can easily represent is fine too.)
 9. Write a guessing game where the user has to guess a secret number. After every guess the program tells the user whether their number was too large or too small. At the end the number of tries needed should be printed. I counts only as one try if they input the same number multiple times consecutively.
 10. Write a program that prints the next 20 leap years.
