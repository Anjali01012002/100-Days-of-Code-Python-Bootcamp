# **Operators in Python**

## 📚 Introduction  
Operators in Python are special symbols that perform operations on variables and values. Python supports various types of operators, including arithmetic, comparison, logical, bitwise, assignment, identity, and membership operators.

---

## 📝 Types of Operators in Python  

| **Operator Type**        | **Operators**                                    | **Description** |
|--------------------------|-------------------------------------------------|----------------|
| **Arithmetic**           | `+`, `-`, `*`, `/`, `//`, `%`, `**`             | Perform mathematical operations. |
| **Comparison (Relational)** | `==`, `!=`, `>`, `<`, `>=`, `<=`             | Compare values and return `True` or `False`. |
| **Logical**              | `and`, `or`, `not`                             | Used to combine conditional statements. |
| **Bitwise**              | `&`, `\|`, `^`, `~`, `<<`, `>>`                 | Perform operations on bits. |
| **Assignment**           | `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`       | Assign values to variables. |
| **Identity**             | `is`, `is not`                                 | Check if two variables reference the same object. |
| **Membership**           | `in`, `not in`                                 | Check if a value exists in a sequence (list, tuple, string, etc.). |

---

## 🔹 1. Arithmetic Operators  
Used to perform mathematical operations.

| **Operator** | **Example** | **Result** |
|-------------|------------|------------|
| `+`         | `5 + 3`    | `8`        |
| `-`         | `5 - 3`    | `2`        |
| `*`         | `5 * 3`    | `15`       |
| `/`         | `5 / 3`    | `1.6667`   |
| `//`        | `5 // 3`   | `1` (floor division) |
| `%`         | `5 % 3`    | `2` (modulus) |
| `**`        | `5 ** 3`   | `125` (exponentiation) |

---

## 🔹 2. Comparison (Relational) Operators  
Used to compare values and return `True` or `False`.

| **Operator** | **Example** | **Result** |
|-------------|------------|------------|
| `==`        | `5 == 3`   | `False`    |
| `!=`        | `5 != 3`   | `True`     |
| `>`         | `5 > 3`    | `True`     |
| `<`         | `5 < 3`    | `False`    |
| `>=`        | `5 >= 3`   | `True`     |
| `<=`        | `5 <= 3`   | `False`    |

---

## 🔹 3. Logical Operators  
Used to combine conditional statements.

| **Operator** | **Example** | **Result** |
|-------------|------------|------------|
| `and`      | `True and False` | `False` |
| `or`       | `True or False`  | `True`  |
| `not`      | `not True`       | `False` |

---

## 🔹 4. Bitwise Operators  
Used to perform bit-level operations.

| **Operator** | **Example** | **Binary Representation** | **Result** |
|-------------|------------|--------------------------|------------|
| `&` (AND)  | `5 & 3`    | `101 & 011`             | `1`        |
| `|` (OR)   | `5 | 3`    | `101 | 011`             | `7`        |
| `^` (XOR)  | `5 ^ 3`    | `101 ^ 011`             | `6`        |
| `~` (NOT)  | `~5`       | `~101`                  | `-6`       |
| `<<` (Left Shift) | `5 << 1` | `101 << 1` | `10` |
| `>>` (Right Shift) | `5 >> 1` | `101 >> 1` | `2` |

---

## 🔹 5. Assignment Operators  
Used to assign values to variables.

| **Operator** | **Example** | **Equivalent To** |
|-------------|------------|-------------------|
| `=`         | `x = 5`    | `x = 5`          |
| `+=`        | `x += 3`   | `x = x + 3`      |
| `-=`        | `x -= 3`   | `x = x - 3`      |
| `*=`        | `x *= 3`   | `x = x * 3`      |
| `/=`        | `x /= 3`   | `x = x / 3`      |
| `//=`       | `x //= 3`  | `x = x // 3`     |
| `%=`        | `x %= 3`   | `x = x % 3`      |
| `**=`       | `x **= 3`  | `x = x ** 3`     |

---

## 🔹 6. Identity Operators  
Used to compare memory locations of objects.

| **Operator** | **Example** | **Result** |
|-------------|------------|------------|
| `is`       | `x is y`   | `True` if `x` and `y` are the same object |
| `is not`   | `x is not y` | `True` if `x` and `y` are different objects |

---

## 🔹 7. Membership Operators  
Used to check if a value is in a sequence.

| **Operator** | **Example** | **Result** |
|-------------|------------|------------|
| `in`       | `"a" in "apple"` | `True`  |
| `not in`   | `"b" not in "apple"` | `True` |

---

## ✅ Key Takeaways  
- **Arithmetic operators** perform mathematical operations.  
- **Comparison operators** return `True` or `False` based on conditions.  
- **Logical operators** help in combining multiple conditions.  
- **Bitwise operators** perform operations at the bit level.  
- **Assignment operators** assign and modify values.  
- **Identity operators** check if two objects are the same.  
- **Membership operators** verify if an item exists in a sequence.  
- Operators can be used in **expressions and conditions** to control program flow.  

---

## 📂 Reference Code  
[🔗 Click here to view basic operator examples](./basic_operator.py)  
[🔗 Click here to view more operator examples](./more_on_operators.py)  


---
