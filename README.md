# JS Runtime using Python and QuickJS

## Overview

This project is a lightweight JavaScript runtime built using Python and the QuickJS engine.

It allows users to execute JavaScript files from the command line while supporting common JavaScript features such as variables, functions, arrays, objects, loops, modern ES6 syntax, and built-in JavaScript objects.

---

## Features

- Execute JavaScript files
- Interactive REPL mode
- Inline JavaScript execution using -e
- Runtime version information using --version
- Error handling
- Modern JavaScript support through QuickJS

Supported JavaScript concepts include:

* Variables (let, const)
* Functions
* Arrays
* Objects
* Loops
* Conditional statements
* Arrow functions
* Array methods (map, filter, reduce)
* Spread operator
* Math object
* Date object
* Template literals

---

## Project Structure

```text
JS-RUNTIME/
│
├── runtime.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── examples/
└── tests/
```

---

## Requirements

* Python 3.8 or higher
* Git (optional for cloning the repository)

---

## Installation

Create a virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run any JavaScript file:

```bash
python runtime.py example.js
```

Example:

```bash
python runtime.py examples/odd_even.js
```

### Show Version

```bash
python runtime.py --version
```

### Execute Inline JavaScript

```bash
python runtime.py -e "console.log(5+5)"
```

### Interactive REPL

```bash
python runtime.py
```

---

## Sample Commands

Run an example:

```bash
python runtime.py examples/armstrong.js
```

Run a custom JavaScript file:

```bash
python runtime.py myfile.js
```

---

## Example Output

Input:

```javascript
let num = 7;

if (num % 2 === 0) {
    console.log(num + " is Even");
} else {
    console.log(num + " is Odd");
}
```

Output:

```text
7 is Odd
```

---

## Supported Features

* Variable declarations (`let`, `const`)
* Functions and arrow functions
* Arrays and objects
* Loops (`for`, `while`)
* Conditional statements
* Array methods (`map`, `filter`, `reduce`)
* Spread operator
* Template literals
* Math object
* Date object
* console.log()

---

## Technologies Used

* Python
* QuickJS
* Git
* GitHub
