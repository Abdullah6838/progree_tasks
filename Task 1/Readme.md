# 🐍 Fibonacci Sequence Generator & Benchmark

A simple and efficient Python program that **generates a Fibonacci sequence** for a user-specified number of terms and **benchmarks its execution time** using Python's built-in `timeit` module. 🚀

## ✨ Features

- 🔢 Generates the first `n` Fibonacci numbers.
- ✅ Validates the input to ensure it is an integer.
- 🚫 Prevents negative sequence lengths.
- 🎯 Handles edge cases such as `n = 0` and `n = 1`.
- ⏱️ Benchmarks the Fibonacci generation function over multiple iterations.
- 📊 Displays the generated sequence and total benchmark runtime.
- 🧮 Uses an efficient iterative approach instead of recursion.

## 🛠️ Requirements

- 🐍 Python 3.x
- 📦 No external packages are required.

The program uses Python's built-in modules:

```python
import timeit
from typing import List
````

 > 💡 **Note:** `List` is imported in the original code but is currently not used.

 ## 📖 What is the Fibonacci Sequence?

 The Fibonacci sequence is a series of numbers where each number is the sum of the two numbers before it.

 It starts with:

```
0, 1, 1, 2, 3, 5, 8, 13, 21, ...
```

 The mathematical relationship is:

```
F(n) = F(n-1) + F(n-2)
```

 For example, requesting 10 terms produces:

```
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

 ## ⚙️ Functions

 ### 🔢 `generate_fibonacci(n)`

 Generates a Fibonacci sequence containing `n` terms.

 ### 📥 Parameters

 | Parameter | Type | Description |
| --- | --- | --- |
| `n` | `int` | Number of Fibonacci terms to generate |

### 📤 Returns

 A Python list containing the first `n` Fibonacci numbers.

 ### ⚠️ Exceptions

 - ❌ `TypeError` — Raised when `n` is not an integer.
- 🚫 `ValueError` — Raised when `n` is negative.

 ### 💡 Examples

```
generate_fibonacci(5)
```

 Output:

```
[0, 1, 1, 2, 3]
```

 For zero terms:

```
generate_fibonacci(0)
```

 Output:

```
[]
```

 For one term:

```
generate_fibonacci(1)
```

 Output:

```
[0]
```

 ## ⏱️ `benchmark_fibonacci(n, iterations=10000)`

 Measures the execution time of `generate_fibonacci(n)` using Python's `timeit` module.

 ### 📋 Parameters

 | Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `n` | `int` | — | Number of Fibonacci terms |
| `iterations` | `int` | `10000` | Number of times the function is executed |

The main program runs the benchmark for **5,000 iterations**:

```
elapsed_time = benchmark_fibonacci(target_terms, iterations=5000)
```

 ⏱️ The returned value represents the **total execution time in seconds** for all iterations.

 > 💡 **Note:** The exact benchmark runtime will vary depending on your computer and system load.

 ## 🛡️ Input Validation

 The program validates the sequence length before generating the Fibonacci sequence.

 ### 🚫 Negative Input

 Input:

```
Enter length: -5
```

 Output:

```
Parameter Validation Error: Sequence upper bound cannot be negative.
```

 ### ⚠️ Non-Integer Input

 The `generate_fibonacci()` function checks that its argument is an integer:

```
if not isinstance(n, int):
    raise TypeError("Sequence upper bound must be an integer.")
```

 However, the command-line interface first converts the user's input using:

```
target_terms = int(input("Enter length: "))
```

 Therefore, entering text instead of a number will cause `int()` to raise a `ValueError`.

 ## 🧠 Algorithm

 The program uses an **iterative approach**:

```
sequence = [0, 1]

while len(sequence) < n:
    sequence.append(sequence[-1] + sequence[-2])
```

 Instead of recursively calculating Fibonacci numbers, the program stores the previously generated values and calculates each new value using the last two numbers. ⚡

 ### 📈 Complexity

 For generating `n` terms:

 - ⏱️ **Time Complexity:** `O(n)`
- 💾 **Space Complexity:** `O(n)`

 The complete Fibonacci sequence is stored in a Python list, so memory usage grows with `n`.

 ## 🔬 Benchmarking

 The program uses Python's `timeit` module:

```
total_time = timeit.timeit(
    statement,
    setup=setup_code,
    number=iterations
)
```

 Running the function thousands of times provides a more useful measurement than timing a single execution, especially for small values of `n`. 📊

 The benchmark reports the **total execution time**, rather than the average time per iteration.

 ### 📌 Average Execution Time

 If you want to calculate the average time for one iteration:

```
average_time = total_time / iterations
```

 ## 🔄 Alternative Loop Implementation

 The code also contains a commented-out `for` loop:

```
# for _ in range(2, n):
#     sequence.append(sequence[-1] + sequence[-2])
```

 This can replace the `while` loop:

```
sequence = [0, 1]

for _ in range(2, n):
    sequence.append(sequence[-1] + sequence[-2])
```

 Both approaches produce the same Fibonacci sequence and have the same overall complexity. ✅

 ## 📁 Project Structure

```
Task 2/
│
├── 🐍 fibonacci.py
└── 📖 README.md
```

 ## 🌟 Possible Improvements

 Future versions could include:

 - 📝 Adding complete type hints to the functions.
- 🛡️ Handling invalid command-line input more gracefully.
- ⏱️ Reporting average execution time per iteration.
- 🎛️ Allowing users to configure the number of benchmark iterations.
- 🧪 Adding automated unit tests.
- 📦 Separating Fibonacci logic and benchmarking into different modules.
- 💻 Adding a command-line interface using `argparse`.
- 📈 Comparing iterative and recursive Fibonacci implementations.
- 🚀 Supporting more efficient algorithms for extremely large `n`.

 For example:

```
def generate_fibonacci(n: int) -> List[int]:
```

 ## 🎓 Learning Objectives

 This project is useful for practicing:

 - 🐍 Python programming
- 🔢 Lists and sequences
- 🔁 Loops
- 🛡️ Exception handling
- ⏱️ Performance benchmarking
- 🧠 Algorithm complexity
- 📝 Type hints
- 📊 Basic performance analysis

## 🚀 Running the Program

 Save the Python code in a file named:

```
fibonacci.py
```

 Then run it from the terminal:

```
python fibonacci.py
```

 The program will ask:

```
Enter length:
```

 Enter the desired number of Fibonacci terms. 🔢

 ### 🎯 Example

 Input:

```
Enter length: 10
```

 Output:

```
Generated Sequence (10 terms): [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
Benchmark Runtime: 0.004321 seconds (5,000 iterations for n=10)
```
