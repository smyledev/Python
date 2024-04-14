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
