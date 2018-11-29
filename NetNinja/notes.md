## On the language

In Python, pretty much everything is an object.

Higher-level language.

LOTS of libraries ==> VERY interesting.

Interpreted.

## Data types

#### Numbers

Integer, float...
NB: the single division operator retuns a float, use // to return an integer.
Same BIDMAS applies. Same shorthand operators apply, like `+= *= -=`.
Check the type of an object with `type()`

#### Strings

Sequence of characters between quotes, single or double. Same way of escaping characters.
Same for indexing, starts at 0. A string an be searched with `"some_string"[0] ==> "s"`.

Slicing is done by adding another index(up to, non inclusive) `"some_string"[0:4] ==> "some"`.
Concatenation with `+`.
Multiplying a string by X(integer) returns a string composed of X-times the original string like so: `some * 3 ==> "somesomesome"`.
`some_string.upper()` and `some_string.lower()` to transform in upper/lower case.

Spliting with `split()` returns a list (similar to JS arrays) `"some more string".split(" ") ==> ['some', 'more', 'string']`.

Length of a string: `len("some_string") ==> 11`. Returns an integer.

#### Lists

Similar to JS arrays. `some_list[2] ==> element at index 2, starting from 0`. A negative value starts form the list end. Slicing with `[start:up_to]`.

Concatenate lists with `+`: `[1, 2, 3] + [4, 5, 6] ==> [1, 2, 3, 4, 5, 6]`.
`some_list.append(element)` adds `elememt` to the end of the list. `some_list.pop()` removes the last element of the list.

`some_list.remove(element)` will remove the **_first_** occurence of `element` in the list. `del(some_list[1])` removes the element at index 1. Can also use a range with `[start:up_to]`.

Lists accepts all data types, including lists. Access by specifying the levels: `[1, 2, [3, 4]][2][0] ==> 3`.

`some_list.count(val)` return the number of occurrences of `val` in `some_list`.

Lists can be created from other lists, while performing an operation on the elements. For loop works, or comprehension method, see comprehension.py.

#### Dictonaries

Similar to objects in JS, key-value pairs in curly brackets. `some_dict[some_key] = some_value` to assign a value to a key.

Keys can be retrieved as a list with `list(some_dict.keys())`, where `list()` is used to typecast its arg into a proper list. Same for values with `list(some_dict.values())`.

Other way to create a dictionary is with `dict(key1 = val1, key2 = val2, ...)`.

#### Sets

`set(list)` return a set of the unique values in `list`. NB: `set()` does not preserve the order.

Example in dictionaries.py

## input() print()

`input("some label")` expects an input from the console, can be stored in a variable. The variable is a string. If integer is needed, typecast the variable with `int(some_string)`.

`type(int(some_string)) ==> <class 'int'>`.

`print(some_variable)` returns some_variable in the console. Concatenate with a comma. Python adds a space with `print()` between elements separated by a comma.

## String formatting

`print()` with commas breaks the string(s). To avoid it, 2 other ways. See `string-format.py`

`"string is {val1:.3f}...".format(val1, ...)` where val1 is a float, and refered to by index in `.format()` parameters.

Or using F-Strings like so: `f"string is {val1:.3f}..."` where the options are placed as well after a column. `.3f` means a float with 3 numbers after the decimal point. `.3` would return the three first numbers of `val1`.

## if | elif | else statement

```python
if some_condition:
  # code block
elif other_condition:
  # other code block
else:
  # last code block
```

Comparaison operators: `< > <= >= == !=`.

## for | while loop

Iterating through a list or portion of a list.

```python
some_list = [1,2,3,4,5,6,7,8]

for element in some_list:
  # code block

for element in some_list[2:5]:
  # code block
```

`break` keyword can be used to exit the loop. The code block can be an `if else` statement or anything else needed.

```python
age = 25
iterator = 0

while iterator < age
  # code block
  iterator += 1
# some other code
```

`continue` allows to go back to the initial `while`, but the `iterator` still needs to be incremented, otherwise **infinite loop**

## range()

In `for n in range(val):` range() generates a list of numbers UP TO `val` not included.

`range()` can take 3 args: start-val, end-val, step-val. End value is not optional. End value can be also the length of a list. Using a triple `-1`, the iteration will happen from the end of the list backward.

## Functions and variable scope

```python
def function_name(args...):
  # code block
  # return statement

function_name(args...) # invocation
```

Args can be value or any datatypes, including lists, functions and so on. They can be assigned a default value directly between the parenthesis, if/when a parameter is not passed in (same as JS).

In functions.py, the variables `radius` and `length` are global, defined outside of the functions. If defined inside the functions, they are then in local scope. A global var can be reassigned inside a function, and this is in the local scope. Using `global var_name` will reassign the var_name value in the global scope **from within** the function. Avoid globally declared variables as much as possible.

## Sorting a list

`sorted(some_iterable [, reverse][, key])` will sort the list, in ascending order. BEWARE that strings are sorted by ASCII value, so `B` comes before `a`.

```python
sorted([2, 1, 3, 7, 45, 21]) ==> [1, 2, 3, 7, 21, 45]
sorted(['a', 'b', 'C']) ==> ['C', 'a', 'b']
```

Also with `list.sort()` method, and only for lists: `list.sort(reverse=True|False, key=myFunc)` where `key` is a callback.

## Classes, methods and attributes

Class names start with a capital letter.

Similar to JS. `__init__()` is the required constructor. The atttributes can be dynamically defined in the init() function. What is defined with `self` is instance level, not accessible by the class.

Class attributes, class methods and static methods are accessible by the class AND the instances. See classes.py.

## Modularity

Very easy to do with modules and packages.

Modules are just made of classes or functions which are imported where needed.

Packages are groups of modules with a `__init__.py` file in this folder to identify them as package.

## Map method

Takes a callback and a list and returns an object where each element is the result of applying the callback to each element of the passed-in list as an input. To get a list, typecast with `list()`.

See maps.py.

## filter()

It takes a callback returning a Boolean and a list as inputs. See filters.py.

## Lambda functions

Anonymous functions defined in line, like so:

```python
nums = [1, 2, 3, 4, 5, 6]
def squared(n):
    return n**2

# with named function squared()
print(list(map(squared, nums)))

# with lambda function
print(list(map(lambda n: n**2, nums)))
```

## Decorators

Extend the behavior of a function. It wraps a block of logic around the function it sits on. There can be a block of code before the function is invoked and/or one after.

Decorators are functions. They can be re-used when and where needed. See decorators.py.
