# General syntax
Every non blank line contains a single statement, which (with the exception of conditional statements) ends with a `;`. Indentation is ignored, and using it is not recommended. Comments can on lines that don't contain code, and are indicated by starting a line with a letter character.

## Data
Plus++ only has built in support for integers. Booleans are handled as normal integer 0's and 1's.
The only other built in data structure is a list of integers.

### Variables
Variable names are made of a combination of the + and - symbols, and have a minimum length of 3 symbols.
To declare the variable `++-`, use the following statement:
```
+ ++-;
```
Variables are always global and have a default value of 0. To assign a value to the previously mentioned variable, use the following statement:
```
++- E;
```
Where E is the expression whose value will be assigned to the variable `++-`.

Other statements that can change the value of a variable are (in this case for the variable `--+`)
- `[--+]++;` increments the value of `--+` by one
- `[--+]--;` decrements the value of `--+` by one
- `++x;` and `--x;` throw special errors, because they are stupid

### Lists
Lists can be declared with the following statement, in this case for the list with name +--+:
```
+ +--+[];
```
By default lists are empty, but values can be assigned at any index, but these values can only be integers, not lists themselves. To assign a value to the element at index n (list are zero indexed, so this will be the (n+1)-th element) use the following statement:
```
+--+[n] E;
```
Where E again is the expression whose will be assigned. If any indexes below n are empty before the assignment they will be automatically filled with zeroes.