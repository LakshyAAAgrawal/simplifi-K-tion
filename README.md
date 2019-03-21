# simplifi-K-tion
python program to simplify a given boolean function of any size to it's minimum cover.
To use, import as:
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

minFunc(4, '(0,1,4,5,7,9,10,11,13,15)
>> w'y'+wx'y+wz+xz OR w'y'+wx'y+xz+y'z
```

Tests can be run by
 ```
 python3 Ksimplifier_testing.py
 ```
 
