# Day03 - Score Analyzer

## What I Practiced

### 1. `while True` loop

I learned that:

while True:

means the loop will continue forever until `break` is used.

I also learned:

* the line under `while` must be indented
* Python uses indentation to show code structure

### 2. `if` statement and indentation

I practiced using:

if score == "done":

and learned:

* `if` inside a loop must align with other code inside the loop
* code under `if` needs another indentation level


### 3. `break`

I learned that:

break

immediately stops the current loop.

### 4. `input()` and `float()`

I learned:

* `input()` always returns a string
* `float()` converts a string into a number

Example:

score = float(score)

### 5. `try / except`

I learned how to prevent the program from crashing when the user enters invalid input.

Example:

try:
    score = float(score)
except:
    print("Invalid input")
    continue

### 6. Counting and totaling

I practiced:

count = count + 1
total = total + score

* `count` tracks how many valid scores were entered
* `total` stores the sum of all scores


### 7. Finding largest and smallest values

I learned that:

largest = None
smallest = None

is safer than setting random numbers like `0` or `-1`.

The program updates the values during the loop.

## Reflection

Today was my first time really understanding how loops work.

At first, the logic felt confusing because programming requires thinking step by step very carefully.

But after building the project myself, I started understanding that:

* programs work by repeating instructions
* variables keep changing during loops
* Python depends heavily on indentation and logic structure

