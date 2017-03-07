# Elementary

Эта секция для начинающих

## Список упражнений

### 1. Hello World!
- Напечатайте ‘Hello World!’ на экран.  

    ```
    output: Hello World!
    ```
    
### 2. Привет!
- Спросите у пользователя его имя и скажите ему привет.  

    ```
    output: What's your name?  
    input: Gregory  
    output: Hi, Gregory!   
    ```
- Измените код программы так, чтобы приветствие показывалось только пользователям Admin или Master.  

    ```
    output: What's your name?
    input: Gregory
    output: Bye
    ```
    
### 3. Сумма
- Напишите программу, которая просит пользователя ввести число n и печатает сумму чисел от 1 до n  

    ```
    output: Enter a number: 
    input: 10
    output: 55
    ```
- Измените код программы так, чтобы можно было вводить только положительные числа  

    ```
    output: Enter a number: 
    input: -5
    output: ValueError: Input value must be > 0 
    ```
- Измените код программы так, чтобы любой человек понял, что именно считает ваша программа  

    ```
    output: Enter a number: 
    input: 6
    output: 1 + ... + 6 = 21
    ```
- Измените код программы так, чтобы в сумме учитывались только числа кратные 3 и 5  
  + easy  
  
    ```
    output: Enter a number: 
    input: 11
    output: 33
    ```  
  + hard  
  
    ```
    output: Enter a number: 
    input: 11
    output: (3 + ... + 9) + (5 + ... + 10) = 33
    ```

### 4. Циклы и списки
- Напишите программу, которая печатает n звездочек в столбик  

    ```
    output: Enter n:  
    input: 3
    output: *
    output: *
    output: *
    ```
- Напишите программу, которая печатает треугольник из звездочек

    ```
    output: Enter n:
    input: 3
    output: ***
    output: **
    output: *
    ```
- Напишите программу, которая печатает числа от 1 до n через пробел

    ```
    output: Enter n:
    input: 5
    output: 1 2 3 4 5
    ```

- Напишите программу, которая печатает числа от 1 до n через пробел n раз

    ```
    output: Enter n:
    input: 5
    output: 1 2 3 4 5
    output: 1 2 3 4 5
    output: 1 2 3 4 5
    output: 1 2 3 4 5
    output: 1 2 3 4 5
    ```

- Напишите программу, которая печатает таблицу сложения

    ```
    output: 0 1 2 3 4 
    output: 1 2 3 4 5
    output: 2 3 4 5 6
    output: 3 4 5 6 7
    output: 4 5 6 7 8
    ```

- напишите программу, которая рисует 'кружок' радиуса n звездочками

    ```
    output: Enter radius: 
    input: 3
    output:     *   
    output:   ***** 
    output:   ***** 
    output:  *******
    output:   ***** 
    output:   ***** 
    output:     *   
    ```
    Подсказка: использовать неравенство для круга x\*x + y\*y <= r\*r
