## General syntax
Every non blank line that is not a label contains a single statement, which ends with a `;`. Indentation is ignored, and using it is not recommended. Comments can only appear on lines that don't contain code, and are indicated by starting a line with a letter character.

## Data
Plus++ only has built in support for integers. Booleans are handled as normal integer 0's and 1's. All numbers are 16 bit unsigned integers.

### Literals
Literals are formed by placing a combination of "`+`" and "`-`" symbols between brackets. These "`+`" and "`-`" symbols are interpreted as binary numbers, where a "`+`" stands for a 1 and a "`-`" for a 0. So the expression "`(+--+)`" means 9 (1001 in binary) and "`(-)`" means 0.

### Storing and Retrieving Data
All data is stored in a global buffer containing 64k 16 bit words, so you can use the 16 bit integers to index into this buffer.

To assign a value to a spot in the buffer, use the following statement:
```
[X] E;
```
Where the value of the expression E will be stored at the index that expression X is equal to. So the following statement stores a 3 at index 4.
```
[(+--)] (++);
```
This is the only context in which you can use a space, to indicate an asignment.

The value of a place in the buffer can be retrieved and used in an expression by writing `[X]` in an expression, where X is the index to retrieve the value from. So `[(+-+)]` means the value at index 0.

## Expressions
Expressions can be made by putting literals and/or references to the buffer between parentheses, which can be connected with the following operators. Remember, spaces are never allowed inside expressions.

### Standard numerical operators
- `+` can be used to add two expressions together. So adding 3 to 2 looks like `((++)+(+-))`
- To multiply two expressions, put them next to each other without anything in between. So 4 times 4 looks like `((+--)(+-+))`
- Putting `++` after an expression increments that expression by one, and `--` decrements by one. These operators can also have side effects, see below. So `((++)++)` means 3 incremented by one.

### Boolean expressions
x greater than y: x +- y
x smaller than y: x -+ y
x equal to y: x +-+ y

These expressions are evaluated to integer ones and zeroes. There are no logical connectives present, these have to be implementated via the normal numerical operators.

### Expressions with side effects
The following operators create expressions that have side effects (in this case for the variable `--+`).
- `[(+)]++;` increments the value at index one by one, and returns the new value
- `[(+)]--;` decrements the value at index one by one, and returns the new value
- `++[x];` and `--[x];` throw special errors, because they are stupid

## Conditional jumps
Conditional jumps are implemented as an if-goto. The statement `E1{E2}` means if E1 is not zero, go to line E2.

## I/O statements
In an expression you can put `E?`, which prints the value of E to the output and then accepts input, which it then returns as a value. This input has to be a binary number in the + and - format, but `E??` can accept decimal input and `E???` accepts a single ASCII character, although these alternative input methods will give a warning, as they are not recommended.

The following statement prints the value of E to the output:
```
E!;
```
Again the alternative modes can be used with `E!!;` and `E!!!;` respectively, but these will give warnings.