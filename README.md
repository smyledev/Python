## Examples


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

