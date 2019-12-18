# simplifi-K-tion
Python and Common Lisp program to simplify a given boolean function of any size to it's minimum cover.
## Python
The python module is present under Ksimplifier.py.
### Usage
```python
from Ksimplifier import minFunc
```
Then use it as:
```python
minFunc(<number of variables>, 
        '(<comma separated list of minterms>) d (<comma separated list of don't cares>)')
```
Example:
```python
minFunc(1, '() d (1)')
>> 0

# For 0 Don't care conditions, use '-'
minFunc(4, '() d -')
>> 0

minFunc(4, '(0,1,4,5,7,9,10,11,13,15) d -')
>> w'y'+wx'y+wz+xz OR w'y'+wx'y+xz+y'z
```

Tests can be run by
 ```
 python3 Ksimplifier_testing.py
 ```

## Common Lisp
The Common Lisp program is intended to work with Maxima CAS and is now part of the core [Maxima repository](https://sourceforge.net/p/maxima/)(Merged in May 2019 through Sourceforge [merge #10](https://sourceforge.net/p/maxima/code/merge-requests/10/)). The program is present under Ksimplifier.lisp.
### Usage
In a Maxima repl:
```maxima
load(logic);
load("Ksimplifier.lisp");
```
Example usage:
```maxima
(%i4) logic_simplify(a or (a or b));
(%o4)                               a or b
```
