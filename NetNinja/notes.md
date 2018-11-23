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

## input() print()

`input("some label")` expects an input from the console, can be stored in a variable. The variable is a string. If integer is needed, typecast the variable with `int(some_string)`. `type(int(some_string)) ==> <class 'int'>`.

`print(some_variable)` returns some_variable in the console. Concatenate with a comma. Python adds a space between elements with `print()`.

## String formatting

`print()` with commas breaks the string(s). To avoid it, 2 other ways. See `string-format.py`

`"string is {val1:.3f}...".format(val1, ...)` where val1 is a float, and refered to by index in `.format()` parameters.

Or using F-Strings like so: `f"string is {val1:.3f}..."` where the options are placed as well after a column. `.3f` means a float with 3 numbers after the decimal point. `.3` would return the three first numbers of `val1`.
