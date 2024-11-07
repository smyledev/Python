# My solutions

## Example of using unit test
```python
import unittest 
  
class TestStringMethods(unittest.TestCase): 
    def test_negative(self): 
        firstValue = "geeks"
        secondValue = "gfg"
        message = "First value and second value are not equal !"
        self.assertEqual(firstValue, secondValue, message) 
  
if __name__ == '__main__': 
    unittest.main() 
```

## Example of using map and lambda
```python
numbers = (1, 2, 3, 4)
result = map(lambda n : n * 2, numbers)
print(list(result))
```


### Spining words with length more than 5 words

```Python
def spin_words(sentence):
    return " ".join([word if len(word) < 5 else word[::-1] for word in sentence.split(" ")])
```

### Replacing words

```Python
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))
```

### Finding max and min from a string with numbers separated by spaces

```Python
def high_and_low(numbers):
  numbers = [int(c) for c in numbers.split(' ')]
  return f"{max(numbers)} {min(numbers)}"
```


### Getting count of special words

```Python
def getCount(s):
    return sum(c in 'aeiou' for c in s)
```

### Getting elements from an array that are not in another array

```Python
def array_diff(a, b):
    return [x for x in a if x not in b]
```


### Filtering list by int
```Python
def filter_list(l):
    return [i for i in l if isinstance(i, int)] 
```

### Separating string from camel case to string with spaces 
```Python
def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)
```

### Check if braces using correct
```Python
def validBraces(s):
  while '{}' in s or '()' in s or '[]' in s:
      s=s.replace('{}','')
      s=s.replace('[]','')
      s=s.replace('()','')
  return s==''
```

### Check string is pangram
```Python
def is_pangram(s):
uniq_s = []
for i in s:
    if i not in uniq_s and i.isalpha():
        uniq_s.append(i.lower())
return len(uniq_s) == 26
```

### Define speed of last cog by first
```Python
def cog_RPM(cogs):
    length = len(cogs)
    return cogs[0] / cogs[-1] * (-1)**(length - 1) if length > 0 else 1
```

### Continued fraction
```Python
def continued_fraction(nu: int, de:int) -> list[int]:
    arr = []
    while nu and de:
        arr.append(nu // de)
        nu, de = de, nu % de
    return arr
```


### Changing words of string by ruls(reverse 1-st and last symbol of words and adding ay)
```Python
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
```


### Calculating with Functions, like five(divided_by(four()))
```Python
def zero(arg=""):  return eval("0" + arg)
def one(arg=""):   return eval("1" + arg)
def two(arg=""):   return eval("2" + arg)
def three(arg=""): return eval("3" + arg)
def four(arg=""):  return eval("4" + arg)
def five(arg=""):  return eval("5" + arg)
def six(arg=""):   return eval("6" + arg)
def seven(arg=""): return eval("7" + arg)
def eight(arg=""): return eval("8" + arg)
def nine(arg=""):  return eval("9" + arg)

def plus(n):       return '+' + str(n)
def minus(n):      return '-' + str(n)
def times(n):      return '*' + str(n)
def divided_by(n): return '//' + str(n)
```

### Finding polygon area for a given n.
```Python
def shape_area(n):
    if (n % 2 == 0):
        t = n - 1
        sum = 0 
        while t >= 1:
            sum += t * 4
            t -= 2        
        return (n - 1) * (n - 1) + sum

    else:
        t = n - 2
        sum = 0 
        while t >= 1:
            sum += t * 4
            t -= 2        
        return n * n + sum
```

### Continued fraction. For example, if the numerator is 311 and the denominator is 144, then you would have to return [2, 6, 3, 1, 5]
```Python
def continued_fraction(nu: int, de:int) -> list[int]:
    arr = []
    wh_part = nu
    if nu != 0:
        while (de != 0) and (wh_part // de > 0 or wh_part % de > 0): 
            arr.append(wh_part // de)
            wh_part, de = de, wh_part % de
        if (de != 0): arr.append(wh_part // de)
    return arr
```

### Interesting numbers 
Interesting numbers are 3-or-more digit numbers that meet one or more of the following criteria:

Any digit followed by all zeros: 100, 90000
Every digit is the same number: 1111
The digits are sequential, incementing†: 1234
The digits are sequential, decrementing‡: 4321
The digits are a palindrome: 1221 or 73837
The digits match one of the values in the awesome_phrases array

```Python
# boring" numbers
is_interesting(3, [1337, 256])    # 0
is_interesting(3236, [1337, 256]) # 0
```

```Python
# progress as we near an "interesting" number
is_interesting(11207, []) # 0
is_interesting(11208, []) # 0
is_interesting(11209, []) # 1
is_interesting(11210, []) # 1
is_interesting(11211, []) # 2
```

```Python
# nearing a provided "awesome phrase"
is_interesting(1335, [1337, 256]) # 1
is_interesting(1336, [1337, 256]) # 1
is_interesting(1337, [1337, 256]) # 2
```

```Python
def is_interesting(number, awesome_phrases):
    result = 0
    if len(str(number)) in range(3, 10):
          
        result = max(result, awesomePhrases(number, awesome_phrases)) 
        if result == 2: return result           
           
        result = max(result, decorator(number, nullAfter)) 
        if result == 2: return result
       
        result = max(result, sameNumber(number)) 
        if result == 2: return result
        
        result = max(result, incNumber(number))
        if result == 2: return result
        
        result = max(result,decNumber(number)) 
        if result == 2: return result
        
        result = max(result, decorator(number, polyndrom))
    
    elif number in range(98, 100):
        return 1
    
    return result 
    
def awesomePhrases(number, awesome_phrases):
    strNumber = str(number)
    lenStrNumber = len(strNumber)
    for item in awesome_phrases: 
        strItem = str(item)
        lenStrItem = len(strItem)
        if number == item: 
            return 2        
        elif (number + 1 == item) or (number - 1 == item) or (number + 2 == item) or (number - 2 == item) or (strNumber[lenStrNumber - 1] == '9' and strItem[lenStrItem - 1] == '0' and strNumber[:lenStrNumber - 2] == strItem[:lenStrItem - 2]) or (strNumber[lenStrNumber - 1] == '8' and strItem[lenStrItem - 1] == '0' and strNumber[:lenStrNumber - 2] == strItem[:lenStrItem - 2]) or (strNumber[lenStrNumber - 1] == '9' and strItem[lenStrItem - 1] == '1' and strNumber[:lenStrNumber - 2] == strItem[:lenStrItem - 2]):                     
            return 1
    return 0
    
def nullAfter(number):    
    strNumber = str(number)    
    return True if (strNumber.count('0') == (len(strNumber) - 1)) else False

def sameNumber(number):
    strNumber = str(number) 
    return 2 if strNumber.count(strNumber[0]) == len(strNumber) else 0

def incNumber(number): 
    strNumber = str(number) 
    result = 2   
    for i in range(len(strNumber) - 1):
        if (int(strNumber[i + 1]) != int(strNumber[i]) + 1) and not (strNumber[i] == '9' and strNumber[i + 1] == '0'):
            if (strNumber[i] == '8' and strNumber[i + 1] == '0') or (strNumber[i] == '9' and strNumber[i + 1] == '0') or (strNumber[i] == '9' and strNumber[i + 1] == '1'):
                result = 1 
            elif (int(strNumber[i + 1]) == int(strNumber[i]) or (int(strNumber[i]) == int(strNumber[i + 1]) - 2) or (int(strNumber[i]) == int(strNumber[i + 1]) + 2) or (int(strNumber[i]) == int(strNumber[i + 1]) + 1)):
                result = 1
            else:
                result = 0 
                break                
    return result

def decNumber(number):
    strNumber = str(number) 
    result = 2  
    for i in range(len(strNumber) - 1):
        if (int(strNumber[i + 1]) != int(strNumber[i]) - 1):
            if (int(strNumber[i]) == int(strNumber[i + 1]) - 2) or (int(strNumber[i]) == int(strNumber[i + 1]) - 1) or (int(strNumber[i]) == int(strNumber[i + 1]) + 2) or (int(strNumber[i]) == int(strNumber[i + 1]) + 1):
                result = 1                 
            elif (strNumber[i] == '0' and strNumber[i + 1] == '9') or (strNumber[i] == '0' and strNumber[i + 1] == '8') or (strNumber[i] == '1' and strNumber[i + 1] == '9'):
                result = 1 
            else: 
                result = 0
                break
    return result

def polyndrom(number):   
    strNumber = str(number)
    middle = len(strNumber) // 2
    if (strNumber[:middle] == strNumber[middle + 1:]): return True
    else: return False

def decorator(number, func):  
    if func(number): return 2
    elif func(number + 1) or func(number + 2) or func(number - 1) or func(number - 2): return 1
    else: return 0
```
