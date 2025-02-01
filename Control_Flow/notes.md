# **Control Flow in Python**

## 📚 Introduction

Control flow in Python refers to the order in which individual statements, instructions, or function calls are executed in a script. Python provides several control flow statements like `if`, `if-else`, `if-elif-else`, and conditional expressions to manage decision-making in programs.

---

## 📝 Topics Covered

| **Topic**                                              | **Description**                                                             |
| ------------------------------------------------------ | --------------------------------------------------------------------------- |
| **Control Flows Introduction**                         | Overview of how Python controls the execution of code.                      |
| **Simple if Statement & Example**                      | Using `if` statements to execute code only when a condition is met.         |
| **Boolean Expressions as Python Statements**           | Understanding how Boolean expressions drive decision-making.                |
| **Simple if-else Statements**                          | Handling two possible conditions in a program.                              |
| **Compound Boolean Expressions & Operator Precedence** | Using `and`, `or`, `not` along with precedence rules.                       |
| **Pass Statement & Floating Point Equality**           | The use of `pass` as a placeholder and handling floating-point comparisons. |
| **Nested if-else Conditionals**                        | Structuring multiple conditional statements inside one another.             |
| **Multi-Way vs Sequential if-else Conditionals**       | Understanding different ways of handling multiple conditions.               |
| **Conditional Expressions**                            | Writing short conditional expressions using Python's ternary operator.      |
| **Errors in Conditional Statements**                   | Common mistakes and debugging techniques in control flow.                   |
| **Logic Complexity**                                   | Understanding how increasing conditions affect readability and performance. |

---

## 🔹 1. Simple `if` Statement
- Used to execute a block of code **only if** a condition is `True`.

### ✅ Syntax:
```python
if condition:
    # Code to execute when condition is True
```

### 🔸 Example:
```python
x = 10
if x > 5:
    print("x is greater than 5")
```

### 🔹 Output:
```
x is greater than 5
```

---

## 🔹 2. Boolean Expressions as Python Statements
- Boolean expressions return `True` or `False` and can be used directly in control flow statements.

### 🔸 Example:
```python
x = 5
y = 10
if x < y:
    print("x is smaller than y")
```

### 🔹 Output:
```
x is smaller than y
```

---

## 🔹 3. Simple `if-else` Statement
- Executes one block if the condition is `True`, and another if it's `False`.

### ✅ Syntax:
```python
if condition:
    # Code if condition is True
else:
    # Code if condition is False
```

### 🔸 Example:
```python
num = 7
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

### 🔹 Output:
```
Odd number
```

---

## 🔹 4. Compound Boolean Expressions & Operator Precedence
- Conditions can be combined using logical operators `and`, `or`, and `not`.

### 🔸 Example:
```python
x = 15
y = 25
if x > 10 and y > 20:
    print("Both conditions are True")
```

### 🔹 Output:
```
Both conditions are True
```

---

## 🔹 5. `pass` Statement & Floating Point Equality
- The `pass` statement is used as a placeholder for future code.
- Floating point numbers can have precision issues, so it's better to compare using a small threshold.

### 🔸 Example:
```python
x = 0.1 + 0.2
y = 0.3
if abs(x - y) < 1e-9:  # Using a small threshold
    print("Equal")
else:
    print("Not equal")
```

### 🔹 Output:
```
Equal
```

---

## 🔹 6. Nested `if-else` Conditionals
- `if-else` statements can be nested within each other.

### 🔸 Example:
```python
x = 10
if x > 0:
    print("Positive")
    if x % 2 == 0:
        print("Even number")
else:
    print("Negative")
```

### 🔹 Output:
```
Positive
Even number
```

---

## 🔹 7. Multi-Way vs Sequential `if-else` Conditionals
- **Multi-Way (`if-elif-else`)**: Uses multiple conditions.
- **Sequential (`if` statements separately)**: Each condition is checked independently.

### 🔸 Example (Multi-Way):
```python
num = 0
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

### 🔹 Output:
```
Zero
```

---

## 🔹 8. Conditional Expressions (Ternary Operator)
- A compact way to write `if-else` statements.

### ✅ Syntax:
```python
value_if_true if condition else value_if_false
```

### 🔸 Example:
```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)
```

### 🔹 Output:
```
Adult
```

---

## 🔹 9. Errors in Conditional Statements
- **Common Mistakes:**
  - **Indentation errors**
  - **Using `=` instead of `==`**
  - **Not handling all cases**

### 🔸 Example (Incorrect Indentation):
```python
if True:
print("Hello")  # ❌ Incorrect (should be indented)
```

Corrected:
```python
if True:
    print("Hello")  # ✅ Correct
```

### 🔹 Output:
```
Hello
```

---

## 🔹 10. Logic Complexity
- Too many nested `if-else` statements make code harder to read.
- Use **boolean variables**, **functions**, and **simplified logic** to improve clarity.

### 🔸 Example (Reducing Complexity):
```python
# Instead of this:
if age >= 18:
    if has_id:
        print("Eligible to vote")
    else:
        print("ID required")
else:
    print("Not eligible")

# Use this:
if age >= 18 and has_id:
    print("Eligible to vote")
elif age >= 18:
    print("ID required")
else:
    print("Not eligible")
```

### 🔹 Output:
```
(ID required or Eligible to vote based on values)
```

---

## ✅ Key Takeaways
- **`if`, `if-else`, and `if-elif-else`** control decision-making.
- **Logical operators (`and`, `or`, `not`)** help in combining conditions.
- **The `pass` statement** is useful as a placeholder.
- **Conditional expressions** provide a concise way to write `if-else`.
- **Avoid deeply nested `if-else` statements** to maintain readability.

---

